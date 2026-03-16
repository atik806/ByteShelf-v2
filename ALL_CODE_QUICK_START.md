# All Code Folder - Quick Start

## What's New

Flask app is now in the "All code" folder for easier Vercel deployment.

## Files Created

✅ `All code/app.py` - Main Flask app
✅ `All code/wsgi.py` - WSGI entry point
✅ `All code/vercel.json` - Vercel config
✅ `All code/.env` - Environment
✅ `All code/requirements.txt` - Dependencies

## Quick Deploy

### Step 1: Navigate to folder
```bash
cd "All code"
```

### Step 2: Update environment
Edit `.env`:
```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secure-key
```

### Step 3: Deploy
```bash
vercel
```

### Step 4: Test
```bash
curl https://your-url.vercel.app/health
```

## What It Does

- ✅ Serves frontend from `frontend/` folder
- ✅ Serves backend API from `backend/` folder
- ✅ Handles all routes automatically
- ✅ CORS enabled
- ✅ Production ready

## File Structure

```
All code/
├── app.py              ← Main Flask app
├── wsgi.py             ← WSGI entry
├── vercel.json         ← Vercel config
├── .env                ← Environment
├── requirements.txt    ← Dependencies
├── backend/
│   ├── app.py
│   ├── config.py
│   └── routes/
└── frontend/
    ├── index.html
    ├── pdf-reader.html
    └── ...
```

## API Endpoints

- `GET /` - Frontend index
- `GET /health` - Health check
- `GET /api/books` - Books API
- `GET /api/categories` - Categories API
- `GET /<filename>` - Static files

## Local Testing

```bash
cd "All code"
pip install -r requirements.txt
python app.py
```

Then visit: `http://localhost:5000`

## Environment Variables

```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-key
HOST=0.0.0.0
PORT=5000
SUPABASE_URL=https://...
SUPABASE_KEY=your-key
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | Check backend/ exists |
| Frontend not loading | Check frontend/ exists |
| 500 error | Check .env variables |
| API not working | Check backend routes |

## Status

✅ Ready for Vercel deployment
✅ All files created
✅ Tested and working
✅ Production ready

---

**Next**: Update `.env` and deploy!

