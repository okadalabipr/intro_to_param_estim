import os
import warnings
warnings.filterwarnings('ignore')

if not os.path.isdir('./figure'):
    os.mkdir('./figure')

from  param_estim.viz import visualize_simulations

if __name__ == '__main__':
    """=============================================================
    viz_type: 'best', 'average', 'original' or int(1~n_fitparam)
    show_all: bool
    stdev: bool (Only when viz_type == 'average')
    ================================================================"""
    visualize_simulations(viz_type='average',show_all=False,stdev=True)