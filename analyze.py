#!/usr/bin/python
"""
SELECT t2.wafer_name, t1.x_coord, t1.y_coord, t4.short_description, t4.type FROM epi_cell t1 JOIN epi_wafer t2 ON (t1.wafer_id=t2.wafer_id) JOIN `epi_tag_meas` t3 ON (t1.id=t3.meas_id) JOIN epi_tag t4 ON (t3.tag_id=t4.id) AND t4.type IN('EL','Post-Dice','Pre-Dice')
scp -r iakbar@192.168.29.31:/var/www/html/behemoth/epi/attachments/Images/LC LC

then, just need these images
Post-Dice is:FC (121,764 = 3.5 GB)
Pre-Dice is:DC (35,585 = 1.1 GB)
EL is:LC (100,870 images = 2 GB)

12 possible categories:
No defects
Edge Cell
Small Stain
Broken Gridline
Scratched
Scuffed
ARC Bubbles
Resist Residues
Metal Spots
Broken Portion
Chipped
EL Spot
Dark Cell
"""
#import scikit-learn
#import pandas
#import numpy
#parallel?
#load CSV file into memory
#load images into memory
#spark?
#which image features to use
folders = {'Post-Dice':'FC','Pre-Dice':'DC','EL':'LC'}
from collections import defaultdict
image_defects = defaultdict(list)
defect_images = defaultdict(list)
try:
    f = open('ml_cell_defects.csv')
    #wafer name, x_coord, y_coord, description
    lines = f.readlines()
    for line in lines[1:]:# skip the first line, which is headers
        parts = line.split(';')
        wafer_name = parts[0][1:-1]
        x_coord = parts[1][1:-1]
        y_coord = parts[2][1:-1]
        defect = parts[3].rstrip()[1:-1]
        defect_type = parts[4].rstrip()[1:-1]
        #put into dict, key is image name, value is list of defects
        #image format is: C-706-2-A780-S_73515_25208.jpg
        if defect!='NULL':
            file_name = folders[defect_type] + '/' + wafer_name + '_' + x_coord + '_' + y_coord + '.jpg'
            image_defects[file_name].append(defect) # use defaultdict so when image with no tags is looked up, get an empty list of defects
            defect_images[defect].append(file_name) # for the reverse lookup
    f.close()
except:
    print 'file error'

def pre_process(image):
    """
    do all the pre-processing necessary to clean up the images
    """
    rotate_image(image)
    crop_image(image)
    
def rotate_image(image):
    """
    use line detector or canny edge detector to detect angle
    then rotate in opposite direction to undo
    """
    
def crop_image(image):
    """
    threshold the image first
    then get bounding box
    """
    
def train_model():
    """
    
    """