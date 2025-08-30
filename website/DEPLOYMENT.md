# Deployment Guide

## GitHub Pages Deployment

This Astro website is configured for automatic deployment to GitHub Pages using GitHub Actions.

### Setup

1. **Enable GitHub Pages**:
   - Go to repository Settings > Pages
   - Set Source to "GitHub Actions"
   - The workflow will automatically deploy on pushes to `main` or `development` branches

2. **Environment Variables**:
   - `ASTRO_BASE`: Set automatically by GitHub Actions based on repository name
   - Site URL: `https://shootani.github.io/gen-ai-journal-dev/`

### Manual Deployment

If you need to deploy manually:

```bash
# Build the site
cd website
npm run build

# The built files will be in the dist/ directory
```

### Development

```bash
# Start development server
cd website
npm run dev

# Visit http://localhost:4321
```

### Build Process

The deployment workflow includes:
1. Type checking with TypeScript
2. Code linting with Biome
3. Building the Astro site
4. Uploading to GitHub Pages

### Base Path Handling

The site uses the `withBase()` utility function to handle GitHub Pages base paths correctly. All internal links should use this utility to ensure proper navigation.

### Triggering Deployment

Deployment is triggered by:
- Pushes to `main` or `development` branches that modify files in `website/` or `journals/`
- Pull requests with the `deploy-preview` label that modify files in `website/` or `journals/`
- Manual workflow dispatch from the Actions tab

#### Pull Request Deployments

To deploy a preview of your changes in a pull request:
1. Create a pull request with changes to `website/` or `journals/`
2. Add the `deploy-preview` label to the pull request
3. The workflow will automatically build and deploy the preview

Note: PR deployments will overwrite the main site temporarily. Remove the `deploy-preview` label if you want to stop deployments for that PR.