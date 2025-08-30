/**
 * MarkdownRenderer Web Component
 * Renders markdown content as HTML using the marked library
 */

class MarkdownRenderer extends HTMLElement {
  connectedCallback() {
    // Get the markdown content from the slot
    const markdownContent = this.textContent || '';
    
    if (markdownContent.trim()) {
      this.renderMarkdown(markdownContent);
    }
  }

  async renderMarkdown(content) {
    try {
      // Wait for marked to be available (loaded from CDN)
      await this.waitForMarked();
      
      // Configure marked for better output
      if (typeof marked !== 'undefined') {
        marked.setOptions({
          breaks: true,
          gfm: true,
        });
        
        // Convert markdown to HTML
        const htmlContent = marked.parse(content);
        // Replace the content with rendered HTML
        this.innerHTML = htmlContent;
      } else {
        this.fallbackRender(content);
      }
    } catch (error) {
      console.warn('Failed to parse markdown:', error);
      this.fallbackRender(content);
    }
  }

  async waitForMarked(timeout = 5000) {
    return new Promise((resolve, reject) => {
      // If marked is already available, resolve immediately
      if (typeof marked !== 'undefined') {
        resolve();
        return;
      }

      let attempts = 0;
      const maxAttempts = timeout / 100; // Check every 100ms
      
      const checkForMarked = () => {
        if (typeof marked !== 'undefined') {
          resolve();
        } else if (attempts >= maxAttempts) {
          reject(new Error('Marked library failed to load within timeout'));
        } else {
          attempts++;
          setTimeout(checkForMarked, 100);
        }
      };
      
      checkForMarked();
    });
  }

  fallbackRender(content) {
    // Basic fallback: convert line breaks to <br> tags
    this.innerHTML = content.replace(/\n/g, '<br>');
  }
}

// Export the class for registration
export { MarkdownRenderer };