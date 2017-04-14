
import os, microclone, getpass, sys
from microclone import base as base
def prt(item):
    m_txt={'main':
             'New product     :1\n'
             'Add new items   :2\n'
             'Show queries    :3\n'
             'Exit            :q\n',
              
           'select_db':
             'Select databse : 1\n'
             'Create new     : 2\n'
             'Exit           : q\n',
           
            'sel_db': '\nEnter name correct DB from list',
            'new_db': '\nEnter name new DB',
            'ak': '\nPress any key',
            'init':
             '\nTry again :any key\n'
               'Exit      :q\n',
           
           'add_prod': '\nEnter medium name, amoun(l) and pH\n',
                
        }
    print(m_txt[item])


def log_pass():
    print('Enter login : ',end='')
    log=input()
    print('\nEnter password : ',end='')
    pas=getpass.getpass()
    return {'log':log,
            'pass':pas}
def cls():print ("\n" * 100)
def prt_a(): prt('ak');input()

    
class menu():
    mn=None
    
    def __init__(self):
##        mn=base(l_p['log'],l_p['pass'],'127.0.0.1',3306)
        def init():
            l_p=log_pass()
            self.mn=base('root','903930','127.0.0.1',3306)
            a=self.mn.connect()
            if a==False:
                prt('init')
                i=input()
                if i=='q':sys.exit()
                else: init()
        init()
                
            
    def main_menu(self):
        self.select_db_items()
        self.select_menu_items()
        
    def select_db_items(self):
        cls()
        prt('select_db')
        i=input()
        if i=='1':self.select_db()
        elif i=='2':self.create_db()
        elif i=='q':sys.exit()
        else: self.select_db_items()
        
    def select_menu_items(self):
        cls()
        prt('main')
        i=input()
        if i=='1':self.new_product()
        elif i=='2':self.add_items()
        elif i=='3':self.show()
        elif i=='q':sys.exit()
        else: self.select_menu_items()
        
    def select_db(self):
        self.mn.show_db()
        prt('sel_db')
        a=self.mn.select_db(input())
        if a==False:

            self.select_db_items()
        
    def create_db(self):
        prt('new_db')
        self.mn.create(input())
        prt_a()
        self.select_db_items()
        
    def new_product(self):
        cls()
        self.mn.join("join_medium")
        prt('add_prod')
        n=input()
        a=input()
        ph=input()
        x=self.mn.add_product(n,a,ph)
        if x==False: prt_k()
        self.select_menu_items()
        
##    def add_items(self):
##    def show(self):



if __name__ == "__main__":
    m=menu()
    m.main_menu()
    
