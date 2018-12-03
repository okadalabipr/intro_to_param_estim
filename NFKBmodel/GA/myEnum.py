def myEnum(string):
    array = eval(string)
    path_w = './{}.py'.format(string)
    with open(path_w,mode='w') as f:
        for i in range(len(array)):
            f.write('%s = %d\n'%(array[i],i))
    with open('./{}.py'.format(string), mode='r') as f:
        s = f.read()
    exec(s,globals())
    os.remove('./{}.py'.format(string))