#! /usr/bin/env python3

import os
import requests
import csv

# directory holding feedback text files:
# fdbk_dir = "/workspaces/python/feedback/"
fdbk_dir = "./feedback/"

# create list of feedback text files:
# feeback_files = os.listdir("/workspaces/python/feedback/")
feeback_files = os.listdir("./feedback/")
print("feedback files:" + str(feeback_files))

def feeding_dic(textfile):
    # dictionary keys and initialisation
    feedback_keys = ["title", "name", "date", "feedback"]
    feedback_dic = {}
    
    with open(fdbk_dir + textfile, "r") as f:

        for i, line in enumerate(f):
            # print(feedback_keys[i])
            # print(line)
            feedback_dic[feedback_keys[i]] = line
    
    return feedback_dic

# list of feedbacks
feedback_list = []
for file in feeback_files:
    print("file:" + file)
    dico = feeding_dic(file)
    feedback_list.append(dico)
print(str(feedback_list))


# set host url:
url = "http://localhost/feedback/"
test_url = "http://127.0.0.1:8000/feedback/"

# POST - Customer reviews:
for payload in feedback_list:
    response = requests.post(url, data=payload)
    if response.ok:
        print("New Customer review has been POSTED")
    else:
        print('POST {} RESPONSE CODE ERROR'.format(response.status_code))
