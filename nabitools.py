# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 00:19:18 2021

@author: junob
"""
import glob
from PIL import Image
import numpy as np
import hashlib

def all_files_path(folders, recursives):
    files = []
    for i in range(len(folders)):
        if not folders[i] == '':
            if recursives[i]:
                files += glob.glob(folders[i] + '\**\*.*', recursive = True)
            else:
                files += glob.glob(folders[i] + '\*.*', recursive = False)
    return files

class Nabi:
    def __init__(self, img_size = (16, 16), color_rank = 16):
        self.img_size = img_size # resized img size setting
        
        self.color_rank = color_rank # color rank setting
        self.inverse_color_rank = 256//color_rank
        
        np.set_printoptions(threshold=img_size[0]*img_size[1], linewidth=np.inf) #numpy array setting
    
    def image_simplification(self, image_file_name):
        img = Image.open(image_file_name)
        img_resize = img.resize(self.img_size)
        img_gray = img_resize.convert('L')
        return np.array(img_gray)//self.inverse_color_rank
        
    def image_to_hash(self, image_file_name):
        simple_image = self.image_simplification(image_file_name)
        return hashlib.sha256(str(simple_image).encode()).hexdigest()

    def find_duplicate_images(self, files, func1 = print, func2 = print):
        duplicate_img_list = []
        img_hash_list = []
        count = 0
        for f in files:
            count += 1
            func1(count)
            try:
                img_hash = self.image_to_hash(f)
                for i in range(len(img_hash_list)):
                    if img_hash_list[i] == img_hash:
                        is_duplicate = False
                        for duplicate_img in duplicate_img_list:
                            if duplicate_img[0] == img_hash:
                                duplicate_img.append(f)
                                is_duplicate = True
                                break
                        if not is_duplicate:
                            duplicate_img_list.append([img_hash, files[i], f])
                        break
                img_hash_list.append(img_hash)
            except OSError as e:
                img_hash_list.append(None)
                func2('Error: ' + str(e))
                pass
        func2('Duplicate images list: ' + str(duplicate_img_list) + '\n\nDone!!')
        return duplicate_img_list

if __name__ == '__main__':
    import time
    nabi = Nabi()    
    
    folders = [r'C:\Users\junob\OneDrive\바탕 화면\\', r'D:\Media\사진\‍\위험물질\\']
    recursives = [True, False]
    
    files = all_files_path(folders, recursives)
    # files = glob.glob(r'D:\Programing\python_folder\파이썬\**\*.png', recursive = True)
    # files1 = glob.glob(r'D:\Media\사진\‍\위험물질\**\*', recursive = True)
    # files = glob.glob(r'C:\Users\junob\OneDrive\바탕 화면\**\*', recursive = True)
    
    start = time.time()
    duplicate_img_list = nabi.find_duplicate_images(files)
    print("time :", time.time() - start)
    # print(img_hash_list)
    print(duplicate_img_list)
    print(len(duplicate_img_list))
    # print(len(img_hash_list))