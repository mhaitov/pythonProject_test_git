import smtplib
from email.message import EmailMessage

smtp = smtplib.SMTP_SSL('smtp.zone.eu', 465)
smtp.login('python@mrartful.com', 'dsf342asda')

msg = EmailMessage()
msg['Subject'] = 'Sample mail sent by python'
msg['From'] = 'python@mrartful.com'
msg['To'] = 'haitovmarian@gmail.com'
msg.set_content('Sample email sent by Python')
msg.add_alternative("""
<!DOCTYPE html>
<html>
<body>
<h1 style="color: red";Hello this is header</h1>
<p style="color: blue";>This is first paragraph</h1>

""", subtype='html')


smtp.send_message()


