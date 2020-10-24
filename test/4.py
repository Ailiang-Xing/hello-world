import requests
import json

def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname'] + '：\n\n')
            file.write(each['content'] + '\n')
            file.write("---------------------------------------\n")

def get_comments(url):
    # 给它传个 referer 以免服务器疑神疑鬼的@_@
    # 当然，你这有时间的话将headers头部填写完整，那样妥妥会更好一些……
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'referer': 'http://music.163.com/'
        }

    params = "EH8/xHwDk8YOb0hPgzAt8C6X8tVqlC5hNIAifhM6dHnRnrQrYDEE/PL+E8mmUMZQTlGYBQNyH7TtGxUV0Ut40aXdR/+h6euX9cd2GJ5nk2Ne0VKagpDtEYB/h7pf3QWqGjOERBVfn22OuT3QHgIZ8guzuiPVjsxq9OjUq4sOp9gQdPNfgsON648Zn/j9LO9YObQc2JRuGK9xiI0R7Hv93WY/M/hjKlG2+Xt02Qe8aV4W5BKyUYzVhZGatDM32hv8BvBQ/DMVMC3lnRRwYODocg=="
    encSecKey = "97dddb6366dd97ad2247efca1d9bedc49ea07d7efc307cae8a9ec4537b28e62e153392d87e2294fea4ac45997be7c7c64b286ca5e6b92bb5ceeb31caeef13ed0a1a248c9ac3a38cea13a16cef35032e25d1a319696c7e45b70e579a55140a8602ca07e38441a2435853fecbf8e493889ea893a076dfb0bd78410f3e8e9bf79aa"
    data = {
        "params": params,
        "encSecKey": encSecKey
        }

    target_url = "https://music.163.com/api/comment/resource/comments/get?csrf_token="

    res = requests.post(target_url, headers=headers, data=data)

    return res

def main():
    url = input("请输入链接地址：")
    res = get_comments(url)
    get_hot_comments(res)

if __name__ == "__main__":
    main()