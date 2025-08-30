/**
 * MarkdownRenderer Web Component
 * Modern web component with Shadow DOM and HTML templates
 * Renders markdown content as HTML using the marked library
 */

// HTML template for the component
const template = document.createElement('template');
template.innerHTML = `
  <style>
    :host {
      display: block;
      font-family: var(--font-family-sans, 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', Meiryo, 'Yu Gothic', 'Noto Sans CJK JP', sans-serif);
      line-height: 1.7;
      color: var(--color-text, #1f2937);
    }

    .markdown-container {
      word-wrap: break-word;
      overflow-wrap: break-word;
    }

    .loading {
      color: var(--color-text-light, #6b7280);
      font-style: italic;
      opacity: 0.7;
    }

    .error {
      color: #dc2626;
      background-color: #fef2f2;
      padding: 1rem;
      border-radius: 0.5rem;
      border-left: 4px solid #dc2626;
    }

    /* Markdown content styling */
    ::slotted(*), .rendered-content * {
      max-width: 100%;
    }

    .rendered-content h1,
    .rendered-content h2,
    .rendered-content h3,
    .rendered-content h4,
    .rendered-content h5,
    .rendered-content h6 {
      margin-top: 2rem;
      margin-bottom: 1rem;
      font-weight: 600;
      line-height: 1.25;
      color: var(--color-text, #1f2937);
    }

    .rendered-content h1 {
      font-size: 2rem;
      border-bottom: 2px solid var(--color-border, #e5e7eb);
      padding-bottom: 0.5rem;
    }

    .rendered-content h2 {
      font-size: 1.5rem;
      border-bottom: 1px solid var(--color-border, #e5e7eb);
      padding-bottom: 0.3rem;
    }

    .rendered-content h3 {
      font-size: 1.25rem;
    }

    .rendered-content p {
      margin-bottom: 1rem;
      line-height: 1.7;
    }

    .rendered-content ul,
    .rendered-content ol {
      margin-bottom: 1rem;
      padding-left: 2rem;
    }

    .rendered-content li {
      margin-bottom: 0.5rem;
    }

    .rendered-content blockquote {
      margin: 1.5rem 0;
      padding: 1rem;
      background-color: var(--color-surface, #f8fafc);
      border-left: 4px solid var(--color-primary, #2563eb);
      border-radius: 0.5rem;
    }

    .rendered-content pre {
      background-color: var(--color-surface, #f8fafc);
      padding: 1rem;
      border-radius: 0.5rem;
      overflow-x: auto;
      margin: 1rem 0;
      font-family: var(--font-family-mono, 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace);
    }

    .rendered-content code {
      background-color: var(--color-surface, #f8fafc);
      padding: 0.25rem 0.5rem;
      border-radius: 0.25rem;
      font-family: var(--font-family-mono, 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace);
      font-size: 0.875rem;
    }

    .rendered-content pre code {
      background: none;
      padding: 0;
    }

    .rendered-content a {
      color: var(--color-primary, #2563eb);
      text-decoration: underline;
      text-decoration-color: rgba(37, 99, 235, 0.3);
      transition: text-decoration-color 0.2s;
    }

    .rendered-content a:hover {
      text-decoration-color: var(--color-primary, #2563eb);
    }

    .rendered-content strong {
      font-weight: 600;
    }

    .rendered-content em {
      font-style: italic;
    }

    .rendered-content table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
    }

    .rendered-content th,
    .rendered-content td {
      border: 1px solid var(--color-border, #e5e7eb);
      padding: 0.75rem;
      text-align: left;
    }

    .rendered-content th {
      background-color: var(--color-surface, #f8fafc);
      font-weight: 600;
    }
  </style>

  <div class="markdown-container">
    <div class="loading">マークダウンを読み込み中...</div>
    <div class="rendered-content" style="display: none;"></div>
    <div class="error" style="display: none;">
      <strong>エラー:</strong> マークダウンの読み込みに失敗しました。
    </div>
  </div>
`;

class MarkdownRenderer extends HTMLElement {
  constructor() {
    super();
    
    // Create shadow DOM with declarative shadow DOM support
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(template.content.cloneNode(true));
    
    // Get references to elements
    this.loadingEl = this.shadowRoot.querySelector('.loading');
    this.renderedEl = this.shadowRoot.querySelector('.rendered-content');
    this.errorEl = this.shadowRoot.querySelector('.error');
    
    // Initialize marked library reference
    this.marked = null;
  }

  async connectedCallback() {
    // Get the markdown content from the slot (text content)
    const markdownContent = this.textContent || '';
    
    if (markdownContent.trim()) {
      await this.renderMarkdown(markdownContent);
    } else {
      this.showError('マークダウンコンテンツが見つかりません。');
    }
  }

  async renderMarkdown(content) {
    try {
      // Show loading state
      this.showLoading();
      
      // Initialize marked library
      await this.initializeMarked();
      
      if (this.marked) {
        // Configure marked for better output
        this.marked.setOptions({
          breaks: true,
          gfm: true,
          headerIds: false,
          sanitize: false, // We handle sanitization server-side
        });
        
        // Convert markdown to HTML
        const htmlContent = this.marked.parse(content);
        
        // Render the content
        this.showContent(htmlContent);
      } else {
        throw new Error('Marked library not available');
      }
    } catch (error) {
      console.warn('Failed to parse markdown:', error);
      this.showError('マークダウンの変換に失敗しました。');
      
      // Fallback rendering
      this.fallbackRender(content);
    }
  }

  async initializeMarked() {
    try {
      // Import micromark and GFM extension
      const { micromark } = await import('micromark');
      const { gfm, gfmHtml } = await import('micromark-extension-gfm');
      
      // Configure micromark with GFM extensions
      this.marked = {
        parse: (content) => {
          return micromark(content, {
            extensions: [gfm()],
            htmlExtensions: [gfmHtml()]
          });
        },
        setOptions: () => {
          // Compatibility method - micromark doesn't need this
          // but keeping for API consistency
        }
      };
    } catch (importError) {
      console.warn('Failed to import micromark, falling back to basic parser:', importError);
      
      // Fallback to basic markdown parsing if micromark fails to load
      this.marked = {
        parse: (content) => {
          return this.basicMarkdownToHtml(content);
        },
        setOptions: () => {}
      };
    }
  }

  basicMarkdownToHtml(markdown) {
    return markdown
      // Headers
      .replace(/^### (.*$)/gim, '<h3>$1</h3>')
      .replace(/^## (.*$)/gim, '<h2>$1</h2>')
      .replace(/^# (.*$)/gim, '<h1>$1</h1>')
      // Bold
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      // Italic
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      // Links
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>')
      // Line breaks and paragraphs
      .replace(/\n\n/g, '</p><p>')
      .replace(/\n/g, '<br>')
      // Wrap in paragraph if not starting with header
      .replace(/^(?!<h[1-6])/i, '<p>')
      // Add closing paragraph if doesn't end with header
      .replace(/(?!<\/h[1-6]>)$/i, '</p>')
      // Clean up empty paragraphs
      .replace(/<p><\/p>/g, '')
      .replace(/<p>(<h[1-6]>)/g, '$1')
      .replace(/(<\/h[1-6]>)<\/p>/g, '$1');
  }

  showLoading() {
    this.loadingEl.style.display = 'block';
    this.renderedEl.style.display = 'none';
    this.errorEl.style.display = 'none';
  }

  showContent(htmlContent) {
    this.loadingEl.style.display = 'none';
    this.renderedEl.style.display = 'block';
    this.errorEl.style.display = 'none';
    this.renderedEl.innerHTML = htmlContent;
  }

  showError(message) {
    this.loadingEl.style.display = 'none';
    this.renderedEl.style.display = 'none';
    this.errorEl.style.display = 'block';
    this.errorEl.innerHTML = `<strong>エラー:</strong> ${message}`;
  }

  fallbackRender(content) {
    // Basic fallback: convert line breaks and basic formatting
    const basicHtml = content
      .replace(/\n\n/g, '</p><p>')
      .replace(/\n/g, '<br>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/^## (.*$)/gm, '<h2>$1</h2>')
      .replace(/^### (.*$)/gm, '<h3>$1</h3>');
    
    this.showContent(`<p>${basicHtml}</p>`);
  }

  // Static method to check if the component is supported
  static get observedAttributes() {
    return ['theme', 'loading-text', 'error-text'];
  }

  attributeChangedCallback(name, oldValue, newValue) {
    if (oldValue === newValue) return;
    
    switch (name) {
      case 'loading-text':
        if (this.loadingEl) {
          this.loadingEl.textContent = newValue || 'マークダウンを読み込み中...';
        }
        break;
      case 'error-text':
        if (this.errorEl && this.errorEl.style.display !== 'none') {
          this.showError(newValue || 'マークダウンの読み込みに失敗しました。');
        }
        break;
      case 'theme':
        // Allow theme customization through CSS custom properties
        this.style.setProperty('--theme', newValue);
        break;
    }
  }
}

// Export the class for registration
export { MarkdownRenderer };