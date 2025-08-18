# Development Workflow Guide

## Quick Start

### Prerequisites
- **Node.js 18+** installed
- **Git** configured
- Access to the parent repository with journal content

### Initial Setup
```bash
# Navigate to the project root
cd /path/to/gen-ai-journal-dev

# Navigate to website directory
cd website/

# Install dependencies
npm install

# Start development server
npm run dev
```

The development server will be available at `http://localhost:4321`

## Development Commands

### Core Development
```bash
npm run dev          # Start development server with hot reload
npm run build        # Build for production
npm run preview      # Preview production build locally
npm run clean        # Clean build artifacts
```

### Code Quality
```bash
npm run check        # Run all quality checks (type + lint)
npm run type-check   # TypeScript type checking only
npm run lint         # Biome linting only
npm run lint:fix     # Auto-fix linting issues
npm run format       # Format code with Prettier
npm run check:fix    # Auto-fix all issues (format + lint)
```

### Testing
```bash
npm run test         # Run tests (when implemented)
npm run test:watch   # Run tests in watch mode
```

## Code Quality Standards

### TypeScript
- **Strict mode enabled**: All type errors must be resolved
- **No any types**: Use proper type definitions
- **Interface definitions**: Define interfaces for all data structures
- **Path mapping**: Use `@/` aliases for clean imports

### Linting (Biome)
- **ESLint-compatible rules**: Modern JavaScript/TypeScript standards
- **Import sorting**: Automatic import organization
- **Performance rules**: Prevent common performance anti-patterns
- **Accessibility rules**: Basic a11y compliance checking

### Formatting (Prettier)
- **Astro components**: Consistent component formatting
- **TypeScript/JavaScript**: Standard formatting rules
- **CSS**: Organized property ordering
- **Markdown**: Consistent markdown formatting

## File Organization

### Component Structure
```typescript
// Good: Proper component structure
---
// Frontmatter: imports and logic
import Layout from '@/layouts/BaseLayout.astro';
import type { SummaryEntry } from '@/utils/content-parser';

interface Props {
  summary: SummaryEntry;
}

const { summary } = Astro.props;
---

<!-- HTML template -->
<Layout title={summary.title}>
  <article>
    <h1>{summary.title}</h1>
    <div set:html={summary.content} />
  </article>
</Layout>

<style>
  /* Scoped styles */
  article {
    max-width: 800px;
    margin: 0 auto;
  }
</style>
```

### Import Organization
```typescript
// 1. Node modules
import { defineConfig } from 'astro/config';

// 2. Internal utilities
import { parseJournalContent } from '@/utils/content-parser';

// 3. Components
import Layout from '@/layouts/BaseLayout.astro';
import SummaryCard from '@/components/SummaryCard.astro';

// 4. Types
import type { JournalEntry, SummaryEntry } from '@/utils/types';
```

### CSS Guidelines
```css
/* Use CSS custom properties for theming */
:root {
  --color-primary: #2563eb;
  --color-text: #1f2937;
  --font-body: 'Hiragino Kaku Gothic ProN', sans-serif;
  --spacing-unit: 1rem;
}

/* Use semantic class names */
.journal-preview {
  padding: calc(var(--spacing-unit) * 2);
  border-radius: 8px;
}

/* Mobile-first responsive design */
.summary-grid {
  display: grid;
  gap: var(--spacing-unit);
  
  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }
  
  @media (min-width: 1024px) {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

## Git Workflow

### Branch Strategy
```bash
# Main development branch
main

# Feature branches
feature/add-search-functionality
feature/improve-mobile-navigation
feature/add-rss-feed

# Bug fix branches
fix/summary-parsing-error
fix/mobile-layout-issue

# Documentation updates
docs/update-architecture
docs/add-api-reference
```

### Commit Convention
```bash
# Format: type(scope): description
# Types: feat, fix, docs, style, refactor, test, chore

# Examples
feat(components): add SummaryCard component
fix(parser): handle malformed summary filenames
docs(readme): update setup instructions
style(css): improve Japanese typography
refactor(utils): simplify date parsing logic
test(parser): add content parsing tests
chore(deps): update Astro to v4.1.0
```

### Pre-commit Workflow
```bash
# Before committing, run quality checks
npm run check:fix    # Auto-fix formatting and linting
npm run type-check   # Ensure no type errors
npm run build       # Verify build works

# Then commit
git add .
git commit -m "feat(pages): add journal archive page"
```

## Content Development

### Working with Journal Content
```typescript
// Content is read from ../journals/ directory
// Development workflow respects the existing structure:

../journals/2025-08-16/
├── 00_weekly_journal_2025_08_16.md     # → /journals/2025-08-16/main/
├── 01_annex_journal_2025_08_16.md      # → /journals/2025-08-16/annex/
├── 02_omitted_summaries.md             # → Used in summary listing
└── summaries/
    ├── 001_example_com_article.md      # → /summaries/2025-08-16/001/
    └── ...
```

### Testing Content Changes
```bash
# When journal content is updated:
npm run dev          # Hot reload will pick up changes
npm run build        # Test production build
npm run preview      # Test built site locally
```

### Adding New Content Types
1. Update TypeScript interfaces in `src/utils/types.ts`
2. Modify content parser in `src/utils/content-parser.ts`
3. Add new page templates in `src/pages/`
4. Update navigation in `src/components/Navigation.astro`
5. Add tests for new functionality

## Performance Optimization

### Development Performance
- **Hot Module Replacement**: Changes reflect instantly during development
- **Incremental Builds**: Only changed files are rebuilt
- **TypeScript Caching**: Type checking is cached for faster rebuilds

### Production Performance
```bash
# Analyze bundle size
npm run build        # Check build output size
npm run preview      # Test performance locally

# Check Core Web Vitals
# Use browser dev tools or online tools to verify:
# - First Contentful Paint < 1.5s
# - Largest Contentful Paint < 2.5s
# - Cumulative Layout Shift < 0.1
```

### Image Optimization
```astro
---
// Use Astro's built-in image optimization
import { Image } from 'astro:assets';
import heroImage from '@/assets/hero.jpg';
---

<Image 
  src={heroImage} 
  alt="Hero image" 
  width={800} 
  height={400}
  format="webp"
  quality={80}
/>
```

## Debugging

### Common Issues and Solutions

#### Content Not Loading
```bash
# Check content path resolution
npm run dev -- --verbose

# Verify file structure
ls -la ../journals/

# Check content parser
npm run type-check
```

#### Build Failures
```bash
# Clear cache and rebuild
rm -rf node_modules/.astro
npm run build

# Check for TypeScript errors
npm run type-check

# Check for linting issues
npm run lint
```

#### Styling Issues
```bash
# Check CSS compilation
npm run dev          # Check browser console for CSS errors

# Verify CSS syntax
npm run lint         # Biome checks CSS in .astro files
```

### Debug Configuration
```typescript
// astro.config.mjs - Enable debugging
export default defineConfig({
  // Enable verbose logging
  vite: {
    logLevel: 'info',
    build: {
      sourcemap: true  // Enable source maps for debugging
    }
  }
});
```

## IDE Configuration

### VS Code Settings
```json
// .vscode/settings.json
{
  "typescript.preferences.importModuleSpecifier": "relative",
  "editor.defaultFormatter": "biomejs.biome",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true,
    "source.fixAll": true
  },
  "files.associations": {
    "*.astro": "astro"
  }
}
```

### Recommended Extensions
- **Astro**: Official Astro language support
- **Biome**: Linting and formatting
- **TypeScript Importer**: Auto-import management
- **Japanese Language Pack**: Better Japanese character support

## Deployment

### GitHub Actions Pipeline
```yaml
# Automatic deployment on push to main
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
  
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: 'npm'
          cache-dependency-path: website/package-lock.json
      
      - name: Install dependencies
        run: cd website && npm ci
        
      - name: Run quality checks
        run: cd website && npm run check
        
      - name: Build site
        run: cd website && npm run build
        
      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v2
        with:
          path: website/dist
```

### Manual Deployment
```bash
# Build for production
npm run build

# The built site is in dist/ directory
# Deploy dist/ contents to your hosting service
```

## Troubleshooting

### Environment Issues
```bash
# Check Node.js version
node --version       # Should be 18+

# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### Content Issues
```bash
# Verify journal structure
find ../journals -name "*.md" | head -10

# Check content parser
node -e "
const { parseJournalContent } = require('./src/utils/content-parser.ts');
console.log(parseJournalContent('../journals/2025-08-16'));
"
```

---

This development workflow ensures consistent, high-quality code while maintaining fast development cycles and reliable deployments.