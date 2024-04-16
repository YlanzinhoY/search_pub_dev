import requests
from scrapy.http import HtmlResponse

package = input("Typing package what do you need: ")
print("\n")
URL = f"https://pub.dev/packages/{package}/install"

req = requests.get(url=URL)

scr = HtmlResponse(url=URL, body=req.content, encoding='utf-8')

if req.status_code == 404:
    print("not found")
if req.status_code != 200:
    print("error")
    
title = scr.xpath("/html/body/main/div[1]/div[2]/div/div/div/h1/text()").get()
separete_name_in_version = title.split(" ")

print(f"Install {package} with two ways! \n")
install_mode_1 = print(f"flutter pub add {package}")
print("\n")
install_mode_2 = print(f"dependencies: \n {package}: ^{separete_name_in_version[1]}")







