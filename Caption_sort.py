#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:21:49 2017

@author: ashish
"""

import numpy as np
import os
import sys
import shutil
import pandas as pd


test_ids=pd.read_csv('/home/ashish/Downloads/Files by Kshitij/test.csv',header=None);
train_ids=pd.read_csv('/home/ashish/Downloads/Files by Kshitij/train.csv',header=None);
validate_ids=pd.read_csv('/home/ashish/Downloads/Files by Kshitij/validate.csv',header=None);
#mixed_ids=pd.read_csv('/home/ashish/Downloads/captions.csv',header=None)

#mixed_ids=pd.read_csv('/home/ashish/Desktop/trial_lines.csv',header=None)


caption_id=['#0','#1','#2','#3','#4','#5','#6']
no_of_cap=0
found=False
new_ids=mixed_ids
with open('/home/ashish/Desktop/Validate_sorted.txt' ,'w') as Validate:
   for i in validate_ids.iteritems():        
                    avail_ids=len(validate_ids);   
                    k=0;
                    while(k<1000):
                        search_text=i[1][k]+caption_id[0]
                        
                        print('K: ',k)
                        l=0
                        avail_mixed_ids=len(mixed_ids)
                        while(avail_mixed_ids):
                           if search_text==mixed_ids.iloc[l,0]:
                                for j in range(5):
                                    Validate.write(mixed_ids.iloc[l+j][0]+','+mixed_ids.iloc[l+j][1]+'\n')
                                new_ids=new_ids.drop(new_ids.index[l:l+5])
                                mixed_ids.drop(mixed_ids.index[l:l+5],inplace=True)
                                avail_mixed_ids=len(mixed_ids)
                                l=0
                                break
                           l+=5
                        
                        k=k+1
                                
                          