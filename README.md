# 🚀 ImageSync Pro | by ShadyBilla

A high-performance local & cloud web dashboard built with Streamlit for optimizing images and serving them instantly via GitHub.

## 🤔 What's the Use Case?
- **Speed**: Optimize and sync images to your repo in seconds, even from your phone.
- **Hosting**: Instant `raw.githubusercontent.com` links for your websites or portfolio.
- **Portability**: No more opening your PC just to upload an image—use the mobile web app!
- **Personally I use this repository exclusively to host public domain screenshots of apps/sites/softwares/tools etc**
---

## 🔒 Security Architecture
How does this app stay secure when live?
1. **The Key (GITHUB_TOKEN)**: Your personal access token acts as a master key. It is stored safely in **Streamlit Secrets** (on the cloud) or your **Environment Variables** (locally). It is **never** visible to users.
2. **The Guard (DASHBOARD_PIN)**: To prevent strangers from spamming your repository, I've added a **PIN Protection** layer. You define a PIN in your Secrets, and the "Deploy" button will only work if the correct PIN is entered in the dashboard.
3. **The Storage**: Images are processed and pushed to the `/assets` folder of this repository.

---

## 🛠️ How to Create Your Own Dashboard

### Option A: Use This Repository (The Fast Way)
1. **Fork this Repo**: Click the "Fork" button at the top of this page.
2. **Deploy to Streamlit**:
   - Go to [Streamlit Community Cloud](https://share.streamlit.io/).
   - Connect your forked repo.
3. **Configure Secrets**: In your Streamlit App settings, go to **Secrets** and add:
   ```toml
   GITHUB_TOKEN = "your_github_token"
   DASHBOARD_PIN = "your_secret_pin"
   ```
4. **Update app.py**: Change `GITHUB_USER` and `GITHUB_REPO` at the top of `app.py` to your own!

### Option B: Build from Scratch (The Pro Way)
1. **Core Logic**: Use **Streamlit** for the UI and **PyGithub** for API interactions.
2. **Processing**: Use the **Pillow** library to open images, convert color modes (`RGB`/`RGBA`), and save them as `.webp` with `quality=80`.
3. **API Upload**:
   - Use `repo.create_file()` or `repo.update_file()` to push the image bytes to GitHub.
   - Tip: Use `io.BytesIO()` to handle image data in memory without needing local storage.
4. **Multi-threading**: Implement `concurrent.futures.ThreadPoolExecutor` to process multiple images at once for maximum speed.

---

## 💻 Local Setup Guide
1. **Clone & Environment**:
   ```bash
   git clone [your_repo_url]
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Environment Variables**:
   Create a `.env` file or set them in your terminal:
   - `GITHUB_TOKEN`: Your GitHub PAT.
   - `DASHBOARD_PIN`: Your chosen security PIN.
4. **Run**:
   ```bash
   python -m streamlit run app.py
   ```

---

## 🚀 Ready to Sync?
Just enter your PIN, drop your images, and let **ImageSync Pro** handle the rest! ✨
