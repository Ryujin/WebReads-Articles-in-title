from selenium import webdriver
import time
import os.path
import csv
from csv import writer
art = "A"
firstlet = "s"
#import library for handling dropdown menus
from selenium.webdriver.support.ui import Select
username = "PHILLBPH20"
password = "L@mplighter18"
# The line below can vary depending on where cmptr mounts USB stick:
driver = webdriver.Chrome(executable_path="F:\\chromedriver.exe")
driver.get("https://reads.nlstalkingbooks.org/WebREADS/")
main_page = driver.current_window_handle
select = Select(driver.find_element_by_name("ddlLibraries"))
select.select_by_visible_text("PA1A - Philadelphia")
driver.find_element_by_id("txtPatronId").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("txtPassword").send_keys(password)
# wait for Terms and Conditions to load
# click Log In button
time.sleep(1)
driver.find_element_by_id("btnLogIn").click()
#Give self time to manually click "Agree"...
time.sleep(3)
driver.get("https://reads.nlstalkingbooks.org/WebREADS/pageBooks.aspx")
time.sleep(2)
driver.find_element_by_id("aSC_header_Label49").click()
#from selenium.webdriver.common.action_chains import ActionChains
time.sleep(2)
from selenium.webdriver.common.keys import Keys
# Type in the string to search on:
driver.find_element_by_id("aSC_content_txtBSTitle").send_keys(art + " " + firstlet)
time.sleep(1)
driver.find_element_by_id("aSC_content_btnBSTitle").click()
time.sleep(3)
# Because there might be fewer than 25 results, hence no ‘Show’ dropdown
try:
   select = Select(driver.find_element_by_name("aSR_content$ddlShowResults"))
   select.select_by_visible_text("50")
   driver.find_element_by_id("aSR_content_gSR_ctl02_lnkBookID").click()
except:
   driver.find_element_by_id("aSR_content_gSR_ctl02_lnkBookID").click()
   time.sleep(2)
finally:
   time.sleep(3)
# Add the article in the dropdown
   select = Select(driver.find_element_by_name("apT_content$fT$ddlArticle"))
   select.select_by_visible_text(art)
# Copy the existing title entry
   theTitle = driver.find_element_by_name("apT_content$fT$txtTitle").get_attribute("value")
# Copy the book ID number as well:
   IDprefix = driver.find_element_by_name("apT_content$fT$txtMediaId").get_attribute("value")
   IDnum = driver.find_element_by_name("apT_content$fT$txtTitleId").get_attribute("value")
   bookID = IDprefix + " " + IDnum
# THIS IS WHERE WE COULD STOP EVERYTHING IF THERE'S AN INITIAL QUOTE
# And/or could avoid changing titles containing OTHER and STORIES, e.g.
# Log the title to a list!
   f = open("C:/Users/jensenr/Downloads/somefile.txt", "a")
   f.write("\n" + bookID + "  " + theTitle)
   f.close()
   with open ("C:/Users/jensenr/Downloads/WR_log.csv", "a", newline="") as csv_file:
      csv_writer = csv.writer(csv_file)
      csv_writer.writerow([bookID,theTitle])
# Empty the Title field
   titleBox = driver.find_element_by_name("apT_content$fT$txtTitle")
   titleBox.clear()
# Slice the article off the beginning of the Title field
   theTitle = theTitle.split(' ', 1)[1]
   time.sleep(2)
   driver.find_element_by_name("apT_content$fT$txtTitle").send_keys(theTitle)
# Hit the Update button and make it stick!
   driver.find_element_by_name("apT_content$btnUpdateTitle").click()
   time.sleep(2)
# Okay! All that works. Now to loop the process. Click Search Results and get the topmost
# title again; rinse & repeat. Try it with smaller sets (50 not 500) to see how to
# recursively go through longer lists, and what happens with they're all done.
#    span id="aSR_header_lblSearchResults" : gets the Search Results list
# THE BELOW IS ALMOST THERE BUT NOT QUITE:
   count = 0
   while count < 32:
      driver.find_element_by_id("aSR_header_lblSearchResults").click()
      try:
         time.sleep(2)
         select = Select(driver.find_element_by_name("aSR_content$ddlShowResults"))
         select.select_by_visible_text("50")
         driver.find_element_by_id("aSR_content_gSR_ctl02_lnkBookID").click()
      except:
         driver.find_element_by_id("aSR_content_gSR_ctl02_lnkBookID").click()
         time.sleep(2)
      finally:
         time.sleep(3)
      # Add the article in the dropdown
         select = Select(driver.find_element_by_name("apT_content$fT$ddlArticle"))
         select.select_by_visible_text(art)
      # Copy the existing title entry
         theTitle = driver.find_element_by_name("apT_content$fT$txtTitle").get_attribute("value")
      # Copy the book ID number as well:
      IDprefix = driver.find_element_by_name("apT_content$fT$txtMediaId").get_attribute("value")
      IDnum = driver.find_element_by_name("apT_content$fT$txtTitleId").get_attribute("value")
      bookID = IDprefix + " " + IDnum
   # THIS IS WHERE WE COULD STOP EVERYTHING IF THERE'S AN INITIAL QUOTE
   # And/or could avoid changing titles containing OTHER and STORIES, e.g.
   # Log the title to a list!
      f = open("C:/Users/jensenr/Downloads/somefile.txt", "a")
      f.write("\n" + bookID + "  " + theTitle)
      f.close()
      with open ("C:/Users/jensenr/Downloads/WR_log.csv", "a", newline="") as csv_file:
         csv_writer = csv.writer(csv_file)
         csv_writer.writerow([bookID,theTitle])
      # Empty the Title field
         titleBox = driver.find_element_by_name("apT_content$fT$txtTitle")
         titleBox.clear()
      # Slice the article off the beginning of the Title field
         theTitle = theTitle.split(' ', 1)[1]
         time.sleep(2)
         driver.find_element_by_name("apT_content$fT$txtTitle").send_keys(theTitle)
      # Hit the Update button and make it stick!
         driver.find_element_by_name("apT_content$btnUpdateTitle").click()
         count+=1
         time.sleep(3)

#action.pause(2000) #THIS DOES NOTHING
# A JS page does the login; button id is "tac-yes"
# That script is on https://reads.nlstalkingbooks.org/WebREADS/pageLogin.js
# Changing handles to access T&C page
#for handle in driver.window.handles:
#	if handle != main_page:
#		login_page = handle
#driver.switch_to_window(login_page)
#driver.find_element_by_id("\#tac-yes").click()
# The above doesn't work yet--but being able to send the Enter key would do it...
#from selenium.webdriver.common.action_chains import ActionChains
#driver.send_keys(Keys.ENTER)
#actions = ActionChains(self.driver)
#actions.send_keys(Keys.RETURN)
#actions.key_down(Keys.ENTER).perform()
#actions.perform()
#driver.find_element_by_id("tac-yes").send_keys(Keys.RETURN)

# This would probably click the Update button, were we in control of the browser:
#driver.find_element_by_id("apT_content_btnUpdateTitle").click()

#driver.get("https://reads.nlstalkingbooks.org/WebREADS/pagePatrons.aspx")
#select = Select(driver.find_element_by_name("hlMaterials"))
#select.select_by_visible_text("pageBooks.aspx")
#driver.find_element_by_id("pageBooks.aspx").click()
#This was used to shave the space off the RH side of article:
#   select.select_by_visible_text(art[:-1])
