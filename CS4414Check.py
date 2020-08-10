import CourseCheck
import EmailSender

#Search info
searchCourses = [("Computer Science", "4414B")]
webdriver_path = "chromedriver.exe"
searchingforlec = True
searchingforlab = True

#Need to fill this in before running
myEmail = ""
myEmailPassword = ""
sendtoEmail = ""
emailSubject = f"results for {searchCourses}"


#Will return a list containing string explaining which lec/labs are open
courseOpenings = CourseCheck.CheckCourseOpen(searchCourses, webdriver_path, searchingforlec, searchingforlab)


#Check that open courses were found
if len(courseOpenings) > 0:
    #iterate through each string in list and add a newline to end of it
    emailBody = '\n'.join(str(p) for p in courseOpenings) 
    EmailSender.SendEmail(myEmail,myEmailPassword, sendtoEmail, emailSubject, emailBody)

