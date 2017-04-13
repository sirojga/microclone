
import os, microclone
from microclone import base

_txt={'sel_db':'Please input correct database name',
       'new_db':'Do you want to create new database? y/n',
      'name_db':'Enter database name: ' }
_p={'add_c':'add new reagent'}

def l():
    print('Enter login : ',end='')
    log=input()
    print('\nEnter password : ',end='')
    pas=input()
    return {'login':log,
            'password':pas}
def c(db):
    
def menu():
    a=''
    while a!='q':
        aut=l()
        db=base(aut['login'],aut['password'],'127.0.0.1',3306) 
        connect=db.connect()
        if connect:
            print(_txt['new_db'])
            if input()=='y':
                print(_txt['name_db'])
                db.create(input())
            db.show_db()
            print(_txt['name_db'])
            db.select_db(input())
        else: print(connect)
        a=input()
if __name__ == "__main__":
    menu()
