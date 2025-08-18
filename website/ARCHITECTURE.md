# GenAI Journal Website Architecture

## Overview

This document describes the architecture for the GenAI Journal website, an Astro-based static site that publishes weekly curated journals about AI and coding developments. The website provides access to main journals, annex journals, and individual summaries including omitted content.

## System Architecture

```
┌─────────────────────┐    ┌──────────────────────┐    ┌─────────────────────┐
│   Content Source    │    │    Astro Website     │    │   GitHub Pages      │
│   (../journals/)    │───▶│   (website/)         │───▶│   (Published Site)  │
│                     │    │                      │    │                     │
│  - Weekly journals  │    │  - Static site gen   │    │  - Public website   │
│  - Individual       │    │  - Content parsing   │    │  - Fast CDN         │
│    summaries        │    │  - Japanese typography│    │  - HTTPS/SSL        │
│  - Metadata         │    │  - Responsive design │    │                     │
└─────────────────────┘    └──────────────────────┘    └─────────────────────┘
```

## Directory Structure

```
website/
├── ARCHITECTURE.md              # This document
├── TECHNICAL_SPECS.md           # Technical specifications
├── DEVELOPMENT.md               # Development workflow
├── CONTENT_INTEGRATION.md       # Content processing details
├── README.md                    # Project overview and setup
├── package.json                 # Dependencies and scripts
├── astro.config.mjs            # Astro configuration
├── tsconfig.json               # TypeScript configuration
├── biome.json                  # Biome linter configuration
├── .prettierrc                 # Prettier formatter configuration
├── .prettierignore             # Prettier ignore rules
├── .gitignore                  # Git ignore patterns
├── src/
│   ├── layouts/
│   │   ├── BaseLayout.astro        # Base layout with meta tags, nav
│   │   ├── JournalLayout.astro     # Layout for journal pages
│   │   └── SummaryLayout.astro     # Layout for individual summaries
│   ├── pages/
│   │   ├── index.astro             # Homepage
│   │   ├── archive.astro           # Archive of all journals
│   │   ├── journals/
│   │   │   └── [date]/
│   │   │       ├── index.astro         # Journal week overview
│   │   │       ├── main.astro          # Main journal
│   │   │       ├── annex.astro         # Annex journal
│   │   │       └── summaries.astro     # All summaries list
│   │   └── summaries/
│   │       └── [date]/
│   │           └── [id].astro          # Individual summary page
│   ├── components/
│   │   ├── Navigation.astro        # Site navigation
│   │   ├── JournalPreview.astro    # Journal preview card
│   │   ├── SummaryCard.astro       # Summary preview card
│   │   └── Meta.astro              # SEO meta tags component
│   ├── utils/
│   │   ├── content-parser.ts       # Parse journal/summary content
│   │   ├── url-utils.ts           # URL generation and parsing
│   │   └── date-utils.ts          # Date formatting utilities
│   └── styles/
│       ├── global.css             # Global styles
│       ├── typography.css         # Japanese typography
│       └── components.css         # Component-specific styles
├── public/
│   ├── favicon.ico               # Site favicon
│   └── robots.txt               # Search engine directives
└── dist/                        # Built static site (generated)
```

## Data Flow

### Content Source to Website

1. **Content Source**: Existing journal structure in `../journals/`
2. **Content Parsing**: Astro reads and parses markdown files during build
3. **Static Generation**: Astro generates static HTML/CSS/JS
4. **Deployment**: GitHub Actions builds and deploys to GitHub Pages

```
../journals/2025-08-16/
├── 00_weekly_journal_2025_08_16.md     ──┐
├── 01_annex_journal_2025_08_16.md      ──┤
├── 02_omitted_summaries.md             ──┼──▶ Astro Build ──▶ Static Site
└── summaries/                          ──┤
    ├── 001_source_url.md               ──┤
    ├── 002_another_source.md           ──┤
    └── ...                             ──┘
```

## Component Architecture

### Layout Hierarchy
```
BaseLayout.astro (HTML structure, meta tags, navigation)
├── JournalLayout.astro (Journal-specific styling and structure)
├── SummaryLayout.astro (Summary-specific styling and structure)
└── Page-specific components
```

### Component Relationships
```
Navigation.astro ──┬── Used in BaseLayout.astro
                   └── Provides site-wide navigation

JournalPreview.astro ──┬── Used in homepage and archive
                       └── Shows journal preview cards

SummaryCard.astro ──┬── Used in summary lists
                    └── Shows summary preview cards

Meta.astro ──┬── Used in BaseLayout.astro
             └── Handles SEO meta tags and Open Graph
```

## Routing Strategy

### URL Structure
```
/                                    # Homepage
/archive/                           # Archive of all journals
/journals/2025-08-16/               # Journal week overview
/journals/2025-08-16/main/          # Main journal
/journals/2025-08-16/annex/         # Annex journal
/journals/2025-08-16/summaries/     # All summaries list
/summaries/2025-08-16/001/          # Individual summary
/summaries/2025-08-16/002/          # Another summary
```

### Dynamic Routes
- `[date]` parameter: Matches journal dates (YYYY-MM-DD format)
- `[id]` parameter: Matches summary IDs (3-digit numbers)

## Content Processing

### Journal Content
- **Main Journal**: `00_weekly_journal_YYYY_MM_DD.md`
- **Annex Journal**: `01_annex_journal_YYYY_MM_DD.md`
- **Omitted Summaries**: `02_omitted_summaries.md`

### Individual Summaries
- **Location**: `summaries/XXX_domain_path.md`
- **ID Extraction**: First 3 digits of filename
- **URL Extraction**: Remainder of filename converted to URL
- **Metadata**: Derived from filename and content

### Content Collections
Astro content collections provide type-safe access to:
- Journal entries with frontmatter
- Summary metadata and content
- Date-based organization and sorting

## Static Analysis and Quality

### Tools Integration
- **Biome**: Fast linting and formatting for TypeScript/JavaScript
- **Prettier**: Code formatting for Astro, CSS, and Markdown
- **TypeScript**: Type checking and IntelliSense
- **Astro Check**: Astro-specific type checking

### Development Workflow
```
Code Changes ──▶ Biome Lint ──▶ Prettier Format ──▶ TypeScript Check ──▶ Build
```

## Build and Deployment

### Local Development
```bash
cd website/
npm run dev          # Start dev server with hot reload
npm run check        # Run all quality checks
npm run build        # Production build
npm run preview      # Preview production build
```

### GitHub Actions Pipeline
```
Push to main ──▶ Install deps ──▶ Quality checks ──▶ Build ──▶ Deploy to Pages
```

### Performance Considerations
- **Static Generation**: All pages pre-built for fast loading
- **Image Optimization**: Astro's built-in image optimization
- **CSS Optimization**: Scoped styles and automatic optimization
- **JavaScript**: Minimal client-side JavaScript for fast loading

## Accessibility and Internationalization

### Japanese Typography
- Proper font stacks for Japanese text
- Appropriate line heights and spacing
- Responsive typography for mobile devices

### Accessibility
- Semantic HTML structure
- Proper heading hierarchy
- Alt text for images
- Keyboard navigation support
- Screen reader compatibility

## Security Considerations

### Content Security
- Static site generation eliminates many attack vectors
- No server-side processing of user input
- Content sourced from trusted local files only

### Deployment Security
- HTTPS by default through GitHub Pages
- No sensitive data in client-side code
- Secure build pipeline through GitHub Actions

## Future Extensibility

### Planned Enhancements
- Full-text search functionality
- Advanced filtering and categorization
- Tag-based discovery
- Related content suggestions
- RSS feed enhancements

### Extension Points
- Plugin system through Astro integrations
- Custom components for enhanced functionality
- API integration for dynamic features
- Progressive Web App capabilities

## Performance Targets

### Loading Performance
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Cumulative Layout Shift: < 0.1

### Build Performance
- Full site build: < 2 minutes
- Incremental builds during development: < 10 seconds

---

This architecture provides a solid foundation for the GenAI Journal website while maintaining flexibility for future enhancements and ensuring excellent performance and user experience.