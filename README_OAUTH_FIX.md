# ByteShelf OAuth Login Fix - Complete Guide

## 🎯 Problem
Users clicking "Continue with Google" or "Continue with GitHub" get a "This site can't be reached" error after selecting their account.

## ✅ Solution Applied

### Code Changes (Already Done)
Your code has been updated to fix the OAuth redirect issue:

1. **login.html** - OAuth redirect URL changed from `/index.html` to `/dashboard.html`
2. **signup.html** - OAuth redirect URL changed from `/index.html` to `/dashboard.html`
3. **auth.js** - Verified Supabase configuration is correct

### What You Need to Do (IMPORTANT)

You must configure OAuth in your Supabase project. Follow these steps:

## 📖 Step-by-Step Setup

### Step 1: Access Supabase Dashboard
1. Go to https://app.supabase.com
2. Sign in with your account
3. Select your project: `wslsihrnaeoqojpzkjpy`

### Step 2: Configure Redirect URLs (CRITICAL)
1. Navigate to: **Authentication** → **URL Configuration**
2. Add these redirect URLs:
   ```
   http://localhost:5000/dashboard.html
   http://localhost:5000/login.html
   http://localhost:5000/signup.html
   ```
3. For production, also add:
   ```
   https://yourdomain.com/dashboard.html
   https://yourdomain.com/login.html
   https://yourdomain.com/signup.html
   ```
4. Click **Save**

### Step 3: Setup Google OAuth

#### Get Google Credentials:
1. Go to https://console.cloud.google.com
2. Create a new project (or use existing)
3. Enable **Google+ API**
4. Go to **Credentials** → **Create Credentials** → **OAuth 2.0 Client ID**
5. Choose **Web application**
6. Add authorized redirect URI:
   ```
   https://wslsihrnaeoqojpzkjpy.supabase.co/auth/v1/callback?provider=google
   ```
7. Copy the **Client ID** and **Client Secret**

#### Add to Supabase:
1. In Supabase, go to: **Authentication** → **Providers** → **Google**
2. Enable the provider
3. Paste your **Client ID** and **Client Secret**
4. Click **Save**

### Step 4: Setup GitHub OAuth

#### Get GitHub Credentials:
1. Go to https://github.com/settings/developers
2. Click **New OAuth App**
3. Fill in:
   - **Application name**: ByteShelf
   - **Homepage URL**: `http://localhost:5000`
   - **Authorization callback URL**: 
     ```
     https://wslsihrnaeoqojpzkjpy.supabase.co/auth/v1/callback?provider=github
     ```
4. Copy the **Client ID** and **Client Secret**

#### Add to Supabase:
1. In Supabase, go to: **Authentication** → **Providers** → **GitHub**
2. Enable the provider
3. Paste your **Client ID** and **Client Secret**
4. Click **Save**

## 🧪 Testing

1. Start your application:
   ```bash
   npm run start
   ```

2. Open your browser and go to:
   ```
   http://localhost:5000/login.html
   ```

3. Click **"Continue with Google"** or **"Continue with GitHub"**

4. Select your account

5. You should be redirected to `http://localhost:5000/dashboard.html`

6. You should see "Welcome back!" message

## 🔍 Troubleshooting

### Error: "This site can't be reached"
**Cause**: Redirect URL not registered in Supabase
**Fix**: 
- Go to Supabase → Authentication → URL Configuration
- Add `http://localhost:5000/dashboard.html`
- Make sure your app is running on port 5000

### Error: "Invalid redirect_uri"
**Cause**: Redirect URL doesn't match exactly
**Fix**:
- Check for typos in the URL
- Ensure no trailing slashes
- Verify protocol (http vs https)
- Check port number

### Error: "OAuth provider not configured"
**Cause**: Provider not enabled or credentials missing
**Fix**:
- Go to Supabase → Authentication → Providers
- Enable the provider (toggle switch)
- Add valid Client ID and Client Secret
- Click Save

### OAuth button doesn't work
**Cause**: Supabase client not initialized
**Fix**:
- Check browser console (F12) for errors
- Ensure Supabase CDN is loaded: `https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2`
- Verify Supabase URL and Key are correct

### Session not persisting after login
**Cause**: localStorage disabled or session not detected
**Fix**:
- Check browser console for errors
- Ensure localStorage is enabled
- Check that `auth.js` is loaded
- Verify `onAuthStateChange()` is working

## 📊 How OAuth Flow Works

```
┌─────────────────────────────────────────────────────────────┐
│ 1. User clicks "Continue with Google/GitHub"                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Browser redirects to Google/GitHub login page            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. User authenticates with their account                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Google/GitHub redirects to Supabase callback URL         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Supabase processes auth code and creates session         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. Browser redirected to /dashboard.html                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 7. auth.js detects session via onAuthStateChange()          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 8. User logged in, session stored in localStorage           │
└─────────────────────────────────────────────────────────────┘
```

## 🔐 Security Notes

- **Publishable Key** (`sb_publishable_Ni8gulqDIn21i7qOGqymgQ_EiBZtdrv`) is safe to expose in frontend code
- **Client Secret** from Google/GitHub must be kept secure (server-side only)
- Never commit OAuth credentials to git
- Use environment variables for sensitive data in production
- Always use HTTPS in production

## 📁 Files Modified

| File | Change |
|------|--------|
| `All code/frontend/login.html` | OAuth redirect: `/index.html` → `/dashboard.html` |
| `All code/frontend/signup.html` | OAuth redirect: `/index.html` → `/dashboard.html` |
| `All code/frontend/assets/js/auth.js` | Verified Supabase configuration |

## 📚 Additional Resources

- **Supabase Auth Docs**: https://supabase.com/docs/guides/auth
- **Google OAuth Setup**: https://developers.google.com/identity/protocols/oauth2
- **GitHub OAuth Setup**: https://docs.github.com/en/developers/apps/building-oauth-apps
- **Supabase Community**: https://discord.supabase.com

## ✨ What's Next

1. ✅ Code changes applied
2. 📋 Configure Supabase (follow steps above)
3. 🧪 Test OAuth flow
4. 🚀 Deploy to production
5. 📊 Monitor for errors

## 💬 Need Help?

If you encounter issues:
1. Check browser console (F12) for error messages
2. Verify all Supabase settings match the guide
3. Ensure OAuth credentials are correct
4. Check that redirect URLs are registered
5. See troubleshooting section above

---

**Status**: ✅ Code Fixed | ⏳ Awaiting Supabase Configuration

