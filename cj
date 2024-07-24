import requests

urls = [
    "https://video.lijboy.top/api.php/timming/index.html?enforce=1&name=heimuer",
    "https://video.lijboy.top/api.php/timming/index.html?enforce=1&name=ff",
    "https://video.lijboy.top/api.php/timming/index.html?enforce=1&name=kuaikan",
    "https://video.lijboy.top/api.php/timming/index.html?enforce=1&name=lz"
]

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully accessed {url}")
    else:
        print(f"Failed to access {url}, status code: {response.status_code}")
