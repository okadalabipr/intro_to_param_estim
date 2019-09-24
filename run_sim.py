import os
import warnings
warnings.filterwarnings('ignore')

if not os.path.isdir('./figure'):
    os.mkdir('./figure')

from  param_estim.viz import visualize_result

if __name__ == '__main__':
    visualize_result(viz_type='average',show_all=False,stdev=True)