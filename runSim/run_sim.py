import os
import sys
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

if not os.path.isdir('./Fig'):
    os.mkdir('./Fig')


def include(src_file):
    src_dir = '../src/'
    if '.py' in src_file:
        with open(src_dir+src_file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(src_dir+src_file)
        for file in files:
            include(file[len(src_dir):])


include('model/f_parameter.py')
include('model/f_variable.py')
include('model/differential_equation.py')
include('model/initial_condition.py')
include('experimental_data.py')
include('search_parameter.py')
include('simulation.py')
include('plot_func.py')
include('viz.py')