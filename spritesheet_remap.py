# Cantersoft
# Rearranges the tiles in an image generated from an 8x16 NES CHRROM into a visually intelligible and adjacent format for editing; unarranges the tiles back into the original format.

# Rearrange a spritesheet:				python sprite_remap.py remap "image_generated_from_CHRROM.bmp"
# Unarrange into the original format:	python sprite_remap.py unremap "image_generated_from_CHRROM_output.bmp"	

import os
import sys
from enum import Enum
from PIL import Image

Modes = Enum('Modes', 'remap, unremap')
	
mode = sys.argv[1]
if mode == "remap":
	mode = Modes.remap
elif mode == "unremap":
	mode = Modes.unremap
else:
	mode = Modes.remap
	
image_filename = sys.argv[2]
image_filename_no_ext = os.path.splitext(image_filename)[0]

# Load the source image
src_img = Image.open(str(image_filename)).convert("RGB")

# Create a new image
dst_img = Image.new('RGB', (src_img.width, src_img.height))

if mode == Modes.remap:
	tile_height = 8
	tile_width = 16
elif mode == Modes.unremap:
	tile_height = 16	
	tile_width = 8

dst_x = 0
dst_y = 0

for y in range(0, src_img.height, tile_height):
	for x in range(0, src_img.width, tile_width):
		# Copy upper tile
		upper_tile = src_img.crop((x, y, x + 8, y + 8))
		# Copy lower tile
		if mode == Modes.remap:
			lower_tile = src_img.crop((x + 8, y, x + 16, y + 8))
			
		elif mode == Modes.unremap:
			lower_tile = src_img.crop((x, y + 8, x + 8, y + 16))
			
		# Paste upper tile
		dst_img.paste(upper_tile, (dst_x, dst_y))
		# Paste lower tile
		if mode == Modes.remap:
			dst_img.paste(lower_tile, (dst_x, dst_y + 8))
			dst_x += 8
		elif mode == Modes.unremap:
			dst_img.paste(lower_tile, (dst_x + 8, dst_y))
			dst_x += 16 

		# Wrap to next row
		if dst_x >= src_img.width:
			# Reset x paste position, now that we're on a new row
			dst_x = 0
			if mode == Modes.remap:
				dst_y += 16 
			elif mode == Modes.unremap:
				dst_y += 8  

# Save the result
dst_img.save(f"{image_filename_no_ext}_output.bmp")