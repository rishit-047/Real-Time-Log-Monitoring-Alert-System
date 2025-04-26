import re
import smtplib
import configparser
import time 
import subprocess
from email.mime.text import MIMEText

# Loading configuration from config.ini
config= configparser.ConfigParser()
config.read('config.ini')

# Extract the values from config.ini file 
sender_email= config['Email']['sender']
receiver_email= config['Email']['receiver']
smtp_server= config['Email']['smtp_server']
smtp_port= int(config['Email']['smtp_port'])
password= config['Email']['password']
log_file= config['Monitor']['log_file']
check_interval= int(config['Monitor'].get('check_interval',5)) # if check_interval is somehow missed in config.ini, it will take the value as 5
email_subject= config['Alert'].get('subject', "Suspicious Activity Detected")

# Loading regex patterns form the patterns.txt
with open('patterns.txt', 'r') as f:
	patterns = [
		re.compile(line.strip())
		for line in f
		if line.strip() and not line.strip().startswith('#') 
	]

# Sending email alert 
def send_email(message):
	msg= MIMEText(message) # Setting the email body 
	msg['Subject']= email_subject # Setting the email suject 
	msg['From']= sender_email 
	msg['To']= receiver_email
	
	# Connecting to gmail's SMTP server securely 
	with smtplib.SMTP(smtp_server, smtp_port) as server:
		server.starttls() # Upgrade to secure connection 
		server.login(sender_email, password) # Logging using sender email + app password
		server.send_message(msg) # Sending the email
		
def trigger_alert_script(message):
	try:
		subprocess.run(["./alert.sh", message], check=True)
	except Exception as e:
		print(f"alert.sh failed: {e}")
		
def monitor_log():
	print(f"Monitoring {log_file} for suspicious activity....")
	with open(log_file, 'r') as f:
		f.seek(0, 2)
		
		while True:
			line= f.readline()
			
			if not line:
				time.sleep(check_interval)
				continue
			
			for pattern in patterns:
				if pattern.search(line):
					print(f"Suspicious activity found: {line.strip()}")
					send_email(f"Suspicious activity detected : \n\n{line}")
					trigger_alert_script(line.strip())
					break
					
if __name__ == "__main__":
	try:
		monitor_log()
	except KeyboardInterrupt:
		print("\n Monitoring stopped by user. ")
		
