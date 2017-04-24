import pickle
def cfg(host, port, log, pas):
    try:
        f=open('cfg.txt', 'wb')
        data={'host':host,
              'port':port,
              'login':log,
              'pass':pas}
        pickle.dump(data,f)
        return True
    except Exception as err:
        print(err)
        return False
    
def init_cfg(f):
    try:
        data=pickle.load(open('cfg.txt','rb'))
        return data
    except Exception as err:
        i=f()
        if cfg(host=i['host'],
               port=i['port'],
               log=i['login'],
               pas=i['pass'],)==False:
            prt_a()
            return False
        else:return i
    









