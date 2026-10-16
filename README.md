# AfriShield Gold Ltd: Website

One-page, mobile-first website for **AfriShield Gold Ltd**, a *hypothetical* licensed gold trading company (Uganda & DRC) created for a business class assignment.

Live site: **https://afrishieldgold.com** (GitHub Pages)

## What's inside
| Path | Purpose |
|---|---|
| `index.html` | The whole site (HTML, CSS and JS in one file) |
| `assets/` | Shield logo, favicons, social share image |
| `docs/` | Six specimen licence/policy PDFs (watermarked, no legal effect) |
| `tools/build_docs.py` | Rebuilds the PDFs: `python3 tools/build_docs.py docs` (needs `reportlab`) |
| `CNAME` | Custom domain for GitHub Pages: `afrishieldgold.com` |
| `404.html`, `robots.txt`, `sitemap.xml` | Hosting extras |

## Features
- 4-slide hero slider (swipe, arrows, dots, keyboard, autoplay with pause, reduced-motion support)
- Sections: About, Products, Mines (real haul-truck photos, credited), Operations, Compliance, Process, Licences & Documents, Contact
- Contact form composes a pre-filled **email to info@afrishieldgold.com** or a **WhatsApp message to +256 746 840 004** (works on any static host, no backend)
- Brand: shield logo, chocolate-brown + gold + cream palette, tagline "Secure. Ethical. African Gold."

## Updating the site
Edit files, then commit and push to `main`. GitHub Pages republishes automatically in about a minute.

## Custom domain (Namecheap → GitHub Pages)
In Namecheap **Advanced DNS** for `afrishieldgold.com`:

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<github-username>.github.io.` |

Remove any parking-page / URL-redirect records for `@` and `www`. Then in the repo: **Settings → Pages → Custom domain** = `afrishieldgold.com`, wait for the DNS check, and tick **Enforce HTTPS**.

---
Created for educational / class assignment purposes only. AfriShield Gold Ltd is not a real company.
