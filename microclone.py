import pymysql
import tables
from tables import queries as q

class base:
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
            
            print( "can't connect to database with error: {}".format(err))
            return False
        if self.connection: 
            return True

        
    def close(self):
        self.connection.close()
        self.connection=None

        
    def create(self,name):
        if self.connection==None:
            print("connection is not established")
            return False
        cursor=self.connection.cursor()
        try:
            cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(name))
            self.connection.select_db(name)
            for x in tables.tab:
                cursor.execute(x)  
            print("base {} was created ".format(name))
        
        except Exception as err:
            print("Failed creating database: {}".format(err))
            return False

       
        
        
    def show_db(self):
        self.print_q('SHOW DATABASES')
        
    def check_tables(self):
        s={'chem_amount', 'chem', 'hormones_medium',
           'product', 'chem_medium', 'chem_plant_gr',
           'plant_gr_medium', 'hormones', 'hormones_amount',
           'medium', 'plant_gr'}

        return s==set([x[0] for x in self.rest('show_tables')])
    

    def select_db(self,name):
        try:
            self.connection.select_db(name)
            if self.check_tables()== False:
                print('Wrong database')
                return False
        except Exception as err:
            print(err)
            return False
        
    def get_id_by_name(self, table_name, name):
        try:
            a=None
            cursor=self.connection.cursor()
            cursor.execute("select id, name from {} where name= '{}';".format(table_name,name))
            a=[x for x in cursor][0][0]
        except Exception as err:
            if a==None:
                print('There is no item in table')
                return None
            print(type(err))
            return None
        cursor.close()
        return a
    
    def add_func(self, arr):
        try:
            cursor=self.connection.cursor()
            id1=self.get_id_by_name(arr['table1'],arr['table1_name'])
            id2=self.get_id_by_name(arr['table2'],arr['table2_name'])
<<<<<<< HEAD
=======

>>>>>>> 5908a4b4000c202921dd32ba546b7875db8a312b
            id_=int('1'+str(id1)+'2'+str(id2))
            query = ("INSERT INTO `{}`(`id`,`{}`,`{}`,`amount`)"
                     "VALUES ('{}','{}','{}','{}');".format(arr['table_name'], arr['col_1'], arr['col_2'],
                                                           id_, id1, id2, arr['amount']))

            cursor.execute(query)
        except Exception as err:
            print(err)
            return False
        cursor.close()
        
    
    def print_q(self, query=None, arr=None):
        if arr==None:
            cursor=self.connection.cursor()
            try:
                cursor.execute(query)
            except Exception as err:
                print(err)
                print(query)
                return False
            
            arr=[[item[0] for item in cursor.description]]+[[str(col) for col in row]  for row in cursor]
            cursor.close()
        arr1=[]
        _l=lambda x:x*(sum(arr1)+len(arr1)*2)
        
        for x in range(len(arr[0])):
            arr1.append(max([len(arr[y][x]) for y in range(len(arr))]))
        print(_l('#'))
        for x in arr:
            
            for i in range(len(x)):
                print(x[i], ' '*(arr1[i]-len(x[i])), end='|')
                
            print('')
            if x==arr[0]:print(_l('-'))
                
        print(_l('#'))
        
        
    def add_chem(self, name, amount):
        cursor=self.connection.cursor()          
        try:
            cursor.execute("INSERT INTO `chem` (`name`) VALUES ('{}');".format(name))            
        except Exception as err:
                    print(err)
        try:
             cursor.execute("INSERT INTO `chem_amount` (`chem_id`,`amount`,`date`)"
                           "VALUES ({},{},curdate());".format(self.get_id_by_name('chem',name),amount))
        except Exception as err:
                    print(err)
                    return False
        cursor.close()

    def add_hormones(self, name, amount):
        cursor=self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `hormones` (`name`) VALUES ('{}');".format(name))
        except Exception as err:
            print(err)

        try:
            name=self.get_id_by_name('hormones',name)
            cursor.execute("INSERT INTO `hormones_amount` (`horm_id`,`amount`,`date`)"
                           "VALUES ({},{},curdate());".format(name,amount))
        except Exception as err:
            print(err)
            return False
        cursor.close()
            
    def add_plant_gr(self, name):
        cursor=self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `plant_gr` (`name`) "
                           "VALUES ('{}');".format(name))
        except Exception as err:
            print(err)
            return False
        cursor.close()

    def add_medium(self, name):
        cursor=self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `medium` (`name`)"
                           "VALUES ('{}');".format(name))
        except Exception as err:
            print(err)
            return False
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


    def add_hormones_medium(self,medium, hormones,  amount):
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
        try:
            cursor=self.connection.cursor()
            medium_name=self.get_id_by_name('medium',medium_name)
            cursor.execute("INSERT INTO `product` (`medium_id`,"
                           "`amount`,`date`,`ph`) VALUES ({},{},"
                           "curdate(),{});".format(medium_name,int(amount),float(ph)))
        except Exception as err:
            print(err)
            return False
        cursor.close()

        
    def join(self, qu, name=None):
        if name!=None: return self.print_q(q[qu].format(name))
        return self.print_q(q[qu])
    
    def rest(self, qu):
        query=q[qu]
        cursor=self.connection.cursor()
        try:
            cursor.execute(query)
        except Exception as err:
            print(err)
            return False
        
        return [[str(col) for col in row]  for row in cursor]
    
    
    def rest_c(self):
        arr=lambda t1,t2:[[y[1],int(y[2])*int(x[1])] for y in self.rest(t2) for x in self.rest(t1) if y[0]==x[0]]
        arr2=lambda t1,t2:[[y[1],int(y[2])*int(x[1])/100] for y in self.rest(t2) for x in self.rest(t1) if y[0]==x[0]]
        arr3=lambda arr,t2:[[y[1],int(y[2])*x[1]] for y in self.rest(t2) for x in arr if y[0]==x[0]]

        medium_c=arr('sum_p','sum_mc')
        p=arr2('sum_p','sum_mp')

        chemicals=self.rest('rest_c')
        plant_c=arr3(p,'sum_pc')
        for x in medium_c:
            for y in plant_c:
                if y[0]==x[0]:y[1]+=x[1];continue

        for x in chemicals:
            x.append(int(x[2]))
            for y in plant_c:
                if x[0]==y[0]:x[3]-=y[1]
            x[3]=str(x[3])

        self.print_q(arr=[['id','reagent','amount','rest']]+chemicals)
        
    def rest_h(self):
        hormones=self.rest('rest_h')
        for x in hormones:
            x.append(int(x[2]))
            for y in [[y[1],int(y[2])*int(x[1])] for y in self.rest('sum_mh') for x in self.rest('sum_p') if y[0]==x[0]]:
                if x[0]==y[0]:x[3]-=y[1]
            x[3]=str(x[3])
        self.print_q(arr=[['id','horm','amount','rest']]+hormones)

if __name__ == "__main__":

    bd=base('root', '903930', '127.0.0.1',3306)
    print(bd.connect())

    bd.connection.select_db('microclone')


    print(bd.check_tables())

    bd.close()
