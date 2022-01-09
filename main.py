import random, string, requests
from colorama import Fore
from os import system

system("cls && title Cvip Roblox Bypass Name Gen && MODE 52,14")

proxies = open("proxy.txt").read().splitlines()

def getProxy():
    return random.choice(proxies)
def main():

    woeking = 0
    notworking = 0

    logo_names = ("""
    [1] Nigger
    [2] Nigga
    [3] Fuck
    [4] Bitch
    [5] Shit
    [6] Ass

    """)
    print(logo_names)
    name_chose = input("What Name Do You Wnat?> ")
    if name_chose == "1":
        while True:
            firstPart = "ni"
            #the best is 2 up
            random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
            EndPart = "gger"
            name = f"{firstPart}{random_shit}{EndPart}"
            checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
            code1 = checker['message']

            if code1 == "Username is valid":
                woeking+=1
                print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
                with open("Names.txt", "a") as f:
                    f.write(f"{name}\n")
                    f.close()
            else:
                notworking+=1
                print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
    if name_chose == "2":
        while True:
            firstPart = "ni"
            #the best is 2 up
            random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
            EndPart = "gga"
            name = f"{firstPart}{random_shit}{EndPart}"
            checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
            code1 = checker['message']

            if code1 == "Username is valid":
                woeking+=1
                print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
                with open("Names.txt", "a") as f:
                    f.write(f"{name}\n")
                    f.close()
            else:
                notworking+=1
                print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
    if name_chose == "3":
        while True:
            firstPart = "fu"
            #the best is 2 up
            random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
            EndPart = "qk"
            name = f"{firstPart}{random_shit}{EndPart}"
            checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
            code1 = checker['message']

            if code1 == "Username is valid":
                woeking+=1
                print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
                with open("Names.txt", "a") as f:
                    f.write(f"{name}\n")
                    f.close()
            else:
                notworking+=1
                print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
    if name_chose == "4":
        while True:
            firstPart = "bit"
            #the best is 2 up
            random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
            EndPart = "ch"
            name = f"{firstPart}{random_shit}{EndPart}"
            checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
            code1 = checker['message']

            if code1 == "Username is valid":
                woeking+=1
                print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
                with open("Names.txt", "a") as f:
                    f.write(f"{name}\n")
                    f.close()
            else:
                notworking+=1
                print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
    if name_chose == "5":
        while True:
            firstPart = "sh"
            #the best is 2 up
            random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
            EndPart = "it"
            name = f"{firstPart}{random_shit}{EndPart}"
            checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
            code1 = checker['message']

            if code1 == "Username is valid":
                woeking+=1
                print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
                with open("Names.txt", "a") as f:
                    f.write(f"{name}\n")
                    f.close()
            else:
                notworking+=1
                print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
    if name_chose == "6":
        while True:
            firstPart = "as"
            #the best is 3 up
            random_shit = ("").join(random.choice(string.ascii_letters)for k in range(3))
            EndPart = "s"
            name = f"{firstPart}{random_shit}{EndPart}"
            checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
            code1 = checker['message']

            if code1 == "Username is valid":
                woeking+=1
                print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
                with open("Names.txt", "a") as f:
                    f.write(f"{name}\n")
                    f.close()
            else:
                notworking+=1
                print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
                system("title Working: "+ str(woeking)+ " Not Working: "+str(notworking))
main()
