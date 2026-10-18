import cv2, os, sys, numpy as np
crops_dir, repo_dir = sys.argv[1], sys.argv[2]
orb = cv2.ORB_create(3000)
def feats(path, maxw=1000):
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if im is None: return None
    s = maxw / im.shape[1]; im = cv2.resize(im, None, fx=s, fy=s)
    im = cv2.equalizeHist(im)
    k, d = orb.detectAndCompute(im, None); return im, k, d, s
repo = {}
for f in sorted(os.listdir(repo_dir)):
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')) and not f.startswith('01_poster-hero'):
        r = feats(os.path.join(repo_dir, f)); 
        if r and r[2] is not None: repo[f] = r
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
for c in sorted(os.listdir(crops_dir)):
    ci, ck, cd, cs = feats(os.path.join(crops_dir, c))
    best = []
    for f, (ri, rk, rd, rs) in repo.items():
        m = bf.knnMatch(cd, rd, k=2)
        good = [a for a, b in (p for p in m if len(p) == 2) if a.distance < 0.75 * b.distance]
        inl = 0; box = None
        if len(good) >= 10:
            src = np.float32([ck[g.queryIdx].pt for g in good]).reshape(-1, 1, 2)
            dst = np.float32([rk[g.trainIdx].pt for g in good]).reshape(-1, 1, 2)
            H, mask = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
            if H is not None:
                inl = int(mask.sum())
                h, w = ci.shape
                pts = cv2.perspectiveTransform(np.float32([[0,0],[w,0],[w,h],[0,h]]).reshape(-1,1,2), H).reshape(-1,2) / rs
                box = [round(float(v)) for v in (pts[:,0].min(), pts[:,1].min(), pts[:,0].max(), pts[:,1].max())]
        best.append((inl, f, box))
    best.sort(reverse=True)
    print(c, best[0], best[1][:2])
