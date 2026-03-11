# 🚀 ImageSync Pro | by ShadyBilla

A high-performance local web dashboard built with Streamlit for optimizing images and serving them instantly via GitHub.

## 🤔 What's the Use Case?
If you're a developer, blogger, or designer, you often need a fast way to:
1. **Compress Images**: Save storage space by converting heavy PNGs/JPGs to WebP format.
2. **Auto-Host**: Get direct links for your website, GitHub README, or portfolio without manual uploads.
3. **Speed Up Workflow**: Drag-and-drop multiple images, let them optimize in parallel, and push them to your repo in one click! ⚡

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

### 🗝️ Troubleshooting "Bad Credentials" (401)
If you see a `401 Bad Credentials` error, check your token settings on GitHub:
- **Token Type**: Use a **Classic Token** (easier) or a Fine-grained Token.
- **Classic Token Permissions**: Ensure you check the **`repo`** scope (Full control of private repositories).
- **Fine-grained Token Permissions**:
  - `Contents`: Read & Write
  - `Metadata`: Read-only
- **Format**: Ensure there are no extra spaces or quotes inside the `""` in your Streamlit Secrets.

---

## 🛠️ Local Setup
To run this project on your own machine:
1. `pip install -r requirements.txt`
2. Set your token as an environment variable: `export GITHUB_TOKEN=your_token`
3. `python -m streamlit run app.py`

---

## 🛡️ Security Check
- **No Personal Tokens**: Ensure your token is strictly kept in Steamlit Secrets or local environment variables. **Never** hardcode it in `app.py`.
- **Assets Folder**: Processed images are stored in `assets/`.

## 🚀 Get Started Now!
Just drop an image into the dashboard and watch the magic happen. ✨
