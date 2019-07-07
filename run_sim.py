import os
import warnings
warnings.filterwarnings('ignore')

if not os.path.isdir('./Fig'):
    os.mkdir('./Fig')


from  src.viz import viz