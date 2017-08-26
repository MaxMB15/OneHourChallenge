#!/usr/bin/python

import cgi, cgitb, urllib2
from subprocess import call


"""get the input from the html file"""
form = cgi.FieldStorage()
inputString = form.getvalue('MSG')

"""save it to a file"""
textFile = open("data.txt", "a")
textFile.write("%s\n" %inputString)
textFile.close

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<center><h3>'
print 'Your message has been sent. <3'
print '</h3></center>'
print '</html>'
