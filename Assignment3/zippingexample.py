# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
first_item = []
second_item = []
cues = ['cue1'] * 50 + ['cue2'] * 50
imgs_f = ['face1.png'] * 5 + ['face2.png'] * 5 + ['face3.png'] * 5 + ['face4.png'] * 5 + ['face5.png'] * 5
imgs_h = ['house1.png'] * 5 + ['house2.png'] * 5 + ['house3.png'] * 5 + ['house4.png'] * 5 + ['house5.png'] * 5

first_item.extend(imgs_f)
first_item.extend(imgs_h)
first_item.extend(imgs_f)
first_item.extend(imgs_h)
print(first_item)
print(len(first_item))

imgs_fs = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 5
imgs_hs = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 5
second_item.extend(imgs_hs)
second_item.extend(imgs_fs)
second_item.extend(imgs_hs)
second_item.extend(imgs_fs)
print(second_item)
print(len(second_item))



catimgs = list(zip(first_item, second_item, cues))

np.random.shuffle(catimgs)
print(catimgs)