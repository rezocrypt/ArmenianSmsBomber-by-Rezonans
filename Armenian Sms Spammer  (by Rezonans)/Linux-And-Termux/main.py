from Modules.spam_functions import alfapharm
from Modules.banner import bn

# For printing banner
for i in bn:
    print(i)

number = input("\n\n\033[36mEnter phone number (Example 098100100):\t")
count = int(input("\nEnter count (Recommented from 10 to 100):\t"))
number = "+374" + number[1:]
print("\n")
failed = 0
sended = 0
for x in range(count):
	value = alfapharm(number)
	if value==1:
		print(f"\033[32m[+]One sms has been sent[+]\t[{x+1} from {count}]")
		sended+=1
	else:
		print(f"\033[31m[-]Error while sending sms[-]\t[{x+1} from {count}]")
		failed+=1
print(f"\n\033[33m{sended} sms from {count} has been sent successfully")
print(f"\033[32m{sended} - sended")
print(f"\033[31m{failed} - failed")
