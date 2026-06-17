# UrbanCool AI Pro

**Geospatial Urban Heat Intelligence and Cooling Decision Platform**

Tagline: “See urban heat. Understand its causes. Design a cooler city.”

This is a free, static-first, production-ready MVP using React, TypeScript, Vite, Tailwind CSS, MapLibre GL JS, Turf.js, Recharts, NASA GIBS, Nominatim and Open-Meteo. It works locally without paid APIs, paid maps, paid databases, credit cards or custom domains.

## Run frontend
```bash
cd frontend
npm install
npm run dev
```

## Optional backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Important scientific transparency
The demo uses real global search, real OpenStreetMap basemaps, real NASA GIBS satellite imagery, and real Open-Meteo weather. The default heat surface is **modelled/simulated** from weather, land-cover proxies and location context unless the user uploads measured LST CSV/GeoJSON. It never claims restricted ISRO/SpaceX/private data is connected.

## Free deployment
Frontend can be deployed to Cloudflare Pages, GitHub Pages, Netlify free tier, or Vercel hobby tier.
