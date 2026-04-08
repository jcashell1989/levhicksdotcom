# Deploying levhicks.com to Netlify

A step-by-step guide for your exact setup: Squarespace registrar, no CLI, drag-and-drop deploy.

---

## Before you start

Make sure you have:
- [ ] Access to your Squarespace account (you'll need to edit DNS records)
- [ ] 30–60 minutes of uninterrupted time (most of it is waiting for DNS)
- [ ] The `site/` folder in this project — that's what you'll drag onto Netlify

---

## Step 1 — Sign up for Netlify

1. Go to **https://netlify.com**
2. Click **Sign up**
3. Sign up with **GitHub** (easiest — links your account for future use) or email
4. Complete the onboarding prompts; skip anything about connecting a repository

---

## Step 2 — Deploy the site

1. From the Netlify dashboard, click **"Add new site"** → **"Deploy manually"**
2. You'll see a drag-and-drop zone
3. Open Finder, navigate to this project folder (`levhicksdotcom/`), and drag the **`site/`** folder onto the drop zone
4. Netlify uploads it and gives you a random URL like `cosmic-horse-1234.netlify.app`
5. Click that URL — your site is live at that address immediately
6. **Test it:** open it in a browser, open it on your phone, check that the font loads and all three links work

If anything looks wrong, fix the files locally and re-drag the folder (Step 6 below covers this).

---

## Step 3 — Add your custom domain in Netlify

1. In the Netlify dashboard, go to your site → **"Domain management"** → **"Add a domain"**
2. Type `levhicks.com` and click **Verify**
3. Netlify will say you don't own it yet — click through and confirm you do
4. Netlify will show you DNS records to add. You want **Option B: keep DNS at Squarespace**
5. Note down the two records Netlify gives you — they'll look like:

   | Type  | Host | Value |
   |-------|------|-------|
   | A     | `@`  | `75.2.60.5` (use the exact IP Netlify shows you) |
   | CNAME | `www` | `your-site-name.netlify.app` |

---

## Step 4 — Add DNS records at Squarespace

1. Log into **Squarespace** → **Account** → **Domains** → click `levhicks.com`
2. Go to **DNS Settings** (sometimes called "Custom Records" or "Advanced DNS")
3. Add the **A record**:
   - Type: `A`
   - Host: `@`
   - Value: the IP address Netlify gave you (e.g. `75.2.60.5`)
   - TTL: `3600` (or leave as default)
4. Add the **CNAME record**:
   - Type: `CNAME`
   - Host: `www`
   - Value: your Netlify URL (e.g. `cosmic-horse-1234.netlify.app`)
   - TTL: `3600` (or leave as default)
   - **Note:** if Squarespace adds a trailing dot to the CNAME value, remove it
5. Save

---

## Step 5 — Wait for DNS to propagate

DNS changes take anywhere from 5 minutes to 48 hours. Usually under an hour.

- **Don't panic** if `levhicks.com` doesn't load immediately
- To check progress: go to **https://dnschecker.org**, enter `levhicks.com`, and watch the green checkmarks fill in globally
- Back in Netlify, the domain status will change from "Awaiting External DNS" to verified once it resolves

Once DNS is verified, Netlify automatically provisions a free HTTPS certificate (Let's Encrypt). This takes a few extra minutes. You'll see a padlock appear in the Netlify dashboard.

---

## Step 6 — Set the canonical domain (www vs no-www)

In Netlify → Domain management, set your **primary domain** to `https://levhicks.com` (no www). Netlify will automatically redirect `www.levhicks.com` to it.

---

## Step 7 — Verify everything

Visit **https://levhicks.com** — you should see:
- Your homepage with a padlock (HTTPS)
- Correct font and colors
- All three links working

Also test **https://www.levhicks.com** — it should redirect to the non-www version.

---

## Making future updates

Every time you want to update the site:

1. Edit the files locally in the `site/` folder
2. Open Netlify dashboard → your site → **Deploys** tab
3. Drag the updated `site/` folder onto the drop zone
4. Done — live in seconds

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| Site doesn't load after DNS changes | Propagation delay | Wait up to 48h. Check https://dnschecker.org |
| "Site can't be reached" after propagation | Wrong record or typo | Double-check the A record IP matches exactly what Netlify showed you |
| HTTPS certificate not provisioning | DNS not fully resolved yet | Wait 10–15 min after DNS verified, then in Netlify: HTTPS → Renew certificate |
| Font not loading | Google Fonts blocked or offline | Check browser console. Not a hosting issue — the font loads from Google's CDN |
| www doesn't redirect | Primary domain not set | In Netlify → Domain management, confirm `levhicks.com` (no www) is the primary |
