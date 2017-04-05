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
        a=None
        cursor=self.connection.cursor()
        cursor.execute("select id, name from {} where name= '{}';".format(table_name,name))
        try:
            a=[x for x in cursor][0][0]
        except Exception as err:
            print(err)
        cursor.close()
        return a

        
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
        cursor=self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `chem` (`name`) VALUES ('{}');".format(name))
        except Exception as err:
            print(err)
        cursor.execute("INSERT INTO `chem_amount` (`chem_id`,`amount`,`date`) VALUES ({},{},curdate());".format(self.get_id_by_name('chem',name),amount))
        cursor.close()
        

    def add_hormones(self, name, amount):
        cursor=self.connection.cursor()
        name=self.get_id_by_name('hormones',name)
        try:
            cursor.execute("INSERT INTO `hormones` (`name`) VALUES ('{}');".format(name))
        except Exception as err:
            print(err)
        cursor.execute("INSERT INTO `hormones_amount` (`horm_id`,`amount`,`date`) VALUES ({},{},curdate());".format(name,amount))
        cursor.close()

            
    def add_plant_gr(self, name):
        cursor=self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `plant_gr` (`name`) VALUES ('{}');".format(name))
        except Exception as err:
            print(err)
        cursor.close()

        
    def add_medium(self, name,plant_gr,ph,conc):
        cursor=self.connection.cursor()
        plant_gr=self.get_id_by_name('plant_gr',plant_gr)
        try:
            cursor.execute("INSERT INTO `medium` (`name`, `plant_id`, `ph`, `conc`) VALUES ('{}','{}','{}','{}');".format(name,plant_g,ph,conc))
        except Exception as err:
            print(err)
        cursor.close()


    def add_chem_medium(self, chem, medium, amount):
        cursor=self.connection.cursor()
        chem=self.get_id_by_name('chem',chem)
        medium=self.get_id_by_name('medium',medium)
        try:
            cursor.execute("INSERT INTO `chem_medium` (`medium_id`, `chem_id`, `amount`) VALUES ('{}', '{}', '{}');".format(medium,chem,amount))
        except Exception as err:
            print(err)
        cursor.close()


    def add_pgr_chem(self, pgr, chem, amount):
        cursor=self.connection.cursor()
        pgr=self.get_id_by_name('plant_gr',pgr)
        chem=self.get_id_by_name('chem',chem)
        try:
            cursor.execute("INSERT INTO `pgr_chem` (`id`,`pgr_id`, `chem_id`, `amount`) VALUES ('','{}', '{}', '{}');".format(pgr+chem,pgr,chem,amount))
        except Exception as err:
            print(err)
        cursor.close()

    def add_hormones_medium(self, hormones, medium, amount):
        cursor=self.connection.cursor()
        hormones=self.get_id_by_name('hormones',hormones)
        medium=self.get_id_by_name('medium',medium)
        try:
            cursor.execute("INSERT INTO `hormones_medium` (`id`, `hormones_id`, `medium_id`,`amount`) VALUES ('{}', '{}', '{}');".format(hormones+medium,hormones,medium,amount))
        except Exception as err:
            print(err)
        cursor.close()
        
    def add_product(self,medium_name,amount):
        cursor=self.connection.cursor()
        medium_name=self.get_id_by_name('medium',medium_name)
        cursor.execute("INSERT INTO `product` (`medium_id`,`amount`,`date`) VALUES ({},{},curdate());".format(medium_name,amount))
        cursor.close()
        

        
bd=microclone('root', '903930', '127.0.0.1',3306 )
print(bd.connect())
bd.connection.select_db('microclone')
bd.create()
##bd.add_plant_gr('wpm')
##bd.show('plant_gr')
##bd.add_medium('sasi','iba','wpm','666')
##bd.show('medium')
##bd.add_chem_medium('c2h5oh','sasi','777')
##bd.show('chem_medium')
##bd.close()
