# from web_crawl import crawler
import crawler
import json

url = "https://www.tdi.texas.gov/tips/what-to-do-after-a-wreck.html"
# url= "https://www.tamucc.edu/sail"

start_anchor="/"
urls=crawler.crawl(url, start_anchor)
# print("length is ", len(urls))
print(len(urls), urls)

# Function to save data to JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
        

save_to_json(urls,'data.json')