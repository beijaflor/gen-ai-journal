# GenAI Journal Website Technical Specifications

## Technology Stack

### Core Framework
- **Astro 5.x**: Static site generator with island architecture
- **TypeScript 5.9**: Type-safe development and build-time checking
- **Node.js 18+**: Runtime environment for build tools and development

### Development Tools
- **Biome 2.2**: Fast linter and formatter for TypeScript/JavaScript
- **Prettier 3.6**: Code formatting for Astro, CSS, and Markdown files
- **Git**: Version control and collaboration

### Deployment
- **GitHub Actions**: CI/CD pipeline for automated builds
- **GitHub Pages**: Static site hosting with HTTPS and CDN

## Content Schema

### Journal Entry
```typescript
interface JournalEntry {
  date: string;           // YYYY-MM-DD format
  type: 'main' | 'annex'; // Journal type
  title: string;          // Japanese title
  content: string;        // Markdown content
  summaryCount: number;   // Number of associated summaries
  metadata: {
    publishedAt: Date;
    updatedAt: Date;
    tags?: string[];
  };
}
```

### Summary Entry
```typescript
interface SummaryEntry {
  id: string;            // 3-digit ID (001, 002, etc.)
  date: string;          // YYYY-MM-DD (parent journal date)
  sourceUrl: string;     // Original article URL
  domain: string;        // Extracted domain name
  title: string;         // Japanese title from content
  content: string;       // Markdown summary content
  status: 'main' | 'annex' | 'omitted'; // Inclusion status
  filename: string;      // Original filename
  metadata: {
    wordCount: number;
    readingTime: number; // Estimated reading time in minutes
    tags?: string[];
  };
}
```

### Archive Entry
```typescript
interface ArchiveEntry {
  date: string;          // YYYY-MM-DD
  mainJournal: JournalEntry;
  annexJournal: JournalEntry;
  summaries: SummaryEntry[];
  omittedSummaries: SummaryEntry[];
  stats: {
    totalSummaries: number;
    mainSummaries: number;
    annexSummaries: number;
    omittedSummaries: number;
  };
}
```

## File Naming Conventions

### Source Content Structure
```
../journals/YYYY-MM-DD/
├── 00_weekly_journal_YYYY_MM_DD.md     # Main journal
├── 01_annex_journal_YYYY_MM_DD.md      # Annex journal
├── 02_omitted_summaries.md             # Omitted summaries
└── summaries/
    ├── 001_domain_com_path_slug.md     # Individual summaries
    ├── 002_another_domain_net_article.md
    └── ...
```

### Generated URL Structure
```
Content File                              → Website URL
00_weekly_journal_2025_08_16.md          → /journals/2025-08-16/main/
01_annex_journal_2025_08_16.md           → /journals/2025-08-16/annex/
summaries/001_example_com_article.md     → /summaries/2025-08-16/001/
summaries/002_another_site_jp_post.md    → /summaries/2025-08-16/002/
```

## Content Processing Logic

### Date Extraction
```typescript
function extractDateFromPath(filePath: string): string {
  // Extract YYYY-MM-DD from file path or filename
  const dateMatch = filePath.match(/(\d{4}-\d{2}-\d{2})/);
  return dateMatch ? dateMatch[1] : '';
}
```

### Summary ID Extraction
```typescript
function extractSummaryId(filename: string): string {
  // Extract 3-digit ID from filename like "001_example_com.md"
  const idMatch = filename.match(/^(\d{3})_/);
  return idMatch ? idMatch[1] : '';
}
```

### URL Reconstruction
```typescript
function reconstructUrl(filename: string): string {
  // Convert "001_example_com_path_article.md" to "https://example.com/path/article"
  const parts = filename.replace(/^\d{3}_/, '').replace(/\.md$/, '').split('_');
  const domain = parts[0].replace('_', '.');
  const path = parts.slice(1).join('/');
  return `https://${domain}/${path}`;
}
```

## Performance Requirements

### Loading Performance
- **First Contentful Paint (FCP)**: < 1.5 seconds
- **Largest Contentful Paint (LCP)**: < 2.5 seconds
- **Cumulative Layout Shift (CLS)**: < 0.1
- **First Input Delay (FID)**: < 100 milliseconds

### Build Performance
- **Full site build**: < 2 minutes for 1000+ pages
- **Incremental development builds**: < 10 seconds
- **Asset optimization**: Automatic image and CSS optimization

### Bundle Size Targets
- **Initial JavaScript bundle**: < 50KB gzipped
- **CSS bundle**: < 30KB gzipped
- **Images**: WebP format with fallbacks, responsive sizing

## Browser Support

### Primary Support
- **Chrome**: Latest 2 versions
- **Firefox**: Latest 2 versions
- **Safari**: Latest 2 versions
- **Edge**: Latest 2 versions

### Mobile Support
- **iOS Safari**: Latest 2 versions
- **Chrome Mobile**: Latest 2 versions
- **Samsung Internet**: Latest version

### Feature Requirements
- **CSS Grid**: Required for layout
- **CSS Custom Properties**: Required for theming
- **ES2020**: Minimum JavaScript feature set
- **WebP Images**: With fallback to JPEG/PNG

## Accessibility Requirements

### WCAG 2.1 Level AA Compliance
- **Color Contrast**: 4.5:1 for normal text, 3:1 for large text
- **Keyboard Navigation**: All interactive elements accessible via keyboard
- **Screen Reader Support**: Semantic HTML and ARIA labels
- **Focus Management**: Clear focus indicators and logical tab order

### Japanese Typography Accessibility
- **Font Size**: Minimum 16px for body text
- **Line Height**: 1.6-1.8 for optimal Japanese text readability
- **Character Spacing**: Appropriate spacing for Japanese characters
- **Mixed Content**: Proper handling of Japanese/English mixed text

## SEO Requirements

### Meta Tags
```html
<meta name="description" content="Weekly AI coding journal with curated articles and summaries">
<meta name="keywords" content="AI, プログラミング, コーディング, 開発, 人工知能">
<meta property="og:type" content="website">
<meta property="og:title" content="GenAI週刊 - AI・コーディング関連の週刊ジャーナル">
<meta property="og:description" content="AI開発ツールとコーディングの最新動向を週刊でお届け">
<meta property="og:image" content="/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
```

### Structured Data
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "GenAI週刊",
  "description": "AI・コーディング関連の週刊ジャーナル",
  "url": "https://example.github.io/gen-ai-journal",
  "inLanguage": "ja-JP"
}
```

### Sitemap Generation
- Automatic sitemap.xml generation
- Include all journal pages and summaries
- Update frequency: weekly
- Priority weighting based on content type

## Content Security Policy

### CSP Headers
```
Content-Security-Policy: 
  default-src 'self'; 
  script-src 'self' 'unsafe-inline'; 
  style-src 'self' 'unsafe-inline'; 
  img-src 'self' data: https:; 
  font-src 'self' https://fonts.googleapis.com https://fonts.gstatic.com;
```

### Security Considerations
- No inline scripts (except for critical CSS)
- All external resources loaded over HTTPS
- No user-generated content or forms
- Static content only, no server-side processing

## Internationalization

### Language Support
- **Primary Language**: Japanese (ja-JP)
- **Secondary Language**: English (for technical terms)
- **Text Direction**: Left-to-right (ltr)
- **Character Encoding**: UTF-8

### Typography
```css
font-family: 
  'Hiragino Kaku Gothic ProN', 
  'Hiragino Sans', 
  Meiryo, 
  'Yu Gothic', 
  sans-serif;
```

## Build Configuration

### Astro Configuration
```typescript
export default defineConfig({
  site: 'https://username.github.io',
  base: '/gen-ai-journal',
  output: 'static',
  integrations: [
    sitemap(),
    compress(),
  ],
  vite: {
    build: {
      rollupOptions: {
        output: {
          assetFileNames: 'assets/[name].[hash][extname]',
          chunkFileNames: 'chunks/[name].[hash].js',
          entryFileNames: 'entry/[name].[hash].js'
        }
      }
    }
  }
});
```

### TypeScript Configuration
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@/components/*": ["src/components/*"],
      "@/layouts/*": ["src/layouts/*"],
      "@/utils/*": ["src/utils/*"]
    }
  }
}
```

## Error Handling

### Build-Time Errors
- **Missing Content**: Graceful handling of missing journal files
- **Invalid Dates**: Validation of date formats and ranges
- **Broken Links**: Detection and reporting of invalid URLs
- **Content Parsing**: Error recovery for malformed markdown

### Runtime Errors
- **404 Pages**: Custom 404 page with navigation
- **Image Loading**: Fallback for missing images
- **JavaScript Errors**: Graceful degradation for JS failures

## Monitoring and Analytics

### Performance Monitoring
- Core Web Vitals tracking
- Build time monitoring
- Page load speed analysis

### Usage Analytics
- Google Analytics 4 (optional)
- Privacy-compliant tracking
- Japanese user behavior insights

---

These technical specifications ensure the GenAI Journal website meets high standards for performance, accessibility, and maintainability while providing an excellent user experience for Japanese content consumption.