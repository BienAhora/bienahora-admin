const { chromium } = require(process.env.PW);
(async () => {
  const [url, outDir, ...names] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ deviceScaleFactor: 2, viewport: { width: 7880, height: 4240 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.waitForFunction(() => window.__listo);
  await p.evaluate(async () => { await document.fonts.ready; await Promise.all(Array.from(document.images).map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))); });
  await p.waitForTimeout(800);
  const piezas = await p.$$('#root > div > div > div:nth-child(2)');
  console.log('piezas', piezas.length);
  for (let i = 0; i < piezas.length; i++) await piezas[i].screenshot({ path: `${outDir}/${names[i]}.png` });
  await b.close();
})();
