import marshal, os, time

banner=("""\033[1;36m
\033[1;32m[+] \033[1;91mScript anda sering di Recode oleh orang yang
\033[1;31        \033[1;91mTidak bertanggung jawab?
\033[1;31         \033[1;91mSilahlan Encript agar Code nya agak rumit :+
     _  _
   _| || |_          \033[1;32mCOMPILER PYTHON\033[1;36m
  |_  ..  _|
  |_      _| \033[1;31mAuthor=>MAESTRO\033[1;36m
    |_||_|   \033[1;31mType : \033[1;91mCompiler Python
            \033[1;31mGithub : \033[1;91mhttps://github.com/maestro-a
""")
def py():
	try:
		os.system('clear')
		print(banner)
		a=input("\033[1;37mMasukan Nama File => \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("Enc"+a,'w')
		d.write('\n##############\n Terkompiler By Maestro\nWA : 081360479719\n#########\nimport marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mFile Berhasil Tercompile: \033[1;36mEnc"+a)
		print()
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: PASTIKAN FILE YANG MAU DI COMPILE BERADA DI FOLDER YANG SAMA DAN PASTIKAN ANDA MENGINPUT FILE DENGAN BENAR")
		exit()
	
def py2():
	try:
		os.system('clear')
		print(banner)
		a=raw_input("\033[1;37mMasukan Nama File => \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("Enc"+a,'w')
		d.write('\n##############\n#Terkompiler By Maestro\n#WA : 081360479719\n#########\nimport marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mFile Berhasil Tercompile: \033[1;36mEnc"+a)
		print
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: PASTIKAN FILE YANG MAU DI COMPILE BERADA DI FOLDER YANG SAMA DAN PASTIKAN ANDA MENGINPUT FILE DENGAN BENAR")
		exit()

os.system('clear')
print(banner)
print("\033[1;32m[1] Python3")
print("[2] Python2")
ask=input("\033[1;37m[?] => \033[1;32m")
if ask == '1':
	py()
elif ask == 2:
	py2()
else:
	print("\n\033[1;31m[!] LOL")
