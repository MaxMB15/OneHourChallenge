#!/usr/bin/python

import cgi, cgitb, urllib2
from subprocess import call


"""get the input from the html file"""
form = cgi.FieldStorage()
inputString = form.getvalue('command')

"""get the current password"""
passF = open("controller.png", "r")
password = passF.readline()
passF.close()

"""COMMANDS:
RESET pass - Clear text doc with password
DOWN pass - Download text doc with password
REMOVE beginning of statement
COUNT
PASS opass npass
"""

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<center><h3>'

"""get the responses in a string array"""
compFile = open("data.txt", "r")
responses = compFile.read().split("~*(!)@\n")
responses = responses[:-1]
compFile.close()

if inputString.upper() == "RESET %s" %password.upper():
	tempFile = open("data.txt", "w")
	tempFile.close()
	print "All messages have been reset."
elif inputString.upper() == "DOWN %s" %password.upper():
	for i in range(len(responses)):
    		print("%s" %responses[i])
		print "<br><br>"
elif inputString.upper().startswith("REMOVE "):	
	matching = [s for s in responses if inputString[7:] in s]
	if len(matching) == 1:
		print "Removed: %s" %matching[len(matching)-1]
		responses.remove(matching[len(matching)-1])
		tempFile = open("data.txt", "w")
		for i in range(len(responses)-1):
			tempFile.write("%s~*(!)@\n" %responses[i])
		tempFile.close()
	elif len(matching) < 1:
		print "Nothing to remove with info."
	elif len(matching) > 1:
		print "Please be more specific. %d results found." %len(matching)
	else:
		print "ERROR!!!"
elif inputString.upper() == "COUNT":
	print len(responses)
elif inputString.upper().startswith("PASS %s " %password.upper()):
	splitArray = inputString.split(" ")
	if len(splitArray) > 3:
		print 'Sorry, invalid command.'
	else:
		tempFile = open("controller.png", "w")
		tempFile.write(splitArray[2])
		tempFile.close()
		print "Password has been successfully changed."
else:
	print 'Sorry, invalid command.'
print '</h3></center>'
print '</html>'