# -*- coding: UTF-8 -*-
import time
import requests
import json

import self as self

if __name__ == '__main__':
    cookiesss = {}
    cookies = input("请输入当前B站cookie，直接粘贴进来就好\n")
    cookies_txt = cookies.strip(';')  # 读取文本内容
    for cookie in cookies_txt.split(';'):
        name, value = cookie.strip().split('=', 1)  # 用=号分割，分割1次
        cookiesss[name] = value  # 为字典cookies添加内容
    cookiesJar = requests.utils.cookiejar_from_dict(cookiesss, cookiejar=None, overwrite=True)
    with open("uid.txt", 'r') as inp:
        with open("follower.csv", 'w', encoding="utf-8")as fi:
            for uid in inp.readlines():
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                }
                uid = str(uid).replace('\n', '')
                response = requests.get("https://api.bilibili.com/x/space/acc/info?mid=" + uid, headers=headers)
                print(response.text)
                d = json.loads(response.text)
                fi.write(d['data']['name'])
                fi.write(',')
                fi.write(str(uid))
                fi.write(',')
                response = requests.get("https://api.bilibili.com/x/relation/stat?vmid=" + uid, headers=headers)
                print(response.text)
                d = json.loads(response.text)
                fi.write(str(d['data']['follower']))
                fi.write(',')
                response = requests.get("https://api.bilibili.com/x/space/upstat?mid=" + uid, headers=headers, cookies=cookiesss)
                print(response.text)
                d = json.loads(response.text)
                fi.write(str(d['data']['archive']['view']))
                fi.write('\n')
            fi.close()
        inp.close()
