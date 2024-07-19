import requests
import csv
import os
from datetime import datetime

# 从环境变量中读取URL列表
urls = os.getenv("URLS").split(",")

# 打开CSV文件，准备写入
with open("url_check_results.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    
    # 写入表头（如果文件为空）
    if file.tell() == 0:
        writer.writerow(["URL", "Status Code", "Timestamp"])
    
    # 逐个检查URL
    for url in urls:
        try:
            response = requests.get(url)
            status_code = response.status_code
        except requests.RequestException as e:
            status_code = f"Error: {e}"
        
        # 获取当前时间戳
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 写入结果到CSV文件
        writer.writerow([url, status_code, timestamp])

print("URL检查完成，结果已写入url_check_results.csv")
