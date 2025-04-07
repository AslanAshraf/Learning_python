from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import instaloader
import re
import requests
import os
from io import BytesIO
from fastapi.responses import StreamingResponse

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://localhost:8101","http://35.154.81.229/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_reel_data(url: str):
    """Fetch Instagram Reel data including video URL and thumbnail"""
    try:
        L = instaloader.Instaloader()
        post_id = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, post_id)
        
        # Get thumbnail - we'll use the post's display URL which usually works better
        thumbnail_url = f"https://www.instagram.com/p/{post.shortcode}/media/?size=m"
        
        return {
            "video_url": post.video_url,
            "thumbnail_url": thumbnail_url,
            "shortcode": post.shortcode
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/download/")
async def download_reel(url: str):
    """API to Fetch Instagram Reel Data"""
    url = url.strip()
    
    if not re.match(r"https://www.instagram.com/reel/[A-Za-z0-9_-]+/", url):
        raise HTTPException(status_code=400, detail="Invalid Instagram Reel URL.")

    try:
        reel_data = get_reel_data(url)
        return {
            "download_url": reel_data["video_url"],
            "thumbnail_url": reel_data["thumbnail_url"],
            "shortcode": reel_data["shortcode"]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/thumbnail/")
async def get_thumbnail(url: str):
    """Proxy endpoint to serve thumbnails"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, stream=True)
        
        if response.status_code == 200:
            return StreamingResponse(BytesIO(response.content), media_type="image/jpeg")
        else:
            raise HTTPException(status_code=400, detail="Failed to fetch thumbnail")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
    
    
# from fastapi import FastAPI, HTTPException
# from starlette.middleware.trustedhost import TrustedHostMiddleware
# from fastapi.middleware.cors import CORSMiddleware
# import instaloader
# import re
# import requests
# import os
# from io import BytesIO
# from fastapi.responses import StreamingResponse

# app = FastAPI()

# app.add_middleware(
#     TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1","your-frontend-domain.com", "*.your-frontend-domain.com"]
# )
# # CORS Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://your-frontend-domain.com"],  # Only your frontend
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )

# @app.get("/secure-endpoint")
# def secure_data():
#     return {"message": "This is a secure API endpoint!"}


# def get_reel_data(url: str):
#     """Fetch Instagram Reel data including video URL and thumbnail"""
#     try:
#         L = instaloader.Instaloader()
#         post_id = url.split("/")[-2]
#         post = instaloader.Post.from_shortcode(L.context, post_id)
        
#         # Get thumbnail - we'll use the post's display URL which usually works better
#         thumbnail_url = f"https://www.instagram.com/p/{post.shortcode}/media/?size=m"
        
#         return {
#             "video_url": post.video_url,
#             "thumbnail_url": thumbnail_url,
#             "shortcode": post.shortcode
#         }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @app.get("/download/")
# async def download_reel(url: str):
#     """API to Fetch Instagram Reel Data"""
#     url = url.strip()
    
#     if not re.match(r"https://www.instagram.com/reel/[A-Za-z0-9_-]+/", url):
#         raise HTTPException(status_code=400, detail="Invalid Instagram Reel URL.")

#     try:
#         reel_data = get_reel_data(url)
#         return {
#             "download_url": reel_data["video_url"],
#             "thumbnail_url": reel_data["thumbnail_url"],
#             "shortcode": reel_data["shortcode"]
#         }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @app.get("/thumbnail/")
# async def get_thumbnail(url: str):
#     """Proxy endpoint to serve thumbnails"""
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#         }
#         response = requests.get(url, headers=headers, stream=True)
        
#         if response.status_code == 200:
#             return StreamingResponse(BytesIO(response.content), media_type="image/jpeg")
#         else:
#             raise HTTPException(status_code=400, detail="Failed to fetch thumbnail")
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))