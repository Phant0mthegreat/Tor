import colorama
from colorama import Fore
import re
import ipaddress
import socket
import system
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

system("clear")
print(Fore.YELLOW + ' ')
print(r"""▄▄▄█████▓ ▒█████   ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░      ░ ░ ░ ▒    ░░   ░ 
             ░ ░     ░     
                           """)
print(Fore.RESET + ' ')
print("\n***********************************************")
print("\n *Made by Phant0m The Great                               ")
print("\n *Discord tag: 𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150                                  ")
print("***********************************************")


while True:
    ip_add_entered = input("\nPlease enter the IP to see if it is valid:")
    
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("___________")
        print(Fore.GREEN + "IP valid.|")
        print(Fore.RESET + '-----------')
        break
    except:
        print("_____________")
        print(Fore.RED + "IP invalid.|")
        print(Fore.RESET + "_____________")


def scan_port(ipa,port):
 try:
   sock = socket.socket()
   sock.settimeout(.5)
   sock.connect((ipa,port))
   jj = (Fore.GREEN + '[+] port '+str(port)+ ' is open' + Fore.RESET + ' ')
   print(Fore.RESET + '\n'+jj)
   l = open('openPorts.txt','w+')
   l.write(jj)
   l.close()
 except:
   print('port '+str(port)+ ' is not open')
ipa = input('enter ip:')
for port in range(1,65535):
  scan_port(ipa,port)
