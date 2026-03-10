# ByteShelf Frontend

Modern, responsive website for the ByteShelf CS knowledge platform.

## Structure

```
frontend/
├── assets/
│   ├── css/           # Future CSS files (currently inline)
│   └── js/            # Future JS files (currently inline)
├── index.html         # Main website file
├── package.json       # Frontend configuration
└── README.md          # This file
```

## Features

### Design
- **Modern UI**: Clean, professional design with CS theme
- **Responsive**: Mobile-first approach, works on all devices
- **Dark Theme**: Modern dark color scheme with accent colors
- **Typography**: Space Mono (monospace) and Syne (sans-serif) fonts

### Interactive Elements
- **Custom Cursor**: Animated cursor with ring effect (desktop only)
- **Smooth Scrolling**: CSS scroll-behavior and JavaScript animations
- **Hover Effects**: Interactive cards, buttons, and navigation
- **Mobile Menu**: Hamburger menu for mobile devices

### Sections
1. **Hero**: Main landing with animated statistics
2. **Categories**: CS topic categories with hover effects
3. **Featured Books**: Book showcase with overlay previews
4. **How It Works**: 4-step process explanation
5. **Pricing**: 3-tier pricing plans
6. **Testimonials**: Student reviews
7. **CTA**: Call-to-action section
8. **Footer**: Links and company information

### Technical Details
- **CSS Grid & Flexbox**: Modern layout techniques
- **CSS Custom Properties**: Consistent theming with CSS variables
- **Intersection Observer**: Scroll-triggered animations
- **Media Queries**: Responsive breakpoints
- **Semantic HTML**: Accessible markup structure

## Development

The website is currently a single HTML file with inline CSS and JavaScript. For larger projects, consider:

1. **Extracting CSS**: Move styles to `assets/css/main.css`
2. **Extracting JS**: Move scripts to `assets/js/main.js`
3. **Build Process**: Add bundling/minification tools
4. **Component System**: Consider a framework like React/Vue

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Graceful degradation for older browsers

## Performance

- **Optimized CSS**: Efficient selectors and minimal reflows
- **Lazy Loading**: Intersection Observer for animations
- **Font Loading**: Google Fonts with display=swap
- **Minimal JavaScript**: Vanilla JS, no heavy frameworks