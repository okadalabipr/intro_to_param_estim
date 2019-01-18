def name2idx(array):
    path_w = './tmp.py'
    with open(path_w,mode='w',encoding='utf-8') as f:
        for i in range(len(array)):
            f.write('%s = %d\n'%(array[i],i))

    with open('./tmp.py', mode='r',encoding='utf-8') as f:
        s = f.read()

    exec(s,globals())

    os.remove('./tmp.py')
