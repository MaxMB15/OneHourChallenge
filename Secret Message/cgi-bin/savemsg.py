import cgi, cgitb, urllib2
from subprocess import call


"""get the input from the html file"""
form = cgi.FieldStorage()
inputString = form.getvalue('MSG')

"""save it to a file"""
textFile = open("data.txt", "a")
textFile.write("Test\n")
textFile.close()