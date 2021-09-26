# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:20:02 2021

@author: junob
"""
from nabi_tools import *
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count
import os
class Nabi_MP:
    def __init__(self):
        self.num_cores = cpu_count()
        self.result = list()
        
    def helper_function(self, nabis_files):
        duplicate_img_list = nabis_files[0].find_duplicate_images(nabis_files[1])
        self.result.append(duplicate_img_list)
        print(duplicate_img_list)
        print(str(os.getpid())+'\n')
        
    def main_function(self, nabis_files_list):
        pool = ThreadPool(self.num_cores)
        pool.map(self.helper_function, nabis_files_list)
        print(self.result)
    
if __name__ == '__main__':
    import time
    nabis = [Nabi(), Nabi((8,8)), Nabi((4,4)), Nabi((2,2))]
    files1 = all_files_path([r'D:\Media\사진\‍\위험물질\\'],[False])
    files2 = all_files_path([r'D:\Media\사진\‍\위험물질\\'], [True])
    files3 = all_files_path([r'D:\Media\사진\‍\위험물질\\'], [True])
    files4 = all_files_path([r'C:\Users\junob\OneDrive\바탕 화면\\'],[False])
    files_list = [files1, files2, files3, files4]
    nabis_files_list = list(zip(nabis, files_list))
    c = Nabi_MP()
    start = time.time()
    c.main_function(nabis_files_list)
    print("time :", time.time() - start)