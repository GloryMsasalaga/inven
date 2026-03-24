# Inventions Technologies — Wireframe Developer Review Document

**File:** `index.html`
**Last Updated:** March 24, 2026
**Status:** Wireframe — ready for developer review

---

## 1. Overview

Single-page wireframe for the Inventions Technologies corporate website. Built as a self-contained HTML file with embedded CSS and vanilla JavaScript. The wireframe defines the visual structure, color system, layout grid, interactive behaviors, and content hierarchy for all sections of the landing page.

**Max width:** 960px, centered
**Layout approach:** CSS Grid + Flexbox
**No external dependencies** — no frameworks, no libraries, no build tools

---

## 2. Color System

All color values used across the wireframe. Developers must use these exact tokens when implementing.

### Primary Palette

| Token | Hex | Usage |
|-------|-----|-------|
| Burgundy (primary) | `#800020` | All buttons, CTA elements, active indicators, accent dividers, logo box background |
| Burgundy light | `#b8445a` | Service tags, service links, news "Read more", eyebrow labels on dark cards |
| Burgundy annotation | `#a0304a` | Annotation badge text color |
| Navy (card base) | `#1a1a3e` | All card backgrounds (services, news, testimonials, clients, partners), heading text |
| Navy deep | `#12122e` | Footer background |
| Navy inner | `#222255` | Testimonial card inner background |
| Navy image area | `#252550` | Service card and news card image placeholder areas |

### Neutral Palette

| Token | Hex | Usage |
|-------|-----|-------|
| Whitesmoke | `#f5f5f5` | Body/page background |
| Page surface | `#f0f0f0` | `.page` container background, nav background |
| White | `#ffffff` | Button text, card title text, partner pill highlight text |
| Star gold | `#EF9F27` | Rating star fill |

### Functional Colors

| Token | Hex | Usage |
|-------|-----|-------|
| Blue (tech tag) | `#378ADD` / `#6aa8e0` | Tech news tags, hero slide 1 globe illustration |
| Green (insight tag) | `#1D9E75` / `#5DCAA5` | Insight news tags, software dev icon, green annotation badges |
| Green annotation | `#1a8a60` | Green annotation text on light background |

### Opacity Patterns

- Card borders: `rgba(26,26,62,0.2)` to `rgba(26,26,62,0.3)`
- Light-bg text: `rgba(0,0,0,0.4)` to `rgba(0,0,0,0.6)`
- Dark-bg text: `rgba(255,255,255,0.4)` to `rgba(255,255,255,0.85)`
- Dark-bg borders: `rgba(255,255,255,0.08)` to `rgba(255,255,255,0.2)`

---

## 3. Typography

The wireframe uses the system font stack:

```
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Scale

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Hero H1 | 30px | 500 | `#1a1a3e`, accent word in `#800020` |
| Section H2 | 20px | 500 | `#1a1a3e` |
| Partner title | 15px | 500 | `#fff` |
| Hero subheading | 14px | 400 | `#800020` |
| Service card title | 13px | 500 | `#fff` |
| Nav links / body text | 12px | 400 | varies by context |
| Footer column title | 12px | 500 | `rgba(255,255,255,0.85)` |
| Body paragraphs (hero) | 12px | 400 | `rgba(0,0,0,0.5)`, line-height 1.8 |
| Card descriptions | 11px | 400 | `rgba(255,255,255,0.5)`, line-height 1.6 |
| Eyebrow/tags | 9–10px | 500 | uppercase, letter-spacing 0.8–1.2px |

---

## 4. Page Sections & Component Specs

### 4.1 Navigation Bar

**Location:** Top of page, sticky-capable
**Layout:** Flexbox, `space-between`
**Structure:**

```
[Logo Box + Logo Text]    [Home | About | Services | Blogs | Career]    [Contact Us]
```

- **Logo box:** 30×30px, burgundy background, rounded 6px, white SVG arrow icon
- **Logo text:** "INVENTIONS / TECHNOLOGIES" two-line, 11px, navy color
- **Nav links:** 12px, inactive `rgba(0,0,0,0.5)`, active `#1a1a3e` with burgundy 1.5px bottom border
- **CTA button:** Burgundy background, white text, 12px, padding 8×18px, rounded 7px
- **Bottom border:** `0.5px solid rgba(0,0,0,0.08)`

### 4.2 Hero Slider

**Type:** Horizontal sliding carousel, 4 slides
**Container:** `overflow: hidden`, border-bottom
**Track:** 400% width flex container, `translateX` animation
**Transition:** `0.6s cubic-bezier(0.4, 0, 0.2, 1)`
**Auto-advance:** Every 4 seconds
**Min height:** 320px per slide

#### Slide Content Structure

Each slide follows the same two-column layout:

```
[Left: eyebrow pill → H1 → subheading → paragraph → buttons]    [Right: 180px circle with SVG illustration]
```

#### Slide 1 — "We are Inventions"
- **Eyebrow:** "We are Inventions"
- **H1:** "The Technology **Solutions** Provider"
- **Body:** Company intro paragraph (founded 2010)
- **Buttons:** "Learn More" (primary) + "Our Services" (outline)
- **Illustration:** Globe/orbit SVG in blue (#378ADD)

#### Slide 2 — "Revolutionize Collaboration"
- **Eyebrow:** "Next-Gen Collaboration"
- **H1:** "Revolutionize **Collaboration**"
- **Subheading:** "Next-Gen Video Conferencing" (14px, burgundy)
- **Body:** Video conferencing benefits paragraph
- **Buttons:** "Explore Solutions" (primary) + "Watch Demo" (outline)
- **Illustration:** Video conference grid layout SVG

#### Slide 3 — "Secure Your Network"
- **Eyebrow:** "Protect Your Business"
- **H1:** "Secure Your **Network**"
- **Subheading:** "Advanced Security Solutions" (14px, burgundy)
- **Body:** Network security capabilities paragraph
- **Buttons:** "Get Protected" (primary) + "Security Audit" (outline)
- **Illustration:** Shield with checkmark SVG

#### Slide 4 — "Call Center Solutions"
- **Eyebrow:** "Communication Hub"
- **H1:** "Call Center **Solutions**"
- **Subheading:** "Intelligent Customer Engagement" (14px, burgundy)
- **Body:** Call center capabilities paragraph
- **Buttons:** "Get Started" (primary) + "Request Demo" (outline)
- **Illustration:** Headset with dial pad SVG

#### Slider Controls
- **Arrows:** 30×30px circles, `0.5px` border, hover → burgundy border + color
- **Dots:** 4 indicators, inactive = 8×8px circle `rgba(0,0,0,0.15)`, active = 24×8px rounded rect in `#800020`
- **Layout:** Centered row: `[← arrow] [dot] [dot] [dot] [dot] [→ arrow]`

### 4.3 Partners Section — Infinite Scrolling Marquee

**Card style:** Navy `#1a1a3e` background, rounded 14px, padding 24×28px, `overflow: hidden`
**Layout:** Centered text header + infinite scrolling logo marquee

- **Eyebrow:** "TRUSTED PARTNERS" — 10px, `#b8445a`, uppercase
- **Title:** "Our trusted partnership" — 15px, white
- **Subtitle:** 11px, `rgba(255,255,255,0.45)`
- **Divider:** 30×2px burgundy bar, centered

#### Marquee Specs

- **Container (`.logo-marquee`):** `overflow: hidden` with edge fade using CSS `mask-image` gradient (transparent at 0% and 100%, solid from 8% to 92%)
- **Track (`.logo-track`):** `display: flex`, `width: max-content`, CSS keyframe animation
- **Animation:** `@keyframes marquee` — `translateX(0)` to `translateX(-50%)`, 20s linear infinite
- **Pause on hover:** `animation-play-state: paused`
- **Seamless loop:** Logo pills are duplicated (7 items × 2 = 14 elements) so the second set fills in as the first scrolls out
- **Logo pills:** `rgba(255,255,255,0.06)` background, 0.5px border, `white-space: nowrap`, `flex-shrink: 0`
  - Standard: `rgba(255,255,255,0.55)` text
  - Highlighted (`.hi`): `rgba(255,255,255,0.8)` text, brighter border
  - Partners listed: Extron, Lenovo, Grandstream, Gonsin, ManageEngine, Xorcom, HP

### 4.4 Services Section — Stacking Cards on Scroll

**Layout:** Vertical stack with `position: sticky`
**Animation:** Cards stack on top of each other as the user scrolls

#### Stacking Specs

- **Container (`.services-stack`):** `flex-direction: column`, `min-height: 320px`
- **Cards (`.srv-card`):** `position: sticky` with staggered `top` values
  - Card 1: `top: 80px`, `z-index: 1`
  - Card 2: `top: 96px`, `z-index: 2`
  - Card 3: `top: 112px`, `z-index: 3`
- **Overlap:** `margin-top: -40px` on cards 2 and 3 creates the stacking overlap
- **Transition:** `transform 0.4s cubic-bezier(0.4, 0, 0.2, 1)`, `box-shadow 0.4s ease`
- **Dynamic shadow:** JS listener deepens `box-shadow` to `0 8px 28px rgba(0,0,0,0.3)` when a card is pinned (within 20px of its sticky top)
- **Default shadow:** `0 2px 12px rgba(0,0,0,0.15)`

#### Card Structure (horizontal layout)

```
┌────────────┬──────────────────────────────────────┐
│            │  TAG LABEL         ← 9px uppercase   │
│  Icon area │  Card Title        ← 14px white      │
│  (120px)   │  Description text  ← 11px light      │
│  #252550   │  [→] Learn more    ← burgundy link   │
└────────────┴──────────────────────────────────────┘
```

- **Icon area:** 120px wide, `min-height: 130px`, `#252550` background, centered 40×40px icon
- **Content area:** `padding: 18px 20px`, flex column, vertically centered

#### Service Cards

| # | Tag | Title | Icon Color |
|---|-----|-------|------------|
| 1 | UC & AV | Unified Communication & Audiovisual | Burgundy `#b8445a` |
| 2 | Security | Networking and Security | Blue `#378ADD` |
| 3 | Development | Software Development | Green `#1D9E75` |

### 4.5 News & Updates Section

**Layout:** 3-column CSS Grid, gap 14px
**Card background:** Navy `#1a1a3e`, rounded 12px

#### Card Structure

```
┌──────────────────────┐
│  Image Area (80px)   │  ← #252550 background
│    [Placeholder]     │  ← 36×36px rounded square
├──────────────────────┤
│  [Tag] [Date]        │  ← Tag badge + date string
│  Article Title       │  ← 12px white
│  Excerpt text        │  ← 11px, light
│  Read more →         │  ← burgundy link
└──────────────────────┘
```

#### Tag Styles

| Tag | Background | Text Color |
|-----|-----------|------------|
| Tech News | `rgba(55,138,221,0.2)` | `#6aa8e0` |
| In Sights | `rgba(29,158,117,0.2)` | `#5DCAA5` |

#### Articles

1. "Odoo Roadshow 2024 – Dar Es Salaam" — In Sights, 01 July 2024
2. "Why 2-factor authentication?" — Tech News, 01 July 2024
3. "Odoo ERP and CRM Software: Everything You Need to Know" — In Sights, 01 July 2024

### 4.6 Testimonials Section

**Outer container:** Navy `#1a1a3e`, rounded 14px, padding 28px
**Card background:** `#222255`, rounded 10px, padding 16px
**Layout:** 3-column CSS Grid, gap 12px

#### Card Structure

```
┌──────────────────────┐
│  ★ ★ ★ ★ ★          │  ← 12×12px gold squares
│                      │
│  "Quote text..."     │  ← 11px italic, rgba(255,255,255,0.6)
│  ─────────────       │  ← 0.5px divider
│  [Avatar] Name       │  ← 28px circle + name/role
│           Role       │
└──────────────────────┘
```

#### Testimonials Data

| # | Name | Role | Avatar BG | Stars |
|---|------|------|-----------|-------|
| 1 | Lucas Ndyamkama | MD, Logmath Ltd | `#800020` (burgundy) | 5/5 |
| 2 | Maria Kihwele | CTO, NMB Bank | `#185FA5` (blue) | 5/5 |
| 3 | John Msemwa | Director, CRDB Bank | `#0F6E56` (green) | 4/5 (last star faded) |

### 4.7 Clients Section

**Layout:** Tabs bar + horizontal scroll row + pagination dots

#### Tabs
- 4 tabs: Banks (active), Government, Telecom, Others
- Active: `#1a1a3e` text, burgundy 2px bottom border
- Inactive: `rgba(0,0,0,0.4)` text

#### Logo Carousel
- **Scroll buttons:** 28×28px circles at left/right
- **Logo cards:** Navy `#1a1a3e` background, rounded 10px, white text, min-width 90px
- **Logos shown:** NMB, NBC, CRDB, BOA, EXIM
- **Overflow:** Hidden (horizontal scroll expected)

#### Pagination Dots
- 3 dots, inactive = 6×6px circle `rgba(0,0,0,0.15)`
- Active = 18×6px rounded rect, burgundy `#800020`

### 4.8 Footer

**Background:** `#12122e` (darkest navy)
**Layout:** 5-column CSS Grid (`1.4fr 1.2fr 1fr 1fr 1.2fr`), gap 20px
**Top border:** `0.5px solid rgba(26,26,62,0.3)`

#### Column 1 — Brand
- Logo (28×28px burgundy box) + "INVENTIONS TECHNOLOGIES" in white
- Tagline: "Your trusted IT solutions partner since 2010."
- Social buttons: 4 circles (28×28px) — f, in, X, ig

#### Column 2 — Useful Links
Support, UC and AV, Network integration, Cyber security, System design

#### Column 3 — About Us
Who we are, Our ambition & values, Online store, Our locations, Careers

#### Column 4 — Contact Us
- +255 22 277 5873
- +255 746 985 750
- info@it.co.tz
- P.O.Box 34647
- Each preceded by a 14×14px burgundy-tinted icon square

#### Column 5 — Newsletter
- Description text
- Input field (placeholder "Email address") + "Subscribe" button (burgundy)

#### Footer Bottom Bar
- `0.5px` top border
- Left: "Copyright © 2026 IT. All rights reserved. · VAT reg: 111-443-025"
- Right: "202 Lukuledi, Regent Estate, Dar es Salaam"

---

## 5. Interactive Behaviors

### 5.1 Hero Slider

| Behavior | Detail |
|----------|--------|
| Auto-advance | 4-second interval, loops infinitely |
| Manual navigation | Arrow buttons (prev/next), dot buttons (go-to-slide) |
| Transition | `translateX` on `.hero-track`, 0.6s cubic-bezier |
| Reset on interaction | Any manual click resets the 4s auto-advance timer |
| State tracking | `currentSlide` variable, modular arithmetic for wrapping |

**JavaScript functions:**
- `updateSlider()` — applies `translateX` and updates active dot
- `slideHero(dir)` — advance by ±1 with wrap
- `goToSlide(idx)` — jump to specific slide
- `resetAutoSlide()` — clears and restarts the 4s interval

### 5.2 Services Stacking Cards

| Behavior | Detail |
|----------|--------|
| Mechanism | CSS `position: sticky` with staggered `top` offsets |
| Scroll effect | As user scrolls, each card pins at its top position; the next card slides up and covers it |
| Shadow feedback | JS scroll listener deepens box-shadow when card distance from sticky top < 20px |
| z-index order | Card 1 = 1, Card 2 = 2, Card 3 = 3 (later cards on top) |

### 5.3 Partners Infinite Scroll

| Behavior | Detail |
|----------|--------|
| Mechanism | CSS `@keyframes marquee` animation on `.logo-track` |
| Duration | 20 seconds, `linear`, `infinite` |
| Direction | Right to left (`translateX(0)` → `translateX(-50%)`) |
| Seamless loop | Logos duplicated (7 × 2 = 14 items); animation shifts exactly 50% |
| Hover | `animation-play-state: paused` |
| Edge fade | CSS `mask-image` linear gradient fades edges to transparent |

### 5.4 Back-to-Top Button

| Behavior | Detail |
|----------|--------|
| Trigger | Appears when `window.scrollY > 300` |
| Action | `window.scrollTo({top:0, behavior:'smooth'})` |
| Transition | opacity, transform, visibility — 0.3s ease |
| Hover | Background darkens to `#5c0018`, shadow deepens |

### 5.5 Hover States (CSS only)

- **Slider arrows:** border-color and color transition to burgundy on hover
- **Slider dots:** 0.3s ease transition on all properties
- **Partner marquee:** animation pauses on hover
- **Back-to-top:** background darkens, shadow deepens

### 5.6 Non-functional Elements (wireframe only)

These elements are visually present but have no JS behavior. Developers must implement:
- Tab switching in Clients section
- Client logo carousel scroll (left/right buttons)
- Client pagination dot state changes
- "Learn more" and "Read more" link navigation
- Newsletter email input and subscribe form submission
- Nav link routing
- CTA button ("Contact Us") action

---

## 6. Annotation System

The wireframe includes developer-facing annotation labels that should be **removed in production**.

| Class | Purpose | Color |
|-------|---------|-------|
| `.section-label` | Section identifier (e.g., "Navigation", "Hero section") | `rgba(0,0,0,0.3)` with burgundy left border |
| `.annot` | Change/improvement note (default) | Burgundy-tinted background, `#a0304a` text |
| `.annot.green` | "No changes needed" note | Green-tinted background, `#1a8a60` text |

These are positioned above each section and should be stripped during implementation.

---

## 7. Responsive Considerations

The wireframe is designed at **960px max-width** and does not include responsive breakpoints. The following elements will need mobile adaptation:

| Section | Desktop | Mobile Consideration |
|---------|---------|---------------------|
| Nav | Horizontal links + CTA | Hamburger menu needed |
| Hero slider | 2-column (text + illustration) | Stack vertically, reduce H1 size |
| Partners marquee | Continuous scroll | Reduce speed, ensure touch-friendly |
| Services stack | Horizontal cards, sticky | Adjust sticky tops for smaller viewport |
| News grid | 3 columns | Single column or 2-col |
| Testimonials grid | 3 columns | Horizontal swiper or single stack |
| Clients carousel | 5 visible logos | 2-3 visible, scroll functional |
| Footer grid | 5 columns | 2-column or single stack |
| Slider dots/arrows | Touch targets 30px | Increase to min 44px for mobile |
| Back-to-top button | 40px fixed bottom-right | Increase to 48px on mobile |

---

## 8. Asset Inventory

All illustrations are inline SVG. No external images, fonts, or assets are required.

| Location | SVG Description |
|----------|----------------|
| Nav logo | Arrow/upload icon (16×16) |
| Hero slide 1 | Globe with orbit lines and dots |
| Hero slide 2 | Video conference grid with monitor stand |
| Hero slide 3 | Shield with checkmark and dashed orbit |
| Hero slide 4 | Headset person with dial pad buttons |
| Service card 1 | Network nodes connected by lines |
| Service card 2 | Padlock with keyhole |
| Service card 3 | Monitor with code lines |
| Footer logo | Arrow/upload icon (14×14, smaller variant) |
| Back-to-top button | Upward chevron (16×16) |

---

## 9. Implementation Checklist

Developers should verify the following during implementation:

- [ ] Color tokens match the palette table in Section 2
- [ ] Hero slider auto-advances every 4 seconds
- [ ] Hero slider wraps from slide 4 back to slide 1 (and vice versa)
- [ ] Slider dots reflect the active slide state
- [ ] Manual slider interaction resets the auto-advance timer
- [ ] Partner logos scroll infinitely with seamless loop
- [ ] Partner marquee pauses on hover
- [ ] Partner marquee edge fade is visible on both sides
- [ ] Service cards stack on top of each other when scrolling
- [ ] Service card sticky positions are correct (80px, 96px, 112px)
- [ ] Service card box-shadow deepens when pinned
- [ ] Back-to-top button appears after scrolling 300px
- [ ] Back-to-top button smooth-scrolls to top on click
- [ ] All annotation labels (`.section-label`, `.annot`) are removed in production
- [ ] Tab switching in Clients section is functional
- [ ] Client logo scroll buttons work
- [ ] Newsletter form has validation and submission logic
- [ ] Nav links route to correct pages
- [ ] "Contact Us" CTA has assigned action
- [ ] All "Learn more" / "Read more" links navigate to correct destinations
- [ ] Responsive breakpoints are added for mobile/tablet
- [ ] Touch swipe support added to hero slider for mobile
- [ ] Accessibility: keyboard navigation for slider, ARIA labels, focus indicators

---

## 10. File Structure

```
/workspace
├── index.html              ← Wireframe (this file)
├── DEVELOPER_REVIEW.md     ← This document
├── DEVELOPER_REVIEW.pdf    ← Downloadable PDF version
└── README.md               ← Repository readme
```

No build system is required to view the wireframe. Open `index.html` directly in a browser.
