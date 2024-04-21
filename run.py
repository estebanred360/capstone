#! /usr/bin/env python3

import requests
import os, sys
import json
import re
from pathlib import Path


class runPOST(object):
    def __init__(self):
        self.format_target_ = ".txt"
        self.image_format_= ".jpeg"
        self.testurl_ = "https://jsonplaceholder.typicode.com/todos"
        self.apiurl_ = "https://jsonplaceholder.typicode.com/todos"
        self.INPUT_DIR_ = "./data/supplier-data/descriptions/"
        self.OUTCOME_DIR_ = "/workspaces/python/data/supplier-data/descriptions/"
        self.feedback_list = []
        return

    def get_filenames(self, inpath):
        '''
        Returns list of filenames in a path
        '''
        # os.path.join will add the trailing slash if it's not already there
        fileDescriptions = [fileDescription for fileDescription in os.listdir(
            inpath) if (os.path.isfile(os.path.join(inpath, fileDescription)) & (fileDescription.endswith("txt")))]
        print("file format :" + str(self.format_target_))
        print("obtained files :" + str(fileDescriptions))
        return fileDescriptions

    def feeding_dic(self, textfile):
        # dictionary keys and initialisation
        feedback_keys = ["name", "weight", "description", "image_name"]
        feedback_dic = {}
        print(feedback_keys)
        ext = self.image_format_
        infile = self.OUTCOME_DIR_ + str(textfile)

        with open(infile, "r") as f:
            print(f.name)
            for i, line in enumerate(f):
                print(i)
                print(feedback_keys[i])
                print(line)
                if  feedback_keys[i] == "name":
                    feedback_dic[feedback_keys[i]] = line.strip()
                elif feedback_keys[i] == "weight":
                    feedback_dic[feedback_keys[i]] = int("".join(char for char in line if char.isdigit()))
                elif feedback_keys[i] == "description":
                    feedback_dic[feedback_keys[i]] = line.strip()
            
        #if feedback_keys[i] == "image_name":
            filenm, _ = os.path.splitext(f.name)
            filenm = filenm.split("/")[-1]
            feedback_dic[feedback_keys[3]] = filenm + ext   
            print(feedback_dic[feedback_keys[3]])                 

        return feedback_dic

    def aggregatedPayload(self, savedico=True):
        feedback_files = self.get_filenames(self.INPUT_DIR_)
        print("List of text files: " + str(feedback_files))
        for file in feedback_files:
            print("file:" + file)
            dico = self.feeding_dic(file)
            self.feedback_list.append(dico)
        print(str(self.feedback_list))
        if savedico == True:
            with open('fruit_dico.jason', 'w') as dicofile:
                dico = self.feedback_list
                json.dump(dico, dicofile)
                dicofile.close()
        return self.feedback_list

    def postering(self):
        # fileDescriptions = self.get_filenames(self, descrip_dir_path)
        # print("List of descriptions: " + str(fileDescriptions))
        payload=self.aggregatedPayload()
        purl = self.testurl_
        for i, p in enumerate(payload):
            try:
                r = requests.post(url=purl, data=p)
                print(r.status_code)
                if r.ok:
                    print("New Customer review has been POSTED")
                else:
                    print('POST {} RESPONSE CODE ERROR'.format(r.status_code))
            except OSError:
                pass
        return


ran = runPOST()
print(ran.INPUT_DIR_)
ran.get_filenames(inpath=ran.OUTCOME_DIR_)
ran.aggregatedPayload()
ran.postering()





