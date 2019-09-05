import os
import sys
import time
import marshal

def mamak(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


banner = '\x1b[1;36m\n\x1b[1;91m[ \x1b[1;37m==============\x1b[1;91m[COMPILE PYTHON]\x1b[1;37m===============\x1b[1;91m ]\n                   \x1b[1;92mAuthor  : \x1b[1;91mMAESTRO\n / / __/\\__ \\ \\    \x1b[1;92mType    : \x1b[1;91mCompile Python\n/ /  \\    /  \\ \\   \x1b[1;92mGithub  : \x1b[1;91mhttps://github.com/maestro-a\n\\ \\  /_  _\\  / /\n \\_\\   \\/   /_/\n \n'

def py():
    try:
        os.system('clear')
        print banner
        a = input('\x1b[1;37mMasukan Nama File :  \x1b[1;32m')
        x = open(a).read()
        b = compile(x, '', 'exec')
        c = marshal.dumps(b)
        d = open('Enc' + a, 'w')
        d.write('##############\n Terkompiler By Maestro\n#WA : 081360479719\n#########\nimport marshal\n')
        d.write('exec(marshal.loads(' + repr(c) + '))')
        d.close()
        time.sleep(1.5)
        jalan('\x1b[1;91m[!]\x1b[1;36mFile Berhasil Tercompile: \x1b[1;91mEnc' + a)
        jalan('\x1b[1;92m    By: MAESTRO :*')
        jalan('\x1b[1;91m[ \x1b[1;37m================\n\x1b[1;91m                 Berpikirlah Pemula\n              Maka Dunia Akan Terbuka\n                        BAGIMU\n\x1b[1;37m                          ==================\x1b[1;91m ] ')
        print ()
    except KeyboardInterrupt:
        print '\n\x1b[1;31m[!] ERROR: PASTIKAN FILE YANG MAU DI COMPILE BERADA DI FOLDER YANG SAMA DAN PASTIKAN ANDA MENGINPUT FILE DENGAN BENAR'
        exit()


def py2():
    try:
        os.system('clear')
        print banner
        a = raw_input('\x1b[1;37mMasukan Nama File => \x1b[1;32m')
        x = open(a).read()
        b = compile(x, '', 'exec')
        c = marshal.dumps(b)
        d = open('Enc' + a, 'w')
        d.write('\n##############\n#Terkompiler By Maestro\n#WA : 081360479719\n#########\nimport marshal\n')
        d.write('exec(marshal.loads(' + repr(c) + '))')
        d.close()
        time.sleep(1.5)
        jalan('\x1b[1;37m[!]\x1b[1;91mTunggu sebentar')
        jalan('\x1b[1;37m[!]\x1b[1;91mProses membutuhkan 3 detik.')
        time.sleep(3)
        jalan('\x1b[1;91m[!]\x1b[1;36mFile Berhasil Tercompile: \x1b[1;91mEnc' + a)
        jalan('\x1b[1;92m    By : MAESTRO :*')
        jalan('\x1b[1;91m[ \x1b[1;37m================\n\x1b[1;91m                 Berpikirlah Pemula\n              Maka Dunia Akan Terbuka\n                        BAGIMU\n\x1b[1;37m                          ==================\x1b[1;91m ] ')
        print
    except KeyboardInterrupt:
        print '\n\x1b[1;31m[!] ERROR: PASTIKAN FILE YANG MAU DI COMPILE BERADA DI FOLDER YANG SAMA DAN PASTIKAN ANDA MENGINPUT FILE DENGAN BENAR'
        exit()


os.system('clear')
print banner
jalan('\x1b[1;37m|=================[\x1b[1;91mPILIH FILE PYTHON]\x1b[1;37m==================|')
print '\x1b[1;91m[1] \x1b[1;36mPython'
print '\x1b[1;91m[2] \x1b[1;36mPython2'
jalan('\x1b[1;91m[INFO]\x1b[1;92mJika memilih nomor 1 jalankan tool ini\n      Dengan python atau sebaliknya')
ask = input('\x1b[1;37m[?] \x1b[1;91mCompile=> \x1b[1;32m')
if ask == '1':
    py()
elif ask == 2:
    py2()
else:
    jalan('\n\x1b[1;31m[!] LOL')
