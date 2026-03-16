# OAuth Login Fix Guide - ByteShelf

## Problem Summary
When users click "Continue with Google" or "Continue with GitHub" and select an account, they get a "This site can't be reached" error. This is because the OAuth redirect URL is not properly configured in your Supabase project.

## Root Causes

1. **Missing Redirect URL Configuration**: The OAuth redirect URLs are not registered in your Supabase project settings
2. **Incorrect Redirect Path**: The redirect was pointing to `/index.html` instead of `/dashboard.html`
3. **CORS/Domain Issues**: The redirect domain might not be whitelisted in Supabase

## Solution Steps

### Step 1: Update Supabase OAuth Redirect URLs

1. Go to your Supabase Dashboard: https://app.supabase.com
2. Select your project: `wslsihrnaeoqojpzkjpy`
3. Navigate to **Authentication** → **URL Configuration**
4. Add the following redirect URLs under "Redirect URLs":
   - `http://localhost:5000/dashboard.html` (for local development)
   - `http://localhost:5000/login.html` (fallback)
   - `http://localhost:5000/signup.html` (fallback)
   - Your production domain (e.g., `https://byteshelf.com/dashboard.html`)

### Step 2: Enable OAuth Providers

1. In Supabase Dashboard, go to **Authentication** → **Providers**
2. Enable **Google**:
   - Add your Google OAuth credentials (Client ID and Secret)
   - These come from Google Cloud Console
3. Enable **GitHub**:
   - Add your GitHub OAuth credentials (Client ID and Secret)
   - These come from GitHub Developer Settings

### Step 3: Verify Configuration

The following changes have been made to your code:

**File: `All code/frontend/login.html`**
- Updated OAuth redirect URL from `/index.html` to `/dashboard.html`

**File: `All code/frontend/signup.html`**
- Updated OAuth redirect URL from `/index.html` to `/dashboard.html`

**File: `All code/frontend/assets/js/auth.js`**
- Verified Supabase configuration is correct
- The `handleOAuthSession()` function properly handles OAuth callbacks

### Step 4: Test the Fix

1. Start your application:
   ```bash
   npm run start
   ```

2. Navigate to `http://localhost:5000/login.html`

3. Click "Continue with Google" or "Continue with GitHub"

4. Select your account

5. You should now be redirected to `/dashboard.html` successfully

## How OAuth Flow Works

1. User clicks "Continue with Google/GitHub"
2. Browser redirects to Supabase OAuth endpoint
3. User authenticates with Google/GitHub
4. OAuth provider redirects back to your app with auth code
5. Supabase processes the code and creates a session
6. User is redirected to the `redirectTo` URL (now `/dashboard.html`)
7. `auth.js` detects the session and logs the user in

## Troubleshooting

### "This site can't be reached" Error
- **Cause**: Redirect URL not registered in Supabase
- **Fix**: Add the URL to Supabase URL Configuration (Step 1)

### "Invalid redirect URL" Error
- **Cause**: The redirect URL doesn't match exactly what's registered
- **Fix**: Ensure the URL matches exactly (including protocol, domain, and path)

### OAuth Provider Not Showing
- **Cause**: Provider not enabled or credentials missing
- **Fix**: Enable the provider and add credentials in Supabase (Step 2)

### Session Not Persisting
- **Cause**: `handleOAuthSession()` not detecting the session
- **Fix**: Check browser console for errors, ensure Supabase client is loaded

## Important Notes

- The Supabase URL and Key are already configured in your code
- The OAuth session is automatically detected via `onAuthStateChange()`
- User data is stored in localStorage for persistence
- The session expires after 24 hours unless "Remember me" is checked

## Files Modified

1. `All code/frontend/login.html` - OAuth redirect URL
2. `All code/frontend/signup.html` - OAuth redirect URL

## Next Steps

1. Get OAuth credentials from Google and GitHub
2. Add them to your Supabase project
3. Register the redirect URLs in Supabase
4. Test the OAuth flow
5. Deploy to production with your production domain

