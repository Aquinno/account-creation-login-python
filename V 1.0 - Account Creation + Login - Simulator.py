#Account Creation + Login - Simulator
#
#
#               Author: Vinícius Aquino (aka. Aquinno)
#                
#                
#               OBS: It's a one time account, and one time Login, experience. You can create multiple accounts, but just Login once.
#               Feel free to make opinions and copy this code :D

import time
lista = [] #All accounts will be saved here
quest = 'y' #y will keep the loop, n will break
temp_list = dict() #Temporary dictionary to append to lista.
try_again = 1 #1 will keep the loop, 0 will break the loop
exist = 0 #Verify if and username is already in use.

print('-=-'*10)
print('Account Creation + Login - Simulator')
print('Author : Aquinno')
print('-=-'*10)

#Account Creation Step

while quest == 'y': 
    temp_list['Name'] = str(input("Name: "))
    temp_list['Nick'] = str(input("Username: "))
    for i in range(len(lista)): #Checking if the Username is already in use.
        if temp_list['Nick'] == lista[i]['Nick']:
            print("Username is already used")
            exist = 1
            continue
        else:
            exist = 0
    if exist == 1:
        continue
    else:
        temp_list['Pass'] = str(input("Password: "))
        while True: #A loop for Password Confirmation
            senha_c = str(input("Password confirmation:  "))
            if senha_c == temp_list['Pass']:
                break
            else:
                print("Passwords don't match!")
                continue
        lista.append(temp_list.copy())
        temp_list.clear()
        while True: #This loop exists only if someone input something != 'y' and != 'n'
            quest = str(input(("Create another account? [Y/N]"))).lower()
            if quest != 'y' and quest != 'n':
                print("Choose a valid option.")
                continue
            elif quest == 'n':
                break
            elif quest == 'y':
                break

#Login Step
print('-=-'*10)
print('---------LOGIN---------')
print('-=-'*10)
print(' ')

while try_again == 1:
    user_log = str(input("User: "))
    while True:
        senha_log = str(input("Password: "))
        for i in range(len(lista)): #Checking if Username is in lista[]
            if user_log in lista[i]['Nick']:
                id = i
                confirm_user = 1 #Saving that exists. But not showing any information about that
                break
            else:
                confirm_user = 0 #Saving that doesn't exists. But not showing any information about that
                continue
        if confirm_user == 0:
            print("User or Password are incorrect!")
            try_again = 1 #Keep on the loop
            break
        else:
            for i in range(len(lista)):
                if senha_log in lista[i]['Pass']:
                    confirm_pass = 1  #Saving that exists. But not showing any information about that
                    break
                else:
                    confirm_pass = 0 #Saving that doesn't exists. But not showing any information about that
                    continue
            if confirm_pass == 0: #If doesn't exists, will return to line 62
                print("User or Password are incorrect!")
                try_again == 1
                break
            else: #If exist, will check if the Username and Password are saved on the same person.
                if senha_log == lista[id]['Pass']:
                    try_again = 0 #Will break the loop when 'break'
                    time.sleep(1)
                    print(f"Welcome {lista[id]['Name']}!") #Confirmation that username and Password match
                    break 
                else:
                    print("User or Password are incorrect!") #Will break the loop and return to line 62
                    try_again == 1
                    break

time.sleep(2)
print("Thank you for your attention! I'm glad you tested.")
print(" -- Aquinno")                    