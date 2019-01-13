import json
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import io
import pylab
import os
import sys

## Usage: $python3 labelbox_generate_masks.py annotation_file image_output_dir mask_output_dir width_of_roads_in_pixels

## Getting Arguments -------------
if len(sys.argv) > 1:
    ann_file = sys.argv[1]
else:
    ann_file = 'latest.json'
if len(sys.argv) > 2:
    im_dir = sys.argv[2]
else:
    im_dir = 'Images'
if len(sys.argv) > 3:
    mask_dir = sys.argv[3]
else:
    mask_dir = 'Masks'
if len(sys.argv) > 4:
    width = sys.argv[4]
else:
    width = 25
##---------------------------------
        
ann = json.load(open(ann_file))

total_anns = len(ann)
for i in ann:
    if i['Label'] == 'Skip':
        total_anns -= 1
print('Total VALID annotations :', total_anns)

def get_points(points):
    points = points['geometry']
    pnts = np.zeros((len(points), 2), dtype=np.int32)
    for i in range(len(pnts)):
        pnts[i][0] = points[i]['x']
        pnts[i][1] = points[i]['y']
    
    return pnts.reshape((-1, 1, 2))

def get_mask(ann, shape, width=25):
    mask = np.zeros((shape[0], shape[1]))
    for i in ann['Label']['Roads']:
        cv2.polylines(mask, [get_points(i)], False, 255, width)
    return mask

def generate_data(ann, width, how_many=-1 ,im_dir='Images', mask_dir='Masks', suffix='mmi_', ext='.png'):
    count = 0
    mask_dir = 'Masks'
    im_dir = 'Images'
    suffix = 'mmi_'
    ext = '.png'
    if how_many != -1:
        ann = ann[:how_many]
    for i, sample in enumerate(ann, 1):
        if sample['Label'] == 'Skip':
            print('Skipped Image :',i)
            continue
        print('Downloading Image :', i)
        try:
	        img = io.imread(sample['Labeled Data'])
	    except:
	    	print('Problematic... Skippping')
	    	continue
        mask = get_mask(sample, img.shape, width)

        filename = suffix + str(count) + ext

        cv2.imwrite(os.path.join(mask_dir, filename), mask)
        cv2.imwrite(os.path.join(im_dir, filename), img[:,:,::-1])
        count += 1

    print('Downloaded Dataset Size :' count)
        

generate_data(ann, width, -1, im_dir, mask_dir)