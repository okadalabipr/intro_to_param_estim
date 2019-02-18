#%%
with open('../src/simulation.py','r',encoding='utf-8') as f:
    script = f.read()
    exec(script,globals())

'''for Spyder
%run -i ../src/simulation.py
plt.savefig('./Fig/simResult.png',bbox_inches='tight')
plt.show()
'''