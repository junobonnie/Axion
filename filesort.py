# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 18:46:11 2021

@author: junob
"""
import os

def file_name_sort(file_list):
    result = sorted(file_list)
    return result

def file_creative_sort(file_list):
    result = sorted(file_list, key=os.path.getctime) # 파일 생성일
    return result
    
def file_access_sort(file_list):
    result = sorted(file_list, key=os.path.getatime) # 파일 최근 접근일
    return result
    
def file_modified_sort(file_list):
    result = sorted(file_list, key=os.path.getmtime) # 파일 최종 수정일
    return result

def file_size_sort(file_list):
    result = sorted(file_list, key=os.path.getsize, reverse=True) # 파일 사이즈로 정렬
    return result

import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

if __name__ == '__main__':
    import glob
    files = glob.glob('*')
    
    files = file_size_sort(files)
    for file in files:
        print(file, ': ', convert_size(os.path.getsize(file)))