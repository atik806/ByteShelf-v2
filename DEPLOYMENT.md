# ByteShelf v1.1.0 - Deployment Guide

## Quick Start

### Deploy Main Application

```bash
cd "All code"
vercel
```

### Deploy Admin Panel (Optional)

```bash
cd admin
vercel
```

---

## Configuration

### All code/.env
```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secure-key
HOST=0.0.0.0
PORT=5000
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-key
```

### admin/.env
```
FLASK_ENV=production
DEBUG=False
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-password
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-key
SECRET_KEY=your-secret-key
```

---

## Features

✅ PDF Reader with zoom, themes, progress tracking
✅ Slideshow Mode (3-second auto-advance)
✅ OAuth Login (Google & GitHub)
✅ Admin Panel for content management
✅ Reading progress tracking
✅ Responsive design

---

## Testing

```bash
cd "All code"
pip install -r requirements.txt
python app.py
```

Then visit: `http://localhost:5000`

---

## API Endpoints

- `GET /` - Frontend
- `GET /health` - Health check
- `GET /api/books` - Books API
- `GET /api/categories` - Categories API

---

**Status**: ✅ Production Ready
