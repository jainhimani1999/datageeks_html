import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("jainhimani1999@gmail.com", "honeypagal@123gml")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("jainhimani1999@gmail.com", "intern3tgovernance@gmail.com", message)

# terminating the session
s.quit()
