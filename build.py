#!/usr/bin/env python3
"""Build the writing section of levhicks.com.

Reads markdown posts from content/writing/*.md, renders the body with
pandoc, fills in templates from templates/, and writes output to
site/writing/<slug>/index.html and site/writing/index.html.

Frontmatter schema (YAML between --- markers):
  title:     required
  date:      required, YYYY-MM-DD
  excerpt:   optional, one-line summary for the listing
  slug:      optional, defaults to the filename stem
  draft:     optional bool, drafts build but are excluded from the listing
  pinned:    optional bool, pinned posts sort above everything else
  featured:  optional bool, reserved for future use

Run from the repo root:  python3 build.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
CONTENT_DIR = ROOT / "content" / "writing"
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_DIR = ROOT / "site" / "writing"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


@dataclass
class Post:
    slug: str
    title: str
    date: date
    excerpt: str
    draft: bool
    pinned: bool
    featured: bool
    body_html: str


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("post is missing --- frontmatter ---")
    raw, body = m.group(1), m.group(2)
    meta = yaml.safe_load(raw) or {}
    if not isinstance(meta, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return meta, body


def load_post(md_path: Path) -> Post:
    meta, body = parse_frontmatter(md_path.read_text())
    for required in ("title", "date"):
        if required not in meta:
            raise ValueError(f"{md_path.name}: missing required field '{required}'")

    raw_date = meta["date"]
    if isinstance(raw_date, date):
        d = raw_date
    else:
        try:
            d = date.fromisoformat(str(raw_date).strip())
        except ValueError as e:
            raise ValueError(
                f"{md_path.name}: bad date '{raw_date}' (want YYYY-MM-DD)"
            ) from e

    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html5", "--no-highlight"],
        input=body,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc failed on {md_path.name}:\n{result.stderr}")

    return Post(
        slug=str(meta.get("slug") or md_path.stem).strip(),
        title=str(meta["title"]).strip(),
        date=d,
        excerpt=str(meta.get("excerpt") or "").strip(),
        draft=bool(meta.get("draft", False)),
        pinned=bool(meta.get("pinned", False)),
        featured=bool(meta.get("featured", False)),
        body_html=result.stdout.strip(),
    )


def render(template: str, vars: dict) -> str:
    out = template
    for k, v in vars.items():
        out = out.replace("{{" + k + "}}", str(v))
    return out


def fmt_month_year(d: date) -> str:
    return d.strftime("%b %Y")


def build() -> None:
    if not CONTENT_DIR.exists():
        print(f"error: {CONTENT_DIR} does not exist", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(CONTENT_DIR.glob("*.md"))
    if not md_files:
        print(f"warning: no posts found in {CONTENT_DIR}")

    posts = [load_post(p) for p in md_files]
    published = [p for p in posts if not p.draft]
    # Sort: pinned first, then by date descending
    published.sort(key=lambda p: (not p.pinned, -p.date.toordinal()))

    post_template = (TEMPLATES_DIR / "post.html").read_text()
    index_template = (TEMPLATES_DIR / "writing-index.html").read_text()
    entry_template = (TEMPLATES_DIR / "writing-entry.html").read_text()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Render each post page (drafts build too — shareable by direct link)
    for p in posts:
        html = render(
            post_template,
            {
                "SLUG": p.slug,
                "TITLE": p.title,
                "EXCERPT": p.excerpt,
                "DATE_ISO": p.date.isoformat(),
                "DATE_HUMAN": fmt_month_year(p.date),
                "BODY": p.body_html,
                "ROBOTS": "noindex, nofollow" if p.draft else "index, follow",
            },
        )
        dest = OUTPUT_DIR / p.slug / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html)
        tag = " [draft]" if p.draft else ""
        print(f"  built site/writing/{p.slug}/index.html{tag}")

    # Render the listing
    if published:
        entries_html = "\n".join(
            render(
                entry_template,
                {
                    "SLUG": p.slug,
                    "TITLE": p.title,
                    "DATE_ISO": p.date.isoformat(),
                    "DATE_HUMAN": fmt_month_year(p.date),
                    "EXCERPT": p.excerpt,
                },
            )
            for p in published
        )
    else:
        entries_html = '      <li class="empty">Nothing published yet.</li>'

    index_html = render(index_template, {"ENTRIES": entries_html})
    (OUTPUT_DIR / "index.html").write_text(index_html)
    print(f"  built site/writing/index.html")

    drafts = len(posts) - len(published)
    print(f"\n{len(published)} published, {drafts} draft(s)")


if __name__ == "__main__":
    build()
