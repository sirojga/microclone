import pymysql
import tables

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
            cursor.execute(query)
        except Exception as err:
            print(err)
        cursor.close()
        
    
        
    def show(self, table_name):
        cursor=self.connection.cursor()
        cursor.execute("select * from {};".format(table_name))
        field_names = [ item[0] for item in cursor.description ]
        print('------',table_name,'--------')
        for field_name in field_names:
            print (field_name, "  ",  end ='')
        for row in cursor:
            print('')
            for col in row:
                print (str(col),'  ',   end='')
        print('\n--------------')
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
        

        
bd=microclone('root', '903930', '127.0.0.1',3306 )
print(bd.connect())
bd.connection.select_db('microclone')
bd.add_plant_gr('ms_mikro')
bd.add_chem('h2o', 111)
bd.show('chem')
bd.show('plant_gr')
bd.add_chem('c2h5ohuy',666)
bd.add_chem('c2h5ohuy',666)
bd.add_pgr_chem( 'wpm', 'c2h5ohuy', 666)
bd.add_pgr_chem( 'wpm', 'h2o', 111)
bd.show('chem_plant_gr')
bd.add_hormones('2ip',1)
bd.show('medium')
bd.add_chem_medium('huita','c2h5ohuy',666 );bd.show('chem_medium')
bd.add_plant_gr_medium('huita','ms_mikro',123 );bd.show('plant_gr_medium')
bd.close()
