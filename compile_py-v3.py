from sys import stdout
import subprocess as sp, sys, os, marshal, re, time, json, bs4, random, requests
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
W = '\033[1;37m' #Putih 
N = '\033[0m' # Tutup
R = '\033[1;37m\033[31m'  #Merah
G = '\033[1;32m' #Ijo
B = '\033[1;37m\033[34m' # biru
O = '\033[33m' # Kuning
C = '\033[36m' #Biru laut
K = '\x1b[1;93m' #Kuning

notic  = "{}{}[*]{} ".format(N,B,N)
warning = "{}[-]{} ".format(R,N)
wa = "{}[{}-{}] ".format(W,R,W)
was = "{}[{}!{}] ".format(W,R,W)
good    = "{}[!]{} ".format(G,N)
warn    = "{}[!]{} ".format(O,N)
gris = "\xe2\x95\x91".format(W,N)
pan = "{}\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90".format(W)
q = 'q'
try:
    from uncompyle6.main import decompile
except Exception as e:
    sp.call('pip2 install uncompyle2', shell=True, stderr=sp.STDOUT)

def banner():
    print (m + '''
      ▒██   ██▒▒██   ██▒▒██   ██▒
      ▒▒ █ █ ▒░▒▒ █ █ ▒░▒▒ █ █ ▒░
      ░░  █   ░░░  █   ░░░  █   ░
       ░ █ █ ▒  ░ █ █ ▒  ░ █ █ ▒ 
      ▒██▒ ▒██▒▒██▒ ▒██▒▒██▒ ▒██▒
      ▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░
      ░░   ░▒ ░░░   ░▒ ░░░   ░▒ ░
       ░    ░   ░    ░   ░    ░  
       ░    ░   ░    ░   ░    ░  
                           
         Compiler & Decompiler
     
                  By
              
           xXx_not_found_xXx
         
    My Telegram > @xXx_not_found_xXx
''')



def rune():
	menu()
	#print "%sBisaa" % W
	
def kirimq():
	global q
	print ('%s[%s#%s] %sSilahkan Meminta konfirmasi kepada Angga' % (G,K,G,W))
	input('%s[%s^%s] %sTekan Enter Untuk Menghubungi Angga via WhatsApp...' % (G,K,G,W))
	subprocess.check_output([
	'am', 'start',
	'https://t.me/xXx_not_found_xXx' + q.replace(' ', '%20') + ''])
	
def whasq():
	print ('')
	print ('   %s[ %sReport %s] ' % (W,G,W))
	print ('\n%ssend message for me...' % wa)
	bug = input('%sEnter your message : ' % was)
	print (42 * '\x1b[1;97m\xe2\x95\x90')
	subprocess.check_output([
	'am', 'start',
	'https://t.me/xXx_not_found_xXx: ' + bug + ''])

def updeq():
	print ('[%s#%s] Updating  ...' % (G, N))
	os.system('git pull')
	print ('%s[%s**%s]%s  was updated. \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (G, R, G, N))


#~MODULE~#
import requests, subprocess, time, os, sys
#~MENU~#
def menuq():
	os.system('clear')
	print ("")
	print ("\n")
	print ("     %s{%s01%s} Start " % (W,G,W))
	print ("     {%s02%s} contact " % (G,W))
	print ("     {%s03%s} Update " % (G,W))
	print ("     {%s00%s} Exit " % (R,W))
	print ("")
	pilih()
	
def pilih():
	mane = input('    %s%s > ' % (pan,G))
	if mane == '':
		userq()
		pilih()
	elif mane in ('1', '01'):
		menu()
	elif mane in ('2', '02'):
		whasq()
	elif mane in ('3', '03'):
		updeq()
	elif mane in ('0', '00'):
		print (" %s\n  [%s!%s] Exit \n" % (W,R,W))
		sys.exit()
	else:
		menuq()


def load(word):
    lix = [
     '/', '-', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.3)
            sys.stdout.flush()


def jalan(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)


def menu():
    os.system('clear')
    banner()
    print (h + '\nMenu ' + p + ': \n [' + h + '1' + p + ']. Compiler\n [' + h + '2' + p + ']. ' + 'Update \n [' + h + '0' + p + '].' + m + ' Exit\n\n ' + p + '[' + h + '99' + p + '].' + u + ' Report Bug\n' + p)
    pilih = input(h + '[' + k + '?' + h + ']' + p + ' @xXx_not_found_xXx--> ')
    if pilih == '1':
        marsh()
    elif pilih == '2':
        try:
            os.system('git pull')
        except:
            print (h + '[' + m + '!' + h + ']' + p + ' Update Failed ')
            pl = input(h + '[' + k + '?' + h + ']' + p + '  Manual Download? y/t ')
            if pl == 'y' or pl == 'Y':
                try:
                    sp.check_output([
                     'am', 'start',
                     'https://github.com/hamalord4444/com'])
                except:
                    sys.exit(h + '[' + k + '!' + h + ']' + p + ' Failed to open the link')

            else:
                menu()

    elif pilih == '0':
        jalan('\n' + h + '[' + k + '#' + h + ']' + p + ' Created by Angga ', 0.01)
        jalan(h + '\n' + '[' + k + '#' + h + ']' + p + ' Thank You for Using This Program ', 0.01)
        jalan(h + '\n' + '[' + k + '#' + h + ']' + p + ' contact(github) : https://github.com/hamalord4444', 0.01)
        jalan(h + '\n' + '[' + k + '#' + h + ']' + p + ' contact(Facebook) : ', 0.01)
        jalan(h + '\n' + '[' + k + '#' + h + ']' + p + ' contact(Telegram) : @xXx_not_found_xXx', 0.01)
        jalan(h + '\n' + '[' + k + '#' + h + ']' + p + ' Good bye `\\_(@)_/`\n', 0.01)
        sys.exit()
    elif pilih == '99':
        jalan(p + 31 * '\xe2\x95\x90' + h + '[' + bm + 'Report' + h + ']' + p + '>', 0.008)
        print ('\n' + h + '[' + m + '!' + h + ']' + p + ' Report Bug Via WhatsApp ')
        bug = input(h + '[' + k + '?' + h + ']' + p + ' Enter your message : ')
        bug.replace(' ', '%20')
        load(h + '[' + k + '~' + h + ']' + p + 'Loading please wait ...')
        try:
            sp.check_output([
             'am', 'start',
             'https://t.me/hamalord4444 : ' + bug + ''])
        except:
            sys.exit('\n' + h + '[' + k + '!' + h + ']' + p + ' Failed to send message ')

    elif pilih == '':
        print ('\n' + h + '[' + m + '!' + h + ']' + p + ' Not Null ' + m + '!!!')
        input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu')
        menu()
    else:
        print ('\n' + h + '[' + m + '!' + h + ']' + p + ' Pilih Yang Bener ' + m + '!!!')
        input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
        os.system('clear')
        menu()


def marsh():
    jalan(p + 31 * '\xe2\x95\x90' + h + '[' + bm + 'COMPILER' + h + ']' + p + '>', 0.008)
    print (h + '\nMenu ' + p + ':\n [' + h + '1' + p + ']. Compile Python 3\n [' + h + '2' + p + ']. Compile Python to pyc\n [' + h + '0' + p + '].' + k + ' Back\n')
    try:
        pil = input(h + '[' + k + '?' + h + ']' + p + ' @xXx_not_found_xXx--> ')
    except Exception as e:
        marsh()
    else:
        if pil == '1':
            v = 3
        elif pil == '2':
            pyc()
        elif pil == '0':
            menu()
        else:
            print (h + '[' + m + '!' + h + ']' + p + ' Choose the right one')
            marsh()
        try:
            if v == 2:
                print (h + '[' + k + '#' + h + ']' + p + ' For Example : /path/file.py')
                file = input(h + '[' + k + '?' + h + ']' + p + ' Input File : ')
            elif v == 3:
                py3()
                try:
                    sp.call('python3 cac.py', shell=True, stderr=sp.STDOUT)
                except Exception as e:
                    sys.exit(h + '[' + k + '!' + h + ']' + p + ' Compile Fail because : ' + e)

                os.system('rm cac.py')
                load(h + '[' + k + '#' + h + ']' + p + ' Compile process Wait a minute ...')
                time.sleep(1.5)
                os.system('clear')
                time.sleep(1)
                delay = open('/sdcard/enc.py', 'r').readlines()
                for x in range(len(delay)):
                    jalan(delay[x], 0.0001)

                print ('\n' + h + '[' + k + '#' + h + ']' + p + ' Successfully Compiled')
                print (h + '[' + k + '#' + h + ']' + p + ' file saved : /sdcard/enc.py')
                ask = input(h + '[' + k + '?' + h + ']' + p + ' Compile Again? y/t ')
                if ask == 'y' or ask == 'Y':
                    menu()
                elif ask == 't' or ask == 'T':
                    sys.exit()
                else:
                    print (h + '[' + m + '!' + h + ']' + p + ' Choose the right one ' + m + '!!!')
                    input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
                    os.system('clear')
                    menu()
        except IndexError:
            print (h + '[' + m + '!' + h + ']' + p + ' Program Error!!!')
            sys.exit()
        except KeyboardInterrupt:
            print (h + '[' + k + '^' + h + ']' + p + ' ctrl+c \n')
            print (h + '[' + k + '#' + h + ']' + p + ' Exit!!!\n')
            time.sleep(3)
            sys.exit()
        except EOFError:
            print (h + '[' + k + '^' + h + ']' + p + ' ctrl+d \n')
            print (h + '[' + k + '#' + h + ']' + p + ' Exit!!!\n')
            time.sleep(3)
            sys.exit()
        else:
            try:
                string = open(file, 'r').read()
            except IOError:
                print ('\n' + h + '[' + m + '!' + h + ']' + p + ' File not found')
                input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
                os.system('clear')
                menu()

            try:
                code = compile(string, '<Angga>', 'exec')
                load(h + '[' + k + '#' + h + ']' + p + ' Compile process Wait a minute ...')
                time.sleep(1.5)
                data = marshal.dumps(code)
            except SyntaxError:
                jalan('\n' + h + '[' + m + '!' + h + ']' + p + ' script Using python version 3 \n', 0.1)
                jalan(h + '[' + m + '!' + h + ']' + p + ' Use the Menu [2]. Compile Python 3\n', 0.1)
                input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
                menu()
            except TypeError:
                os.system('clear')
                banner()
                print ('\n' + h + '[' + k + '#' + h + ']' + p + ' file already compiled\n')
                sys.exit()

    fileout = open('/sdcard/enc.py', 'wb')
    fileout.write('#Compiled By xXx_not_found_xXx')
    fileout.write('\n#Github : https://github.com/hamalord4444')
    fileout.write('\n#Telegram : @xXx_not_found_xXx')
    fileout.write('\nimport marshal')
    fileout.write('\nexec(marshal.loads(' + repr(data) + '))')
    fileout.close()
    os.system('clear')
    time.sleep(1)
    delay = open('/sdcard/enc.py', 'r').readlines()
    for x in range(len(delay)):
        jalan(delay[x], 0.0001)

    print ('\n' + h + '[' + k + '#' + h + ']' + p + ' file successfully compiled')
    print (h + '[' + k + '#' + h + ']' + p + ' file saved : /sdcard/enc.py')
    ask = input(h + '[' + k + '?' + h + ']' + p + ' Compile Again? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    elif ask == 't' or ask == 'T':
        sys.exit()
    else:
        print (h + '[' + m + '!' + h + ']' + p + ' Choose the right one ' + m + '!!!')
        input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
        os.system('clear')
        menu()


def py3():
    text = "import marshal, os, sys, time\np = '\x1b[0m'\nm = '\x1b[91m'\nh = '\x1b[92m'\nk = '\x1b[93m'\n\ndef jalan(z, t):\n    for e in z :\n        sys.stdout.write(e)\n        sys.stdout.flush()\n        time.sleep(t)  \n\nprint(h +'['+ k +'#'+ h +']'+ p + ' For Example : /path/marsh.py')\nf = input(h +'['+ k +'?'+ h +']'+ p + ' Enter Your File : ')\ntry:\n    file = open(f).read()\nexcept IOError:\n    print( h +'['+ m +'!'+ h +']'+ p +' File Not Found')\n    input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')\n    os.system('clear')\n    os.system('python2 data/main.py')\n\ntry:\n    x = compile(file, '<Angga>', 'exec')\n    data = marshal.dumps(x)\nexcept SyntaxError:\n    jalan(h +'['+ m +'!'+ h +']'+ p +' script Using python version 2 \\n', 0.1)\n    jalan(h +'['+ m +'!'+ h +']'+ p +' Use the Menu [1]. Compile Python 2\\n', 0.1)\n    input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')\n    os.system('python2 data/main.py')\nexcept TypeError:\n    os.system('clear')\n    banner()\n    print(h +'['+ k +'#'+ h +']'+ p +' File Already Compiled')\n    sys.exit()\n\nopen('com/com-3.py', 'w').write('import marshal\\n#Compile by Angga\\n#Facebook : \\nexec(marshal.loads('+repr(data)+'))')"
    cac = open('cac.py', 'w')
    cac.write(text)
    cac.close()


def pyc():
    print (h + '[' + k + '#' + h + ']' + p + ' For Example : /path/file.py')
    f = input(h + '[' + k + '?' + h + ']' + p + ' Enter Your File : ')
    from py_compile import compile
    compile(f)
    load(h + '[' + k + '#' + h + ']' + p + ' Compile process Wait a minute ...')
    jalan('\n' + h + '[' + k + '#' + h + ']' + p + ' file successfully compiled', 0.01)
    print ('\n' + h + '[' + k + '#' + h + ']' + p + (' File Saved: {}c').format(f))
    ask = input(h + '[' + k + '?' + h + ']' + p + ' Compile Again? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    elif ask == 't' or ask == 'T':
        sys.exit()
    else:
        print (h + '[' + m + '!' + h + ']' + p + ' Choose the right one ' + m + '!!!')
        input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
        os.system('clear')
        menu()



if __name__ == '__main__':
    if os.path.exists('com') or os.path.exists('dec'):
        menuq()
    else:
        os.system('mkdir com')
        os.system('mkdir dec')
        
        