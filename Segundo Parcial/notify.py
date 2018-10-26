import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

mailsender = 'asr4cm3@gmail.com'
password = 'redes34cm3'
mailreceip = 'olbrlvalbt@gmail.com'
mailserver = 'smtp.gmail.com: 587'

def sendAlertEmail(subject, img, rrd):
    """ Will send e-mail, attaching png
    files in the flist.
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip

    with open(img, 'rb') as f:
        part = MIMEApplication(f.read(), Name = basename(img))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(img)
        msg.attach(part)
    with open(rrd, 'rb') as f:
        part = MIMEApplication(f.read(), Name = basename(rrd))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(rrd)
        msg.attach(part)
    
    mserver = smtplib.SMTP(mailserver)
    mserver.starttls()
    mserver.login(mailsender, password)

    mserver.sendmail(mailsender, mailreceip, msg.as_string())
    mserver.quit()