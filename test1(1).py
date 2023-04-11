import requests
import json
from concurrent.futures import ThreadPoolExecutor

# 定义获取email结果
def fetch_comments(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [item['email'] for item in data]
    else:
        return []

# 并发执行
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_comments, i) for i in range(1, 101)]
        emaillist = []
        for future in futures:
            result = future.result()
            if result:
                emaillist += result

print(emaillist)