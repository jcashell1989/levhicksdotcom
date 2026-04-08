# Threshold — Personal Brand Identity System

## Julian Hicks · levhicks.com

---

## 1. Concept

Two asymmetric pillars separated by a deliberate gap. The logo is the space between — a threshold. Derived from Hermes Strophaios ("of the door-hinge"), the god of boundaries, translation, and movement between worlds.

The left pillar is heavier and taller with a 45° chamfer on its inner edge at ~40% height, creating a subtle doorway gesture. The right pillar is narrower with a slight outward lean (~5°), introducing directionality — something is about to move through.

---

## 2. Logo Geometry (Authoritative)

All coordinates reference a 256×256 viewBox.

**Left pillar (with threshold notch):**
```
M 72 32 L 132 32 L 132 112 L 116 128 L 116 224 L 72 224 Z
```

**Right pillar (outward lean):**
```
M 152 48 L 192 44 L 200 224 L 160 224 Z
```

| Property        | Value           |
|-----------------|-----------------|
| Left width      | 60 (top), 44 (below notch) |
| Right width     | 40              |
| Gap (top)       | 20              |
| Gap (bottom)    | 44              |
| Notch angle     | 45°             |
| Notch depth     | 16              |
| Notch position  | ~42% from top   |
| Right lean      | ~5° outward     |

---

## 3. Logo Assets

| File | Description |
|------|-------------|
| `logo/logo-mark.svg` | Primary — ink on parchment background |
| `logo/logo-mark-black.svg` | Black on transparent |
| `logo/logo-mark-white.svg` | White on transparent |
| `logo/logo-mark-bronze.svg` | Bronze (#8B4513) on transparent |
| `logo/favicon.svg` | Favicon source (64px render, 256 viewBox) |
| `logo/logo-lockup-horizontal.svg` | Mark + "Julian Hicks" wordmark (Atkinson Hyperlegible Next) |

---

## 4. Color System

### Base Palette

| Token | Light | Dark |
|-------|-------|------|
| bg-primary | `#F5F0E8` | `#0B0B0B` |
| bg-secondary | `#EAE3D6` | `#1A1A1A` |
| bg-tertiary | `#DFD8CA` | `#2A2A28` |
| ink-primary | `#0B0B0B` | `#F5F0E8` |
| ink-secondary | `#1A1A1A` | `#EAE3D6` |
| ink-muted | `#4A4A48` | `#9C9A92` |

### Accents

| Token | Light | Dark | Use |
|-------|-------|------|-----|
| bronze | `#8B4513` | `#C4813A` | Primary accent, links |
| warm | `#A05A2C` | `#D4844A` | Hover states |
| slate | `#3A4A5A` | `#7A9AB4` | Secondary text, Chinese name |
| sage | `#6B7D6D` | `#8FA88F` | Tertiary accent, tags |

### Rules
- Background: parchment tones only (bg-primary or bg-secondary)
- Logo: always single-color fill
- Accents: <10% of any composition
- No gradients

---

## 5. Typography

### Primary: Atkinson Hyperlegible Next
Self-hosted variable font (see `site/assets/fonts/`). Used for body, headings,
labels, and wordmark. Accessibility-first design — letterform disambiguation is
a core brand value, which takes priority over stylistic variety.

- Body: weight 400
- Headings (h1): weight 700, -0.03em tracking
- Labels: weight 700, uppercase, 0.08em tracking
- Wordmark: weight 700, -0.03em tracking

### Fallback Stack
```
Sans: "Atkinson Hyperlegible Next", system-ui, sans-serif
```

No serif display face. No monospace face (add only if a /code page ever needs one).

---

## 6. Spacing

Base unit derived from right pillar width: **10px** (40/256 × 64).

| Token | Value |
|-------|-------|
| xs | 5px |
| sm | 10px |
| md | 20px |
| lg | 40px |
| xl | 80px |

---

## 7. Layout Principles

- Prefer edge alignment over center
- Allow slight asymmetry (left-heavy, matching the mark)
- Container max-width: 960px
- Offset content by 10% from left when appropriate
- Base grid: 10px increments

---

## 8. Motion

- Gap subtly widens on reveal (scaleX 0.92 → 1)
- Pillars stagger in (left first, right 100ms later)
- Easing: cubic-bezier(0.22, 1, 0.36, 1)
- No bounce, no overshoot
- Respect prefers-reduced-motion

---

## 9. Exports

| File | Size | Use |
|------|------|-----|
| `export/favicon-16.png` | 16×16 | Browser tab |
| `export/favicon-32.png` | 32×32 | Browser tab (retina) |
| `export/apple-touch-icon.png` | 180×180 | iOS home screen |
| `export/logo-512.png` | 512×512 | Social / OG image |
| `export/logo-mark-black-256.png` | 256×256 | General use |
| `export/logo-mark-black-512.png` | 512×512 | Print |
| `export/logo-mark-white-256.png` | 256×256 | Dark backgrounds |
| `export/logo-mark-white-512.png` | 512×512 | Dark backgrounds (print) |
| `export/logo-mark-bronze-256.png` | 256×256 | Accent use |

---

## 10. Non-Negotiable Rules

1. No outlines on the mark
2. No gradients anywhere
3. No centering everything — prefer left/edge alignment
4. No rotating the mark
5. No enclosing shapes (circles, squares, shields)
6. No drop shadows
7. The gap is sacred — never fill it, overlay it, or place text in it

---

## File Structure

```
/brand
  /logo
    logo-mark.svg
    logo-mark-black.svg
    logo-mark-white.svg
    logo-mark-bronze.svg
    favicon.svg
    logo-lockup-horizontal.svg
  /export
    favicon-16.png
    favicon-32.png
    apple-touch-icon.png
    logo-512.png
    logo-mark-black-256.png
    logo-mark-black-512.png
    logo-mark-white-256.png
    logo-mark-white-512.png
    logo-mark-bronze-256.png
```
