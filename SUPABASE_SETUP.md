# Supabase OAuth Setup Instructions

## Your Supabase Project Details
- **Project URL**: https://wslsihrnaeoqojpzkjpy.supabase.co
- **Publishable Key**: sb_publishable_Ni8gulqDIn21i7qOGqymgQ_EiBZtdrv

## Quick Setup Checklist

### 1. Access Supabase Dashboard
- Go to: https://app.supabase.com
- Sign in with your account
- Select project: `wslsihrnaeoqojpzkjpy`

### 2. Configure Redirect URLs
**Path**: Authentication → URL Configuration

Add these redirect URLs:
```
http://localhost:5000/dashboard.html
http://localhost:5000/login.html
http://localhost:5000/signup.html
```

For production, add:
```
https://yourdomain.com/dashboard.html
https://yourdomain.com/login.html
https://yourdomain.com/signup.html
```

### 3. Setup Google OAuth

**Path**: Authentication → Providers → Google

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select existing one
3. Enable Google+ API
4. Create OAuth 2.0 credentials (Web application)
5. Add authorized redirect URIs:
   - `https://wslsihrnaeoqojpzkjpy.supabase.co/auth/v1/callback?provider=google`
6. Copy Client ID and Client Secret
7. Paste into Supabase Google provider settings
8. Click "Save"

### 4. Setup GitHub OAuth

**Path**: Authentication → Providers → GitHub

1. Go to [GitHub Developer Settings](https://github.com/settings/developers)
2. Click "New OAuth App"
3. Fill in:
   - Application name: ByteShelf
   - Homepage URL: `http://localhost:5000` (or your domain)
   - Authorization callback URL: `https://wslsihrnaeoqojpzkjpy.supabase.co/auth/v1/callback?provider=github`
4. Copy Client ID and Client Secret
5. Paste into Supabase GitHub provider settings
6. Click "Save"

### 5. Test OAuth Flow

1. Start your app:
   ```bash
   npm run start
   ```

2. Go to: `http://localhost:5000/login.html`

3. Click "Continue with Google" or "Continue with GitHub"

4. Select your account

5. You should be redirected to dashboard.html

## Troubleshooting

### Error: "Invalid redirect_uri"
- **Solution**: Ensure the redirect URL in Supabase URL Configuration matches exactly
- Check for trailing slashes, protocol (http vs https), and port numbers

### Error: "OAuth provider not configured"
- **Solution**: Enable the provider in Authentication → Providers
- Add valid Client ID and Client Secret

### Error: "This site can't be reached"
- **Solution**: Add the redirect URL to Supabase URL Configuration
- Make sure your app is running on the correct port (5000)

### Session not persisting after OAuth
- **Solution**: Check browser console for errors
- Ensure localStorage is enabled
- Check that Supabase client is properly initialized

## OAuth Flow Diagram

```
User clicks "Continue with Google"
         ↓
Browser redirects to Google OAuth
         ↓
User authenticates with Google
         ↓
Google redirects to Supabase callback
         ↓
Supabase processes auth code
         ↓
Browser redirected to /dashboard.html
         ↓
auth.js detects session via onAuthStateChange()
         ↓
User logged in and session stored in localStorage
```

## Security Notes

- Never commit your OAuth credentials to git
- Use environment variables for sensitive data in production
- The publishable key is safe to expose (it's for client-side use)
- Keep your Client Secret secure (server-side only)

## Support

For issues with Supabase OAuth:
- [Supabase Auth Docs](https://supabase.com/docs/guides/auth)
- [Supabase Discord Community](https://discord.supabase.com)

