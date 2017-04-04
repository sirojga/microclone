tab = []
tab.append(
    "CREATE TABLE IF NOT EXISTS`chem` ("
    "  `idchem` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `name` VARCHAR(45) NOT NULL DEFAULT '',"
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
        
tab.append(
        "CREATE TABLE IF NOT EXISTS `pgr_ch` ("
        "`pgr_id` INT(10) NOT NULL,"
        "`ch_id` INT(10) NOT NULL,"
        "`amount` INT(10) UNSIGNED NOT NULL,"
        "INDEX `fk_pgr_ch_1_idx` (`pgr_id` ASC),"
        "INDEX `fk_pgr_ch_2_idx` (`ch_id` ASC),"
        "CONSTRAINT `fk_pgr_ch_1`"
        "   FOREIGN KEY (`pgr_id`)"
        "   REFERENCES `plant_gr` (`id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION,"
        "CONSTRAINT `fk_pgr_ch_2`"
        "   FOREIGN KEY (`ch_id`)"
        "   REFERENCES `chem` (`idchem`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")
        
tab.append(
        "CREATE TABLE IF NOT EXISTS `product` ("
        "`idproduct` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,"
        "`Medium` INT(11) NULL DEFAULT NULL,"
        "`amount` INT(11) NULL DEFAULT NULL,"
        "`data` DATE NULL DEFAULT NULL,"
        "PRIMARY KEY (`idproduct`),"
        "INDEX `fk_product_1_idx` (`Medium` ASC),"
        "CONSTRAINT `fk_product_1`"
        "   FOREIGN KEY (`Medium`)"
        "   REFERENCES `medium` (`medium_id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")
        
tab.append(
        "CREATE TABLE IF NOT EXISTS `chem_amount` ("
        "`idtransaction` INT NOT NULL,"
        "`idchem` INT NOT NULL,"
        "`amount` INT NULL,"
        "PRIMARY KEY (`idtransaction`),"
        "INDEX `fk_chem_amount_1_idx` (`idchem` ASC),"
        "CONSTRAINT `fk_chem_amount_1`"
        "   FOREIGN KEY (`idchem`)"
        "   REFERENCES `microclone`.`chem` (`idchem`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")
