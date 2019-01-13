# A Script to help fix polyline image segmentation annotations exported from www.labelbox.com

Labelbox is a popular and easy to use tool to make the labelling process streamlined across teams. My team was annotating certain images where we were drawing lines over roads in satellite images. When exporting these annotations from labelbox, we found that instead of leaving the roads as just lines with a specific thickness, labelbox's service exported them as closed figues. 

The script `labelbox_generate_masks.py` solves this issue. <br>
<br>
Note: You need to export your segmentations using the JSON option in the export UI on labelbox's website to get this to work.<br>

## Requirements
Matplotlib<br>
Numpy<br>
OpenCV<br>
Skimage<br>
Pylab<br>
Os<br>
Sys<br>
Json<br>

## Usage:
Usage: $python labelbox_generate_masks.py annotation_file image_output_dir mask_output_dir element_name width_of_roads_in_pixels<br>

*Defaults :*<br>
`annotation_file = 'latest.json'` (Name of the exported JSON file from labelbox)<br>
`image_output_dir = 'Images'` (Directory to output Images downloaded from labelbox)<br>
`mask_output_dir = 'Masks'` (Directory to output generated masks in png format)<br>
`element_name = 'Roads'` (Name of the element corresponding to which the annotations are to be generated - this has to be exactly the same as the name of the element setup on labelbox)<br>
`width_of_roads_in_pixels = 25` (Since the masks generated will only have lines, we need to specify their width)<br>

### Example:<br>
`python labelbox_generate_masks.py ann_file.json Img_output_dir Masks_output_dir 'Roads' 30`<br>

This will download all the images from labelbox and generate their corresponding annotations in the specified folders.
