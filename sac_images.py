"""
code adapted from the following source:
https://codereview.stackexchange.com/questions/199694/python-class-for-organizing-images-for-machine-learning
"""

from PIL import Image
import os, sys
from pathlib import Path

class sac_images(object):
    def __init__(self):
        self.new_img_resolution_ = 128, 128
        self.format_target_ = ".jpeg"
        self.theta_rot_ = 270
        self.INPUT_DIR_ = "./images"
        self.OUTCOME_DIR_ = "/opt/icons/"
        self.OUTCOME_DIR2_ = "/workspaces/python/images_outcome/"

    def get_filenames(self, path):
        '''
        Returns list of filenames in a path
        '''
        # os.path.join will add the trailing slash if it's not already there
        files = [file for file in os.listdir(
            path) if os.path.isfile(os.path.join(path, file))]
        """print("obtained files :" + str(files))"""
        return files

    def make_dir_if_needed(self, folder):
        '''
        Checks if a directory already exists and if not creates it
        '''
        if not os.path.isdir(folder):
            os.makedirs(folder)
    
    def scale_and_convert(self, img_dir_path, result_format='list of PIL images', new_size=0, rotation=0):
        """
        Convert an image using PIL applying the following:

        The images received are in the wrong format:
            .tiff format
            Image resolution 192x192 pixel (too large)
            Rotated 90° anti-clockwise

        The images required for the launch should be in this format:
            .jpeg format
            Image resolution 128x128 pixel
            Should be straight

        from_file: The image file that should be converted
        to_file: The file to save the image to
        """
        files = self.get_filenames(img_dir_path)
        path_out = self.make_dir_if_needed(self.OUTCOME_DIR2_)

        for file in files:
            infile = os.path.join(img_dir_path, file)
            try:
                with Image.open(infile) as im:
                    print(infile, im.format, f"{im.size}x{im.mode}")
                    """im.show()"""
                    if im.mode != "RGB":
                        #  Take out any Alpha or Palette mode
                        im = im.convert("RGB")
                    if new_size != 0:
                        im = im.resize(size=new_size)
                        # print(infile, im.format, f"{im.size}x{im.mode}")
                    if rotation != 0:
                        # im = im.rotate(angle=rotation)
                        im.transpose(Image.Transpose.ROTATE_270)
                        # print(infile, im.format, f"{im.size}x{im.mode}")
                    if result_format != str('list of PIL images'):
                        outfile = os.path.dirname(infile) + "/../"
                        # print("outfile :" + str(outfile))
                        outfile = os.path.normpath(outfile)
                        # print("outfile :" + str(outfile))
                        outfile = outfile + "/"  + str(self.OUTCOME_DIR_) + "/" + os.path.basename(infile) + str(result_format)
                        # print("outfile :" + str(outfile))
                        # print("infile path :" + str(os.path.dirname(infile)))
                        # print("outfile :" + str(outfile))
                        im.save(outfile, "JPEG")
                    if result_format == str('list of PIL images'):
                        outfile = str(self.OUTCOME_DIR2_)  + os.path.basename(infile)
                        im.save(outfile, "JPEG")
                        # print(outfile, im.format, f"{im.size}x{im.mode}")
            except OSError:
                pass

sac = sac_images()
image_path = sys.argv[1:]
# sac.scale_and_convert(img_dir_path=sac.INPUT_DIR_, result_format=sac.format_target_, new_size=sac.new_img_resolution_, rotation=sac.theta_rot_)
sac.scale_and_convert(img_dir_path=sac.INPUT_DIR_, result_format='list of PIL images', new_size=sac.new_img_resolution_, rotation=sac.theta_rot_)
