import os
import os,sys,time,mechanize
from bs4 import BeautifulSoup as sup
#Browsex
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders =[('Connection','keep-alive'),('Pragma','no-cache'),('Cache-Control','no-cache'),('Origin','http://sms.payuterus.biz'),('Upgrade-Insecure-Requests','1'),('Content-Type','application/x-www-form-urlencoded'),('User-Agent','Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'),('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'),('Referer','http://sms.payuterus.biz/alpha/'),('Accept-Encoding','gzip, deflate'),('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),]
url = 'http://sms.payuterus.biz/alpha'
z = []


def menu():
	os.system('reset')
	print ("\n")
	print ('          [ SMSae.in ]\033[1;93mv0.2\033[0m'.center(60))
	print ('[ Coded By DwI P ]'.center(60))
	print ('-----------------'.center(60))
	print ('           (\033[1;92m01\033[0m) : Send only one'.center(50))
	print ('          (\033[1;92m02\033[0m) : Send massal'.center(50))
	print ('(\033[1;91m00\033[0m) : Exit'.center(51))
	print
	pilih = input("               \033[1;92mChoose \033[0m: ")
	if pilih =="":
		exit()
	elif pilih =="01":
		solo()
	elif pilih =="1":
		solo()
	elif pilih =="02":
		print ("\033[1;91mTahap pengembangan !")
		exit()
	elif pilih =="2":
		print ("\033[1;91mTahap pengembangan !")
		exit()
	else:
		exit()
		
def solo():
	print("")
	nomer = int(input("               \033[1;92m>\033[0mNomor Target \033[0m: "))
	nsend = input("               \033[1;92m>\033[0mNama pengirim \033[0m: ")
	pes   = input("               \033[1;92m>\033[0mPesan \033[0m: ")
	note  = pes.split(' ')
	if pes =="":
		exit()
	else:
		by = "Free SMS by Dwi Purnomo"
		olh = ". Dikirim oleh "
		note = pes+olh+nsend+" I       "+by
		bs = sup(br.open(url),features="html.parser")
		for x in bs.find_all("span"):
			z.append(x.text)
		bypass = int(str(z)[2])+int(str(z)[6])
		br.select_form(nr=0)
		br.form['nohp']=str(nomer)
		br.form['pesan']=str(note)
		br.form['captcha']=str(bypass)
		get = br.submit().read()
		if 'SMS Gratis Telah Dikirim' in str(get):
			print ("")
			print('               \033[0m[\033[1;92mOK\033[0m] Berhasil dikirim ke : \033[1;92m'+str(nomer))
			print ("")
			input("\033[0m[ \033[1;92mBack \033[0m]")
			menu()
		else:
			print ("")
			print('               \033[0m[\033[1;91mGAGAL\033[0m] Gagal mengirim ke : \033[1;92m'+str(nomer))
			print ("")
			input("\033[0m[ \033[1;91mBack \033[0m]")
			menu()
			
menu()