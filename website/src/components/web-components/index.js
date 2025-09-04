/**
 * Web Components Registry
 * Central place to register all custom web components
 */

import { MarkdownRenderer } from './MarkdownRenderer.js';

/**
 * Register a web component with error handling
 * @param {string} tagName - The custom element tag name
 * @param {typeof HTMLElement} componentClass - The web component class
 */
function registerComponent(tagName, componentClass) {
  try {
    // Check if component is already registered
    if (customElements.get(tagName)) {
      console.warn(`Web component "${tagName}" is already registered`);
      return;
    }
    
    customElements.define(tagName, componentClass);
    console.log(`✅ Registered web component: ${tagName}`);
  } catch (error) {
    console.error(`❌ Failed to register web component "${tagName}":`, error);
  }
}

/**
 * Register all available web components
 */
export function registerAllComponents() {
  registerComponent('markdown-renderer', MarkdownRenderer);
}

/**
 * Register individual components (for selective loading)
 */
export function registerMarkdownRenderer() {
  registerComponent('markdown-renderer', MarkdownRenderer);
}

// Note: Auto-registration removed to prevent duplicate registrations.
// Components are now registered explicitly from the consuming pages.