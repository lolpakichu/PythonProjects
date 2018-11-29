import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print('Enter your email')
email = input('')

print('Enter your password')
password = input('')

server.login(email, password)

print('Enter your subject')
subject = input('')

print('Enter your message')
body = input('')

print('Enter the recipients email')
recipients = input('')

server.sendmail(email, recipients, body)
server.quit()