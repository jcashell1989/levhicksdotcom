# levhicks.com Hosting Plan

**Goal:** Get the Smart Assistant brochure (and eventually other pages) live at levhicks.com with zero ongoing cost and minimal ops burden.

**Starting assumptions:**
- `levhicks.com` is currently registered at **Squarespace** (formerly Google Domains — Squarespace bought the Google Domains business in 2023, so old Google Domains registrations migrated automatically).
- You have zero prior hosting experience.
- The content today is a single static HTML file (`smart-assistant-brochure.html`) with no backend, no build step, no database. Future pages will likely also be static.
- You want this to be easy to maintain and easy to update.

---

## Recommendation: Netlify + keep Squarespace as the registrar

**Why Netlify over the alternatives:**
- **Zero CLI required.** You can literally drag a folder onto their dashboard and it's live. Perfect for a first-time experience.
- **Free forever for what you need.** The free tier gives 100 GB/month bandwidth and unlimited sites. A brochure site will use less than 1% of that.
- **Free HTTPS automatically.** Netlify issues Let's Encrypt certificates for you — no cert management.
- **Custom domain support on the free tier.** Many free hosts charge for custom domains; Netlify doesn't.
- **You don't have to move the domain registration.** Squarespace keeps being your registrar. You just point DNS at Netlify.
- **Good docs for beginners.** Their custom domain walkthrough is one of the clearest in the industry.

**Why not the alternatives (briefly):**
- **GitHub Pages** — good, but requires learning git basics and using the command line or GitHub Desktop. More steps for a first hosting experience.
- **Cloudflare Pages** — excellent technically, but the dashboard is denser and assumes more familiarity. Worth graduating to later.
- **Vercel** — equivalent to Netlify but historically more focused on developers building apps. Slightly more intimidating UI.
- **Squarespace hosting** — Squarespace offers hosting, but it's ~$16/month and it forces you into their template/editor system. Not appropriate for hand-written HTML.

---

## Plan

### Phase 1: Prepare the content (before touching anything online)

1. **Finalize the design first.** Don't host a mockup you're going to redesign in a week. Wait for:
   - The color scheme (cleo-parchment) applied
   - The logo added
   - One end-to-end review pass
2. **URL structure (decided):**
   - `levhicks.com` → a proper personal homepage
   - `levhicks.com/mockups/914ai/` → the Smart Assistant brochure
   - Future mockups can live at `levhicks.com/mockups/<project>/`
3. **Site folder structure:**
   ```
   site/
     index.html                      (personal homepage — to be written)
     assets/                         (shared CSS, logos, fonts if we self-host any)
     mockups/
       914ai/
         index.html                  (the brochure, renamed from smart-assistant-brochure.html)
         logo.svg                    (when ready)
   ```
   Naming the brochure `index.html` inside `mockups/914ai/` is what makes the URL `levhicks.com/mockups/914ai/` work without a visible `.html` extension.

### Phase 2: Set up Netlify (15-20 min, first time)

1. Go to https://netlify.com and sign up with your GitHub or email (GitHub login is easier if you end up wanting to auto-deploy from a repo later).
2. On the dashboard, click **"Add new site"** → **"Deploy manually"**.
3. Drag the `site/` folder you prepared onto the drop zone. Netlify uploads it.
4. Netlify gives you a random URL like `cosmic-horse-1234.netlify.app`. Open it — your site is already live at that address.
5. Test the URL in a browser. Test it on your phone. Make sure everything loads, fonts render, images show.

### Phase 3: Wire up levhicks.com (20-30 min, first time)

This is the step that feels scary but is routine once you've done it.

1. **In the Netlify dashboard**, go to your site → **"Domain management"** → **"Add a domain"**.
2. Enter `levhicks.com`. Netlify will say "You don't own this domain yet" — click through anyway and confirm you own it.
3. Netlify will then show you **DNS records** you need to add at Squarespace. There are two approaches Netlify will offer:

   **Option A: Use Netlify DNS (Netlify recommended, simplest long-term)**
   - Netlify becomes your domain's nameserver
   - You change nameservers at Squarespace to point at Netlify's (4 addresses like `dns1.p01.nsone.net`)
   - Everything domain-related (DNS, records) is then managed in Netlify
   - **Downside:** if you ever use email on this domain (like `julian@levhicks.com`), you'd also need to configure the email DNS records inside Netlify instead of Squarespace.

   **Option B: Keep DNS at Squarespace, add a CNAME / A record (simplest first time)**
   - You stay with Squarespace DNS
   - You add a few records that Netlify gives you:
     - An `A` record on `@` (the root) pointing to Netlify's load balancer IP (they'll show you the exact IP, usually `75.2.60.5` for apex domains)
     - A `CNAME` record on `www` pointing to your Netlify URL (like `cosmic-horse-1234.netlify.app`)
   - **Upside:** if you have email or other DNS stuff configured at Squarespace, none of it changes.

   **My recommendation for you: Option B.** It's smaller, less scary, and keeps the number of control panels you juggle low. Switch to Option A later if you ever want Netlify's DNS features.

4. **In Squarespace's domain manager** (Account → Domains → levhicks.com → DNS Settings):
   - Click **Add Record** (or **Custom Records**)
   - Add each record Netlify gave you, exactly as shown
   - Save

5. **Wait.** DNS changes propagate globally in 5 minutes to 48 hours, usually under an hour. Don't panic if levhicks.com doesn't load immediately.

6. **Verify.** Back in Netlify, the domain should eventually go from "Awaiting External DNS" to "Netlify DNS" or "Verified." Once it's verified, Netlify will automatically provision a Let's Encrypt HTTPS certificate (takes another few minutes).

7. Visit `https://levhicks.com` — should show your site, with a padlock.

### Phase 4: Make updates easy

Every future update to the site will be:
1. Edit the files locally
2. Open Netlify dashboard → your site → **Deploys** tab
3. Drag the updated folder onto the drop zone → done

This is the "zero experience" workflow. If you ever want nicer updates (git-based auto-deploy), you can switch later. The manual drag workflow is fine for a brochure.

---

## DNS records cheat sheet (Option B)

When Netlify asks you to add records at Squarespace, you'll see something like this. Use the actual values Netlify gives you, not these examples.

| Type  | Host / Name | Value / Points to            | TTL   |
|-------|-------------|------------------------------|-------|
| A     | `@`         | `75.2.60.5` (Netlify apex)   | 3600  |
| CNAME | `www`       | `your-site.netlify.app`      | 3600  |

Some registrars use `@` for "root" and some use blank — Squarespace uses `@`.

The `www` CNAME makes `www.levhicks.com` also work. Netlify handles the redirect between `www` and non-`www` for you — you can pick which one is canonical in the Netlify dashboard (recommendation: pick `https://levhicks.com` without the `www`).

---

## Cost summary

| Item | Cost |
|------|------|
| Netlify free tier | $0/month |
| Squarespace domain (existing) | ~$12/year (already paying) |
| Let's Encrypt HTTPS | $0 (automatic via Netlify) |
| **Ongoing total for hosting** | **$0/month** |

You'll only pay for hosting if the site gets > 100 GB/month of traffic, which is not going to happen for a personal brochure.

---

## Pre-flight checklist (before starting)

Don't start Phase 2 until these are true:

- [ ] Brochure design is finalized (color scheme, logo, layout)
- [ ] You've decided: will `levhicks.com` root be the brochure, a landing page, or something else?
- [ ] You have access to your Squarespace account and can log into the domain DNS settings
- [ ] You have 30-60 min of uninterrupted time (DNS propagation wait is the biggest unknown)

---

## Things that can go wrong (and what to do)

| Problem | Cause | Fix |
|---------|-------|-----|
| `levhicks.com` doesn't load after DNS changes | Propagation delay | Wait up to 48h. Use https://dnschecker.org to see if your records are visible globally. |
| "Site can't be reached" after DNS propagation | Wrong record type or typo | Double-check the A record IP matches what Netlify gave you. Squarespace sometimes adds trailing dots to CNAMEs — remove them. |
| HTTPS certificate doesn't provision | DNS not fully resolved yet | Wait 10-15 min after DNS verified. Force a retry in Netlify dashboard → HTTPS → Renew certificate. |
| Site loads but fonts are missing | Google Fonts blocked or path issue | Check browser console. Usually not a hosting problem — a file path issue. |
| You want to undo everything | Revert DNS records in Squarespace | Set records back to whatever they were before (Squarespace keeps history). Netlify free-tier sites can just sit there unused. |

---

## Decisions made

- **Root** (`levhicks.com`) → personal homepage (to be designed/written separately)
- **Brochure** → `levhicks.com/mockups/914ai/`
- **Future mockups** → `levhicks.com/mockups/<project>/`

## Still to decide

1. **www or no www?**
   - `https://levhicks.com` (no www) — cleaner, modern convention, my default recommendation
   - `https://www.levhicks.com` — older convention, some people prefer it
   - Either way, Netlify handles redirecting the other one

2. **When to actually execute?**
   - My recommendation: finish cleo-parchment + logo first, host once, then iterate on the homepage.
   - The homepage doesn't need to be done before first deploy — a minimal "Julian Hicks" placeholder is fine at the root until you want to build out the real thing.

---

## When you're ready to actually execute

Ping me and I'll:
- Write a minimal `index.html` landing page if you want one at the root
- Prepare the file structure in this folder (`site/`) ready to drop on Netlify
- Walk you through the Netlify sign-up and DNS wiring step by step, in real time

I can't do the Netlify account creation or the Squarespace DNS edits for you — those need your logins — but I can make every file change and tell you exactly which button to click.
