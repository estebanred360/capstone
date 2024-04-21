import requests
import os, sys
from pathlib import Path

class supplyImage(object):
    def __init__(self):
        self.format_target_ = ".jpeg"
        self.testurl_ = "https://jsonplaceholder.typicode.com/todos"
        self.apiurl_ = "https://jsonplaceholder.typicode.com/todos"
        self.INPUT_DIR_ = "./data/supplier-data/images/"
        self.OUTCOME_DIR_ = "/workspaces/python/data/supplier-data/images/"
        return

    def get_filenames(self, path):
        '''
        Returns list of filenames in a path
        '''
        # os.path.join will add the trailing slash if it's not already there
        fileImages = [fileImage for fileImage in os.listdir(
           path) if (os.path.isfile(os.path.join(path, fileImage)) & (fileImage.endswith(self.format_target_)))]
        print("obtained files :" + str(fileImages))
        return fileImages

    def uploader(self, img_dir_path, result_format='list of PIL images'):
        fileImages = self.get_filenames(img_dir_path)
        print("List of images: " + str(fileImages))

        for f in fileImages:
            infile = os.path.join(img_dir_path, f)
            try:
                with open(infile, 'rb') as opened:
                    r = requests.post(self.testurl_, files={'file': opened})
                    print(r.status_code)
            except OSError:
                pass
        return

supplyImages = supplyImage()
supplyImages.uploader(img_dir_path=supplyImages.INPUT_DIR_, result_format=supplyImages.format_target_)