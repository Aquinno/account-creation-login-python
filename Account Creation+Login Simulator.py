#Account Creation + Login - Simulator
#
#
#               Author: Vinícius Aquino (aka. Aquinno)
#                
#                
#               OBS: It's a script that creates credentials and use them to Sign-In. Using a DataFrame with a .CSV archive.
#               Feel free to make opinions and copy this code :D
import pandas as pd
import time

quest = 'y' #'y' will keep the loop, n will break
try_again = 1 #1 will keep the loop, 0 will break the loop
exist = 0 #Verify if and username is already in use.

print('-=-'*10)
print('Account Creation + Login - Simulator')
print('Author : Aquinno')
print('-=-'*10)

data = pd.read_csv('./data.csv')
df = pd.DataFrame(data)

#Account Creation Step
while True:
    sign = int(input("(1)Sign-In\n(2)Sign-Up?\n:"))
    if sign == 1:
        quest = 'n'
        break
    elif sign != 1 and sign != 2:
        print("Choose a valid option!")
        continue
    elif sign == 2:
        while quest == 'y': 
            temp_list = {} #Temporary dictionary to pd.concat() to DataFrame
            temp_list['Name'] = str(input("Name: "))
            temp_list['Nick'] = str(input("Username: "))
            if temp_list['Nick'] in df['Nick'].values:
                print("Username is already used")
                exist = 1
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
                temp_df = pd.DataFrame([temp_list])  # Create DataFrame from the temp_list
                df = pd.concat([df, temp_df], ignore_index=True)  # Concatenate the new DataFrame
                df.to_csv('./data.csv', index=False)
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
    user_log = str(input("User: "))  # Input Login User
    senha_log = str(input("Password: "))  # Input Login Password

    if user_log in df['Nick'].values:
        user_data = df[df['Nick'] == user_log].iloc[0]

        if user_data['Pass'].strip() == senha_log:
            print(f"Welcome {user_data['Name']}!")
            try_again = 0  # Just o get out from the loop
            time.sleep(1.5)
        else:
            print("User or Password are incorrect!")
            continue
    else:
        print("User or Password are incorrect!")
        continue



time.sleep(0.5)
print("Thank you for your attention! I'm glad you tested.")
print(" -- Aquinno")                    
