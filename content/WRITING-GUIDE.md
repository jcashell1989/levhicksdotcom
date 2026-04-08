# Writing guide

How to add a post to the writing section of levhicks.com.

## 1. Create the file

Drop a markdown file into `content/writing/`. The filename stem becomes
the URL slug by default (e.g. `why-this-site-exists.md` →
`/writing/why-this-site-exists/`).

## 2. Frontmatter

Every post needs YAML frontmatter at the top of the file, between `---`
markers:

```markdown
---
title: Your post title
date: 2026-04-08
excerpt: One-line summary that shows up on the writing index.
slug: your-slug         # optional; defaults to the filename stem
draft: false            # optional; drafts build but don't appear in the listing
pinned: false           # optional; pinned posts sort above everything else
featured: false         # optional; reserved for future use
---

Body starts here in normal markdown.
```

**Required fields:** `title`, `date` (must be `YYYY-MM-DD`).
**Everything else is optional.**

### Draft behavior

`draft: true` means:
- The post still builds to its URL (so you can share a preview link)
- It's excluded from `/writing/` (the public listing)
- It gets `<meta name="robots" content="noindex, nofollow">`

Flip to `draft: false` (or remove the field) when you're ready to publish.

## 3. Write the body

Standard markdown, rendered through pandoc. What works:
- Headings (`##`, `###`)
- Paragraphs, bold, italic
- Lists (ordered + unordered)
- Links and inline code
- Code blocks (```) — rendered in Maple Mono
- Blockquotes (green left border)

## 4. Build

From the repo root:

```bash
python3 build.py
```

This:
- Renders every post to `site/writing/<slug>/index.html` from `templates/post.html`
- Rebuilds the listing at `site/writing/index.html` from `templates/writing-index.html`
- Sorts published posts: pinned first, then by date descending

**Requirement:** pandoc has to be on your PATH. If it isn't:
`brew install pandoc`.

## 5. Deploy

Commit + push:

```bash
git add -A
git commit -m "Add post: <title>"
git push
```

Then drag the updated `site/` folder onto the Netlify dashboard's deploy
drop zone. (Or, if continuous deploy from GitHub is set up later, the
push alone will do it.)

## Quick reference

| Want to... | Do |
|---|---|
| Add a post | New file in `content/writing/`, fill frontmatter, `python3 build.py` |
| Share a draft privately | Set `draft: true`, build, share `/writing/<slug>/` URL directly |
| Pin a post to the top | Set `pinned: true` |
| Change the URL | Set `slug: custom-slug` (without this, the filename stem is used) |
| Unpublish a post | Set `draft: true` and rebuild, or delete the `.md` file and rebuild |

## Notes

- This file lives at `content/WRITING-GUIDE.md` on purpose — `build.py`
  only reads `content/writing/*.md`, so this guide stays out of the
  built site but is still in the repo.
- If you ever need to also exclude files from inside `content/writing/`
  without deleting them, the cleanest route is to add a filename
  convention (e.g. prefix with `_`) and teach `build.py` to skip them.
