#%%
with open('../src/parameter_estimation.py','r',encoding='utf-8') as f:
    script = f.read()
    exec(script,globals())
'''Parameter Estimation'''
ParamEstim()