import requests

dict = {"name":"saeed","id":"95102157"}

#post
url = 'https://api.jsonbin.io/b'
headers = {'Content-Type': 'application/json','secret-key':'$2b$10$zDmWLzYH1A0baKGyc3iVu.MPjLb5mOluA9Yior19RqV8Zx7TAsagS'}

post = requests.post(url, json=dict, headers=headers)

print("************** post ******************")
print("status : " , post.status_code)
print(post.text)

#get
url_get = 'https://api.jsonbin.io/b/' + post.json()['id']
header = {'secret-key':'$2b$10$zDmWLzYH1A0baKGyc3iVu.MPjLb5mOluA9Yior19RqV8Zx7TAsagS'}

get = requests.get(url_get, headers=header)
print("*************** get *********************")
print(get.text)