"""Styling constants for the digital twin Gradio app."""

GOLD = "#03002e"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
:root {
  --twin-gold: #03002e;
  --twin-navy: #00008b;
  --twin-navy-light: #4169e1;
  --twin-blue: #209dd7;
  --twin-purple: #753991;
  --twin-bg: #000000;
  --twin-surface: #ffffff;
  --twin-surface-2: #ededf0;
  --twin-border: #dcdce2;
  --twin-border-strong: #b8b8c0;
  --twin-text: #1a1a20;
  --twin-muted: #6a6a72;
  --twin-page-text: #ececef;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app { background: var(--twin-bg) !important; }

/* ---------- Stable layout ---------- */
.gradio-container {
  background: var(--twin-bg) !important;
  color: var(--twin-page-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 880px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 32px 24px 48px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Title ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-family: 'Ubuntu', sans-serif !important;
  font-size: 20px !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  margin: 0 !important;
  padding: 16px 20px 8px !important;
  text-align: left !important;
}

/* Title banner: white, rounded top corners, flush with the chat window below */
.gradio-container :has(h1):not(:has(.chatbot)):not(h1) {
  background: var(--twin-surface) !important;
  border: 0 !important;
  border-radius: 12px 12px 0 0 !important;
  box-shadow: none !important;
}
.gradio-container .block:has(h1):not(:has(.chatbot)) {
  margin-bottom: calc(-1 * var(--layout-gap, 16px)) !important;
}

/* ---------- Sharp corners on structural pieces ---------- */
.chatbot, .chatbot *, .block, .form,
button, input, textarea,
.examples button {
  border-radius: 0 !important;
}

/* ---------- Block surfaces ---------- */
.block, .form { background: transparent !important; box-shadow: none !important; }

/* ---------- Hide the Chatbot label / header strip ---------- */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* ---------- Chatbot frame ---------- */
.chatbot, .chatbot.block {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-top: 0 !important;
  min-height: 460px !important;
  border-radius: 0 0 12px 12px !important;
  overflow: hidden !important;
  box-shadow: none !important;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ---------- Message rows: strip parent backgrounds ---------- */
.message-row,
.message-row > div,
.message-row .role {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}
.message-wrap, .bubble-wrap {
  background: var(--twin-surface) !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* ---------- Reset borders on every bubble variant first ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: none !important;
  padding: 6px 10px !important;
}

/* No left border (or accent bar) on any message bubble or its wrappers */
.message-row,
.message-row .message,
.message-row .message.bot,
.message-row .message.user,
.message-row .message-bubble,
.message-row .message-bubble-border,
.message-row .message-content,
.message-row .flex-wrap,
.message-row .bubble,
.message-row .prose,
.message-row .md,
.message-row blockquote {
  border-left: 0 none transparent !important;
  border-inline-start: 0 none transparent !important;
}

/* ---------- Bubble backgrounds (broad to cover Gradio variants) ---------- */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: #00008b !important;
  color: #ffffff !important;
}

/* User and response bubbles: rounded instead of square */
.chatbot .message-row.user-row .message,
.chatbot .message-row.user-row .message-bubble,
.chatbot .message-row.user-row .bubble,
.chatbot .message-row[data-role="user"] .message,
.chatbot .message-row[data-role="user"] .message-bubble,
.chatbot .message-row.bot-row .message,
.chatbot .message-row.bot-row .message-bubble,
.chatbot .message-row.bot-row .bubble,
.chatbot .message-row[data-role="assistant"] .message,
.chatbot .message-row[data-role="assistant"] .message-bubble {
  border-radius: 10px !important;
}

/* User bubbles: size to content */
.chatbot .message-row.user-row .message,
.chatbot .message-row.user-row .message-bubble,
.chatbot .message-row.user-row .bubble,
.chatbot .message-row[data-role="user"] .message,
.chatbot .message-row[data-role="user"] .message-bubble {
  min-width: 100px !important;
  width: fit-content !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
}
.chatbot .message-row.user-row .flex-wrap,
.chatbot .message-row.user-row .message-content {
  width: fit-content !important;
  max-width: 100% !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
}

/* ---------- Uniform font size in bubbles ----------
   The "first paragraph different size" was caused by a leaky `.prose p:first-of-type`
   selector. Force every paragraph in a bubble to the same size. */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14px !important;
  line-height: 1.55 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14px !important;
  line-height: 1.55 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

/* Strip stray internal borders/backgrounds from anything inside a bubble */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  text-decoration: underline;
}

/* ---------- Input row alignment ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] { align-items: stretch !important; }

textarea, input[type="text"] {
  background: var(--twin-surface) !important;
  border: 0 !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14px !important;
  padding: 12px 14px !important;
  line-height: 1.4 !important;
  min-height: 48px !important;
}
textarea:focus, input[type="text"]:focus {
  border: 0 !important;
  outline: none !important;
  box-shadow: none !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

/* Chat bar: round the corners to match the chat window */
.gradio-container :has(textarea):not(.main):not(.contain):not(.gradio-container),
.gradio-container textarea,
.gradio-container input[type="text"] {
  border-radius: 12px !important;
}
/* No gray border around the input bar */
.gradio-container .input-wrapper,
.gradio-container .full-container {
  background: var(--twin-surface) !important;
  border-color: transparent !important;
  box-shadow: none !important;
}
.gradio-container :has(textarea):not(:has(.chatbot)):not(.chatbot) {
  background: var(--twin-surface) !important;
}
.gradio-container :has(textarea):not(.main):not(.contain):not(.gradio-container) {
  border: 0 !important;
  box-shadow: none !important;
}

/* ---------- Processing / pending indicator: same color as response text ---------- */
.chatbot .progress-text,
.chatbot .meta-text,
.chatbot .meta-text-center,
.chatbot .pending,
.chatbot .pending * {
  color: var(--twin-text) !important;
}
.chatbot .dot { background-color: var(--twin-text) !important; }

/* ---------- Buttons ---------- */
button {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  border: 1px solid var(--twin-border) !important;
  background: transparent !important;
  color: var(--twin-text) !important;
  padding: 0 16px !important;
  min-height: 48px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  transition: background 0.12s ease, color 0.12s ease, border-color 0.12s ease;
}
button:hover { border-color: var(--twin-gold) !important; color: var(--twin-gold) !important; }

button.primary,
button[variant="primary"],
button[type="submit"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-navy) !important;
  border: 1px solid var(--twin-navy) !important;
  color: #ffffff !important;
  min-height: 48px !important;
  align-self: stretch !important;
  padding: 0 14px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
button.primary:hover,
button[type="submit"]:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: #0000cd !important;
  border-color: #0000cd !important;
  color: #ffffff !important;
}

/* ---------- Submit-button arrow: always white on the navy button ---------- */
button[type="submit"] svg,
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: #ffffff !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}
button[type="submit"] svg *,
button.submit svg *,
button.submit-button svg *,
.submit-button svg *,
button.primary svg *,
button[variant="primary"] svg * {
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Examples ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin: 14px 16px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: stretch !important;
  gap: 10px !important;
  max-width: none !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 400 !important;
  padding: 10px 14px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: block !important;
  width: 100% !important;
  margin: 0 !important;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: #0000cd !important;
  color: #0000cd !important;
  background: var(--twin-surface) !important;
  margin: 0 !important;
  transform: none !important;
}

/* ---------- Icon buttons (clear, retry, copy) ---------- */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 4px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .chatbot .icon-button:hover { color: var(--twin-gold) !important; }

/* Chat toolbar: copy first, clear second, with space from the window edge */
.chatbot .icon-button-wrapper {
  display: flex !important;
  flex-direction: row !important;
  top: 0 !important;
  left: 0 !important;
  right: auto !important;
  align-self: flex-start !important;
  margin: 4px auto 0 20px !important;
}
.chatbot .icon-button-wrapper button[aria-label*="copy" i] { order: 1 !important; }
.chatbot .icon-button-wrapper button[aria-label*="clear" i] { order: 2 !important; }

/* Hide the undo and retry actions (the per-message button bar) */
.gradio-container .message-buttons,
.gradio-container .message-buttons-left,
.gradio-container .message-buttons-right,
.gradio-container .message-row .icon-button-wrapper,
.gradio-container button[title="Retry" i], .gradio-container button[title="Undo" i],
.gradio-container .icon-button[aria-label="Retry" i], .gradio-container .icon-button[aria-label="Undo" i],
.gradio-container [aria-label="Retry" i], .gradio-container [aria-label="Undo" i] {
  display: none !important;
}

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: var(--twin-bg); }
::-webkit-scrollbar-thumb { background: var(--twin-border-strong); }
::-webkit-scrollbar-thumb:hover { background: var(--twin-purple); }

/* ---------- Selection ---------- */
::selection { background: var(--twin-gold); color: #ffffff; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 22px 14px 36px !important; }
  .gradio-container h1 { font-size: 22px !important; }
}
"""

JS = """
() => {
  document.title = 'Resume Bot';
  // Gradio sets the title itself after load, so keep ours.
  new MutationObserver(() => {
    if (document.title !== 'Resume Bot') document.title = 'Resume Bot';
  }).observe(document.querySelector('title'), { childList: true });

  // Load the Ubuntu font used by the title.
  const font = document.createElement('link');
  font.rel = 'stylesheet';
  font.href = 'https://fonts.googleapis.com/css2?family=Ubuntu:wght@700&display=swap';
  document.head.appendChild(font);

  // Permanent light mode: Gradio toggles `.dark` on <body>, so keep it removed.
  const forceLight = () => {
    if (document.body.classList.contains('dark')) document.body.classList.remove('dark');
  };
  forceLight();
  new MutationObserver(forceLight).observe(document.body, { attributes: true, attributeFilter: ['class'] });

  // Pick the visible, enabled message field (Gradio can render other textareas).
  const focusInput = () => {
    const areas = [...document.querySelectorAll('textarea')]
      .filter((a) => a.offsetParent !== null && !a.disabled && !a.readOnly);
    if (areas.length) areas[areas.length - 1].focus({ preventScroll: true });
  };
  // Gradio can blur the field again right after a response, so keep re-applying
  // focus for a short moment.
  const holdFocus = () => {
    let tries = 0;
    const timer = setInterval(() => {
      const active = document.activeElement;
      if (!active || active.tagName !== 'TEXTAREA') focusInput();
      if (++tries >= 10) clearInterval(timer);
    }, 150);
  };
  setTimeout(focusInput, 300);

  // Keep focus in the message field right after a message is sent
  // (Enter key or send button); focus is also restored when Gradio re-enables it.
  // After a message is sent, poll until the response has finished arriving
  // (nothing is pending/generating and the field is enabled), then put the
  // cursor back in the input.
  let waitTimer = null;
  const refocus = () => {
    clearInterval(waitTimer);
    const sentAt = Date.now();
    let sawBusy = false;
    let idleChecks = 0;
    waitTimer = setInterval(() => {
      const busy = document.querySelector(
        '.chatbot .pending, .chatbot .generating, .generating, .stop-button, button[aria-label="Stop" i], textarea:disabled'
      );
      if (busy) { sawBusy = true; idleChecks = 0; } else { idleChecks += 1; }
      const elapsed = Date.now() - sentAt;
      if (idleChecks >= 3 && (sawBusy || elapsed > 2000)) {
        focusInput();
        holdFocus();
        clearInterval(waitTimer);
      } else if (elapsed > 180000) {
        clearInterval(waitTimer);
      }
    }, 200);
  };
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey && e.target.tagName === 'TEXTAREA') refocus();
  });
  document.addEventListener('click', (e) => {
    if (e.target.closest('button[type="submit"], .submit-button, .example, .examples button')) refocus();
  });

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });

  // Gradio doesn't always disable the field while it responds, so also refocus
  // once the chat stops changing (the reply has finished arriving).
  let settleTimer = null;
  new MutationObserver((mutations) => {
    const inChat = mutations.some((m) => {
      const node = m.target.nodeType === 1 ? m.target : m.target.parentElement;
      return node && node.closest('.chatbot');
    });
    if (!inChat) return;
    clearTimeout(settleTimer);
    settleTimer = setTimeout(() => {
      const active = document.activeElement;
      if (!active || active === document.body || active.tagName === 'BUTTON') focusInput();
    }, 400);
  }).observe(document.body, { childList: true, subtree: true, characterData: true });
}
"""
