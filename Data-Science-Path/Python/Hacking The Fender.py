# PYTHON FUNDAMENTALS: Hacking The Fender

# 1. import the CSV module:
import csv
# 12. import json modulte:
import json
# 2. create a new list and save it to the variable compromised_users:
compromised_users = []
# 3. open up the file:
with open('passwords.csv') as password_file:
# 4. Pass the password_file object holder to  CSV reader for parsing:
    password_csv = csv.DictReader(password_file)
    # 5. Create a for loop and save each row of the CSV into the temporary variable password_row:
    for password_row in password_csv:
        # 6. inside your for loop, print out password_row['Username']. 
        # print(password_row[Username"])
        # 7. Remove the print statement.append the username to compromised_users:
        compromised_users.append(password_row["Username"])
# 8. open a file called compromised_users.txt in write-mode and save it as compromised_user_file:
with open("compromised.txt", "w") as compromised_user_file:    
    # 9. start a new for loop and iterate over each of compromised_users:
    for compromised_user in compromised_users:
    # .10 Write the username of each compromised_user in compromised_users to compromised_user_file: 
        compromised_user_file.write(compromised_user)
# 13. Open a new JSON file in write-mode called boss_message.json and save it as boss_message:
with open ("boss_message.json","w") as boss_message:
    # 14. Create a Python dictionary object within your with statement that relays a boss message:
    boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
# 15. Write a boss_message_dict to boss_message using json.dump():
    json.dump(boss_message_dict, boss_message)
# 16. open "new_passwords.csv" in write-mode and save it as new_passwords_obj:
with open ("new_passwords.csv", "w") as new_passwords_obj:
    # 17. Save the multiline string as slash_null_sig:
    slash_null_sig = """
    _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
# 18. Write slash_null_sig to new_passwords_obj:
new_passwords_obj.write(slash_null_sig)