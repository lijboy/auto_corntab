import os
import requests
import logging
from datetime import datetime

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def visit_url():
    url = os.environ.get('TARGET_URL')
    if not url:
        logging.error("Error: TARGET_URL environment variable is not set.")
        return
    
    try:
        logging.info(f"Attempting to visit {url}")
        response = requests.get(url, timeout=30)  # 设置30秒超时
        logging.info(f"Visited {url}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response content length: {len(response.content)} bytes")
        
        # 保存响应到文件
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"response_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Status Code: {response.status_code}\n")
            f.write(f"Headers: {dict(response.headers)}\n")
            f.write(f"Content: {response.text[:500]}...")  # 只保存前500个字符
        logging.info(f"Response saved to {filename}")
        
    except requests.RequestException as e:
        logging.error(f"An error occurred while visiting {url}: {str(e)}")

if __name__ == "__main__":
    visit_url()
