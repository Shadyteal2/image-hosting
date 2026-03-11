import streamlit as st
import os
import concurrent.futures
import time
import io
from PIL import Image
from pathlib import Path
from github import Github, GithubException

# --- Configuration ---
st.set_page_config(
    page_title="ImageSync Pro | Dashboard",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Try to get GitHub Token from secrets (Cloud) or environment (Local)
GITHUB_TOKEN = st.secrets.get("GITHUB_TOKEN", os.getenv("GITHUB_TOKEN"))
OUTPUT_DIR = "assets"
GITHUB_USER = "Shadyteal2"
GITHUB_REPO = "image-hosting"
GITHUB_BRANCH = "main"

# --- Styling ---
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%);
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(106, 17, 203, 0.4);
    }
    .stFileUploader {
        border: 2px dashed #4a4a6a;
        border-radius: 12px;
        padding: 20px;
    }
    .link-container {
        background-color: #2d2d3d;
        padding: 10px;
        border-radius: 6px;
        border-left: 4px solid #6a11cb;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Logic Functions ---

def ensure_dir():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def get_next_filename(original_filename, reserved_names):
    """
    Keep original filename, append serial number, and convert extension to webp.
    Example: photo.jpg -> photo-1.webp
    """
    stem = Path(original_filename).stem
    suffix = ".webp"
    
    # Sanitize stem (remove spaces/special chars if needed, but keeping it simple for now)
    serial = 1
    while True:
        new_name = f"{stem}-{serial}{suffix}"
        if new_name not in reserved_names and not (Path(OUTPUT_DIR) / new_name).exists():
            reserved_names.add(new_name)
            return new_name
        serial += 1

def process_single_image(uploaded_file, dest_name, quality):
    """Process image and return bytes for API upload."""
    try:
        img = Image.open(uploaded_file)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
            
        # Save to buffer
        buf = io.BytesIO()
        img.save(buf, "webp", quality=quality)
        content = buf.getvalue()
        
        # Also save locally for preview/cache
        dest_path = Path(OUTPUT_DIR) / dest_name
        with open(dest_path, "wb") as f:
            f.write(content)
            
        return {"name": dest_name, "success": True, "error": None, "content": content}
    except Exception as e:
        return {"name": dest_name, "success": False, "error": str(e), "content": None}

def sync_to_github_api(results):
    """Upload processed images via GitHub API."""
    if not GITHUB_TOKEN:
        return False, "GITHUB_TOKEN not found. Please add it to Streamlit Secrets or Environment Variables."
    
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_user(GITHUB_USER).get_repo(GITHUB_REPO)
        
        success_list = [r for r in results if r['success']]
        for res in success_list:
            path = f"{OUTPUT_DIR}/{res['name']}"
            message = f"Cloud Upload: {res['name']}"
            
            try:
                # Check if file exists to update
                contents = repo.get_contents(path, ref=GITHUB_BRANCH)
                repo.update_file(path, message, res['content'], contents.sha, branch=GITHUB_BRANCH)
            except GithubException as e:
                if e.status == 404:
                    # Create new file
                    repo.create_file(path, message, res['content'], branch=GITHUB_BRANCH)
                else:
                    raise e
                    
        return True, f"Successfully uploaded {len(success_list)} images via API."
    except Exception as e:
        return False, f"GitHub API Error: {str(e)}"

# --- Main Dashboard ---

def main():
    ensure_dir()
    
    with st.sidebar:
        st.title("⚙️ Settings")
        st.info(f"📍 Output: `/{OUTPUT_DIR}`")
        st.info(f"🔗 Repo: `{GITHUB_USER}/{GITHUB_REPO}`")
        st.info(f"🌿 Branch: `{GITHUB_BRANCH}`")
        if not GITHUB_TOKEN:
            st.warning("⚠️ `GITHUB_TOKEN` is missing! Cloud sync will not work.")
            st.markdown("[How to get a token?](https://github.com/settings/tokens)")
        
        st.divider()
        st.markdown("### 🖼️ Image Settings")
        quality = st.slider("WebP Compression Quality", min_value=10, max_value=100, value=80, step=5, help="Higher = Better quality, lager file size. Recommended: 80")
        
        st.divider()
        st.markdown("### 🛠️ Quick Controls")
        if st.button("Clear Local Assets Cache"):
            for f in Path(OUTPUT_DIR).glob("*.webp"):
                f.unlink()
            st.success("Cleared assets folder!")

    st.title("🚀 ImageSync Pro")
    st.markdown("##### *by ShadyBilla*")
    st.markdown("#### High-Performance Optimization & GitHub Deployment")
    
    # File Uploader
    uploaded_files = st.file_uploader(
        "Drop your images here (PNG, JPG, JPEG, WEBP)", 
        type=['png', 'jpg', 'jpeg', 'webp'], 
        accept_multiple_files=True
    )

    if uploaded_files:
        st.write(f"📂 {len(uploaded_files)} files ready for processing.")
        
        if st.button("⚡ Transform & Deploy"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Step 1: Pre-calculate names (avoids collisions in threads)
            status_text.text("🏷️ Preparing filenames...")
            reserved_names = set()
            tasks = []
            for file in uploaded_files:
                dest_name = get_next_filename(file.name, reserved_names)
                tasks.append((file, dest_name))
            
            # Step 2: Multi-threaded Processing
            status_text.text("⚙️ Optimizing images (High Performance)...")
            results = []
            start_time = time.time()
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                # Submit all tasks with the selected quality
                future_to_file = {executor.submit(process_single_image, f, n, quality): n for f, n in tasks}
                for i, future in enumerate(concurrent.futures.as_completed(future_to_file)):
                    res = future.result()
                    results.append(res)
                    # Update progress (0 to 70% for processing)
                    progress = int(((i + 1) / len(tasks)) * 70)
                    progress_bar.progress(progress)
            
            end_time = time.time()
            processing_time = end_time - start_time
            
            # Step 3: GitHub Sync
            success_count = sum(1 for r in results if r['success'])
            if success_count > 0:
                status_text.text("☁️ Syncing to GitHub API...")
                sync_ok, sync_msg = sync_to_github_api(results)
                progress_bar.progress(100)
                
                if sync_ok:
                    st.success(f"✅ Dashboard Synced! Processed {success_count} images in {processing_time:.2f}s.")
                    
                    # Output Links
                    st.subheader("🔗 Deployment Links")
                    for res in results:
                        if res['success']:
                            raw_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{OUTPUT_DIR}/{res['name']}"
                            st.markdown(f"""
                            <div class="link-container">
                                <b>{res['name']}</b><br>
                                <code style="color: #6a11cb;">{raw_url}</code>
                            </div>
                            """, unsafe_allow_html=True)
                            with st.expander(f"View {res['name']}"):
                                st.image(str(Path(OUTPUT_DIR) / res['name']))
                else:
                    st.error(f"❌ Processing complete but Sync failed: {sync_msg}")
            else:
                st.error("❌ No images were processed successfully.")

    # Instructions at bottom
    with st.expander("ℹ️ Help & One-Line Run Command"):
        st.markdown("""
        **To run this dashboard locally:**
        ```bash
        streamlit run app.py
        ```
        **Prerequisites:**
        - Ensure your SSH key is added to GitHub for seamless `git push`.
        - Install requirements: `pip install streamlit Pillow`
        """)

if __name__ == "__main__":
    main()
