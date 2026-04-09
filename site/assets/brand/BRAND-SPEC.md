# Catkin — Personal Brand Identity System

## Julian Hicks · levhicks.com

---

## 1. Concept

A hand-drawn birch branch — three leaves above, two catkins hanging below. Single-color ink line art, no fills, no shading. Vectorized from a pen-and-ink source drawing (`source/birch-branch.jpg`).

The choice is personal and intentionally not explained on the site. Treat it as a fixed visual identity, not a metaphor to extend: don't generate "threshold-of-spring" copy, don't lean on birch symbolism in writing, don't pair it with seasonal motifs. The mark stands on its own visual character.

---

## 2. Logo Geometry (Authoritative)

The mark is a traced vector path, not a parametric construction — there is no authoritative coordinate table. The canonical source is `logo/logo-mark-black.svg` (viewBox `395 390 1262 1262`, square). All other variants are color swaps of the same path data.

Source bitmap: `source/birch-branch.jpg` (1024×1024). Re-trace pipeline:
```
sips -s format bmp source/birch-branch.jpg --out src.bmp
mkbitmap -f 4 -s 2 -t 0.48 src.bmp -o src.pbm
potrace --svg --turdsize 16 --alphamax 1.2 --opttolerance 0.8 -u 10 src.pbm -o trace.svg
# then crop viewBox to 395 390 1262 1262
```

---

## 3. Logo Assets

| File | Description |
|------|-------------|
| `logo/logo-mark.svg` | Primary — ink on parchment background |
| `logo/logo-mark-black.svg` | Black on transparent |
| `logo/logo-mark-white.svg` | White on transparent |
| `logo/logo-mark-gold.svg` | Gold (#7A6020) on transparent |
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
| gold | `#7A6020` | `#B8922E` | Primary accent, links |
| gold-hi | `#B8922E` | `#D4B24A` | Hover states |
| green | `#3D6B3E` | `#5E9460` | Accent rule, focus outline, blockquote border |
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

Base unit: **10px**. Empirically the right step size for the Atkinson Hyperlegible Next body at the chosen measure — not derived from the mark. Don't rebase the grid to chase a relationship with the logo; consistency across the stylesheet is the value here.

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

- Mark fades in on reveal (opacity 0 → 1, 600ms)
- Easing: cubic-bezier(0.22, 1, 0.36, 1)
- No transform, no bounce, no overshoot
- Respect prefers-reduced-motion (animation: none)

The mark is a still ink drawing and is treated as such. No sway, no settle, no self-drawing wipe — those would all introduce a register the drawing doesn't actually carry. Fade in, get out of the way.

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
| `export/logo-mark-gold-256.png` | 256×256 | Accent use |

---

## 10. Non-Negotiable Rules

1. No outlines on the mark (it is itself line art — never stroke or outline the path)
2. No gradients anywhere
3. No centering everything — prefer left/edge alignment
4. No rotating the mark
5. No enclosing shapes (circles, squares, shields) around the mark
6. No drop shadows
7. No re-coloring outside the four sanctioned variants (black / white / gold / parchment-bg primary)

---

## File Structure

```
/brand
  /source
    birch-branch.jpg          (untracked-from-render source bitmap)
  /logo
    logo-mark.svg
    logo-mark-black.svg
    logo-mark-white.svg
    logo-mark-gold.svg
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
    logo-mark-gold-256.png
```
