The purpose of this CLI tool is to rearrange the tiles of a bitmap image generated from a NES CHRROM spritesheet into a visually intelligible format for editing. The code is a bit lazy, so it's only going to work for 8x16 spritesheets as-is. 

## USE
Rearrange the tiles for editing: `python sprite_remap.py remap "image_generated_from_CHRROM.bmp"`
Unarrange the tiles back into the original format: `python sprite_remap.py unremap "image_generated_from_CHRROM_output.bmp"`
