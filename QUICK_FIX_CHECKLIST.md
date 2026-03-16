# OAuth Fix - Quick Checklist

## ✅ Code Changes (DONE)
- [x] Updated login.html OAuth redirect to `/dashboard.html`
- [x] Updated signup.html OAuth redirect to `/dashboard.html`
- [x] Verified auth.js Supabase configuration

## 📋 Supabase Configuration (YOU NEED TO DO THIS)

### 1. Add Redirect URLs
- [ ] Go to https://app.supabase.com
- [ ] Select project: `wslsihrnaeoqojpzkjpy`
- [ ] Go to: Authentication → URL Configuration
- [ ] Add these URLs:
  - `http://localhost:5000/dashboard.html`
  - `http://localhost:5000/login.html`
  - `http://localhost:5000/signup.html`

### 2. Setup Google OAuth
- [ ] Go to [Google Cloud Console](https://console.cloud.google.com)
- [ ] Create OAuth 2.0 credentials
- [ ] Add redirect URI: `https://wslsihrnaeoqojpzkjpy.supabase.co/auth/v1/callback?provider=google`
- [ ] Copy Client ID and Secret
- [ ] Go to Supabase: Authentication → Providers → Google
- [ ] Paste credentials and save

### 3. Setup GitHub OAuth
- [ ] Go to [GitHub Developer Settings](https://github.com/settings/developers)
- [ ] Create new OAuth App
- [ ] Set Authorization callback URL: `https://wslsihrnaeoqojpzkjpy.supabase.co/auth/v1/callback?provider=github`
- [ ] Copy Client ID and Secret
- [ ] Go to Supabase: Authentication → Providers → GitHub
- [ ] Paste credentials and save

## 🧪 Testing
- [ ] Start app: `npm run start`
- [ ] Go to: `http://localhost:5000/login.html`
- [ ] Click "Continue with Google"
- [ ] Select account
- [ ] Should redirect to dashboard.html ✓
- [ ] Repeat for GitHub

## 📚 Documentation
- Read `SUPABASE_SETUP.md` for detailed instructions
- Read `OAUTH_FIX_GUIDE.md` for troubleshooting
- Read `OAUTH_FIX_SUMMARY.md` for overview

## 🚀 Production Deployment
When deploying to production:
- [ ] Add production domain to Supabase URL Configuration
- [ ] Update OAuth redirect URLs in Google/GitHub
- [ ] Test OAuth flow on production domain
- [ ] Monitor for errors in browser console

## 💡 Key Points
- Redirect URL must match EXACTLY in Supabase settings
- OAuth credentials must be added to Supabase
- Supabase URL: `https://wslsihrnaeoqojpzkjpy.supabase.co`
- Publishable Key: `sb_publishable_Ni8gulqDIn21i7qOGqymgQ_EiBZtdrv`

## ❓ Still Having Issues?
1. Check browser console for errors (F12)
2. Verify redirect URL in Supabase matches exactly
3. Ensure OAuth provider is enabled in Supabase
4. Check that credentials are correct
5. See `OAUTH_FIX_GUIDE.md` for detailed troubleshooting

