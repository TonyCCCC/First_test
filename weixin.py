import requests
from http import cookiejar

cookies = dict(_xxhm_='%7B%22address%22%3A%22%22%2C%22awardPoints%22%3A0%2C%22birthday%22%3A847382400000%2C%22createTime'
                     '%22%3A1534422427000%2C%22headerImg%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2FibPMSbq88dE5'
                     'qibq6jiasaMu8icrmlnBRhYt6ISK1KcbSnQjbFKUCZaFkV7jENa81lvyo2icUy8gEzDxwULLcib5ZVpnp6MSez4Qhq%2F132'
                     '%22%2C%22id%22%3A2178241%2C%22idCardNo%22%3A%2244011119961108001X%22%2C%22isRegisterHistory%22%3'
                     'A0%2C%22latitude%22%3A0.0%2C%22longitude%22%3A0.0%2C%22mobile%22%3A%2215603057947%22%2C%22modify'
                     'Time%22%3A1534430012000%2C%22name%22%3A%22%E5%B2%91%E6%99%BA%E9%9F%AC%22%2C%22nickName%22%3A%22'
                     '%F0%9F%9A%B6%22%2C%22openId%22%3A%22og46NxGwa4xGeI4GbaRTHfEMNRGU%22%2C%22regionCode%22%3A%224401'
                     '12%22%2C%22registerTime%22%3A1534430012000%2C%22sex%22%3A1%2C%22source%22%3A1%2C%22uFrom%22%3A%22'
                     'wx%22%2C%22unionid%22%3A%22o8NLkwYqYx6MvHii6bc62INPGLw8%22%2C%22wxSubscribed%22%3A1%2C%22yn%22%3'
                     'A1%7D',
              _xzkj_='532fa0abc9b534dd276f0f67d9be055b_fa864a74120100b590a1a68f86fcd6fe',
              CNZZDATA1261985103='768456040-1534483126-https%253A%252F%252Fopen.weixin.qq.com%252F%7C1534483126',
              UM_distinctid='1654668394980-09103f54f-6a3f0723-100200-1654668394b5c0')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95'
                  ' Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser'
                  '/9.0.2524.400',
    'Referer': 'https://wx.healthych.com/index.html',
    'tk': '532fa0abc9b534dd276f0f67d9be055b_b4812e583a6bf8c301214bf359746d5d'
}

url = 'https://wx.healthych.com//order/subscribe/findSubscribeAmountByDays.do?depaCode=4403030152&vaccCode=8803&vaccIndex=1&days=20181125,20181126,20181127,20181128,20181129,20181130'

response = requests.get(url, headers=headers, cookies=cookies, verify=False).text

print(response)



