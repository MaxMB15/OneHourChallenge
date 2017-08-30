#!/usr/bin/python

import cgi, cgitb, urllib2, random
from subprocess import call


"""get the input from the html file"""
form = cgi.FieldStorage()
inputString = form.getvalue('MSG')

"""get the responses in a string array"""
compFile = open("data.txt", "r")
responses = compFile.read().split("~*(!)@\n")
if len(responses) != 0:
	responses = responses[:-1]
compFile.close()

"""add new response to array"""
responses.append(inputString)
random.shuffle(responses)

"""save it to a file"""
textFile = open("data.txt", "w")
for i in range(len(responses)):
    	textFile.write("%s~*(!)@\n" %responses[i])
textFile.close()

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<center><h3>'
print 'Your message has been sent. <3'
print '</h3></center>'
print '</html>'
