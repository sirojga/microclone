import pickle
def cfg():
    try:
        f=open('cfg.txt', 'r')
    except Exception as err:
        print(err)
        f=open('cfg.txt', 'w')
        data=['host',
              '127.0.0.1',
              'port',
              3306]
        f.write(data)
    print(open('cfg.txt', 'r'))
    return{'host':open('cfg.txt', 'r').readlines()[1],
            'port':int(open('cfg.txt', 'r').readlines()[3])}
           
print(cfg())








