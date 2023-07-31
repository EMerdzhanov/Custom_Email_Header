# Custom Email Header Script
This script allows sending emails with customized From, Reply-To, and To headers.

## Usage
The script takes custom sender, reply-to, and recipient addresses set in the variables:

```python
from_addr = "custom@sender.com"
reply_to = "noreply@custom.com" 
to_addr = "recipient@company.com"
```
It then constructs a message using the MIMEMultipart class and sets the custom headers:

```python
msg['From'] = from_addr
msg['Reply-To'] = reply_to
msg['To'] = to_addr
```

The message is sent by connecting to an SMTP server and calling sendmail.

## Disclaimer
This script is intended for educational purposes only. Sending emails with forged headers without permission may be against email provider terms of service. Make sure you have authorization to send on behalf of the domains used. Do not use this code for malicious purposes.

## Requirements
* Python 3
* smtplib module
* email modules (MIMEText, MIMEMultipart)

## Author
Emil T Merdzhanov