# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
# import code 
import re
sign_hash=None
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36'})
host='https://bbs.shuiguobang.com'
# host="http://localhost:8000/upload"
r = s.get(host+'/')
def qiandao():
	#'&inajax=1&ajaxtarget=JD_sign'
    # plugin.php?id=k_misign:sign&operation=qiandao&format=text&formhash=f51293fa
    r1= s.post(host+'/plugin.php?id=k_misign:sign&operation=qiandao&'+sign_hash+'&format=empty')
    if r1.ok:
        # print(r1.text)
        print("签到成功")
    else:
        print("签到失败")
def getlist():
    r1= s.get(host+'/plugin.php?id=k_misign:sign&operation=list&op=month')
    soup = BeautifulSoup(r1.text,"html.parser")
    pass
def getqdPH():
	# res=s.get(host+'/k_misign-sign.html')
	# if res.ok:
	# 	soup = BeautifulSoup(res.content,"html.parser")
		
	pass
def getForum():
    r1= s.get(host+'/forum.php?mod=forumdisplay&fid=379&filter=lastpost&orderby=lastpost&mobile=2')
    soup = BeautifulSoup(r1.text,"html.parser")
    ss=ps.find_all("li","subjects_0") #主题
def qiandaoPage():
    global sign_hash
    r1= s.get(host+'/k_misign-sign.html?mobile=2')
    if r1.ok:
        print("连接签到页成功")
        soup = BeautifulSoup(r1.text,"html.parser")
        ss=soup.find_all("script")
        scri=ss[4]
        js=scri.contents[0]
        #sign_hash=js.split("\r\n")[-4].split("&")[3].split(",")[0][:-1]
        #find=re.search("formhash=([a-zA-Z_0-9]*)",s)
        find=re.search("formhash=([a-zA-Z_0-9]*)",js)
        sign_hash=find.group(0)

        visited=soup.find_all("a","btn_visited")
        if len(visited)>0:
            print("已签到")
        else:
            qiandao()
    else:
        print("连接签到页失败")
# <form method="post" autocomplete="off" id="lsform" 
#action="member.php?mod=logging&amp;action=login&amp;loginsubmit=yes&amp;infloat=yes&amp;lssubmit=yes" 
#onsubmit="pwmd5('ls_password');return lsSubmit();"> 
# ajaxpost('lsform', 'return_ls', 'return_ls');       
# fastloginfield: username
# username: (unable to decode value)
# password: 1de4f2bd9d3fb3205376c4476d90eeac
# quickforward: yes
# handlekey: ls
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN
# Cache-Control: max-age=0
# Connection: keep-alive
# Content-Length: 123
# Content-Type: application/x-www-form-urlencoded
# Cookie: PHPSESSID=pvneaq5e2kutj0vt0g1s2so5t3; Zqvh_2132_sid=Qvu1wN; 
#Zqvh_2132_saltkey=JIJLJK81; Zqvh_2132_lastvisit=1609022249; Zqvh_2132_atarget=1; 
#Zqvh_2132_forum_lastvisit=D_399_1609025850; Zqvh_2132_visitedfid=399; 
#Zqvh_2132_sendmail=1; Zqvh_2132_lastact=1609026121%09forum.php%09ajax
# Host: bbs.shuiguobang.com
# Origin: https://bbs.shuiguobang.com
# Referer: https://bbs.shuiguobang.com/forum-399-1.html
# Sec-Fetch-Dest: iframe
# Sec-Fetch-Mode: navigate
# Sec-Fetch-Site: same-origin
# Sec-Fetch-User: ?1
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.47 Safari/537.36
# Cookie(version=0, 
#name='Zqvh_2132_lastact', value='1609026297%09member.php%09logging', 
#port=None, port_specified=False, domain='bbs.shuiguobang.com', 
#domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, 
#secure=False, expires=1609112697, discard=False, comment=None, 
#comment_url=None, rest={}, rfc2109=False), 

# &inajax=1
#&lssubmit=yes

# formhash=38117a8c&referer=https%3A%2F%2Fbbs.shuiguobang.com%2Ftouch%2F&fastloginfield=username&cookietime=2592000&username=%E9%A9%AC%E7%BA%A2%E6%9D%83&password=mhq730208&questionid=0&answer=

# formhash    "38117a8c"
# referer "https://bbs.shuiguobang.com/touch/"
# fastloginfield  "username"
# cookietime  "2592000"
# username    "马红权"
# password    "mhq730208"
# questionid  "0"
# answer  ""
def login():
    r1= s.post(host+'/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LXK7J&mobile=2&handlekey=loginform&inajax=1'
        , data = {
        'username':'马红权'
        ,'fastloginfield': 'username'
        ,'cookietime':"2592000"
        ,'questionid':"0"
        ,'answer':""
        ,'formhash':"38117a8c"
        ,'referer':"https://bbs.shuiguobang.com/touch/"
        ,'password':'mhq730208'})
    #7f3ad9cf1a369f9b1ab2c54b8db8cf69
    if "马红权" in r1.text:
        print("登录成功")
        qiandaoPage()
    else:
        print("登录失败")
    return r1
if r.ok:
    print("连接成功")
    login()
else:
    print("连接失败")
# i=code.InteractiveConsole(locals=locals())
# i.interact()
# <?xml version="1.0" encoding="utf-8"?>
# <root><![CDATA[<script type="text/javascript" reload="1">if(typeof succeedhandle_login=='function') {succeedhandle_login('http://localhost:8000/upload/index.php', '欢迎您回来，新手上路 马红权，现在将转入登录前页面', {'username':'马红权','usergroup':'新手上路','uid':'2','groupid':'10','syn':'0'});}hideWindow('login');showDialog('欢迎您回来，新手上路 马红权，现在将转入登录前页面', 'right', null, function () { window.location.href ='http://localhost:8000/upload/index.php'; }, 0, null, null, null, null, null, 2);</script>]]></root>

# <?xml version="1.0" encoding="utf-8"?>
# <root><![CDATA[<script type="text/javascript" reload="1">if(typeof errorhandle_ls=='function') {errorhandle_ls('', {'type':'1'});}</script><script type="text/javascript">showWindow('login', 'member.php?mod=logging&action=login&auth=9f129FSLF4CYpaVFm43b4X29IBkUu97UkX4jfU5VZC403Gc48C8Rd8tQAFdxrxE0J2EgaeHTKLAeYwhvql10LUofcKjAvw85vw&referer=http%3A%2F%2Flocalhost%3A8000%2Fupload%2F.%2F')</script>]]></root>
# r2= s.get(host+'/member.php?mod=logging&action=login&auth=3de6IMdvoK%2FUE71AVTavrqWd8eg5zUsoumSGw0hH3Fe3UDYkCJtzHzB4jyTFyJ%2BmVMP5dzG6H32ZcKl0ZTsyH%2B3jbwJcYIrGjQ')