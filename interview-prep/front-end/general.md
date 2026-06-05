# General Frontend Concepts

**What is the CSS box model?**

Every element is a rectangular box composed of four layers (inside out):
1. **Content** — the actual text/image area, sized by `width`/`height`.
2. **Padding** — transparent space between content and border.
3. **Border** — the visible edge around padding.
4. **Margin** — transparent space outside the border, separating elements.

By default (`box-sizing: content-box`) `width` applies to the content only, so padding and border add to the total size. `box-sizing: border-box` (recommended, often applied globally) makes `width` include padding and border.

```css
*, *::before, *::after { box-sizing: border-box; }
```

---

**What is CSS specificity?**

Specificity determines which CSS rule wins when multiple rules target the same element. It is calculated as a score `(id, class, element)`:

| Selector | Score |
|---|---|
| Inline style | `(1,0,0,0)` — always wins |
| `#id` | `(0,1,0,0)` |
| `.class`, `[attr]`, `:pseudo-class` | `(0,0,1,0)` |
| `div`, `p`, `::pseudo-element` | `(0,0,0,1)` |
| `*` | `(0,0,0,0)` |

`!important` overrides specificity entirely (avoid it). When specificity ties, the *last* rule in the stylesheet wins (cascade order).

---

**Flexbox vs CSS Grid — when to use which?**

- **Flexbox**: one-dimensional layout (a row *or* a column). Best for aligning items within a component — nav bars, button groups, centering a single element.
- **Grid**: two-dimensional layout (rows *and* columns simultaneously). Best for overall page layout or any component that needs items to align across both axes.

```css
/* Flexbox — horizontal nav */
nav { display: flex; gap: 1rem; align-items: center; }

/* Grid — 3-column page layout */
.layout {
  display: grid;
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: auto 1fr auto;
}
```

They can be nested: a Grid for the page shell, Flexbox inside each cell.

---

**What is the browser's critical rendering path?**

The sequence of steps the browser takes to render a page:

1. **Parse HTML** → build the **DOM** tree.
2. **Parse CSS** → build the **CSSOM** tree.
3. DOM + CSSOM → **Render Tree** (only visible nodes).
4. **Layout** (reflow) — compute position and size of every node.
5. **Paint** — fill in pixels (colors, text, images).
6. **Composite** — merge layers and display on screen.

JavaScript blocks HTML parsing (unless `defer`/`async`). Render-blocking CSS blocks paint. Minimizing render-blocking resources is the main lever for improving initial load performance.

---

**What is the difference between `<script>`, `<script defer>`, and `<script async>`?**

All three load the script file in parallel with HTML parsing, but differ in when they *execute*:

| | Blocks parsing? | Execution timing |
|---|---|---|
| `<script>` | Yes | Immediately when encountered |
| `<script async>` | Yes (when ready) | As soon as downloaded, before DOM is complete |
| `<script defer>` | No | After HTML is fully parsed, in document order |

Use `defer` for most scripts. Use `async` for fully independent scripts (analytics) that don't depend on the DOM or other scripts.

---

**What are Core Web Vitals?**

Google's metrics for measuring real-user page experience:

| Metric | Measures | Good threshold |
|---|---|---|
| **LCP** (Largest Contentful Paint) | Load performance — when the largest visible element renders | ≤ 2.5 s |
| **INP** (Interaction to Next Paint) | Responsiveness — latency from user interaction to visual response | ≤ 200 ms |
| **CLS** (Cumulative Layout Shift) | Visual stability — how much content unexpectedly shifts | ≤ 0.1 |

Common fixes: optimize images (LCP), avoid heavy JS on the main thread (INP), set explicit `width`/`height` on media (CLS).

---

**What is CORS?**

Cross-Origin Resource Sharing is a browser security mechanism that restricts web pages from making requests to a *different origin* (scheme + host + port) than the one that served the page.

The browser sends an `Origin` header with cross-origin requests. The server must respond with `Access-Control-Allow-Origin` granting permission, otherwise the browser blocks the response.

For non-simple requests (e.g., `PUT`, custom headers), the browser first sends a **preflight** `OPTIONS` request to check permissions.

CORS is enforced by the *browser* — server-to-server requests are unaffected.

```
# Server response header granting access
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST, PUT
```

---

**What is the difference between localStorage, sessionStorage, and cookies?**

| | Capacity | Persists | Sent with requests? | Accessible from JS? |
|---|---|---|---|---|
| `localStorage` | ~5–10 MB | Until explicitly cleared | No | Yes |
| `sessionStorage` | ~5–10 MB | Until tab/window closes | No | Yes |
| Cookies | ~4 KB | Until expiry date | Yes (same-origin) | Yes (unless `HttpOnly`) |

Use cookies for authentication tokens (they can be `HttpOnly` + `Secure`, protecting against XSS). Use `localStorage` for user preferences. Avoid storing sensitive data in `localStorage`/`sessionStorage` — they are fully accessible to any JS on the page.

---

**What is XSS? What is CSRF?**

**Cross-Site Scripting (XSS)**: an attacker injects malicious script into a page that other users view. The script runs with the victim's privileges, able to steal cookies or tokens.

Prevention: escape/sanitize all user-generated HTML, use a strict Content Security Policy (CSP), avoid `dangerouslySetInnerHTML`.

**Cross-Site Request Forgery (CSRF)**: a malicious site tricks a logged-in user's browser into making an unintended request to another site (cookies are sent automatically).

Prevention: use `SameSite=Strict/Lax` on cookies, CSRF tokens in forms, and check the `Origin`/`Referer` header on state-changing requests.

---

**What is accessibility (a11y) and why does it matter?**

Accessibility means building UIs usable by people with disabilities (visual, motor, auditory, cognitive). It's also a legal requirement in many jurisdictions.

Key practices:
- Use semantic HTML (`<button>`, `<nav>`, `<main>`) — assistive tech understands it.
- Every image needs an `alt` attribute.
- Interactive elements must be keyboard-focusable and operable with Enter/Space.
- Sufficient color contrast (WCAG AA: 4.5:1 for normal text).
- ARIA attributes (`role`, `aria-label`, `aria-live`) only when semantic HTML isn't sufficient.

```html
<!-- Bad -->
<div onclick="submit()">Submit</div>

<!-- Good -->
<button type="submit">Submit</button>
```

---

**What is responsive design?**

Responsive design makes UIs adapt to different screen sizes and devices.

Key tools:
- **Media queries**: apply CSS conditionally based on viewport size.
- **Fluid units**: `%`, `vw`, `em`, `rem` instead of fixed `px`.
- **Flexible images**: `max-width: 100%` prevents overflow.
- **CSS Grid/Flexbox**: naturally adapt to available space.

```css
/* Mobile-first: base styles for small screens, enhance upward */
.container { padding: 1rem; }

@media (min-width: 768px) {
  .container { max-width: 960px; margin: 0 auto; }
}
```

---

**What is server-side rendering (SSR) vs client-side rendering (CSR) vs static site generation (SSG)?**

- **CSR** (React SPA default): browser downloads a minimal HTML shell + JS bundle, then renders everything client-side. Slower initial load, faster subsequent navigation. Bad for SEO without extra work.
- **SSR**: server renders full HTML on each request and sends it to the browser. Faster first paint, better SEO, more server load.
- **SSG**: HTML is generated at *build time* and served as static files (CDN). Fastest possible delivery, but content is fixed until the next build. Ideal for blogs, marketing pages.

Frameworks like Next.js support all three per-route.
