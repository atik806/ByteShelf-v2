# ByteShelf - All Code Folder Deployment Guide

## Overview

The Flask application has been moved to the "All code" folder for easier deployment to Vercel.

## Files Created in "All code" Folder

✅ `All code/app.py` - Main Flask application
✅ `All code/wsgi.py` - WSGI entry point
✅ `All code/vercel.json` - Vercel configuration
✅ `All code/.env` - Environment variables
✅ `All code/requirements.txt` - Python dependencies

## File Structure

```
All code/
├── app.py                    ✅ Main Flask app
├── wsgi.py                   ✅ WSGI entry point
├── vercel.json               ✅ Vercel config
├── .env                      ✅ Environment
├── requirements.txt          ✅ Dependencies
├── backend/
│   ├── app.py               (imported by root app.py)
│   ├── config.py
│   └── routes/
│       └── main.py
└── frontend/
    ├── index.html
    ├── pdf-reader.html
    ├── login.html
    ├── signup.html
    └── ...
```

## How It Works

1. **Vercel detects** `All code/app.py`
2. **App.py creates** Flask app with:
   - Backend routes from `backend/`
   - Frontend static files from `frontend/`
   - CORS enabled
3. **Routes registered**:
   - Backend API routes
   - Frontend static file serving
4. **App runs** on Vercel

## Deployment Steps

### Step 1: Update Environment Variables

Edit `All code/.env`:
```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secure-key
HOST=0.0.0.0
PORT=5000
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-key
```

### Step 2: Deploy to Vercel

**Option A: Using Vercel CLI**
```bash
cd "All code"
vercel
```

**Option B: Using GitHub**
1. Push to GitHub
2. Go to vercel.com/new
3. Import repository
4. Select "All code" as root directory
5. Add environment variables
6. Deploy

### Step 3: Configure Vercel Settings

1. Go to Vercel project settings
2. Navigate to "Environment Variables"
3. Add all variables from `.env`
4. Redeploy

### Step 4: Verify Deployment

Test the health endpoint:
```bash
curl https://your-backend-url.vercel.app/health
```

Should return:
```json
{
  "status": "healthy",
  "message": "ByteShelf server is running",
  "service": "backend"
}
```

## API Endpoints

After deployment:

- `GET /` - Main index page
- `GET /health` - Health check
- `GET /blog` - Blog page
- `GET /about` - About page
- `GET /<filename>` - Static files (HTML, CSS, JS)
- `GET /api/books` - Books from admin
- `GET /api/categories` - Categories
- `GET /api/stats` - Statistics

## Frontend Routes

The frontend files are served as static files:

- `/` - index.html
- `/login.html` - Login page
- `/signup.html` - Signup page
- `/dashboard.html` - Dashboard
- `/pdf-reader.html` - PDF reader
- `/my-books.html` - My books
- `/browse.html` - Browse library
- `/assets/js/auth.js` - Auth script
- `/assets/css/style.css` - Styles

## Environment Variables

### Required
```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secret-key
HOST=0.0.0.0
PORT=5000
```

### Optional (Supabase)
```
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-key
```

## Local Testing

Before deploying to Vercel:

```bash
# Navigate to All code folder
cd "All code"

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Test endpoints
curl http://localhost:5000/health
curl http://localhost:5000/
curl http://localhost:5000/api/books
```

## Vercel Configuration Details

### vercel.json Settings

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "50mb",
        "runtime": "python3.11"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### Key Settings

- **version**: 2 (Vercel v2 API)
- **builds**: Specifies Python runtime
- **routes**: All requests go to app.py
- **maxLambdaSize**: 50MB for large files
- **runtime**: Python 3.11

## Troubleshooting

### Error: Module not found

**Cause**: Python path not set correctly

**Solution**:
- Verify `backend/` directory exists
- Check `sys.path.insert()` in app.py
- Ensure `config.py` exists in backend

### Error: Cannot find frontend files

**Cause**: Frontend path incorrect

**Solution**:
- Verify `frontend/` directory exists
- Check `static_folder` in app.py
- Ensure files are in correct location

### Error: 500 Internal Server Error

**Cause**: Configuration or import issue

**Solution**:
1. Check Vercel logs
2. Verify environment variables
3. Test locally first
4. Check Python path

### Error: Static files not serving

**Cause**: Frontend path not configured

**Solution**:
- Verify `frontend/` folder exists
- Check `static_folder='frontend'` in app.py
- Ensure HTML files are in frontend folder

## Production Checklist

- [ ] Update `.env` with production values
- [ ] Change `SECRET_KEY` to secure value
- [ ] Set `DEBUG=False`
- [ ] Set `FLASK_ENV=production`
- [ ] Test all endpoints locally
- [ ] Deploy to Vercel
- [ ] Test health endpoint
- [ ] Verify frontend loads
- [ ] Verify API endpoints work
- [ ] Check error handling
- [ ] Monitor logs
- [ ] Set up alerts

## Performance Optimization

### For Vercel

1. **Minimize cold starts**:
   - Keep dependencies minimal
   - Use efficient imports
   - Cache static files

2. **Optimize routes**:
   - Use blueprints
   - Minimize database calls
   - Cache responses

3. **Monitor performance**:
   - Check Vercel analytics
   - Monitor response times
   - Track error rates

## Security

### Production Security

1. **Environment Variables**:
   - Never commit `.env`
   - Use Vercel secrets
   - Rotate keys regularly

2. **CORS Configuration**:
   - Restrict origins
   - Validate requests
   - Use HTTPS only

3. **Error Handling**:
   - Don't expose stack traces
   - Log errors securely
   - Monitor for attacks

## Monitoring

### Health Checks

```bash
# Check health
curl https://your-url.vercel.app/health

# Check specific endpoint
curl https://your-url.vercel.app/api/books
```

### Logs

- View in Vercel dashboard
- Check function logs
- Monitor error rates

### Alerts

- Set up error notifications
- Monitor response times
- Track uptime

## Next Steps

1. ✅ Update `.env` with production values
2. ✅ Deploy to Vercel
3. ✅ Test health endpoint
4. ✅ Verify frontend loads
5. ✅ Verify API endpoints work
6. ✅ Monitor logs
7. ✅ Go live!

---

**Status**: ✅ Ready for Vercel Deployment

