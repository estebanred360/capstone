import psutil
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your email configuration
SMTP_SERVER = "your_smtp_server"
SMTP_PORT = 587
SMTP_USERNAME = "your_username"
SMTP_PASSWORD = "your_password"
FROM_EMAIL = "automation@example.com"
TO_EMAIL = "student@example.com"

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > 80:
        return f"Error - CPU usage is {cpu_percent:.2f}% (above 80%)."

def check_disk_space():
    disk_usage = psutil.disk_usage("/")
    if disk_usage.percent > 80:
        return f"Error - Disk space is {disk_usage.percent:.2f}% full (above 80%)."

def check_memory():
    memory = psutil.virtual_memory()
    if memory.available < 100 * 1024 * 1024:  # 100MB
        return "Error - Available memory is less than 100MB."

def check_hostname_resolution():
    try:
        resolved_ip = socket.gethostbyname("localhost")
        if resolved_ip != "127.0.0.1":
            return "Error - Hostname 'localhost' does not resolve to '127.0.0.1'."
    except socket.gaierror:
        return "Error - Hostname 'localhost' cannot be resolved."

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    while True:
        errors = []
        errors.append(check_cpu_usage())
        errors.append(check_disk_space())
        errors.append(check_memory())
        errors.append(check_hostname_resolution())

        error_messages = "\n".join(filter(None, errors))
        if error_messages:
            subject = "Case - System Alert"
            body = f"{error_messages}\n\nPlease check your system and resolve the issue as soon as possible."
            send_email(subject, body)

        # Wait for 60 seconds before checking again
        psutil.cpu_percent(interval=60)