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


def include(pyfile):
    if '.py' in pyfile:
        with open('../'+pyfile,'r',encoding='utf-8') as f:
            script = f.read()
            exec(script,globals())
    else:
        files = glob.glob('../'+pyfile)
        for file in files:
            include(file[len('../'):])


include('src/model/f_parameter.py')
include('src/model/f_variable.py')
include('src/model/differential_equation.py')
include('src/model/initial_condition.py')
include('src/experimental_data.py')
include('src/search_parameter.py')
include('src/simulation.py')
include('src/plot_func.py')
include('src/viz.py')