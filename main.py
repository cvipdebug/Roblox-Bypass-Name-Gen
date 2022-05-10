import random, string, requests, threading
from colorama import Fore
from os import system

system("title Cvip Roblox Bypass Name Gen && MODE 52,14")

proxies = open("proxy.txt").read().splitlines()

class title:
    woeking = 0
    notworking = 0

def getProxy():
    return random.choice(proxies)

amount = int(input("How many threds? : "))
def assbeater420():

    firstPart = "as"
    #the best is 2 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
    EndPart = "sBeater42I0"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def nigger():

    firstPart = "ni"
    #the best is 2 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
    EndPart = "gger"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def Nigga():

    firstPart = "ni"
    #the best is 2 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
    EndPart = "gga"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def Fuck():

    firstPart = "fu"
    #the best is 2 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
    EndPart = "qk"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def Bitch():

    firstPart = "bit"
    #the best is 2 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
    EndPart = "ch"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def Shit():
    firstPart = "sh"
    #the best is 2 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
    EndPart = "it"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def Ass():
    firstPart = "as"
    #the best is 3 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(3))
    EndPart = "s"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def GeorgeFloyd():
    firstPart = "George"
    #the best is 2 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
    EndPart = "Floyd"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username={name}&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working {name}")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def Ishootniggasforfun():
    firstPart = "ni"
    #the best is 2 up
    random_shit = ("").join(random.choice(string.ascii_letters)for k in range(2))
    EndPart = "ggas"
    name = f"{firstPart}{random_shit}{EndPart}"
    checker = requests.get(f"https://auth.roblox.com/v2/usernames/validate?request.username=Ishoot{name}forfun&request.birthday=2000-01-01&request.context=Signup", proxies={"http": 'http://' + getProxy()}).json()
    code1 = checker['message']

    if code1 == "Username is valid":
        title.woeking+=1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Working Ishoot{name}forfun")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))
        with open("Names.txt", "a") as f:
            f.write(f"Ishoot{name}forfun\n")
            f.close()
    else:
        title.notworking+=1
        print("["+Fore.RED+"INFO"+Fore.WHITE+f"] Not Working Ishoot{name}forfun")
        system("title Working: "+ str(title.woeking)+ " Not Working: "+str(title.notworking))

def main():
    logo_names = ("""
    [1] Nigger
    [2] Nigga
    [3] Fuck
    [4] Bitch
    [5] Shit
    [6] Ass
    [7] George Floyd
    [8] I shoot niggas for fun
    [9] Ass Beater
    [10] All

    """)
    print(logo_names)
    name_chose = input("What Name Do You Wnat?> ")
    if name_chose == "1":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = nigger , daemon= True).start()
                except:
                    pass
    if name_chose == "2":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Nigga, daemon= True).start()
                except:
                    pass
    if name_chose == "3":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Fuck, daemon= True).start()
                except:
                    pass
    if name_chose == "4":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Bitch, daemon= True).start()
                except:
                    pass
    if name_chose == "5":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Shit, daemon= True).start()
                except:
                    pass
    if name_chose == "6":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Ass, daemon= True).start()
                except:
                    pass
    if name_chose == "7":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = GeorgeFloyd, daemon= True).start()
                except:
                    pass
    if name_chose == "8":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Ishootniggasforfun, daemon= True).start()
                except:
                    pass
    if name_chose == "9":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = assbeater420, daemon= True).start()
                except:
                    pass
    if name_chose == "10":
        while True:
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = nigger, daemon= True).start()
                except:
                    pass
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Nigga, daemon= True).start()
                except:
                    pass
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Fuck, daemon= True).start()
                except:
                    pass
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Bitch, daemon= True).start()
                except:
                    pass
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Shit, daemon= True).start()
                except:
                    pass
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Ass, daemon= True).start()
                except:
                    pass
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = GeorgeFloyd, daemon= True).start()
                except:
                    pass
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = Ishootniggasforfun, daemon= True).start()
                except:
                    pass
            if threading.active_count() <= amount:
                try:
                    threading.Thread(target = assbeater420, daemon= True).start()
                except:
                    pass

threading.Thread(target= main()).start()
