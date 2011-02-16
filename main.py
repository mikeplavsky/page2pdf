from PySide.QtWebKit import *
from PySide.QtCore import *
from PySide.QtGui import *

import sys

if len( sys.argv ) < 2:

    print "usage: python.exe main.py <url> <file>"
    sys.exit(-1)

app = QApplication( "webkit" )
web = QWebView()

print "loading: ", sys.argv[1] 

web.load(QUrl(sys.argv[1]))

def loaded(res):    
    
    print "page loaded: ", res
        
    if res: 
    
        prn = QPrinter()
    
        prn.setOutputFormat(QPrinter.PdfFormat)    
        prn.setOutputFileName( sys.argv[2] )
    
        page.mainFrame().print_(prn)   
    
    app.exit() 
    
def finished(res):

    if res.errorString() == "Unknown error":
        print res.url().toString()
    else:
        print res.errorString()
        
page = web.page()
net = page.networkAccessManager()

net.finished.connect( finished )    
page.loadFinished.connect(loaded)

app.exec_()
