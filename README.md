# 🚀 ImageSync Pro | by ShadyBilla

A high-performance local web dashboard built with Streamlit for optimizing images and serving them instantly via GitHub.

## 🤔 What's the Use Case?
If you're a developer, blogger, or designer, you often need a fast way to:
1. **Compress Images**: Save storage space by converting heavy PNGs/JPGs to WebP format.
2. **Auto-Host**: Get direct links for your website, GitHub README, or portfolio without manual uploads.
3. **Speed Up Workflow**: Drag-and-drop multiple images, let them optimize in parallel, and push them to your repo in one click! ⚡
4. Personally i use it for hosting screenshots of apps/tools/sites/softwares... 

---

## 🛠️ How to Create One for Yourself

### 1. Using this Repo (The Fast Way)
1. **Fork or Clone**: Download this repository to your computer.
2. **Setup Virtual Environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure `app.py`**:
   Update the `GITHUB_USER` and `GITHUB_REPO` variables at the top of `app.py` to match your GitHub details.
5. **Run It**:
   ```bash
   python -m streamlit run app.py
   ```

### 2. Building from Scratch
- **Language**: Python 🐍
- **Frontend**: Streamlit (for the UI)
- **Processing**: Pillow (for WebP conversion)
- **Deployment**: Git (to push to GitHub)

Each image you upload is converted to WebP at ~80% quality (customizable!), keeping your repo lean and your websites fast.

---

## 🛡️ Security Check
- **No Personal Tokens**: Ensure your GitHub Auth is handled via SSH or Git Credential Manager locally.
- **Assets Folder**: Processed images are stored in `assets/`. Make sure this folder is tracked by git.

## 🚀 Get Started Now!
Just drop an image into the dashboard and watch the magic happen. ✨
