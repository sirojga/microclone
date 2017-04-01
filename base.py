import mysql.connector

class db:
    cfg = {'user': '','password': '','host': '',  'database': ''}
    connection= None
    def __init__(self, user, password, host, database):
        self.cfg['user']=user
        self.cfg['password']=password
        self.cfg['host']=host
        self.cfg['database']=database
    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.cfg)
        except mysql.connector.Error as err:
            return "can't connect to database with error: {}".format(err)
        if self.connection: return 'connection is established'
    def close(self):
        self.connection.close()
    def create_db(self, name):
        name='microclone'
        cursor=self.connection.cursor()
        try:
            cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(name))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
        self.connection.database=name
        tab = []
        tab.append(
    "CREATE TABLE IF NOT EXISTS`chem` ("
    "  `idchem` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `name` VARCHAR(45) NOT NULL DEFAULT '',"
    "  `amount` INT(10) UNSIGNED NOT NULL DEFAULT '0',"
    "  `date` DATE NULL DEFAULT NULL,"
    "  PRIMARY KEY (`idchem`),"
    "  UNIQUE INDEX `name_UNIQUE` (`name` ASC))"
    "  ENGINE=InnoDB")
        
        tab.append(
    "  CREATE TABLE IF NOT EXISTS `hormones` ("
    "  `idhormones` INT(10) NOT NULL AUTO_INCREMENT,"
    "  `name` VARCHAR(45) NOT NULL,"
    "  PRIMARY KEY (`idhormones`),"
    "  UNIQUE INDEX `name_UNIQUE` (`name` ASC))"
    "  ENGINE = InnoDB"
    "  AUTO_INCREMENT = 2")
    
        tab.append(
    "  CREATE TABLE IF NOT EXISTS `plant_gr` ("
    "  `id` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `name` VARCHAR(45) NOT NULL,"
    " PRIMARY KEY (`id`),"
    "UNIQUE INDEX `name_UNIQUE` (`name` ASC))"
    "  ENGINE = InnoDB"
    "  AUTO_INCREMENT = 2")

        tab.append(
    "CREATE TABLE IF NOT EXISTS `medium` ("
    "`medium_id` INT(10) NOT NULL AUTO_INCREMENT,"
    "`name` VARCHAR(45) NOT NULL,"
    "`plant_id` INT(11) NOT NULL,"
    "`horm_id` INT(11) NOT NULL,"
    "`ph` INT(11) UNSIGNED NOT NULL DEFAULT '0',"
    "PRIMARY KEY (`medium_id`),"
    "UNIQUE INDEX `name_UNIQUE` (`name` ASC),"
    "INDEX `fk_medium_1_idx` (`plant_id` ASC),"
    "INDEX `fk_medium_2_idx` (`horm_id` ASC),"
    "CONSTRAINT `fk_medium_1`"
    "   FOREIGN KEY (`horm_id`)"
    "   REFERENCES `hormones` (`idhormones`)"
    "   ON DELETE NO ACTION"
    "   ON UPDATE NO ACTION,"
    "CONSTRAINT `fk_medium_2`"
    "   FOREIGN KEY (`plant_id`)"
    "   REFERENCES `plant_gr` (`id`)"
    "   ON DELETE NO ACTION"
    "   ON UPDATE NO ACTION)"
    "ENGINE = InnoDB")
        
            
        tab.append(
        "CREATE TABLE IF NOT EXISTS `chem_medium` ("
        "`idmedium` INT(11) NOT NULL,"
        "`idchem` INT(11) NOT NULL,"
        "`amount` INT(11) NOT NULL DEFAULT '0',"
        "INDEX `fk_chem_medium_1_idx` (`idmedium` ASC),"
        "INDEX `fk_chem_medium_1_idx1` (`idchem` ASC),"
        "CONSTRAINT `fk_chem_medium_1`"
        "   FOREIGN KEY (`idchem`)"
        "   REFERENCES `chem` (`idchem`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION,"
        "CONSTRAINT `fk_chem_medium_2`"
        "   FOREIGN KEY (`idmedium`)"
        "   REFERENCES `medium` (`medium_id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")
        for x in tab:
            cursor.execute(x)   
#        tab.append(
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        "")
#        tab.append(
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        "")
#        tab.append(
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        "")
#        tab.append(
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        "")
#        tab.append(
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        ""
#        "")
#        
base=db('root', '903930', '127.0.0.1', 'connect') 
print(base.connect())
base.create_db('microclone')

