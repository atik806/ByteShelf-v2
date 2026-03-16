# ByteShelf Backend - Vercel Deployment Guide

## Problem Fixed

Vercel was not detecting the Flask backend because:
- ❌ No app.py in root directory
- ❌ No vercel.json configuration
- ❌ No requirements.txt in root
- ❌ Incorrect path configuration

## Solution Implemented

Created the following files in root directory (E:\EDU SITE):

✅ `app.py` - Main Flask entry point
✅ `wsgi.py` - WSGI entry point
✅ `vercel.json` - Vercel configuration
✅ `.env` - Environment variables
✅ `requirements.txt` - Python dependencies

## File Structure

```
E:\EDU SITE\
├── app.py                    ✅ Main entry point
├── wsgi.py                   ✅ WSGI entry point
├── vercel.json               ✅ Vercel config
├── .env                      ✅ Environment
├── requirements.txt          ✅ Dependencies
├── All code/
│   ├── backend/
│   │   ├── app.py           (imported by root app.py)
│   │   ├── config.py
│   │   └── routes/
│   └── frontend/
└── admin/
    ├── app.py
    ├── vercel.json
    └── .env
```

## How It Works

1. **Vercel detects** `app.py` in root directory
2. **Root app.py imports** the backend app from `All code/backend/app.py`
3. **Flask app is created** using the `create_app()` factory
4. **Routes are registered** from the backend
5. **Application runs** on Vercel

## Deployment Steps

### Step 1: Update Environment Variables

Edit `.env` in root directory:
```
FLASK_ENV=production
DEBUG=False
HOST=0.0.0.0
PORT=5000
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-key
SECRET_KEY=your-secret-key
```

### Step 2: Deploy to Vercel

**Option A: Using Vercel CLI**
```bash
vercel
```

**Option B: Using GitHub**
1. Push to GitHub
2. Go to vercel.com/new
3. Import repository
4. Select root directory
5. Add environment variables
6. Deploy

### Step 3: Configure Vercel Settings

1. Go to Vercel project settings
2. Navigate to "Environment Variables"
3. Add all variables from `.env`
4. Redeploy

### Step 4: Verify Deployment

Check health endpoint:
```
https://your-backend-url.vercel.app/health
```

Should return:
```json
{
  "status": "healthy",
  "message": "ByteShelf server is running",
  "service": "backend"
}
```

## Environment Variables

### Required
```
FLASK_ENV=production
DEBUG=False
HOST=0.0.0.0
PORT=5000
```

### Optional (Supabase)
```
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-key
SECRET_KEY=your-secret-key
```

## API Endpoints

After deployment, these endpoints are available:

- `GET /` - Main index page
- `GET /health` - Health check
- `GET /blog` - Blog page
- `GET /about` - About page
- `GET /<filename>` - Static files
- `GET /api/books` - All books (from admin)
- `GET /api/categories` - Categories (from admin)

## Troubleshooting

### Error: Module not found

**Cause**: Python path not set correctly

**Solution**:
- Verify `app.py` imports are correct
- Check `sys.path.insert()` in root `app.py`
- Ensure backend directory exists

### Error: Cannot find routes

**Cause**: Routes not imported correctly

**Solution**:
- Check `All code/backend/routes/main.py` exists
- Verify blueprint registration in backend `app.py`
- Check import paths

### Error: 500 Internal Server Error

**Cause**: Configuration issue

**Solution**:
1. Check environment variables
2. Verify `config.py` in backend
3. Check Vercel logs
4. Test locally first

### Error: Static files not found

**Cause**: Frontend path incorrect

**Solution**:
- Verify `All code/frontend/` directory exists
- Check path in `routes/main.py`
- Ensure files are in correct location

## Local Testing

Before deploying to Vercel, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Test health endpoint
curl http://localhost:5000/health
```

## Production Checklist

- [ ] Update `.env` with production values
- [ ] Change `SECRET_KEY` to secure value
- [ ] Set `DEBUG=False`
- [ ] Set `FLASK_ENV=production`
- [ ] Test all endpoints
- [ ] Verify static files serve correctly
- [ ] Check error handling
- [ ] Monitor logs
- [ ] Set up backups
- [ ] Configure monitoring

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
curl https://your-backend-url.vercel.app/health

# Check specific endpoint
curl https://your-backend-url.vercel.app/api/books
```

### Logs

- View in Vercel dashboard
- Check function logs
- Monitor error rates

### Alerts

- Set up error notifications
- Monitor response times
- Track uptime

## Support

For deployment issues:

1. Check Vercel logs
2. Verify environment variables
3. Test locally first
4. Review error messages
5. Contact Vercel support

## Next Steps

1. ✅ Update `.env` with production values
2. ✅ Deploy to Vercel
3. ✅ Test health endpoint
4. ✅ Verify all endpoints work
5. ✅ Monitor logs
6. ✅ Set up alerts
7. ✅ Go live!

---

**Status**: ✅ Ready for Vercel Deployment

