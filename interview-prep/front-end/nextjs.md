# Next.js Questions

**What is Next.js and what does it add over React?**

Next.js is a React framework that provides structure and built-in solutions for production concerns:
- File-based routing (no react-router setup needed)
- Server-side rendering and static generation
- API routes / Route Handlers (backend in the same project)
- Image, font, and script optimization
- Built-in code splitting per page

React is a UI library; Next.js is the full application framework built on top of it.

---

**What is the difference between the Pages Router and the App Router?**

Next.js has two routing systems:

- **Pages Router** (legacy, stable): files in `pages/` map to routes. Data fetching via `getServerSideProps` / `getStaticProps`. All components are client components by default.
- **App Router** (current, Next.js 13+): files in `app/` use React Server Components by default. Layouts, nested routing, Server Actions, and streaming are first-class. Data fetching is done with `async/await` directly in components.

New projects should use the App Router. The two routers can coexist during migration.

---

**What are React Server Components (RSC)?**

Server Components render on the server and send HTML (or a serialized component tree) to the client — no JavaScript is shipped for them. They can directly access databases, file systems, and secrets.

- **Server Component** (default in `app/`): renders on server, zero client JS, cannot use hooks or browser APIs.
- **Client Component** (`"use client"` directive): ships JS to the browser, can use hooks, events, and browser APIs.

```tsx
// app/users/page.tsx — Server Component (no "use client")
async function UsersPage() {
  const users = await db.query("SELECT * FROM users"); // direct DB access
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

```tsx
// components/Counter.tsx — Client Component
"use client";
import { useState } from "react";

export function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

A Server Component can import and render a Client Component, but not the reverse.

---

**How does file-based routing work in the App Router?**

The `app/` directory maps folder structure to URL segments. Special files control each segment's behavior:

| File | Purpose |
|---|---|
| `page.tsx` | The UI for a route (makes the segment publicly accessible) |
| `layout.tsx` | Wraps a segment and its children; persists across navigations |
| `loading.tsx` | Automatic Suspense fallback shown while the page loads |
| `error.tsx` | Error boundary UI for the segment |
| `not-found.tsx` | Rendered when `notFound()` is called |
| `route.ts` | API endpoint (Route Handler) — no UI |

```
app/
  layout.tsx          → wraps every page
  page.tsx            → /
  dashboard/
    layout.tsx        → wraps /dashboard/*
    page.tsx          → /dashboard
    settings/
      page.tsx        → /dashboard/settings
  blog/
    [slug]/
      page.tsx        → /blog/:slug  (dynamic segment)
```

---

**What are the data fetching patterns in the App Router?**

Server Components are `async` functions, so you `await` data directly. Next.js extends the native `fetch` API with caching options:

```tsx
// Default: cached indefinitely (like SSG)
const data = await fetch("https://api.example.com/posts");

// Revalidate every 60 seconds (ISR equivalent)
const data = await fetch("https://api.example.com/posts", {
  next: { revalidate: 60 },
});

// Never cache (like SSR — fresh on every request)
const data = await fetch("https://api.example.com/posts", {
  cache: "no-store",
});
```

For non-fetch data sources (ORMs, SDKs), use `unstable_cache` or `cache()` from React.

---

**What is Incremental Static Regeneration (ISR)?**

ISR lets statically generated pages regenerate in the background after a specified time, without a full rebuild. Old content is served until the new version is ready (stale-while-revalidate).

```tsx
// App Router
export const revalidate = 60; // re-generate this page at most every 60s

// Pages Router equivalent
export async function getStaticProps() {
  const data = await fetchData();
  return { props: { data }, revalidate: 60 };
}
```

On-demand revalidation is also possible via `revalidatePath()` or `revalidateTag()` in a Server Action or Route Handler.

---

**What are layouts and how do nested layouts work?**

A `layout.tsx` wraps its segment and all child segments. It receives `children` as a prop and persists across navigations within its subtree — the layout does *not* re-render when a child route changes.

```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="dashboard">
      <Sidebar />
      <main>{children}</main>
    </div>
  );
}
```

Layouts nest: `app/layout.tsx` wraps everything, then `app/dashboard/layout.tsx` wraps only the dashboard subtree.

---

**What are Server Actions?**

Server Actions are async functions that run on the server, callable directly from Client or Server Components — no separate API route needed. They are the recommended way to handle form submissions and data mutations.

```tsx
// app/actions.ts
"use server";

export async function createPost(formData: FormData) {
  const title = formData.get("title") as string;
  await db.insert({ title });
  revalidatePath("/posts");
}
```

```tsx
// app/new-post/page.tsx (Server Component)
import { createPost } from "../actions";

export default function NewPostPage() {
  return (
    <form action={createPost}>
      <input name="title" />
      <button type="submit">Create</button>
    </form>
  );
}
```

Server Actions are marked with `"use server"` — either at the top of a file (all exports become actions) or inline in a function.

---

**What are Route Handlers?**

Route Handlers (`route.ts`) are the App Router equivalent of Pages Router API routes. They expose HTTP endpoints using Web standard `Request`/`Response`.

```ts
// app/api/users/route.ts
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const users = await db.getUsers();
  return NextResponse.json(users);
}

export async function POST(request: NextRequest) {
  const body = await request.json();
  const user = await db.createUser(body);
  return NextResponse.json(user, { status: 201 });
}
```

A `route.ts` and a `page.tsx` cannot exist at the same path.

---

**What is Next.js middleware?**

Middleware runs before a request is processed, at the Edge (close to the user). Use it for auth checks, redirects, rewrites, and A/B testing without hitting the origin server.

```ts
// middleware.ts (at project root)
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  const token = request.cookies.get("token");
  if (!token && request.nextUrl.pathname.startsWith("/dashboard")) {
    return NextResponse.redirect(new URL("/login", request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: "/dashboard/:path*",
};
```

Middleware runs on *every* matched request, so keep it lightweight.

---

**What is the Next.js caching model?**

Next.js has four layered caches:

| Cache | What it stores | Duration |
|---|---|---|
| **Request Memoization** | Deduplicates identical `fetch` calls within a single render pass | Per request |
| **Data Cache** | `fetch` responses, persisted on the server | Until revalidated |
| **Full Route Cache** | Rendered HTML + RSC payload for static routes | Until revalidated |
| **Router Cache** | Client-side cache of visited route segments | Session / configurable |

Understanding this stack is key: data can be stale at multiple levels. `revalidatePath()` / `revalidateTag()` purge the Data Cache and Full Route Cache. The Router Cache is cleared on navigation or after its TTL.

---

**What is `next/image` and why should you use it?**

`next/image` is an optimized `<img>` replacement that:
- Automatically converts images to modern formats (WebP, AVIF)
- Resizes images to the requested display size (no oversized downloads)
- Lazy-loads by default
- Prevents layout shift by requiring `width` and `height` (or `fill`)

```tsx
import Image from "next/image";

<Image
  src="/hero.jpg"
  alt="Hero"
  width={1200}
  height={600}
  priority // eager-load above-the-fold images
/>
```

Always use `next/image` over a plain `<img>` for local or remote images in a Next.js app.

---

**How does `next/link` work and what is prefetching?**

`<Link>` renders an `<a>` tag and enables client-side navigation — no full page reload. It automatically prefetches the linked route in the background when the link enters the viewport (in production).

```tsx
import Link from "next/link";

<Link href="/about">About</Link>

// Disable prefetch for rarely visited pages
<Link href="/admin" prefetch={false}>Admin</Link>
```

For programmatic navigation use `useRouter` from `next/navigation` (App Router) or `next/router` (Pages Router).

---

**How does the Metadata API work?**

The App Router has a typed `Metadata` API for setting `<head>` tags like `<title>` and `<meta>`, replacing `next/head`.

```tsx
// Static metadata
export const metadata = {
  title: "My App",
  description: "Welcome to my app",
};

// Dynamic metadata
export async function generateMetadata({ params }) {
  const post = await getPost(params.slug);
  return { title: post.title };
}
```

Metadata is inherited and merged down the layout tree. `generateMetadata` runs on the server, so it can fetch data.

---

**What are dynamic segments and generateStaticParams?**

Dynamic segments (e.g., `[slug]`) match any value at that position. `generateStaticParams` pre-renders a set of paths at build time instead of on-demand.

```tsx
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map(post => ({ slug: post.slug }));
}

export default async function PostPage({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug);
  return <article>{post.content}</article>;
}
```

Paths not returned by `generateStaticParams` are rendered on-demand by default (`dynamicParams = true`). Set `export const dynamicParams = false` to 404 instead.

---

**What are environment variables in Next.js?**

Next.js loads `.env.local` automatically. Variables are available server-side only by default.

- **Server-only**: `process.env.DATABASE_URL` — never exposed to the browser.
- **Public (client + server)**: prefix with `NEXT_PUBLIC_`, e.g. `NEXT_PUBLIC_API_URL` — bundled into client JS, so never put secrets here.

```bash
# .env.local
DATABASE_URL=postgres://...       # server only
NEXT_PUBLIC_API_URL=https://...   # safe to expose
```

`.env.local` is git-ignored by default. Commit `.env.example` with placeholder values for documentation.
