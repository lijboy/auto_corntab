import os
import requests

def visit_url():
    url = os.environ.get('TARGET_URL')
    if not url:
        print("Error: TARGET_URL environment variable is not set.")
        return
    
    try:
        response = requests.get(url)
        print(f"Visited {url}")
        print(f"Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while visiting {url}: {str(e)}")

if __name__ == "__main__":
    visit_url()
