/**
 * CopyableId Web Component
 *
 * Renders an article ID badge (e.g. "#001") as a clickable inline element.
 * On click, the ID (with the leading "#") is copied to the clipboard and a
 * brief Japanese tooltip ("コピーしました!") is shown via the
 * :host(.copied) state for ~1.5 seconds.
 *
 * Usage:
 *   <copyable-id>001</copyable-id>
 *   <copyable-id value="042" variant="badge">042</copyable-id>
 *
 * The textContent is treated as the ID. A leading "#" in the textContent is
 * stripped so callers can pass either "001" or "#001" without breaking the
 * copied value (which is always prefixed with exactly one "#").
 */

const templateHTML = `
  <style>
    :host {
      /* Inline so the badge sits inside text or flex rows naturally. */
      display: inline-flex;
      align-items: center;
      position: relative;
      cursor: pointer;
      user-select: none;
      -webkit-user-select: none;
      font-weight: 600;
      color: inherit;
      /* Subtle affordance that this is interactive. */
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
      /* Inherit typography and colors from the surrounding context so that
         external host styling (e.g. background, padding, border) governs the
         visual appearance and the inner badge stays transparent. */
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
      // SSR safety: do nothing when there is no DOM.
      return;
    }

    const template = document.createElement('template');
    template.innerHTML = templateHTML;

    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(template.content.cloneNode(true));

    this.badgeEl = this.shadowRoot.querySelector('.badge');

    // Bound handlers so we can detach them later if needed.
    this._onClick = this._onClick.bind(this);
    this._onKeydown = this._onKeydown.bind(this);

    this._resetTimer = null;
  }

  static get observedAttributes() {
    return ['value'];
  }

  connectedCallback() {
    if (typeof document === 'undefined') return;

    // Make the element keyboard-focusable and announce its role.
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

  /**
   * The raw ID string, without the leading "#".
   */
  get _id() {
    const explicit = this.getAttribute('value');
    const raw = (explicit ?? this.textContent ?? '').trim();
    return raw.startsWith('#') ? raw.slice(1) : raw;
  }

  /**
   * The string copied to the clipboard. Always exactly one "#" prefix.
   */
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
        // Fall through to execCommand fallback.
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
      // Avoid scrolling to bottom and keep it off-screen.
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

export { CopyableId };
