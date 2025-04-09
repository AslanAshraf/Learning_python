# dependencies 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import requests
from bs4 import BeautifulSoup
import re
import configparser
import json
import os 
from urllib.parse import urlparse
import csv  




# setup chormedriver
driver= webdriver.Chrome()
config = configparser.ConfigParser()
config.read('config.ini')
# open the webpage
driver.get("https://www.instagram.com/")
# target username 
username =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

password =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username_value = config['settings']['USERNAME']
username.send_keys(username_value)
password.clear()

password_value = config['settings']['PASSWORD']
password.send_keys(password_value)

#target the login button and click it 
button =username =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


driver.get("https://www.instagram.com/jmarkhel/")
print("Wating ten seconds")
time.sleep(10)

# wait up to 10 second for the search button to be clickable on the page
# search_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Search"]'))
# )


# # click the search button once it become clickable

# search_button.click()
# # target the search input field 
# searchbox=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
# searchbox.clear()
# #search for the @handle or key 
keyword="@jmarkhel"
# searchbox.send_keys(keyword)

# #Check if the keyword start with "@"
# if keyword.startswith("@"):


# # remove the @ symbol
keyword=keyword[1:]
# time.sleep(500)
  
# # find the first element eith the secified Xpath that matches the keyword
first_result=driver.find_element(By.XPATH,f'//span[text(), "{keyword}"]')

# #clikc on the found element (assuming it represents the desired search result)
# first_result.click()
# Get the initial page height
initial_height = driver.execute_script("return document.body.scrollHeight")

# create a list to store htmls
soups = []

# Scroll loop

while True:
  
  # Scroll down to the button of the page 
  driver.execute_script("Window.scrollTo,(0,document.body.scrollHeight)")
  
  # Wait for a moment to allow new content to load (adjust as needed)
  time.sleep(5)
  
  # Parse the HTML
  html= driver.page_source
  
  # Create a BeautifulSoup object from the scraped Html 
  soups.append(BeautifulSoup(html,'html.parser'))
  
  # get the current pae height 
  current_height=driver.execute_script("return document.body.scrollHeight")
  
  if current_height == initial_height:
    break # Exit the loop when you can't scroll further 
  
  # update the initial height for the next iteration 
  initial_height = current_height
  
# List to store the post image URLs
post_urls = []

# Loop through soup elements

for soup in soups:
  
  # Find all image element that natch the specific class in the current soup 
  elements = soup.find_all('a',class_='x1i10hfl xjbqb8w x6umtig s1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr xlmh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg xggy1nq x1a2a7pz _a6hd')
  
  # Extract the href attributes and filter URLs that start with "p" or "/reel/"
  post_urls.extend([element['href'] for element in elements if element['href'].startswith(("/p/","/reel/"))])

# Convert the list to a set to remove dublicates
unique_post_urls= list(set(post_urls))

#Create a list to store the json for each post 
json_list = []

#Define the query parameters to add
query_parameters = "__a=1&__d=dis"

#go through all urls
for url in unique_post_urls:
  
  #Error handling
  try:
    
    #Get the current URL of the page 
    current_url=driver.current_url
    
    #Append the query parameters to the current urls
    modified_url="https://www.instagram.com/" + url + "?" + query_parameters
    
    # Get URL
    driver.get(modified_url)
    
    #wait for a momnent to allow new content to load (adjust as needed)
    time.sleep(1)
    
    # find the <pre> tag containning the JSON data
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div[2]/div[1]/article/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]')))
    pre_tag=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div[2]/div[1]/article/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]')
    
    # Extact the json data from the <pre> tag
    json_script=pre_tag.text
    
    #parse the json data
    json_parsed=json.loads(json_parsed)
  #Error Handling
  except (NoSuchElementException,TimeoutException,json.JSONDecodeError) as e:
    print(f"Error processing URL {url}:{e}")
    
# Lists to store URLs and corresponding dates
all_urls = []
all_dates= []

# Iterate through each JSON data in the list
for json_data in json_list:
  
  # Extract the list from the 'items key
  item_list = json_data.get('items',[])
  
  # iterate through each item in the 'items' list
  for item in item_list:
    
    # Extract the date the item was taken 
    date_taken=json_data.get('taken_at')
    
    # Check if 'carousel_media' is present
    
    carsousel_media = item.get('carousel_media',[])
    
    # Extract the date the item was taken
    data_taken= json_data.get('taken_at') 
    
    # iterate through each media in the 'carsousel_media' list
    for media in carsousel_media:
      
      #Extract the image_url from the media
      image_url = media.get('image_versions',{}).get('candidates',[{}])[0].get('url')
      
      # Check if the image_url field is found inside the 'carsousel_media. lit
      
      if image_url:
        
        #add the image url and corresponding date to the lists
        all_urls.append(image_url)
        all_dates.append(date_taken)
        print("carousel image added")
      
      # check if 'video_versions' key exists
      video_versions=item.get("video_versions",[])
      if video_versions:
        video_url= video_versions[0].get('url')
        if video_url:
          all_urls.append(image_url)
          all_dates.append(date_taken)
          print("carousel video added")
    # handle case of unique image indtead of carousel 
    image_url = media.get('image_versions',{}).get('candidates',[{}])[0].get('url')
    if image_url:
    # add the iamge url and corresponding date to the lists
      all_urls.append(image_url)
      all_dates.append(date_taken)
      print("carousel image added")
    
    # check if 'video_versions' key exists
    video_versions=item.get("video_versions",[])
    if video_versions:
      video_url= video_versions[0].get('url')
      if video_url:
        all_urls.append(image_url)
        all_dates.append(date_taken)
        print("carousel video added")
    
print(len(all_urls))


# Create a directory to store downloaded files
download_dir = "Random"
os.makedirs(download_dir,exist_ok=True)


#create subfolders for images and videos
image_dir = os.path.join(download_dir,"images")
video_dir = os.path.join(download_dir,"videos")
os.makedirs(image_dir,exist_ok=True)
os.makedirs(video_dir,exist_ok=True)

# initialize counters for images and video
image_counter=1
video_counter=1

# Iterate through URLs in the all_urls list and download media 
for index,url in enumerate(all_urls,0):
  response = requests.get(url,stream=True)
  
  # Extract file extension from the url
  url_path = urlparse(url).path
  file_extension=os.path.splitext(url_path)[1]
  
  # determint the file name based on the url
  if file_extension.lower() in {'.jpg','.jpeg','.png','.gif'}:
    file_name= f"{all_dates[index]}-vid-{image_counter}.png"
    destination_folder=image_dir
    image_counter+=1
  elif file_extension.lower() in {'.mp4','.avi','.mkv','.mov'}:
    file_name= f"{all_dates[index]}-vid-{video_counter}.mp4"
    destination_folder=video_dir
    video_counter+=1
  else: 
    #default to the main doenload directory for other file types
    file_name=f"{all_dates[index]}{file_extension}"
    destination_folder=download_dir
  
  # save file to the appropriate folder
  file_path = os.path.join(destination_folder,file_name)
  
  # write the content of the response to the file
  with open (file_path, 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
      if chunk:
        file.write(chunk)
  print(f"downloaded: {file_path}")

# print a message indicate the number of downloaded files and download directory
print(f'Downloaded {len(all_urls)}')
  

           
        
  