import re,sys
src,out=sys.argv[1],sys.argv[2]
t=open(src,encoding='utf-8').read()
style=re.search(r'<helmet>\s*<style>(.*?)</style>\s*</helmet>',t,re.S).group(1)
xdc=re.search(r'<x-dc>(.*?)</x-dc>',t,re.S).group(1)
xdc=re.sub(r'<helmet>.*?</helmet>','',xdc,flags=re.S)
js=re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>',t,re.S).group(1)
page=f'''<!doctype html><html><head><meta charset="utf-8"><style>{style}</style></head><body>
<template id="tpl">{xdc}</template><div id="root"></div>
<script>
class DCLogic {{ constructor(){{ this.props={{}}; this.state={{}}; }} }}
{js}
const vals=new Component().renderVals();
function look(path,scope){{ path=path.trim(); if(path==='true')return true; if(path==='false')return false;
  let v=scope; for(const k of path.split('.')){{ if(v==null)return undefined; v=v[k]; }} return v; }}
function fill(s,scope){{ const m=s.match(/^\\s*\\{{\\{{([^}}]+)\\}}\\}}\\s*$/); if(m){{ const v=look(m[1],scope); return v==null?'':String(v); }}
  return s.replace(/\\{{\\{{([^}}]+)\\}}\\}}/g,(_,p)=>{{ const v=look(p,scope); return v==null?'':String(v); }}); }}
function expand(n,scope,out){{
  if(n.nodeType===3){{ out.push(document.createTextNode(fill(n.textContent,scope))); return; }}
  if(n.nodeType!==1) return;
  const tag=n.localName;
  if(tag==='sc-for'){{ const list=look(n.getAttribute('list').replace(/[{{}}]/g,''),scope)||[]; const as=n.getAttribute('as');
    list.forEach((it,i)=>{{ const s=Object.create(scope); s[as]=it; s.$index=i; n.childNodes.forEach(c=>expand(c,s,out)); }}); return; }}
  if(tag==='sc-if'){{ if(look(n.getAttribute('value').replace(/[{{}}]/g,''),scope)) n.childNodes.forEach(c=>expand(c,scope,out)); return; }}
  const e=n.cloneNode(false);
  for(const a of Array.from(e.attributes)){{ if(a.name.startsWith('hint-'))e.removeAttribute(a.name); else e.setAttribute(a.name,fill(a.value,scope)); }}
  const kids=[]; n.childNodes.forEach(c=>expand(c,scope,kids)); kids.forEach(k=>e.appendChild(k)); out.push(e); }}
const out=[]; document.getElementById('tpl').content.childNodes.forEach(c=>expand(c,vals,out));
out.forEach(o=>document.getElementById('root').appendChild(o));
window.__listo=true;
</script></body></html>'''
open(out,'w',encoding='utf-8').write(page)
