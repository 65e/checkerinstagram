import requests
import time as mm
import sys as n
import threading
import time
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray
def slow(M): 
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 200)
rq = requests.Session()
Cookie = ''
print('''
••••••••••••••••••••••
Rights : الحقوق
𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
CHANNEL : t.me/JailTweaks
GROUP : t.me/sol4o
Bot : t.me/jailtweaks_bot  
•••••••••••••••••••••••
''')


time.sleep(1)
slow("💎 الاداه مجانيه بالكامل 💎 ")
print(" ")

time.sleep(1)
slow("تشيكر انستقرام اصدار 1.01 🎈")
time.sleep(1)
print(" ")
time.sleep(1)
slow("CHECKER INSTAGRAM VERSION 1.01 🎈")
time.sleep(1)

time.sleep(1)
print('')
dd = 'user.txt'
print('')
slow("[!] سيتم ارسال المتاحات في التيليقرام")
print(" ")

print(" ")
time.sleep(1)

ID = input("[؟] ادخل ايدي حسابك في التيليقرام -> : ")
tok = ('1316607340:AAEVQUBpR0OnPRs6THQFYrCoQBlBfvNsuxU')








EditUrl = 'https://i.instagram.com/api/v1/account/edit_profile/'
hea1 = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '285',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=27E7600C-E0C8-4D1C-A1A7-BA33E536A553; mid=XtNB0wALAAHfPyYMvVdKT_5aM4ao; datr=kkraXnOwVrFQ6dUDqFgyR9kW; shbid=9687; shbts=1592904567.8375468; csrftoken=Ov3Ki403DjijeTV9txO6BcIgyiBz4Dgc; rur=VLL',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'x-csrftoken': 'Ov3Ki403DjijeTV9txO6BcIgyiBz4Dgc',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '9fc13b1a222e',
    'x-requested-with': 'XMLHttpRequest'
}
hea3 = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '373',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=27E7600C-E0C8-4D1C-A1A7-BA33E536A553; mid=XtNB0wALAAHfPyYMvVdKT_5aM4ao; datr=kkraXnOwVrFQ6dUDqFgyR9kW; shbid=9687; shbts=1592904567.8375468; csrftoken=Ov3Ki403DjijeTV9txO6BcIgyiBz4Dgc; rur=VLL',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'x-csrftoken': 'Ov3Ki403DjijeTV9txO6BcIgyiBz4Dgc',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '9fc13b1a222e',
    'x-requested-with': 'XMLHttpRequest'
}
head = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'ig_did=27E7600C-E0C8-4D1C-A1A7-BA33E536A553; mid=XtNB0wALAAHfPyYMvVdKT_5aM4ao; datr=kkraXnOwVrFQ6dUDqFgyR9kW; shbid=9687; shbts=1592904567.8375468; csrftoken=Ov3Ki403DjijeTV9txO6BcIgyiBz4Dgc; rur=VLL',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}
head10 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'ig_did=29F366FF-7905-4DAC-86F9-67F7B2F871E0; mid=X8-16wALAAH14jTv0QCkQDnl2jb-; ig_nrcb=1; shbid=841; shbts=1608634144.3552637; rur=RVA; csrftoken=JYRWXSbiXonrfY0r76J5UmKzncx6UFQB; ds_user_id=44356438463; sessionid=44356438463%3AG8jzUuYsuygyA0%3A18; urlgen="{\"178.80.41.77\": 35819\054 \"185.209.179.219\": 396356}:1ksMEk:o2kiGIlKrjksXkdlL_HnBWd1K4k',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
ffile = 'user.txt'
usernamelist = open(ffile, 'r')
while True:
    checklist = usernamelist.readline().split('\n')[0]
    instaurl = f'https://www.instagram.com/{checklist}/'
    rq = requests.get(instaurl, headers=head)
    if rq.status_code == 404:
        req = requests.session()
        instalog = 'https://www.instagram.com/accounts/login/ajax/'
        dat = {
            'username': checklist,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1592912810:ASRQAAWmL/OKiq54WTH/H4ZNuVwjbVBWXL0EgGusm/4DDJwr3bmpOSnAKhyHDk10E1KajZr6VkuJh+WGB/mlp4ap9iZNEHpmIWN1SOYzAiH7WGuZ+YJEjFlaz+/WGsowSvwx9tDYlzG3Ks+/+oxv7MPg',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        logdata = req.post(instalog, data=dat, headers=hea1).text
        if ('"user": false') in logdata:
            s = print(f'[✔︎] اليوزر متوفر -> : {checklist}')
            tele = (f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=𝙷𝚄𝙽𝚃𝙴𝚁 𝙱𝙾𝚃 ☯︎︎␈\n♡︎––––––––––––––——♡︎\n   𝙸 𝙵𝚄𝙲𝙺𝙴𝙳 𝙽𝙴𝚆 𝚄𝚂𝙴𝚁 ☠︎︎ \n♡︎––––––––––––––——♡︎\n𖡃 𝚄𝚂𝙴𝚁 : {checklist}\n𖡃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @jailtweaks\n𖡃 𝙶𝚁𝙾𝚄𝙿 : @sol4o\n𖡃 𝙴𝙽𝙹𝙾𝚈\n♡︎––––––––––––––——♡︎')
            r = requests.post(tele)
            with open('user.txt', 'a') as x:
                x.write(checklist + '\n')
        elif ('"user": true') in logdata:
            print(f'This Username Is Banned >> {checklist}')
    elif rq.status_code == 200:
        print(f'[⚠︎︎] اليوزر غير متوفر -> : {checklist}')
        if (checklist == ""):
        	
        	
