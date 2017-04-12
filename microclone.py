import pymysql
import tables
from tables import test as test
from tables import queries as q
class microclone:
    cfg = {'user': '','password': '','host': '', 'port': 0, 'bd':''}
    connection= None
    
    def __init__(self, user, password, host, port):
        self.cfg['user']=user
        self.cfg['password']=password
        self.cfg['host']=host
        self.cfg['port']=port
        
    def connect(self):
        try:
            self.connection = pymysql.connect(host=self.cfg['host'],
                                              port=self.cfg['port'], 
                                              user=self.cfg['user'], 
                                              passwd=self.cfg['password'],
                                              autocommit=True)
        except Exception as err:
            return "can't connect to database with error: {}".format(err)
        if self.connection: 
            return 'connection is established'

        
    def close(self):
        self.connection.close()
        self.connection=None

        
    def create(self):
        if self.connection==None:
            print("connection is not established")
            return -2
        self.cfg['bd']='microclone'
        name=self.cfg['bd']
        cursor=self.connection.cursor()
        try:
            cursor.execute('DROP DATABASE {};'.format(name))
        except Exception as err:
            print()
        try:
            cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(name))
        except Exception as err:
            print("Failed creating database: {}".format(err))
            return -1
        cursor=self.connection.cursor()
        self.connection.select_db(name)
       
        for x in tables.tab:
            cursor.execute(x)  
        print("base {} was created ".format(name))
        
    def get_id_by_name(self, table_name, name):
        try:
            a=None
            cursor=self.connection.cursor()
            cursor.execute("select id, name from {} where name= '{}';".format(table_name,name))
            a=[x for x in cursor][0][0]
        except Exception as err:
            print(err)
            return None
        cursor.close()
        return a
    
    def add_func(self, arr):
        try:
            cursor=self.connection.cursor()
            id1=self.get_id_by_name(arr['table1'],arr['table1_name'])
            id2=self.get_id_by_name(arr['table2'],arr['table2_name'])
            id_=id1+id2
            query = ("INSERT INTO `{}`(`id`,`{}`,`{}`,`amount`)"
                     "VALUES ('{}','{}','{}','{}');".format(arr['table_name'], arr['col_1'], arr['col_2'],
                                                           id_, id1, id2, arr['amount']))
            print(query)
            cursor.execute(query)
        except Exception as err:
            print(err)
        cursor.close()
        
    
    def print_q(self, query):
        cursor=self.connection.cursor()
        cursor.execute(query)
        arr=[[item[0] for item in cursor.description]]+[[str(col) for col in row]  for row in cursor]
        print(arr)
        
        arr1=[]
        for x in range(len(arr[0])):
            arr1.append(max([len(arr[y][x]) for y in range(len(arr))]))
        print('#'*(sum(arr1)+len(arr1)*2))
        for x in arr:
            
            for i in range(len(x)):
                print(x[i], ' '*(arr1[i]-len(x[i])), end='|')
            print("")
        print('#'*(sum(arr1)+len(arr1)*2))
        cursor.close()
        
    def add_chem(self, name, amount):
        try:
            cursor=self.connection.cursor()       
            cursor.execute("INSERT INTO `chem` (`name`) VALUES ('{}');".format(name))
            cursor.execute("INSERT INTO `chem_amount` (`chem_id`,`amount`,`date`)"
                           "VALUES ({},{},curdate());".format(self.get_id_by_name('chem',name),amount))
        except Exception as err:
                    print(err)
        cursor.close()

    def add_hormones(self, name, amount):
        cursor=self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `hormones` (`name`) VALUES ('{}');".format(name))
            name=self.get_id_by_name('hormones',name) 
            cursor.execute("INSERT INTO `hormones_amount` (`horm_id`,`amount`,`date`)"
                           "VALUES ({},{},curdate());".format(name,amount))
        except Exception as err:
            print(err)
        cursor.close()
            
    def add_plant_gr(self, name):
        cursor=self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `plant_gr` (`name`) "
                           "VALUES ('{}');".format(name))
        except Exception as err:
            print(err)
        cursor.close()

    def add_medium(self, name):
        cursor=self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `medium` (`name`)"
                           "VALUES ('{}');".format(name))
        except Exception as err:
            print(err)
        cursor.close()


    def add_chem_medium(self, medium, chem, amount):
        arr={'table1' : 'medium',
             'table1_name' : medium,
             'table2' : 'chem',
             'table2_name' : chem,
             'table_name' : 'chem_medium',
             'col_1' :'medium_id',
             'col_2' :'chem_id',
             'amount': amount }        
        self.add_func(arr)

    def add_pgr_chem(self, pgr, chem, amount):
        arr={'table1' : 'plant_gr',
             'table1_name' : pgr,
             'table2' : 'chem',
             'table2_name' : chem,
             'table_name' : 'chem_plant_gr',
             'col_1' :'pgr_id',
             'col_2' :'chem_id',
             'amount': amount }
        self.add_func(arr)


    def add_hormones_medium(self, hormones, medium, amount):
        arr={'table1' : 'hormones',
             'table1_name' : hormones,
             'table2' : 'medium',
             'table2_name' : medium,
             'table_name' : 'hormones_medium',
             'col_1' :'hormones_id',
             'col_2' :'medium_id',
             'amount': amount }
        self.add_func(arr)
        

    def add_plant_gr_medium(self, medium, plant_gr, amount):
        arr={'table1' : 'plant_gr',
             'table1_name' : plant_gr,
             'table2' : 'medium',
             'table2_name' : medium,
             'table_name' : 'plant_gr_medium',
             'col_1' :'plant_gr_id',
             'col_2' :'medium_id',
             'amount': amount }
        self.add_func(arr)
         
    def add_product(self,medium_name,amount,ph):
        cursor=self.connection.cursor()
        medium_name=self.get_id_by_name('medium',medium_name)
        cursor.execute("INSERT INTO `product` (`medium_id`,"
                       "`amount`,`date`,`ph`) VALUES ({},{},"
                       "curdate(),{});".format(medium_name,amount,ph))
        cursor.close()


        
    def join(self, qu):
        self.print_q(q[qu])

    def test(self):
        a=100
        for x in test['c']:
            self.add_chem(x,a)
            a+=10
        self.add_plant_gr('wpm_micro')
        a=10
        x=0
        for x in test['g2']:
            self.add_pgr_chem( 'wpm_micro',x,a)
            a+=1
        a=10
        for x in test['h']:
            self.add_hormones( x,a)
            a+=1
            
        self.add_plant_gr('wpm_makro')
        a=10
        x=0
        for x in test['g1']:
            self.add_pgr_chem( 'wpm_makro',x,a)
            a+=1
        self.add_plant_gr('ms_makro')
        a=10
        x=0
        for x in test['g3']:
            self.add_pgr_chem( 'ms_makro',x,a)
            a+=1
            
        def add_med(self, a):
            self.add_medium(a[0])
            self.add_plant_gr_medium(a[0],a[1],a[2])
            self.add_hormones_medium(a[3],a[0],a[4])
            self.add_chem_medium(a[0],a[5],a[6])
            self.add_chem_medium(a[0],a[7],a[8])
        
        add_med(self, test['m1'])

        self.add_product('A',666,4.6)
        self.add_product('A',777,4.7)

        
bd=microclone('root', '903930', '127.0.0.1',3306 )
print(bd.connect())

bd.connection.select_db('microclone')

bd.join("join_pgr")
##bd.join("join_horm")
##bd.join("join_medium")
##bd.join("join_product")
##bd.join_chem()
##bd.join_pgr()
##bd.add_plant_gr('ms_mikro')
##bd.add_chem('h2o', 111)
##bd.show('chem')
##bd.show('plant_gr')
##bd.add_chem('c2h5ohuy',666)
##bd.add_chem('c2h5ohuy',666)
##bd.add_pgr_chem( 'wpm', 'c2h5ohuy', 666)
##bd.add_pgr_chem( 'wpm', 'h2o', 111)
##bd.show('chem_plant_gr')
##bd.add_hormones('2ip',1)
##bd.show('medium')
##bd.add_chem_medium('huita','c2h5ohuy',666 );bd.show('chem_medium')
##bd.add_plant_gr_medium('huita','ms_mikro',123 );bd.show('plant_gr_medium')
bd.close()
