# Real-Time-Log-Monitoring-Alert-System
A Python-based real-time log monitoring tool that scans system logs (like `/var/log/auth.log`) for suspicious activity using regular expressions. On detection, it sends an email alert and shows a desktop notification. Designed for security automation and intrusion detection.

## Features
- **Real-time Log Monitoring:** Continuously watches system log files for new suspicious entries.
- **Regex-Based Matching:** Uses customizable patterns from `patterns.txt` for flexible detection.
- **Email Notifications:** Sends alert emails using Gmail SMTP configured in `config.ini`.
- **Desktop Notifications:** Triggers GUI pop-up alerts via `notify-send` for local awareness.
- **Logging to File:** Logs detected suspicious events to `suspicious_activity.log` for audit tracking.
- **Shell Script Integration:** Uses `alert.sh` to handle logging and alerting outside Python.
- **Custom Configuration:** Easily modify email settings, log paths, and check intervals in `config.ini`.

## Requirements
- **Python 3.6+** – Python version for running the scripts
- **Debian-based OS (Ubuntu, Kali Linux, etc.)** – Operating system on which the project is designed to work
- **SMTP Server Access** – Required for sending email alerts (e.g., Gmail SMTP server). **The script uses a Gmail account for sending emails.**
- **Python Libraries**:
  - **re** – Regular expression support
  - **smtplib** – For sending email alerts
  - **configparser** – For reading configuration files
  - **time** – For time-based operations (sleep intervals)
  - **subprocess** – For triggering external scripts like `alert.sh`
  - **email.mime.text** – For crafting the email body
- **Log File Access** – Access to system logs (e.g., `/var/log/auth.log`) for monitoring
- **Permissions** – Ensure proper file permissions for writing to the log file and executing scripts
- **Notify-send** – Desktop notifications (if running with GUI)
- **Mail Utilities (Optional)** – For sending system mails (requires `mailutils` package)

## Setup
1) Clone the repository using the following link:
   ```bash
   git clone https://github.com/rishit-047/Real-Time-Log-Monitoring-Alert-System.git

3) Edit the following values in `config.ini`:
   - sender=sender@gmail.com
   - receiver=receiver@gmail.com
   - password=abcdefghijklmnop - This is the App password (16-character), not your regular Google Account password

3) How to get an App Password for Gmail:
    - Go to your Google Account: `https://myaccount.google.com/)`.
    - On the left, click **Security**.
    - Under **"Signing in to Google"**, ensure **2-Step Verification** is turned on.
    - After enabling 2-Step Verification, you'll see an option for **App Passwords** or go back and search on the top **App Passwords**.
    - Select **App Passwords** and you may be prompted to sign in again.
    - Under **"Select app"**, choose **Mail**.
    - Under **"Select device"**, choose the device you're using (e.g., Windows, iPhone, etc.).
    - Click **Generate**.
    - A 16-character password will be shown. Copy this password.
    - Paste this app password in the `config.ini` file in place of the existing `password` value.

4) After cloning the repository, navigate into the project directory.  
You will find a file named `suspicious_activity.log`, which is used to record all detected suspicious activities such as failed login attempts. To ensure the script can write to this file, appropriate permissions must be set.  
Run the following command inside the project directory:
   ```bash
   chmod 664 suspicious_activity.log 

## Run the Application
- Run the script with the following command:
   ```bash
   python3 monitor.py

- The system will start monitoring your logs for suspicious activity, sending email alerts and triggering the alert system as defined in `alert.sh`.




