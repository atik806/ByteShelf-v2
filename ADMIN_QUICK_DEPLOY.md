# Admin Panel - Quick Deployment Guide

## What Was Fixed

The Vercel deployment error was caused by:
- ❌ Missing `app.py` file
- ❌ Missing WSGI entry point
- ❌ Missing Vercel configuration
- ❌ Missing environment variables

## What Was Created

✅ `admin/app.py` - Complete Flask application
✅ `admin/wsgi.py` - WSGI entry point for Vercel
✅ `admin/vercel.json` - Vercel deployment config
✅ `admin/.env` - Environment variables
✅ `admin/.env.example` - Environment template

## Quick Deploy Steps

### 1. Update Environment Variables
Edit `admin/.env`:
```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secure-key
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-password
```

### 2. Deploy to Vercel

**Using Vercel CLI**:
```bash
cd admin
vercel
```

**Using GitHub**:
1. Push to GitHub
2. Go to vercel.com/new
3. Import repository
4. Select `admin` as root directory
5. Add environment variables
6. Deploy

### 3. Verify Deployment

Check health endpoint:
```
https://your-admin-url.vercel.app/health
```

Should return:
```json
{
  "status": "healthy",
  "message": "ByteShelf Admin Panel is running",
  "service": "admin"
}
```

## Environment Variables

```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=byteshelf-admin-secret-key-2026
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
HOST=0.0.0.0
PORT=5001
```

## File Structure

```
admin/
├── app.py              ✅ Flask app
├── wsgi.py             ✅ WSGI entry
├── vercel.json         ✅ Vercel config
├── .env                ✅ Environment
├── .env.example        ✅ Template
├── requirements.txt    ✅ Dependencies
├── templates/          ✅ HTML
├── static/             ✅ CSS/JS
└── uploads/            ✅ Files
```

## Troubleshooting

### 500 Error
- Check environment variables
- Verify `app.py` syntax
- Check Vercel logs

### Module Not Found
- Run: `pip install -r requirements.txt`
- Check requirements.txt

### Cannot Find data.json
- Ensure file exists in admin directory
- Check file permissions

## Admin Panel Features

✅ Book Management
✅ Category Management
✅ File Uploads (PDF, DOC, etc.)
✅ Statistics Dashboard
✅ User Management
✅ API Endpoints

## API Endpoints

- `GET /health` - Health check
- `GET /api/books` - All books
- `GET /api/books/<id>` - Single book
- `GET /api/categories` - Categories
- `GET /api/stats` - Statistics
- `POST /api/register-user` - Register user

## Login Credentials

- **Username**: admin
- **Password**: admin123 (change in production)

## Next Steps

1. ✅ Update `.env` with production values
2. ✅ Deploy to Vercel
3. ✅ Test health endpoint
4. ✅ Test login
5. ✅ Test book management
6. ✅ Monitor logs

## Support

For issues:
1. Check Vercel logs
2. Verify environment variables
3. Test locally first
4. Review error messages

---

**Status**: ✅ Ready for Production Deployment

