#!/usr/bin/env python3

import psutil
import socket
import emails
import sys

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=None)
    if cpu_percent > 80:
        return True

def check_disk_space():
    disk_usage = psutil.disk_usage("/")
    if disk_usage.percent > 80:
        return True

def check_memory():
    memory = psutil.virtual_memory()
    if memory.available < 100 * 1024 * 1024:  # 100MB
        return True

def check_hostname_resolution():
    try:
        resolved_ip = socket.gethostbyname("localhost")
        if resolved_ip != "127.0.0.1":
            return True
    except socket.gaierror:
        return True



def main(argv):
    
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."

    subjects_keys = ["CPU", "DISK", "RAM", "HOST"]

    subjects["CPU"] = "Error -CPU usage is over 80%"
    subjects["DISK"] = "Error -Available disk space is lower than 20%"
    subjects["RAM"] = "Error -Available memory is less than 100MB"
    subjects["HOST"] = "Error -hostname 'localhost' cannot be resolved to '127.0.0.1'"

    for i, subject in enumerate(subjects):
        print(i)
        print(subjects[i])
        print(subject)
        if  check_cpu_usage():
            message = emails.generate_error_report(sender, recipient, subjects["CPU"], body)
            print(message)
            emails.send(message)
        if check_disk_space():
            message = emails.generate_error_report(sender, recipient, subjects["DISK"], body)
            print(message)
            emails.send(message)
        if check_memory():
            message = emails.generate_error_report(sender, recipient, subjects["RAM"], body)
            print(message)
            emails.send(message)
        if check_hostname_resolution():
            message = emails.generate_error_report(sender, recipient, subjects["HOST"], body)
            print(message)
            emails.send(message)

if __name__ == "__main__":
  main(sys.argv)