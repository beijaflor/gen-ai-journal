# Web Components

This directory contains reusable web components for the GenAI Journal website.

## Components

### MarkdownRenderer

A web component that converts markdown content to HTML using the marked library.

**Usage:**
```html
<markdown-renderer class="content-class">
# Your Markdown Content

This will be converted to HTML.
</markdown-renderer>
```

**Features:**
- Converts markdown to HTML using marked.js
- Waits for marked library to load from CDN
- Graceful fallback for basic line breaks if marked fails
- Configurable marked options (GFM, breaks enabled)

## Registration

Components can be registered individually or all at once:

```javascript
import { registerAllComponents, registerMarkdownRenderer } from '@/components/web-components/index.js';

// Register all components
registerAllComponents();

// Or register individual components
registerMarkdownRenderer();
```

## File Structure

```
web-components/
├── MarkdownRenderer.js    # MarkdownRenderer component
├── index.js              # Central registry and exports
└── README.md             # This documentation
```

## Adding New Components

1. Create a new component file (e.g., `NewComponent.js`)
2. Export the component class
3. Add import and registration function in `index.js`
4. Update this README

## Dependencies

- **marked.js**: Loaded from CDN for markdown parsing
- **Native Web Components**: Uses standard CustomElementRegistry API