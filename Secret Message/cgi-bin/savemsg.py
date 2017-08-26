#!/usr/bin/python

import cgi, cgitb, urllib2
from subprocess import call


"""get the input from the html file"""
form = cgi.FieldStorage()
inputString = form.getvalue('MSG')
inputString = inputString + ''

"""save it to a file"""
textFile = open("data.txt", "a")
textFile.write("Test\n")
textFile.close

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '%s' %inputString
print '</html>'
