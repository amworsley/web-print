#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:
   
    # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('/scratch2/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
	  
else:
    message = 'No file was uploaded'
	    
print "Content-Type: text/html\n"
print """<html><body> <p>%s</p> </body></html> """ % cgi.escape(message, True)
