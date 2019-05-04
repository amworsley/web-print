#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import subprocess

#message = 'XXXX'
#print "Content-Type: text/html\n"
#print """<html><body> <p>%s</p> </body></html> """ % cgi.escape(message, True)


form = cgi.FieldStorage()

cgitb.enable(display=1, logdir='/tmp/xxx')

# A nested FieldStorage instance holds the file
#(a, b, c) = form
#if 'file' in form:
#if form.has_key('file'):
#    fileitem = form['file']
#else:
#    fileitem = None
fileitem = form['file']

#print c, repr(form)
out = None
out_q = None
out_rot = None
rotate = False

if 'rotate' in form:
    rotate = True

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
            #upfn = '/scratch2/' + fn
            upfn = '/scratch/' + fn
            open(upfn, 'wb').write(fileitem.file.read())
            message = 'The file "' + fn + '" was uploaded successfully'
            if rotate:
                rotfile = upfn + "-rot90"
                out = subprocess.check_output(["pdf90", '--outfile', rotfile, upfn])
                message = message + "\n Rotated to " + rotfile
                os.rename(rotfile, upfn)
            #out = subprocess.check_output(["lpr", upfn])
            #out_q = subprocess.check_output(["lpq"])
            out = subprocess.check_output(["/usr/bin/lpr", upfn])
            out_q = subprocess.check_output(["/usr/bin/lpq"])
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
