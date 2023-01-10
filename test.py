# import requests
# url = "http://www.naver.com"   
# response = requests.get(url)
# text = response.text
# var content = text.replace(/<(\/table|table)([^>]*)>/gi,"");

# print(response.text)

import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = input()
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}
html = session.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

soup_p = soup.p

for script in soup_p(["script", "style"]):
    script.extract()

text = soup_p.get_text()

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)