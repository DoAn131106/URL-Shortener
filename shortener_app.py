from flask import Flask, redirect
import random
import string

url_database = {}

def create_random(length = 6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range)

def get_official_name(original_url, custom_code = None):
    if (custom_code) :
        short_url = custom_code
        counter = 1
        while short_url in url_database:
            short_url = f"{custom_code}_{counter}"
            counter += 1
    else:
        short_url = create_random()
        while short_url in url_database:
            short_url = create_random() #if there exist the same name, create a new one
        
    url_database[short_url] = original_url
    return f"http://shortcut/{short_url}"

def retrieve(short_url):
    while short_url in url_database:
        return url_database.get("short_url")
    else:
        return "There is no long url for this short url"


# while True:
#     action = input("Choose action: shorten/retrieve: ").strip().lower()
#     if action == "shorten":
#         original = input("Provide the original URL: ").strip()
#         custom = input("Provide custom code if needed: ").strip()
#         custom = custom if custom else None
#         print(get_official_name(original, custom))
#     elif action == "retrieve":
#         shortened = input("Provide the shortened URL: ").strip()
#         print(retrieve(shortened))
#     else:
#         break





    

        


