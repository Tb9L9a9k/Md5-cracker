import hashlib
import argparse
import os , time
from colorama import Fore
#color
red = Fore.RED
white = Fore.WHITE
green = Fore.GREEN
magenta = Fore.MAGENTA
parser = argparse.ArgumentParser()

parser.add_argument('--hash',type=str,help='path MD5 file')
parser.add_argument('--word',type=str,help='path wordlist')
arge = parser.parse_args()
def clear():
        os.system('cls' if os.name=='nt' else 'clear')
clear()
print('please wait....')
time.sleep(1)
clear()
print('please wait...')
time.sleep(1)
clear()
print('please wait..')
time.sleep(1)
clear()
print('please wait.')
time.sleep(1)
clear()
def main():
    clear()
    print(rf"""


                                                                                                                       
        {white}@@@@@@@@@@   @@@@@@@   @@@@@@@                    {red}@@@@@@@  @@@@@@@    @@@@@@    @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@   
        {white}@@@@@@@@@@@  @@@@@@@@  @@@@@@@                   {red}@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
        {white}@@! @@! @@!  @@!  @@@  !@@                       {red}!@@       @@!  @@@  @@!  @@@  !@@       @@!  !@@  @@!       @@!  @@@  
        {white}!@! !@! !@!  !@!  @!@  !@!                       {red}!@!       !@!  @!@  !@!  @!@  !@!       !@!  @!!  !@!       !@!  @!@  
        {white}@!! !!@ @!@  @!@  !@!  !!@@!!      @!@!@!@!@     {red}!@!       @!@!!@!   @!@!@!@!  !@!       @!@@!@!   @!!!:!    @!@!!@!   
        {white}!@!   ! !@!  !@!  !!!  @!!@!!!     !!!@!@!!!     {red}!!!       !!@!@!    !!!@!!!!  !!!       !!@!!!    !!!!!:    !!@!@!    
        {white}!!:     !!:  !!:  !!!      !:!                   {red}:!!       !!: :!!   !!:  !!!  :!!       !!: :!!   !!:       !!: :!!   
        {white}:!:     :!:  :!:  !:!      !:!                   {red}:!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!  :!:       :!:  !:!  
        {white}:::     ::    :::: ::  :::: ::                    {red}::: :::  ::   :::  ::   :::   ::: :::   ::  :::   :: ::::  ::   :::  
         {white}:      :    :: :  :   :: : :                     {red}:: :: :   :   : :   :   : :   :: :: :   :   :::  : :: ::    :   : :  
                                                                                                                       
                                    |----------------<@Gigas_TK>----------------|
{magenta}Github {white}: {red}Tb9L9a9k
{magenta}Telegram {white}: {red}@Gigas_TK
""")
    with open(arge.hash,'r') as hash_file:
        h = hash_file.read().split('\n')
    with open(arge.word,"r",encoding='utf-8') as word:
        wordlist = word.read().split('\n')
    t = []

    for i in wordlist:
        enc = hashlib.md5(i.encode()).hexdigest()
        t.append(enc)
        if enc in h:
            print(f'{white}[{red}*{white}]{magenta}password found! {white}hash = {green}{enc} {white}password = {green}{i}')
        else:
            print(f'{white}[{red}*{white}]password not found')

main()