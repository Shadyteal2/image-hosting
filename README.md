# 🚀 ImageSync Pro | by ShadyBilla

A high-performance local web dashboard built with Streamlit for optimizing images and serving them instantly via GitHub.

## 🤔 What's the Use Case?
If you're a developer, blogger, or designer, you often need a fast way to:
1. **Compress Images**: Save storage space by converting heavy PNGs/JPGs to WebP format.
2. **Auto-Host**: Get direct links for your website, GitHub README, or portfolio without manual uploads.
3. **Speed Up Workflow**: Drag-and-drop multiple images, let them optimize in parallel, and push them to your repo in one click! ⚡
4. Personally i use it for hosting screenshots of apps/tools/sites/softwares... 

---

Each image you upload is converted to WebP at customizable quality, keeping your repo lean and your websites fast.

---

## 📱 Mobile & Cloud Setup (Personal Use)

To use this from your phone without leaving your PC on:

### 1. Deploy to Streamlit Cloud
1. Push your code to your GitHub repo.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and connect your repo.
3. **Crucial Step**: In the Streamlit Cloud dashboard, go to **Settings > Secrets** and add your GitHub Token:
   ```toml
   GITHUB_TOKEN = "your_personal_access_token_here"
   ```
   *(Generate a token at [GitHub Settings](https://github.com/settings/tokens) with `repo` permissions.)*

### 2. Use on Mobile
1. Open the deployed URL on your phone's browser.
2. **Android**: Tap the menu (three dots) and select **"Install App"** or **"Add to Home Screen"**.
3. **iOS**: Tap the **Share** button and select **"Add to Home Screen"**.
4. Now you have a high-performance image uploader right on your phone! 🚀

---

## 🛡️ Security Check
- **No Personal Tokens**: Ensure your GitHub Auth is handled via SSH or Git Credential Manager locally.
- **Assets Folder**: Processed images are stored in `assets/`. Make sure this folder is tracked by git.

## 🚀 Get Started Now!
Just drop an image into the dashboard and watch the magic happen. ✨
