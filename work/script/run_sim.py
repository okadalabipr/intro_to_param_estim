import os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

if not os.path.isdir('./Fig'):
    os.mkdir('./Fig')


def using(src_file):
    src_dir = '../src/'
    if '.py' in src_file:
        with open(src_dir+src_file,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob(src_dir+src_file)
        for file in files:
            using(file[len(src_dir):])


using('model/f_parameter.py')
using('model/f_variable.py')
using('model/differential_equation.py')
using('model/initial_condition.py')
using('experimental_data.py')
using('search_parameter.py')
using('simulation.py')
using('plot_func.py')
using('viz.py')
