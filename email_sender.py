import smtplib
from email.utils import formataddr 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Custom From address
from_name = "John Doe"
from_email = "john@customcompany.com"
from_addr = formataddr((from_name, from_email)) 

# Custom Reply-To
reply_to = "noreply@customcompany.com"

# Send To address
to_addr = "sender@email.com" #recipient's email goes here

msg = MIMEMultipart() 

# Set custom headers
msg['From'] = from_addr
msg['Reply-To'] = reply_to
msg['To'] = to_addr
msg['Subject'] = "Email subject goes here"

body = "Email dody goes here"
msg.attach(MIMEText(body, 'plain'))

# Print formatted message  
print(msg.as_string()) 

# Connect to SMTP server 
smtp_server = smtplib.SMTP('smtp.mail.com', 587) #obtain credentials from your smpt provider
smtp_server.starttls()
smtp_server.login('yourmail@mail.com','usernam/api') #obtain credentials from your smpt provider

# Send mail
smtp_server.sendmail(from_addr, to_addr, msg.as_string())
smtp_server.quit()