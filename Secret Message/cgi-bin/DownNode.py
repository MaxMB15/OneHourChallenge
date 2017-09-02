#!/usr/bin/python

import cgi, cgitb, urllib2, random
from subprocess import call

"""get the input from the html file"""
form = cgi.FieldStorage()
StringNum = form.getvalue('Number')
onNum = int(StringNum)

"""get the responses in a string array"""
compFile = open("data.txt", "r")
responses = compFile.read().split("~*(!)@\n")
if len(responses) != 0:
	responses = responses[:-1]
compFile.close()

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<center><h3>%s</h3>' %responses[onNum]

if len(onNum)-1 != onNum:
	print '<form id="NodeTransfer" action="DownNode.py" method="POST">'
	print '<input name="nextNode" type="submit" value="Next">'
	print '<input name="Number" type="hidden" value="%s">' %(onNum+1)
	print '</form>'
print '</center>'
print '</html>'