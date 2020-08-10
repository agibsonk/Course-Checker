from time import sleep
from random import uniform
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def CheckCourseOpen(courses, webdriver_path, checkforlec, checkforlab):
    """
    A function that will scrape current course availability
    No username or password is requried for the student services website
    """
    browser = webdriver.Chrome(webdriver_path)
    
    email_string = []
    
    for course in courses:
        #Navigate to the search page
        browser.get('https://studentservices.uwo.ca/secure/timetables/mastertt/ttindex.cfm')
        sleep(round(uniform(1,4), 2))
        
        #Select subject/deparment
        departmentElem = Select(browser.find_element_by_id("inputSubject"))
        departmentElem.select_by_visible_text(course[0])
        
        #Input course number
        courseElem = browser.find_element_by_id("inputCatalognbr")
        courseElem.send_keys(course[1])
        
        #Click search submit
        searchElem = browser.find_element_by_css_selector('#searchform > fieldset > div:nth-child(5) > div > button')
        searchElem.click()
        sleep(round(uniform(1,4), 2))
    
        #Now at results page
        foundCourse = browser.find_element_by_css_selector('body > div > div > div.span12 > h4').get_attribute("innerText")
        
        #Store collection of tr's in table of first course in results
        courseTable = browser.find_elements_by_css_selector("body > div > div > div.span12 > table > tbody > tr")
        #count how many offerings there are
        offerings = len(courseTable)
        
        openlec = False
        openlab = False
        #Iterates through each row, CSS starts at 1 index so need to add 1 and start from 1
        for row in range(1, offerings + 1):
            #Get the row
            offering = browser.find_element_by_css_selector(f"body > div > div > div.span12 > table > tbody > tr:nth-child({row})")
            #Extract data from row
            section = offering.find_element_by_css_selector("td:nth-child(1)").get_attribute("innerText")
            component = offering.find_element_by_css_selector("td:nth-child(2)").get_attribute("innerText")
            status = offering.find_element_by_css_selector("td:nth-child(10)").get_attribute("innerText")
            courseNumber = offering.find_element_by_css_selector("td:nth-child(3)").get_attribute("innerText")
              
            if checkforlec == True:
                if component == "LEC" and status == "Not Full":
                    email_string.append(f"{component} section {section} (course # {courseNumber}) in {foundCourse} is has open seats!")
                    openlec = True
                    
            if checkforlab == True:
                if component == "LAB" and status == "Not Full":
                    email_string.append(f"{component} section {section} (course # {courseNumber}) in {foundCourse} is has open seats!")
                    openlab = True
        
        #Just for testing if it found any open courses or labs
        #if openlec == False:
        #    print(f"no open {foundCourse} lectures found")
            
        #if openlab == False:
         #   print(f"no open {foundCourse} labs found")
            
    browser.quit()
    return(email_string)

#Have now gotten all info that we want to send into string

