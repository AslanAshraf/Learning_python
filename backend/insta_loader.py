# # dependencies 
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# import time
# import requests
# from bs4 import BeautifulSoup
# import re
# import configparser
# import json
# import os 
# from urllib.parse import urlparse
# import csv  



# class InstaLoader:
  
#   def __init__(self):
#     self.driver= webdriver.Chrome()


#   def goto_reel(self,url):
#     self.driver.get(url)
#     time.sleep(15)
#     try:
#           script_tag = self.driver.find_element(By.XPATH, '//script[contains(text(), "window._sharedData")]')
#           json_text = script_tag.get_attribute('innerHTML')
#           json_data = json.loads(json_text.split(' = ', 1)[1].split(';</script>')[0])

#           # Extract the video URL (for a reel or video post)
#           media_data = json_data['entry_data']['PostPage'][0]['graphql']['graphql']['shortcode_media']
#           video_url = media_data.get('video_url', None)

#           return video_url
        
#     except Exception:
#       return None
  
# if __name__ == "__main__":
#   print(InstaLoader().goto_reel("https://www.instagram.com/jmarkhel/reel/DIEn6wJpxQo"))


# import os
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Setup Chrome with automatic driver
# def setup_driver():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
#     return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# def download_reel(reel_url, download_folder="instagram_reels"):
#     driver = None
#     try:
#         driver = setup_driver()
#         print(f"\nStarting download for: {reel_url}")
        
#         # Open the reel URL
#         driver.get(reel_url)
#         time.sleep(3)  # Wait for page to load
        
#         # Find video element with wait
#         try:
#             video = WebDriverWait(driver, 15).until(
#                 EC.presence_of_element_located((By.TAG_NAME, "video"))
#             )
#             video_url = video.get_attribute("src")
#             if video_url.startswith("blob:"):
#               video_url = video_url.replace("blob:", "")
            
#             if not video_url:
#                 # Alternative method if direct src not found
#                 video_url = driver.execute_script("""
#                     return document.querySelector('meta[property="og:video"]').content;
#                 """)
                
#         except Exception as e:
#             print(f"Error finding video: {str(e)}")
#             return False

#         if not video_url:
#             print("Video URL not found!")
#             return False
            
#         print(f"Found video URL: {video_url[:50]}...")  # Show partial URL
        
#         # Prepare download
#         os.makedirs(download_folder, exist_ok=True)
#         reel_id = reel_url.split("/reel/")[-1].split("/")[0]
#         filename = os.path.join(download_folder, f"reel_{reel_id}.mp4")
        
#         # Download with progress
#         print("Downloading...")
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#             'Referer': 'https://www.instagram.com/'
#         }
        
#         response = requests.get(video_url, headers=headers, stream=True, timeout=30)
#         response.raise_for_status()
        
#         with open(filename, 'wb') as f:
#             for chunk in response.iter_content(chunk_size=8192):
#                 if chunk:
#                     f.write(chunk)
        
#         print(f"Successfully saved to: {filename}")
#         return True
        
#     except Exception as e:
#         print(f"Download failed: {str(e)}")
#         return False
#     finally:
#         if driver:
#             driver.quit()

# # Example usage
# if __name__ == "__main__":
#     # Replace with your reel URL
#     REEL_URL = "https://www.instagram.com/jmarkhel/reel/CclGdQCKyIt/?hl=en"
    
#     if download_reel(REEL_URL):
#         print("\n✅ Download completed successfully!")
#     else:
#         print("\n❌ Download failed. Please check the URL and try again.")

import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def extract_video_url(driver):
    """Extract video URL from page using multiple methods"""
    try:
        # Method 1: Direct video element
        video = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )
        video_url = video.get_attribute("src")
        
        # Handle blob URLs
        if video_url and video_url.startswith("blob:"):
            # Extract from page source if blob URL
            page_source = driver.page_source
            video_url = re.search(r'"video_url":"(https://[^"]+)"', page_source)
            if video_url:
                video_url = video_url.group(1).replace('\\u0026', '&')
        
        # Method 2: Meta tag fallback
        if not video_url:
            video_url = driver.execute_script("""
                return document.querySelector('meta[property="og:video"]')?.content;
            """)
        
        # Method 3: Page source fallback
        if not video_url:
            page_source = driver.page_source
            video_url = re.search(r'"video_url":"(https://[^"]+)"', page_source)
            if video_url:
                video_url = video_url.group(1).replace('\\u0026', '&')
        
        return video_url
        
    except Exception as e:
        print(f"Error extracting URL: {str(e)}")
        return None

def download_reel(reel_url, download_folder="instagram_reels"):
    driver = None
    try:
        driver = setup_driver()
        print(f"\nStarting download for: {reel_url}")
        
        # Open the reel URL
        driver.get(reel_url)
        time.sleep(5)  # Increased wait time
        
        # Get video URL
        video_url = extract_video_url(driver)
        if not video_url:
            print("Video URL not found!")
            return False
            
        print(f"Found video URL: {video_url[:50]}...")  # Show partial URL
        
        # Prepare download
        os.makedirs(download_folder, exist_ok=True)
        reel_id = reel_url.split("/reel/")[-1].split("/")[0]
        filename = os.path.join(download_folder, f"reel_{reel_id}.mp4")
        
        # Download with progress
        print("Downloading...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://www.instagram.com/'
        }
        
        response = requests.get(video_url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f"Successfully saved to: {filename}")
        return True
        
    except Exception as e:
        print(f"Download failed: {str(e)}")
        return False
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    # Replace with your reel URL
    REEL_URL = "https://www.instagram.com/jmarkhel/reel/DIEn6wJpxQo/?hl=en"
    
    if download_reel(REEL_URL):
        print("\n✅ Download completed successfully!")
    else:
        print("\n❌ Download failed. Please check the URL and try again.")
        
        
        
