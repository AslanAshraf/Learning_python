from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import instaloader
import re
import requests
import os

app = FastAPI()

# ✅ CORS Middleware add karein
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" means all domains allowed  0.0.0.0 -> 0.0.0.1  255.255.255.255 
    allow_credentials=True,
    allow_methods=["*"],  # All methods allowed (GET, POST, etc.)
    allow_headers=["*"],  # All headers allowed content-type , stream , mutipart
)

def get_reel_video_url(url: str):
    """Fetch Instagram Reel Video URL""" # pk 3 table 1-1000
    try:
        L = instaloader.Instaloader()
        post_id = url.split("/")[-2]  # Extract post ID
        post = instaloader.Post.from_shortcode(L.context, post_id)
        return post.video_url
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def download_video(video_url: str, post_id: str):
    """Download Reel Video from URL"""
    response = requests.get(video_url)
    if response.status_code == 200:
        file_path = f"downloads/{post_id}.mp4"
        os.makedirs("downloads", exist_ok=True)
        with open(file_path, "wb") as file:
            file.write(response.content)
        # with open(f"hassan/{file_path}","wb").write(response.content):
        #     print("all good")
            
        return file_path
    else:
        raise HTTPException(status_code=400, detail="Failed to download video.")

@app.get("/download/")
def download_reel(url: str):
    """API to Fetch & Download Instagram Reel Video"""
    url = url.strip()
    
    if not re.match(r"https://www.instagram.com/reel/[A-Za-z0-9_-]+/", url):
        raise HTTPException(status_code=400, detail="Invalid Instagram Reel URL.")

    video_url = get_reel_video_url(url)
    post_id = url.split("/")[-2]
    file_path = download_video(video_url, post_id)
    
    return {
        "download_url": video_url,
        "file_path": file_path
    }
