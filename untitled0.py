# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:52:33 2020

@author: jsia1
"""

import json
import os
from glob import glob
import functools
os.chdir('c:/work/Code/integrated_IAP_SDK')

#%%

jsonfiles=glob('json/*.json')
json_list=[]
for i in jsonfiles:
    with open(i) as f:
        json_list.append(json.load(f))
#%%

with open(jsonfiles[0]) as f:
    jsonload=json.load(f)
    
with open(jsonfiles[1]) as f:
    jsonload2=json.load(f)
    
#%%

def combine_dict(x, y):
    
    x['definitions'].update(y['definitions'])
    x['paths'].update(y['paths'])
    return x
#%%
combined_dict=functools.reduce(combine_dict, json_list)
#%%
combined_dict['paths']={i:combined_dict['paths'][i] for i in sorted(combined_dict['paths'].keys())}

#%%
combined_dict['info']['title']='IAP Services'
#%%
with open('IAP.json', 'wt') as f:
    json.dump(combined_dict, f)