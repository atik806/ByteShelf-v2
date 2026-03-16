# Admin Panel Deployment Guide - Vercel

## Overview
This guide explains how to deploy the ByteShelf Admin Panel to Vercel.

## Prerequisites

- Vercel account (https://vercel.com)
- Git repository with the project
- Environment variables configured

## Files Created for Deployment

✅ `admin/app.py` - Main Flask application
✅ `admin/wsgi.py` - WSGI entry point
✅ `admin/vercel.json` - Vercel configuration
✅ `admin/.env` - Environment variables
✅ `admin/.env.example` - Environment template
✅ `admin/requirements.txt` - Python dependencies

## Step 1: Prepare Environment Variables

The `.env` file has been created with:
- Flask configuration
- Admin credentials
- Supabase configuration
- Server settings

**Important**: Update these values for production:
```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secure-secret-key
ADMIN_USERNAME=your-admin-username
ADMIN_PASSWORD=your-secure-password
```

## Step 2: Deploy to Vercel

### Option A: Using Vercel CLI

1. **Install Vercel CLI**:
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy from admin directory**:
```bash
cd admin
vercel
```

4. **Follow the prompts**:
   - Confirm project name
   - Select framework (Python)
   - Set environment variables

### Option B: Using GitHub Integration

1. **Push to GitHub**:
```bash
git add .
git commit -m "Add admin deployment files"
git push origin main
```

2. **Connect to Vercel**:
   - Go to https://vercel.com/new
   - Import your GitHub repository
   - Select the `admin` directory as root
   - Add environment variables
   - Deploy

## Step 3: Configure Environment Variables in Vercel

1. Go to your Vercel project settings
2. Navigate to "Environment Variables"
3. Add the following variables:

```
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secret-key
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-password
SUPABASE_URL=https://wslsihrnaeoqojpzkjpy.supabase.co
SUPABASE_KEY=your-supabase-key
HOST=0.0.0.0
PORT=5001
```

## Step 4: Verify Deployment

After deployment, verify the admin panel is working:

1. **Check health endpoint**:
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

2. **Access admin panel**:
```
https://your-admin-url.vercel.app/login
```

3. **Login with credentials**:
   - Username: admin
   - Password: admin123 (or your configured password)

## Troubleshooting

### Error: FUNCTION_INVOCATION_FAILED

**Cause**: Missing dependencies or incorrect configuration

**Solution**:
1. Verify `requirements.txt` has all dependencies
2. Check environment variables are set
3. Ensure `vercel.json` is correct
4. Check logs in Vercel dashboard

### Error: Module not found

**Cause**: Missing Python packages

**Solution**:
```bash
pip install -r requirements.txt
```

### Error: 500 Internal Server Error

**Cause**: Flask app not starting correctly

**Solution**:
1. Check `app.py` syntax
2. Verify environment variables
3. Check Vercel logs for detailed error
4. Ensure `wsgi.py` is correct

### Error: Cannot find data.json

**Cause**: File system issue

**Solution**:
1. Ensure `data.json` exists in admin directory
2. Check file permissions
3. Use environment variable for data path

## Production Checklist

- [ ] Update `SECRET_KEY` to a secure value
- [ ] Change `ADMIN_USERNAME` and `ADMIN_PASSWORD`
- [ ] Set `DEBUG=False`
- [ ] Set `FLASK_ENV=production`
- [ ] Configure Supabase credentials
- [ ] Test health endpoint
- [ ] Test login functionality
- [ ] Test book management
- [ ] Test file uploads
- [ ] Monitor logs for errors

## File Structure

```
admin/
├── app.py              # Main Flask application
├── wsgi.py             # WSGI entry point
├── vercel.json         # Vercel configuration
├── .env                # Environment variables
├── .env.example        # Environment template
├── requirements.txt    # Python dependencies
├── package.json        # Node configuration
├── data.json           # Data storage
├── templates/          # HTML templates
├── static/             # CSS/JS assets
└── uploads/            # File uploads
```

## Environment Variables Explained

| Variable | Purpose | Example |
|----------|---------|---------|
| FLASK_ENV | Flask environment | production |
| DEBUG | Debug mode | False |
| SECRET_KEY | Session encryption | your-secret-key |
| ADMIN_USERNAME | Admin login username | admin |
| ADMIN_PASSWORD | Admin login password | secure-password |
| SUPABASE_URL | Supabase project URL | https://... |
| SUPABASE_KEY | Supabase API key | your-key |
| HOST | Server host | 0.0.0.0 |
| PORT | Server port | 5001 |

## API Endpoints

After deployment, these endpoints are available:

- `GET /health` - Health check
- `GET /api/books` - Get all books
- `GET /api/books/<id>` - Get single book
- `GET /api/categories` - Get categories
- `GET /api/stats` - Get statistics
- `POST /api/register-user` - Register user

## Monitoring

Monitor your deployment:

1. **Vercel Dashboard**:
   - Check deployment status
   - View logs
   - Monitor performance

2. **Health Endpoint**:
   - Regularly check `/health`
   - Set up monitoring alerts

3. **Error Tracking**:
   - Enable Sentry integration
   - Monitor error rates

## Scaling

For production use:

1. **Database**: Migrate from JSON to PostgreSQL
2. **File Storage**: Use cloud storage (S3, Vercel Blob)
3. **Caching**: Add Redis for performance
4. **CDN**: Use Vercel's built-in CDN

## Support

For deployment issues:

1. Check Vercel logs
2. Review error messages
3. Verify environment variables
4. Test locally first
5. Contact Vercel support

## Next Steps

1. ✅ Deploy admin panel
2. ✅ Configure environment variables
3. ✅ Test all functionality
4. ✅ Set up monitoring
5. ✅ Configure backups
6. ✅ Document access procedures

---

**Status**: Ready for Vercel Deployment

