#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import subprocess

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']
out = None
out_q = None

# Test if the file was uploaded
if fileitem.filename:
   
    # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    # Check file suffix
    suffix = fn.find('.')
    if suffix < 0:
        message = 'Missing file type (.txt .pdf .ps) in file "' + fn + '" '
    else:
        type = fn[suffix+1:].lower()
        if type == 'pdf' or type == 'ps' or type == 'txt':
            upfn = '/scratch2/' + fn
            open(upfn, 'wb').write(fileitem.file.read())
            message = 'The file "' + fn + '" was uploaded successfully'
            out = subprocess.check_output(["lpr", upfn])
            out_q = subprocess.check_output(["lpq"])
        else:
            message = 'Can not print %s - Printing files of type "%s" is not supported:"' % (fn, type)
else:
    message = 'No file was uploaded'
	    
print "Content-Type: text/html\n"
if out != None:
    print """<html><body> <p>%s</p> <p>%s</p> <p>%s</p> </body></html> """ % (
        cgi.escape(message, True), cgi.escape(out, True), cgi.escape(out_q, True)
        )
else:
    print """<html><body> <p>%s</p> </body></html> """ % cgi.escape(message, True)
