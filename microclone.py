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
                                                                     passwd=self.cfg['password'],)
        except Exception as err:
            return "can't connect to database with error: {}".format(err)
        if self.connection: 
            return 'connection is established'
        
    def close(self):
        self.connection.close()
        self.connection=None
    def create_db(self):
        if self.connection==None:
            print("connection is not established")
            return -2
        self.cfg['bd']='microclone'
        name=self.cfg['bd']
        cursor=self.connection.cursor()
        try:
            cursor.execute('DROP DATABASE {};'.format(name))
        except Exception:
            print('')
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
    def show(self, table_name):
        cursor=self.connection.cursor()
        cursor.execute('select * from {}'.format(table_name))
        field_names = [ item[0] for item in cursor.description ]
        for field_name in field_names:
            print (field_name, "  ",  end ='')
        for row in cursor:
            print('')
            for col in row:
                print (str(col),  end='')
bd=microclone('root', '903930', '127.0.0.1',3306 )
print(bd.connect())
bd.connection.select_db('microclone')
bd.show('chem')

