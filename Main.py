from appium import webdriver
import base64
import os
import time as t
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

desired_caps = {
  "platformName": "Android",
  "udid": "emulator-5554",
  "deviceName": "Android Emulator",
  "platformVersion": "11.0",
}

# Connecting to local server!
driver = webdriver.Remote( "http://127.0.0.1:4723/wd/hub", desired_caps )                                               

# Sending image from local computer to emulator!
d_p = "/storage/1112-150C/DCIM/Headspin.png"
driver.push_file( d_p, source_path = r"C:\Users\Manoj\Downloads\Headspin.png" )                                       
t.sleep(5)

# Launching google photos photos app!
os.system('adb shell "am start -n com.google.android.apps.photos/com.google.android.apps.photos.home.HomeActivity"')    
t.sleep(3)

# Eliminating update feature
try:
  driver.back()
  driver.tap([(847,1205)])
  t.sleep(1)
  driver.back()
  t.sleep(2)

except:
  t.sleep(1)


driver.orientation = "LANDSCAPE"
driver.tap([(180, 540)])                                                                                       # Image select
t.sleep(1)

driver.tap([(1010, 140)])                                                                                      # Tap to make icons appear                     

driver.find_element_by_id("com.google.android.apps.photos:id/photos_overflow_icon").click()                    # Click on 3-dots

location = driver.find_elements_by_id("com.google.android.apps.photos:id/label")[1].text                       # Retrive path

# location, d_p = 0 , 0

if location == d_p:
    print("You can continue!")
    driver.orientation = "PORTRAIT"

    os.system('adb shell monkey -p com.google.android.gm -c android.intent.category.LAUNCHER 1')               # Launch GMAIL
    t.sleep(1)

    # If Gmail is launching for the first time
    try:
      driver.find_element_by_id("com.google.android.gm:id/welcome_tour_got_it").click()                        # Got IT button
      t.sleep(1)

    # If not
    except:
      t.sleep(2)
      driver.find_element_by_id("com.google.android.gm:id/welcome_tour_skip").click()                          # Skip Button

    t.sleep(1)  
    driver.find_element_by_id("com.google.android.gm:id/setup_addresses_add_another").click()                  # Add an emailID
    
    t.sleep(1)
    driver.find_element_by_id("com.google.android.gm:id/account_setup_item").click()                           # Select Google                       
    driver.implicitly_wait(15)



'''
    # Keyevents!

    WebDriverWait( driver, 30 ).until( EC.presence_of_all_elements_located(  ) )
    alpha = { 
              "a":29, "b":30, "c":31, "d":32, "e":33, "f":34, "g":35, "h":36, "i":37, "j":38, "k":39, "l":40, "m":41, "n":42, "o":43, "p":44, 
              "q":45, "r":46, "s":47, "t":48, "u":49, "v":50, "w":51, "x":52, "y":53, "z":54, "0":186, "1":187, "2":188, "3":189, "4":190, 
              "5":191, "6":192, "7":193, "8":194, "9":195, "A":97, "B":98, "C":99, "D":100, "E":101, "F":102, "G":103, "H":104, "I":105, "J":106, 
              "K":107, "L":108, "M":109, "N":110, "O":111, "P":112, "Q":113, "R":114, "S":115, "T":116, "U":117, "V":118, "W":119, "X":120, 
              "Y":121, "Z":122, "@":77, ".":56 
            }
  '''
    
    
    # Initializing variables
    mailid_of_sender = "bhairamma1966"
    password = "PASSWORD"
    mailid_of_reciever = "keerthanaravikumarnaidu@gmail.com"

    # click on input user emailID
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View').click()  
    t.sleep(2)
    os.system(f'adb shell input text "{mailid_of_sender}"')                                                     # Enter EmailID
    # Click next button
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.widget.Button").click()
    
    # click on input password
    t.sleep(2)
    os.system(f'adb shell input text "{password}"')                                                             # Enter password

    # click next button
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.widget.Button").click()
    t.sleep(1)
    
    # click I agree button
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.widget.Button").click()
    t.sleep(2)
    
    # click More button
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
    t.sleep(0.5)
    
    # click Accept button
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
    t.sleep(5)
    
    driver.find_element_by_id("com.google.android.gm:id/action_done").click()                               # click to Take me to gmail
    driver.implicitly_wait(5)
    # driver.press_keycode(3)                                                                               # Press Home Screen Button / Middle Button
    
    # Click compose Mail
    driver.find_element_by_id("com.google.android.gm:id/compose_button").click()
    t.sleep(3)

    # Enter recipient mailID
    os.system(f'adb shell input text "{mailid_of_reciever}"')
    driver.find_element_by_id("com.google.android.gm:id/to").click()                                         # click on recipient mailID
    t.sleep(1)

    # click on attachment
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView").click()
    t.sleep(1)

    # click on paper clip icon
    driver.find_element_by_id("com.google.android.gm:id/add_attachment").click()
    t.sleep(1)

    # Click on Attach file
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView").click()
    t.sleep(10)

    # Select The Image
    try:
      titleList = driver.find_elements_by_id("android:id/title")
      for i in titleList:
        if i.text == "Headspin.png":
          print("Got it!")
          i.click()
    except:
      driver.find_elements_by_id("android:id/title")[2].click()


    # Send Mail
    driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Send"]').click()
    t.sleep(10)

    # Logout
    driver.find_element_by_id("com.google.android.gm:id/og_apd_ring_view").click()                          # Select account circle icon
    t.sleep(1)
    
    # Manage accounts button
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]").click()                                      
    
    # Select account to remove
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]").click()
    driver.find_element_by_id("com.android.settings:id/button").click()                                     # select remove account
    driver.find_element_by_id("android:id/button1").click()                                                 # confirm remove