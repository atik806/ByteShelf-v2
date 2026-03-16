# Quick Deployment Checklist

## Backend Deployment to Vercel

### Files Created ✅
- [x] `app.py` - Main Flask entry point
- [x] `wsgi.py` - WSGI entry point
- [x] `vercel.json` - Vercel configuration
- [x] `.env` - Environment variables
- [x] `requirements.txt` - Python dependencies

### Before Deployment
- [ ] Update `.env` with production values
- [ ] Change `SECRET_KEY` to secure value
- [ ] Set `DEBUG=False`
- [ ] Set `FLASK_ENV=production`
- [ ] Test locally: `python app.py`
- [ ] Test health endpoint: `curl http://localhost:5000/health`

### Deployment
- [ ] Install Vercel CLI: `npm install -g vercel`
- [ ] Login to Vercel: `vercel login`
- [ ] Deploy: `vercel`
- [ ] Add environment variables in Vercel dashboard
- [ ] Redeploy after adding variables

### After Deployment
- [ ] Test health endpoint: `curl https://your-url/health`
- [ ] Test API endpoints: `curl https://your-url/api/books`
- [ ] Check Vercel logs for errors
- [ ] Verify static files serve correctly
- [ ] Monitor performance

## Admin Panel Deployment to Vercel

### Files Created ✅
- [x] `admin/app.py` - Flask application
- [x] `admin/wsgi.py` - WSGI entry point
- [x] `admin/vercel.json` - Vercel configuration
- [x] `admin/.env` - Environment variables
- [x] `admin/requirements.txt` - Dependencies

### Before Deployment
- [ ] Update `admin/.env` with production values
- [ ] Change admin password
- [ ] Set `DEBUG=False`
- [ ] Set `FLASK_ENV=production`
- [ ] Test locally: `cd admin && python app.py`

### Deployment
- [ ] Deploy: `cd admin && vercel`
- [ ] Add environment variables in Vercel
- [ ] Redeploy

### After Deployment
- [ ] Test health endpoint
- [ ] Test login functionality
- [ ] Test book management
- [ ] Check file uploads

## Environment Variables

### Root .env
```
FLASK_ENV=production
DEBUG=False
HOST=0.0.0.0
PORT=5000
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-key
SECRET_KEY=your-secret-key
```

### Admin .env
```
FLASK_ENV=production
DEBUG=False
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-password
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-key
SECRET_KEY=your-secret-key
```

## Testing

### Backend Health Check
```bash
curl https://your-backend-url.vercel.app/health
```

### Admin Health Check
```bash
curl https://your-admin-url.vercel.app/health
```

### API Endpoints
```bash
curl https://your-backend-url.vercel.app/api/books
curl https://your-backend-url.vercel.app/api/categories
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 500 Error | Check Vercel logs, verify env vars |
| Module not found | Check Python path in app.py |
| Cannot find routes | Verify backend directory exists |
| Static files not found | Check frontend path in routes |
| Login fails | Verify admin credentials in .env |

## Deployment URLs

- **Backend**: https://your-backend-url.vercel.app
- **Admin**: https://your-admin-url.vercel.app
- **Frontend**: https://your-frontend-url.vercel.app

## Quick Commands

```bash
# Deploy backend
vercel

# Deploy admin
cd admin && vercel

# Test locally
python app.py

# Install dependencies
pip install -r requirements.txt

# Check health
curl https://your-url/health
```

## Status

✅ Backend ready for Vercel
✅ Admin ready for Vercel
✅ All files created
✅ Environment configured
✅ Documentation complete

---

**Next Step**: Update `.env` files and deploy!

