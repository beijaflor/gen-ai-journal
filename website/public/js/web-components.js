/**
 * Bundled Web Components for Production
 * This file contains the web components bundle for client-side loading
 */

// Template HTML string (to avoid document access during SSR)
const templateHTML = `
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
    
    // Only create DOM elements when in browser environment
    if (typeof document !== 'undefined') {
      // Create template and shadow DOM
      const template = document.createElement('template');
      template.innerHTML = templateHTML;
      
      this.attachShadow({ mode: 'open' });
      this.shadowRoot.appendChild(template.content.cloneNode(true));
      
      // Get references to elements
      this.loadingEl = this.shadowRoot.querySelector('.loading');
      this.renderedEl = this.shadowRoot.querySelector('.rendered-content');
      this.errorEl = this.shadowRoot.querySelector('.error');
    }
    
    // Initialize marked library reference
    this.marked = null;
  }

  async connectedCallback() {
    // Skip if not in browser environment
    if (typeof document === 'undefined') return;
    
    // Get the markdown content from the slot (text content)
    const markdownContent = this.textContent || '';
    
    if (markdownContent.trim()) {
      await this.renderMarkdown(markdownContent);
    } else {
      // If no content, show as plain text instead of error
      this.innerHTML = '<div style="color: #6b7280; font-style: italic;">コンテンツが見つかりません</div>';
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
        console.warn('Markdown library not available, using fallback parser');
        this.fallbackRender(content);
      }
    } catch (error) {
      console.warn('Failed to parse markdown:', error);
      
      // Always try fallback rendering first
      this.fallbackRender(content);
      
      // Only show error if fallback also fails
      if (!this.renderedEl || this.renderedEl.innerHTML.trim() === '') {
        this.showError('マークダウンの変換に失敗しました。元のテキストを表示します。');
        // Show raw content as last resort
        if (this.renderedEl) {
          this.renderedEl.innerHTML = `<pre style="white-space: pre-wrap; font-family: inherit;">${this.escapeHtml(content)}</pre>`;
          this.showContent(this.renderedEl.innerHTML);
        }
      }
    }
  }

  async initializeMarked() {
    try {
      // Import micromark and GFM extension
      const { micromark } = await import('https://esm.sh/micromark@4');
      const { gfm, gfmHtml } = await import('https://esm.sh/micromark-extension-gfm@3');
      
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

  escapeHtml(unsafe) {
    return unsafe
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  showLoading() {
    if (!this.loadingEl || !this.renderedEl || !this.errorEl) return;
    this.loadingEl.style.display = 'block';
    this.renderedEl.style.display = 'none';
    this.errorEl.style.display = 'none';
  }

  showContent(htmlContent) {
    if (!this.loadingEl || !this.renderedEl || !this.errorEl) return;
    this.loadingEl.style.display = 'none';
    this.renderedEl.style.display = 'block';
    this.errorEl.style.display = 'none';
    this.renderedEl.innerHTML = htmlContent;
  }

  showError(message) {
    if (!this.loadingEl || !this.renderedEl || !this.errorEl) return;
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

/**
 * CopyableId Web Component
 *
 * Renders an article ID badge (e.g. "#001") as a clickable inline element.
 * On click, the ID (with the leading "#") is copied to the clipboard and a
 * brief Japanese tooltip ("コピーしました!") is shown via the
 * :host(.copied) state for ~1.5 seconds.
 */
const copyableIdTemplateHTML = `
  <style>
    :host {
      display: inline-flex;
      align-items: center;
      position: relative;
      cursor: pointer;
      user-select: none;
      -webkit-user-select: none;
      font-weight: 600;
      color: inherit;
      transition: color 0.15s ease, background-color 0.15s ease;
    }

    :host(:hover) .badge {
      color: var(--copyable-id-hover-color, #2563eb);
    }

    :host(:focus-visible) {
      outline: 2px solid var(--color-primary, #2563eb);
      outline-offset: 2px;
      border-radius: 0.25rem;
    }

    .badge {
      display: inline-block;
      transition: color 0.15s ease;
      font: inherit;
      color: inherit;
      background: transparent;
    }

    .tooltip {
      position: absolute;
      bottom: calc(100% + 6px);
      left: 50%;
      transform: translateX(-50%) translateY(4px);
      padding: 0.25rem 0.5rem;
      background-color: var(--copyable-id-tooltip-bg, #1f2937);
      color: var(--copyable-id-tooltip-color, #ffffff);
      font-size: 0.75rem;
      font-weight: 500;
      line-height: 1;
      white-space: nowrap;
      border-radius: 0.25rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.15s ease, transform 0.15s ease;
      z-index: 10;
    }

    .tooltip::after {
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%);
      border: 4px solid transparent;
      border-top-color: var(--copyable-id-tooltip-bg, #1f2937);
    }

    :host(.copied) .tooltip {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }
  </style>

  <span class="badge" part="badge"></span>
  <span class="tooltip" role="status" aria-live="polite">コピーしました!</span>
`;

class CopyableId extends HTMLElement {
  constructor() {
    super();

    if (typeof document === 'undefined') {
      return;
    }

    const template = document.createElement('template');
    template.innerHTML = copyableIdTemplateHTML;

    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(template.content.cloneNode(true));

    this.badgeEl = this.shadowRoot.querySelector('.badge');

    this._onClick = this._onClick.bind(this);
    this._onKeydown = this._onKeydown.bind(this);

    this._resetTimer = null;
  }

  static get observedAttributes() {
    return ['value'];
  }

  connectedCallback() {
    if (typeof document === 'undefined') return;

    if (!this.hasAttribute('tabindex')) {
      this.setAttribute('tabindex', '0');
    }
    if (!this.hasAttribute('role')) {
      this.setAttribute('role', 'button');
    }
    this._updateAriaLabel();

    this._renderValue();

    this.addEventListener('click', this._onClick);
    this.addEventListener('keydown', this._onKeydown);
  }

  disconnectedCallback() {
    this.removeEventListener('click', this._onClick);
    this.removeEventListener('keydown', this._onKeydown);
    if (this._resetTimer) {
      clearTimeout(this._resetTimer);
      this._resetTimer = null;
    }
  }

  attributeChangedCallback(name) {
    if (name === 'value') {
      this._renderValue();
      this._updateAriaLabel();
    }
  }

  get _id() {
    const explicit = this.getAttribute('value');
    const raw = (explicit ?? this.textContent ?? '').trim();
    return raw.startsWith('#') ? raw.slice(1) : raw;
  }

  get _copyText() {
    return `#${this._id}`;
  }

  _renderValue() {
    if (!this.badgeEl) return;
    this.badgeEl.textContent = this._copyText;
  }

  _updateAriaLabel() {
    this.setAttribute('aria-label', `${this._copyText} をコピー`);
  }

  _onClick(event) {
    event.preventDefault();
    this._copyToClipboard();
  }

  _onKeydown(event) {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      this._copyToClipboard();
    }
  }

  async _copyToClipboard() {
    const text = this._copyText;
    let succeeded = false;

    if (typeof navigator !== 'undefined' && navigator.clipboard?.writeText) {
      try {
        await navigator.clipboard.writeText(text);
        succeeded = true;
      } catch (err) {
        console.warn('navigator.clipboard.writeText failed, using fallback:', err);
      }
    }

    if (!succeeded) {
      succeeded = this._execCommandFallback(text);
    }

    if (succeeded) {
      this._showCopiedFeedback();
      this.dispatchEvent(new CustomEvent('copyable-id:copied', {
        bubbles: true,
        composed: true,
        detail: { value: text },
      }));
    } else {
      console.warn('CopyableId: failed to copy to clipboard');
      this.dispatchEvent(new CustomEvent('copyable-id:copy-failed', {
        bubbles: true,
        composed: true,
        detail: { value: text },
      }));
    }
  }

  _execCommandFallback(text) {
    if (typeof document === 'undefined') return false;
    try {
      const textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.setAttribute('readonly', '');
      textarea.style.position = 'fixed';
      textarea.style.top = '0';
      textarea.style.left = '0';
      textarea.style.opacity = '0';
      textarea.style.pointerEvents = 'none';
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      const ok = document.execCommand && document.execCommand('copy');
      document.body.removeChild(textarea);
      return !!ok;
    } catch (err) {
      console.warn('execCommand copy fallback failed:', err);
      return false;
    }
  }

  _showCopiedFeedback() {
    this.classList.add('copied');
    if (this._resetTimer) {
      clearTimeout(this._resetTimer);
    }
    this._resetTimer = setTimeout(() => {
      this.classList.remove('copied');
      this._resetTimer = null;
    }, 1500);
  }
}

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
function registerAllComponents() {
  registerComponent('markdown-renderer', MarkdownRenderer);
  registerComponent('copyable-id', CopyableId);
}

/**
 * Register individual components (for selective loading)
 */
function registerMarkdownRenderer() {
  registerComponent('markdown-renderer', MarkdownRenderer);
}

function registerCopyableId() {
  registerComponent('copyable-id', CopyableId);
}

// Export functions for module usage
window.WebComponents = {
  registerAllComponents,
  registerMarkdownRenderer,
  registerCopyableId,
  MarkdownRenderer,
  CopyableId
};

// Auto-register for script tag usage
if (typeof module === 'undefined') {
  // Running as script tag, auto-register
  registerMarkdownRenderer();
  registerCopyableId();
}