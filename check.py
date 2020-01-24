import mechanize, time, random
from bs4 import BeautifulSoup

#pycolor
X = "\033[0;37;40m"
DG = "\033[1;30;40m"
R = "\033[1;31;40m"
G = "\033[1;32;40m"
Y = "\033[1;33;40m"
B = "\033[1;34;40m"
M = "\033[1;35;40m"
C = "\033[1;36;40m"
W = "\033[1;37;40m"

ua = open("ua.txt",'r').read().splitlines()
mati = 0
orep = 0

def check(email):
   global ua,mati,orep,R,W,G
   live = open("live.txt",'a')
   die = open("die.txt",'a')
   br = mechanize.Browser()
   br.set_handle_robots(False)
   br.addheaders = [('User-agent', random.choice(ua))]
   br.open("https://www.ip-tracker.org/checker/email-lookup.php")
   br.select_form(nr=0)
   br.form['email'] = email
   submit = br.submit()
   res = submit.read()
   soup = BeautifulSoup(res,'html.parser')
   get = soup.find_all(class_="lookupgreen")
   if "is <br/>a valid deliverable e-mail box address" in str(get):
          live.write(email+"\n")
          print(W+"["+G+"LIVE"+W+"] : "+ email)
          orep += 1
   else:
          die.write(email+"\n")
          print(W+"["+R+"DIE"+W+"] : "+ email)
          mati += 1

print(W+"="*35)
print("")
print("    ..::: EMAIL LOOKUP :::..")
print("")
print("    Coded By : "+Y+"Syhrularv_ ")
print(W+"    Facebook : fb.com/sarul.arif.5")
print("")
print("="*35)
print("")
print("["+Y+"1"+W+"] Manual Checker")
print("["+Y+"2"+W+"] List Checker")
takok = int(input("["+Y+"?"+W+"] Pilih sob "+Y+"> "+W))

if takok == 1:
   mail = input(W+"["+Y+"?"+W+"] Email "+Y+": "+W)
   check(mail)
   if mati > 0:
      print("Data saved die.txt")
   else:
      print("Data saved live.txt")
elif takok == 2:
   list = input(W+"["+Y+"?"+W+"] List file "+Y+": "+W)
   try:
       buka = open(list,'r').read().splitlines()
       for i in buka:
           check(i)
           time.sleep(1)
       print(W+"["+G+"INFO"+W+"] Email Die : " + str(mati))
       print(W+"["+G+"INFO"+W+"] Email Live : " + str(orep))
       print(W+"["+G+"INFO"+W+"] Data saved live.txt & die.txt")
   except FileNotFoundError:
       print(W+"["+R+"ERROR"+W+"] File not found!")
       exit()
else:
   print(W+"["+R+"ERROR"+W+"] Something wrong i can feel it")
