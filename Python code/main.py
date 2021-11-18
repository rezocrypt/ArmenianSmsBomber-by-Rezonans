from Modules.spam_functions import alfapharm

# For printing banner
with open("Modules/banner") as f:
	print(f.read())

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
print(f"{sended} sms from {count} has been sent successfully")
print(f"{sended} - sended")
print(f"{failed} - failed")
