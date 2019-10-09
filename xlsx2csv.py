#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:34:15 2019

@author: Moacyr Rodrigues Neto
"""

import os
import pandas as pd
import sys


if len(sys.argv) != 3:
    print("\n {} <PATH> <FILE NAME> \n or \n {} <PATH> ALL\n"\
          .format(sys.argv[0], sys.argv[0]))
    sys.exit()
else:
    path_name = str(sys.argv[1])
    file_name = str(sys.argv[2])

if not path_name.endswith('/'):
    path_name += '/'


def xlsx2csv(path, file):
    input_file_name = path + file
    output_file_name = input_file_name.strip('.xlsx') + '.csv'
    df_temp = pd.read_excel(input_file_name)
    df_temp.to_csv(output_file_name, index=False)

if file_name.lower() == 'all':
    arquivos = os.listdir(path_name)
    for arquivo in arquivos:
        if arquivo.lower().endswith('.xlsx'):
            xlsx2csv(path_name, arquivo)
else:
    if file_name.lower().endswith('.xlsx'):
        xlsx2csv(path_name, file_name)

sys.exit()
