# To extract the binary seg masks change dir to seg/FracAtlas/images/Fractured/
# then copy the file cp ../../Annotations/COCO\ JSON/COCO_fracture_masks.json
# Create folder inside images/Fractured and name it SegmentationMasks
# make sure to install pycocotools
# pip install pycocotools

import os
import cv2
import numpy as np
from pycocotools.coco import COCO

# Path to the COCO JSON file
coco_json_file = 'COCO_fracture_masks.json'

# Create a directory to store the binary segmentation masks
output_folder = 'SegmentationMasks'
os.makedirs(output_folder, exist_ok=True)

# Initialize the COCO object
coco = COCO(coco_json_file)

# Get the category ID for the desired class
category_name = 'fractured'  # Specify the desired class name
category_id = coco.getCatIds(catNms=[category_name])[0]

# Get all image IDs that have annotations for the desired class
image_ids = coco.getImgIds(catIds=[category_id])

# Iterate over the image IDs
for image_id in image_ids:
    # Load the image
    image_info = coco.loadImgs(image_id)[0]
    image_path = os.path.join(image_info['file_name'])
    image = cv2.imread(image_path)

    # Get the annotation IDs for the desired class in the current image
    annotation_ids = coco.getAnnIds(imgIds=[image_id], catIds=[category_id])

    # Create a blank mask image
    mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    # Iterate over the annotation IDs and draw the segmentation mask
    for annotation_id in annotation_ids:
        annotation_info = coco.loadAnns(annotation_id)[0]
        segmentation = annotation_info['segmentation'][0]
        polygon = np.array(segmentation).reshape((-1, 2)).astype(np.int32)
        cv2.fillPoly(mask, [polygon], color=255)

    # Save the binary mask image
    mask_filename = os.path.splitext(image_info['file_name'])[0] + '.png'
    mask_path = os.path.join(output_folder, mask_filename)
    cv2.imwrite(mask_path, mask)

    print(f'Saved binary mask image: {mask_path}')
