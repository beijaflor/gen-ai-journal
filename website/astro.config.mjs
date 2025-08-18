import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  // GitHub Pages configuration
  site: 'https://beijaflor.github.io',
  base: '/gen-ai-journal-dev',
  
  // Output configuration
  output: 'static',
  
  // Integrations
  integrations: [
    sitemap({
      customPages: [],
      i18n: {
        defaultLocale: 'ja',
        locales: {
          ja: 'ja-JP',
        },
      },
    }),
  ],
  
  // Markdown configuration
  markdown: {
    shikiConfig: {
      theme: 'github-light',
      wrap: true,
    },
  },
  
  // Vite configuration
  vite: {
    build: {
      rollupOptions: {
        output: {
          assetFileNames: 'assets/[name].[hash][extname]',
          chunkFileNames: 'chunks/[name].[hash].js',
          entryFileNames: 'entry/[name].[hash].js',
        },
      },
    },
    resolve: {
      alias: {
        '@': new URL('./src', import.meta.url).pathname,
        '@/components': new URL('./src/components', import.meta.url).pathname,
        '@/layouts': new URL('./src/layouts', import.meta.url).pathname,
        '@/utils': new URL('./src/utils', import.meta.url).pathname,
        '@/styles': new URL('./src/styles', import.meta.url).pathname,
      },
    },
  },
  
  // Server configuration for development
  server: {
    port: 4321,
    host: true,
  },
  
  // Build configuration
  build: {
    assets: 'assets',
  },
});