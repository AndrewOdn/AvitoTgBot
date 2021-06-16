import json
from pprint import pprint
import sqlite3
import fake_useragent
import requests
from bs4 import BeautifulSoup
import TgLib
from datetime import datetime
def avito_db():
    con = sqlite3.connect('avito' + '.db')
    c = con.cursor()
    c.execute("""create TABLE if not exists """ + 'phone' + """ (
            url STRING UNIQUE,
            name STRING,
            price STRING ,
            time STRING,
            status STRING
            );
            """)
    con.commit()
    c.execute("""create TABLE if not exists """ + 'phone_otchet' + """ (
                url STRING UNIQUE,
                post_time STRING,
                name_id STRING,
                status STRING,
                coment STRING,
                start_time STRING,
                end_time STRING
                );
                """)
    con.commit()
def avito(url,bot):
    print(datetime.now())
    user = fake_useragent.UserAgent().random
    header = {
        'user-agent': user,
        'Host' : 'www.avito.ru',
        'Upgrade-Insecure-Requests' : '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same - origin',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_gcl_au=1.1.1368944075.1623751577; _ga=GA1.2.1193651873.1623751578; _gid=GA1.2.1125295510.1623751578; _dc_gtm_UA-2546784-1=1; _fbp=fb.1.1623751577847.984907657; u=2or6sjpm.1g94wj.1w5s4apt7py00; v=1623751578; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9ad42d01242e34c7968e2978c700f15b6831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013aba0ac8037e2b74f971e7cb57bbcb8e0f03c77801b122405c8b1472fe2f9ba6b91d6703cbe432bc2a71e7cb57bbcb8e0f03c77801b122405c2da10fb74cac1eab2da10fb74cac1eab2ebf3cb6fd35a0ac20f3d16ad0b1c546fa967f4e8cd565314e1848a6933553223306f335f11a73c063b0ad70f46873f3047fd43ccbbdbaea728dbf2cb7569f5d3c8025aaa90425cd38f0f5e6e0d2832e80e512d93b0823b0ca257f81b1a1ea9146b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac15e402c38704f62542641f56039504fd2da10fb74cac1eab2da10fb74cac1eabbe1b8fec550f290a09360354b9a5173a3778cee096b7b985bf37df0d1894b088; ft="oWeRZhi1qd3Ji5wBtJ1AiWLD2nRJO4Nxj6caVeVEDOt90NGFKhsF/789XG+P0YgsDyHdfm70OOT9VApxmrlG3ZFGRzYNVzEY4XDrYS2XY2bVF+USJujbuS8wP3urdkbia8ncBcTTJEHxDkDjZX3x+ZY9kWvcL8fyGuvrW9prHMXgoq/cbC2dzMEb/ML5CHZV"; buyer_location_id=637640; luri=moskva; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAwXBUQqAIAwA0Lvsu4%2BlQ4a3qVkrRogNEpLu3nsD0n6dDZMWFmVFRRJxr1QhD3ggw1Jqe%2Ff5Xg8xp25kVp2MhNWtI0ywQZ5TiBwZMXzfD%2B%2BghNlUAAAA; so=1623751602; dfp_group=68; abp=0; _ym_uid=1623751604361883833; _ym_d=1623751604; no-ssr=1; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBYnlzVGk3VTVKRW8wVkZQNXBSVll0ZVlpM0lxVUJ1Q2JQVUtjS0FnSGJvRVNnaDBZQTRSMWd2SjhQWXNYNjZyZVZ2QTR1ajFNRGY0SWIvRmNTbUs2OUJodENUcFBHUTlrakgzWFBoMGV1L1NwL3Q4d3A4T1B3dEx0TW5CVitKeko1UXVCa0g1bEF1YW1LTE5Pd2M4OEhtNFkyR3JFYlQvaEFWUjFLaHRHUHU5TzRBSTFwMTNtN3JCU3loZUtRRmRPcmluSWxJcmVHenYxelVKUHZwR3ordlE4Sm1CUEdGWkJNTmVHLzlyRUhDM1V3aHY4b2pxcUhaMFh3M2VJa2s2dUNERzgxM2Q1K3NTdVhmZGEzbFJUWFZ3eXF6WnRrODNDeEtGSmlUdUc3RnIiLCJpYXQiOjE2MjM3NTE2MDMsImV4cCI6MTYyNDk2MTIwM30.ZJXZyzHPBV_uPa-zptfMJjGpuXe6y1f2WkZ6x4Mv-MI; _ym_isad=2; _ym_visorc=b; isWideScreen=false; ST-TEST=TEST; __gads=ID=b941ed624e2a318c:T=1623751604:S=ALNI_Ma8S-B1y5RTMQ3DM8mkeZk7bOlBlw; isCriteoSetNew=true',
        'Referer': 'https://www.avito.ru/kazan/telefony/mobile-ASgBAgICAUSwwQ2I_Dc?cd=1&s=104',
    }
    r = requests.Session()
    r = requests.get(url, headers = header)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find('div', {'class':'js-initial'})
    s = str(data)
    s = s[str.find(s, '="{')+2:str.rfind(s,'"')]
    qqwe = s.split("&quot;")
    new = '"'.join(qqwe)
    data = json.loads(new)
    st = str(data['catalog']['items'])
    st[:100]
    for i in range(1, len(data['catalog']['items'])):
        try:
            Avito_url = 'https://www.avito.ru'+str(data['catalog']['items'][i]['urlPath'])
            Avito_name = data['catalog']['items'][i]['title']
            Avito_description = data['catalog']['items'][i]['description']
            Avito_price = data['catalog']['items'][i]['priceDetailed']['value']
            Avito_time = data['catalog']['items'][i]['iva']['DateInfoStep'][0]['payload']['absolute']
            gggg = ['blackview','Blackview','oneplus','huawei','Huawei','Xiaomi', 'xiaomi', 'Sony', 'sony', 'Moto', 'Oneplus', 'Poco X3', 'OnePlus', 'Honor', 'honor', 'vertu', 'Vertu', 'Хонор', 'Google Pixel', 'HTC', 'htc', 'Htc', 'Nokia', 'nokia', 'Realme', 'Google pixel', 'Поко Х3', 'redmi', 'Zebra', 'zebra', 'Redmi', 'Nokia', 'nokia', 'Alcatel', 'alcatel', 'Meizu', 'meizu', 'Lenovo', 'lenovo', 'Motorola', 'motorola']
            a = 1
            for h in range(0, len(gggg)):
                if str.find(Avito_name,gggg[h]) != - 1:
                    print(Avito_url)
                    a = 0
                if str.find(Avito_description, gggg[h]) != - 1:
                    a = 0
                    print(Avito_url)
            if int(Avito_price) <= 15000:
                a = 0
        except:
            a = 0
        if a == 1:
            con = sqlite3.connect('avito' + '.db')
            c = con.cursor()
            c.execute("SELECT * FROM " + 'phone' + " WHERE url = " +"'"+ str(Avito_url) +"'")
            con.commit()
            g = list(c)
            if len(g) == 0:
                c.execute("INSERT INTO " + 'phone' + " VALUES (?,?,?,?,?)",
                          (str(Avito_url), str(Avito_name), str(Avito_price), str(Avito_time), 'empty'))
                con.commit()
                TgLib.spam_to_all(bot, '\n'+
                                    str(Avito_url)+'\n'+
                                    str(Avito_name) + '\n'+
                                    str(Avito_price) + '\n'+
                                    str(Avito_time) + '\n', 0)
def avito_print(id, bot):
    con = sqlite3.connect('avito' + '.db')
    c = con.cursor()
    c.execute("SELECT * FROM " + 'phone' + " WHERE status = 'empty'")
    con.commit()
    g = list(c)
    if len(g) > 5:
        b = len(g)
        a = 5
    else:
        b = 0
        a = len(g)
    for i in range(0, a):
        if a > b:
            s = g[a-i-1]
        else:
            s = g[b - i - 1]
        bot.send_message(id, '\n'+
                                    str(s[0])+'\n'+
                                    str(s[1]) + '\n'+
                                    str(s[2]) + '\n'+
                                    str(s[3]) + '\n')
def avito_check(url, id, bot):
    con = sqlite3.connect('avito' + '.db')
    c = con.cursor()
    c.execute("SELECT * FROM " + 'phone' + " WHERE status = " + "'" + str(id) + "'")
    con.commit()
    g1 = list(c)
    if len(g1) != 0:
        return 3
    c.execute("SELECT * FROM " + 'phone' + " WHERE url = " + "'" + str(url) + "'")
    con.commit()
    g = list(c)
    if len(g) == 0:
        return 0
    else:
        s = g[0]
        if str(s[4]) == 'empty':
            c.execute("INSERT or REPLACE INTO " + 'phone' + " VALUES(?,?,?,?,?)", (str(s[0]), str(s[1]), str(s[2]), str(s[3]), id))
            con.commit()
            c.execute("INSERT INTO " + 'phone_otchet' + " VALUES(?,?,?,?,?,?,?)",
                      (str(s[0]), str(s[3]), id, 'IN_PROGRESS', 'empty', str(datetime.now()), 'empty'))
            con.commit()
            return 1
        else:
            return 2
def avito_done(id, text, bot):
    con = sqlite3.connect('avito' + '.db')
    c = con.cursor()
    c.execute("SELECT * FROM " + 'phone' + " WHERE status = " + "'" + str(id) + "'")
    con.commit()
    g1 = list(c)
    if len(g1) == 0:
        return 1
    else:
        s1 = g1[0]
        c.execute("SELECT * FROM " + 'phone_otchet' + " WHERE url = " + "'" + str(s1[0]) + "'")
        con.commit()
        g = list(c)
        s = g[0]
        c.execute("INSERT or REPLACE INTO " + 'phone' + " VALUES(?,?,?,?,?)",
                  (str(s1[0]), str(s1[1]), str(s1[2]), str(s1[3]), 'DONE'))
        con.commit()
        c.execute("INSERT or REPLACE INTO " + 'phone_otchet' + " VALUES(?,?,?,?,?,?,?)",
                  (str(s[0]), str(s[1]), str(s[2]), 'DONE', text,  str(s[5]), str(datetime.now())))
        con.commit()
        return 2