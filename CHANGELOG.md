# ByteShelf Changelog

## Version 1.1.0 - March 16, 2026

### 🎉 Major Features Added

#### PDF Reader Implementation
- ✅ Full-featured PDF viewer with page navigation
- ✅ Zoom controls (50% - 200%)
- ✅ Multiple themes (Dark, Light, Sepia)
- ✅ Reading progress tracking with persistent storage
- ✅ Keyboard shortcuts for navigation
- ✅ Progress bar with click-to-seek functionality
- ✅ Responsive design for all devices

#### Slideshow Mode
- ✅ Automatic page advancement (3 seconds fixed)
- ✅ Hidden controls (show on hover)
- ✅ Full-screen immersive display
- ✅ Smooth fade-in/out transitions
- ✅ Previous/Next/Exit navigation
- ✅ Page information display
- ✅ Multiple exit methods (button, ESC, click)

#### OAuth Login Fixes
- ✅ Fixed Google OAuth redirect URL
- ✅ Fixed GitHub OAuth redirect URL
- ✅ Updated redirect to dashboard.html
- ✅ Proper session handling

### 📁 Files Modified

#### Frontend
- `All code/frontend/pdf-reader.html` - New PDF reader with slideshow
- `All code/frontend/browse.html` - Added Read button
- `All code/frontend/my-books.html` - Added Read button
- `All code/frontend/login.html` - OAuth redirect fix
- `All code/frontend/signup.html` - OAuth redirect fix

#### Backend
- No backend changes required

#### Admin
- No admin changes required

### 📚 Documentation Added

- `PDF_READER_IMPLEMENTATION.md` - PDF reader feature guide
- `PDF_READER_QUICK_START.md` - Quick start guide
- `SLIDESHOW_MODE_GUIDE.md` - Slideshow feature guide
- `SLIDESHOW_QUICK_REFERENCE.md` - Quick reference
- `SLIDESHOW_IMPLEMENTATION_SUMMARY.md` - Implementation details
- `SLIDESHOW_FINAL_SUMMARY.md` - Final summary
- `SLIDESHOW_UPDATED_GUIDE.md` - Updated guide
- `OAUTH_FIX_GUIDE.md` - OAuth troubleshooting
- `OAUTH_FIX_SUMMARY.md` - OAuth fix summary
- `README_OAUTH_FIX.md` - OAuth setup guide
- `SUPABASE_SETUP.md` - Supabase configuration
- `QUICK_FIX_CHECKLIST.md` - Quick checklist

### 🎯 Features

#### PDF Reader
- Full PDF rendering with PDF.js
- Page navigation (buttons, input, keyboard)
- Zoom levels (50-200%)
- Three themes (Dark, Light, Sepia)
- Reading progress tracking
- Responsive design
- Mobile support

#### Slideshow Mode
- Automatic page advancement (3 seconds)
- Hidden controls (show on hover)
- Full-screen display
- Smooth transitions
- Navigation buttons
- Page information
- Exit hint
- Keyboard shortcuts

#### OAuth
- Google OAuth login
- GitHub OAuth login
- Proper redirect handling
- Session management

### 🐛 Bug Fixes

- Fixed OAuth redirect URL (was `/index.html`, now `/dashboard.html`)
- Fixed Google OAuth configuration
- Fixed GitHub OAuth configuration
- Improved session handling

### 🚀 Performance Improvements

- Optimized PDF rendering
- Efficient page caching
- Smooth transitions
- Minimal memory usage
- Fast page navigation

### 📱 Responsive Design

- Desktop support
- Tablet support
- Mobile support
- Touch-friendly controls
- Landscape/Portrait modes

### 🌐 Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers

### 📊 Testing

- ✅ PDF reader functionality
- ✅ Slideshow mode
- ✅ OAuth login
- ✅ Progress tracking
- ✅ Responsive design
- ✅ Browser compatibility
- ✅ Performance

### 🔄 Migration Guide

No migration needed. All features are backward compatible.

### 📝 Notes

- PDF reader requires admin server running on port 5001
- Slideshow uses fixed 3-second timing
- OAuth requires Supabase configuration
- All features are production-ready

### 🙏 Contributors

- ByteShelf Team

---

## Version 1.0.1 - Previous Release

### Features
- Basic website functionality
- Admin panel
- Book management
- User authentication

---

## Version 1.0.0 - Initial Release

### Features
- Initial ByteShelf platform
- Frontend and backend
- Admin panel
- Basic book management

