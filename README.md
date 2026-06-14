# 🏗️ Land Visualizer Pro – AP & TS Real Estate

## 📦 Files in this ZIP
```
frontend/index.html   ← Main app (works standalone in any browser)
backend/app.py        ← Flask backend (optional, for API)
start.bat             ← Double-click to run both together
```

---

## 🚀 Run Locally (No Internet Needed)
1. Extract the ZIP
2. Double-click `start.bat`
   - Opens Flask backend on http://localhost:5000
   - Opens frontend in your default browser automatically

OR just double-click `frontend/index.html` directly — it works without backend too.

---

## 🌐 Host Live (Free Options)

### Option 1 — GitHub Pages (Recommended)
1. Go to https://github.com/new → create a repo named `land-visualizer`
2. Upload `frontend/index.html` → rename it to `index.html` at root
3. Go to Settings → Pages → Branch: main → Save
4. Your live link: `https://<your-username>.github.io/land-visualizer/`

### Option 2 — Netlify Drop (Instant, 0 clicks)
1. Go to https://app.netlify.com/drop
2. Drag and drop the `frontend/` folder
3. Get instant live URL like: `https://amazing-plot-abc123.netlify.app`

### Option 3 — Vercel
1. Go to https://vercel.com/new
2. Upload the `frontend/` folder
3. Live URL in 30 seconds

---

## 📍 Region
- **AP**: Andhra Pradesh (Amaravati, Vijayawada, Visakhapatnam, Guntur)
- **TS**: Telangana (Hyderabad, Warangal, Karimnagar, Nizamabad)

## 🔧 Tech Stack
- Frontend: Pure HTML + CSS + Canvas API
- Backend: Python 3 + Flask + Flask-CORS
- No external dependencies for frontend
