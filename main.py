
import os, microclone, getpass, sys
from microclone import base as base
def prt(item):
    m_txt={'main':
             'New product     :1\n'
             'Add new items   :2\n'
             'Show queries    :3\n'
             'Exit            :q\n',
              
           'select_db':
             'Select databse :1\n'
             'Create new     :2\n'
             'Exit           :q\n',
           
            'sel_db': '\nEnter name correct DB from list',
            'new_db': '\nEnter name new DB',
            'ak': '\nPress enter',
            'init':
             '\nTry again :press enter\n'
               'Exit      :q\n',
           
           'add_prod': '\nEnter medium name, amount(l) and pH\n',
           'add_chem': '\nEnter reagent name and amount(mg)\n',
           'add_horm': '\nEnter hormone name and amount(mg)\n',
           'add_pgr': '\nEnter plant growth name\n',
           'add_pgr_n': '\nDo you want to modify this plant growth?\n',
           'add_med': '\nEnter medium name\n',
           'add_med_n': '\nDo you want to modify this medium?\n',
           'stop': '\nq     :stop\n'
                   'other :continue\n',
           
           'add_items':
             'Add reagent      :1\n'
             'Add hormone      :2\n'
             'Add plant growth :3\n'
             'Add medium       :4\n'
             'Go back          :5\n'
             'Exit             :q\n',
                
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
            self.mn=base(l_p['log'],l_p['pass'],'127.0.0.1',3306)
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
        

        
    def add_items(self):

        cls()
        prt('add_items')
        i=input()
        if i=='1':self.add('join_chem','add_chem',self.add_c,f=self.add_items)
        elif i=='2':self.add('join_horm','add_horm',self.add_h,f=add_items)
        elif i=='3':self.add_p()
        elif i=='4':self.add_m()
        elif i=='5':self.select_menu_items()
        elif i=='q':sys.exit()
        else: self.add_items()
        

    def add(self, _join, _prt, func, r=None, _join2=None,f=None):
            cls()
            print(_join2)
            if _join2 != None:_join2()
            self.mn.join(_join)
            prt(_prt)
            x=func()
            if x==False: prt_a()
            prt('stop')
            i=input()
            if i=='q':
                print("if1");
                if r==None: print("if2");input();f()
                else:print("if2else",r);input(); return
            else: print("if1else");input();self.add(_join,_prt,func,_join2)
            
    def add_c(self): 
        n=input()
        a=input()
        return self.mn.add_chem(n, a)
        
    def add_h(self):
        n=input()
        a=input()
        return self.mn.add_hormones(n, a)
        
    def add_p(self):
        self.mn.join('join_pgr')
        prt('add_pgr')
        n=input()
        if self.mn.add_plant_gr(n)== False :
            prt('add_pgr_n')
            prt('stop')
            i=input()
            if i=='q':self.add_items()
            
        self.add(_join='join_chem',
                 _join2= lambda name=n: self.mn.join('join_pgr_name',n),
                 _prt='add_chem',
                 func=lambda name=n: self.mn.add_pgr_chem(name,input(),input()))
                

        
        
    def add_m(self):
        self.mn.join('join_medium')
        prt('add_med')
        n=input()
        if self.mn.add_medium(n)== False :
            prt('add_med_n')
            prt('stop')
            i=input()
            if i=='q':self.add_items()
            
        self.add(_join='join_chem',
                 _join2= lambda name=n: self.mn.join('join_medium_name',n),
                 _prt='add_chem',
                 func=lambda name=n: self.mn.add_chem_medium(name,input(),input()),
                 r=False)
        
        self.add(_join='join_pgr',
                 _join2= lambda name=n: self.mn.join('join_medium_name',n),
                 _prt='add_pgr',
                 func=lambda name=n: self.mn.add_plant_gr_medium(name,input(),input()),
                 r=False)
        
        self.add(_join='join_horm',
                 _join2= lambda name=n: self.mn.join('join_medium_name',n),
                 _prt='add_horm',
                 func=lambda name=n: self.mn.add_hormones_medium(name,input(),input()),
                 f=self.self.add_items,
                 r=None)

    def new_product(self):
        self.add(_join='join_product',
                 _join2= lambda : self.mn.join('join_medium'),
                 _prt='add_prod',
                 func=lambda : self.mn.add_product(input(),input(),input()),
                 f=self.select_menu_items,
                 
                 r=None)
        
##        cls()
##        self.mn.join("join_medium")
##        self.mn.join("join_product")
##        prt('add_prod')
##        n=input()
##        a=input()
##        ph=input()
##        x=self.mn.add_product(n,a,ph)
##        if x==False: prt_a()
##        self.select_menu_items()

##    def show(self):



if __name__ == "__main__":
    m=menu()
    m.main_menu()
    
