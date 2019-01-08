def myEnum(string):
    array = eval(string)

    path_w = './{}.py'.format(string)
    with open(path_w,mode='w',encoding='utf-8') as f:
        for i in range(len(array)):
            f.write('%s = %d\n'%(array[i],i))

    with open('./{}.py'.format(string), mode='r',encoding='utf-8') as f:
        s = f.read()

    exec(s,globals())

    os.remove('./{}.py'.format(string))
