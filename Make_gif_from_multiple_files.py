# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:37:22 2022

@author: Nusrat
"""

import os
import PIL
import numpy as np
directory = r"C:\Users\Nusrat\Desktop\Air_Quality_gif\CO_gas"
image_frames = []   
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".png"): 
         path1 = (os.path.join(directory, filename))
         new_frame = PIL.Image.open(path1)
         image_frames.append(new_frame)
         
         
image_frames[0].save(r'C:\Users\Nusrat\Desktop\Air_Quality_gif\CO_gas\animation\CO_gas.gif', format = 'GIF', 
            append_images = image_frames[1: ], 
            save_all = True, duration = 4, 
            loop = 0)
         