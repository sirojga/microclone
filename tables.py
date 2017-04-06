tab = []
tab.append(
        "CREATE TABLE IF NOT EXISTS`chem` ("
        "  `id` INT(11) NOT NULL AUTO_INCREMENT,"
        "  `name` VARCHAR(45) NOT NULL DEFAULT '',"
        "  PRIMARY KEY (`id`),"
        "  UNIQUE INDEX `name_UNIQUE` (`name` ASC))"
        "  ENGINE=InnoDB")

        
tab.append(
        "  CREATE TABLE IF NOT EXISTS `hormones` ("
        "  `id` INT(10) NOT NULL AUTO_INCREMENT,"
        "  `name` VARCHAR(45) NOT NULL,"
        "  PRIMARY KEY (`id`),"
        "  UNIQUE INDEX `name_UNIQUE` (`name` ASC))"
        "  ENGINE = InnoDB")

tab.append(
        "  CREATE TABLE IF NOT EXISTS `plant_gr` ("
        "  `id` INT(11) NOT NULL AUTO_INCREMENT,"
        "  `name` VARCHAR(45) NOT NULL,"
        " PRIMARY KEY (`id`),"
        "UNIQUE INDEX `name_UNIQUE` (`name` ASC))"
        "  ENGINE = InnoDB")

tab.append(
        "CREATE TABLE IF NOT EXISTS `chem_amount` ("
        "`id` INT NOT NULL AUTO_INCREMENT,"
        "`chem_id` INT NOT NULL,"
        "`amount` INT NULL,"
        "`date` DATE NULL,"
        "PRIMARY KEY (`id`),"
        "INDEX `fk_chem_amount_1_idx` (`chem_id` ASC),"
        "CONSTRAINT `fk_chem_amount_1`"
        "   FOREIGN KEY (`chem_id`)"
        "   REFERENCES `microclone`.`chem` (`id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")

tab.append(
        "CREATE TABLE `hormones_amount` ("
        "  `id` INT NOT NULL AUTO_INCREMENT,"
        "  `horm_id` INT NOT NULL,"
        "  `amount` INT NOT NULL,"
        "  `date` DATE NOT NULL,"
        "  PRIMARY KEY (`id`),"
        "  INDEX `fk_hormones_amount_1_idx` (`horm_id` ASC),"
        "  CONSTRAINT `fk_hormones_amount_1`"
        "    FOREIGN KEY (`horm_id`)"
        "     REFERENCES `hormones` (`id`)"
        "     ON DELETE NO ACTION"
        "     ON UPDATE NO ACTION);")

tab.append(
        "CREATE TABLE IF NOT EXISTS `medium` ("
        "`id` INT(10) NOT NULL AUTO_INCREMENT,"
        "`name` VARCHAR(45) NOT NULL,"
        "`conc` FLOAT(11) NOT NULL,"
        "`ph` INT(11) UNSIGNED NOT NULL DEFAULT '0',"
        "PRIMARY KEY (`id`),"
        "UNIQUE INDEX `name_UNIQUE` (`name` ASC))"
        "ENGINE = InnoDB")

tab.append(
        "CREATE TABLE IF NOT EXISTS `plant_gr_medium` ("
        "  `id` INT(11) NOT NULL,"
        "  `plant_gr_id` INT(11) NOT NULL,"
        "  `medium_id` INT(10) NOT NULL,"
        "  `amount` INT(10) NOT NULL,"
        "  PRIMARY KEY (`id`),"
        "  INDEX `fk_plant_gr_medium_medium1_idx` (`medium_id` ASC),"
        "  INDEX `fk_plant_gr_medium_plant_gr1_idx` (`plant_gr_id` ASC),"
        "  CONSTRAINT `fk_plant_gr_medium_plant_gr1`"
        "    FOREIGN KEY (`plant_gr_id`)"
        "    REFERENCES `plant_gr` (`id`)"
        "    ON DELETE NO ACTION"
        "    ON UPDATE NO ACTION,"
        "  CONSTRAINT `fk_plant_gr_medium_medium1`"
        "    FOREIGN KEY (`medium_id`)"
        "    REFERENCES `medium` (`id`)"
        "    ON DELETE NO ACTION"
        "    ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")

tab.append(
        "CREATE TABLE IF NOT EXISTS `hormones_medium` ("
        "  `id` INT(10) NOT NULL,"
        "  `hormones_id` INT(10) NOT NULL,"
        "  `medium_id` INT(11) NOT NULL,"
        "  `amount` INT NOT NULL,"
        "  PRIMARY KEY (`id`),"
        "  INDEX `fk_hormones_medium_1_idx` (`hormones_id` ASC),"
        "  INDEX `fk_hormones_medium_2_idx` (`medium_id` ASC),"
        "  CONSTRAINT `fk_hormones_medium_1_idx`"
        "    FOREIGN KEY (`hormones_id`)"
        "    REFERENCES `hormones` (`id`)"
        "    ON DELETE NO ACTION"
        "    ON UPDATE NO ACTION,"
        "  CONSTRAINT `fk_hormones_medium_2_idx`"
        "    FOREIGN KEY (`medium_id`)"
        "    REFERENCES `medium` (`id`)"
        "    ON DELETE NO ACTION"
        "    ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")
        
tab.append(
        "CREATE TABLE IF NOT EXISTS `chem_medium` ("
	"`id` INT(11) NOT NULL,"
        "`medium_id` INT(11) NOT NULL,"
        "`chem_id` INT(11) NOT NULL,"
        "`amount` INT(11) NOT NULL DEFAULT '0',"
	"PRIMARY KEY (`id`),"
        "INDEX `fk_chem_medium_1_idx` (`medium_id` ASC),"
        "INDEX `fk_chem_medium_1_idx1` (`chem_id` ASC),"
        "CONSTRAINT `fk_chem_medium_1`"
        "   FOREIGN KEY (`chem_id`)"
        "   REFERENCES `chem` (`id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION,"
        "CONSTRAINT `fk_chem_medium_2`"
        "   FOREIGN KEY (`medium_id`)"
        "   REFERENCES `medium` (`id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")
        
tab.append(
        "CREATE TABLE IF NOT EXISTS `pgr_ch` ("
        "`id` INT(10) NOT NULL,"
        "`pgr_id` INT(10) NOT NULL,"
        "`chem_id` INT(10) NOT NULL,"
        "`amount` INT(10) UNSIGNED NOT NULL,"
	"PRIMARY KEY (`id`),"
        "INDEX `fk_pgr_ch_1_idx` (`pgr_id` ASC),"
        "INDEX `fk_pgr_ch_2_idx` (`chem_id` ASC),"
        "CONSTRAINT `fk_pgr_ch_1`"
        "   FOREIGN KEY (`pgr_id`)"
        "   REFERENCES `plant_gr` (`id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION,"
        "CONSTRAINT `fk_pgr_ch_2`"
        "   FOREIGN KEY (`chem_id`)"
        "   REFERENCES `chem` (`id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")

tab.append(
        "CREATE TABLE IF NOT EXISTS `product` ("
        "`id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,"
        "`medium_id` INT(11) NULL DEFAULT NULL,"
        "`amount` INT(11) NULL DEFAULT NULL,"
        "`date` DATE NULL DEFAULT NULL,"
        "PRIMARY KEY (`id`),"
        "INDEX `fk_product_1_idx` (`medium_id` ASC),"
        "CONSTRAINT `fk_product_1`"
        "   FOREIGN KEY (`medium_id`)"
        "   REFERENCES `medium` (`id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")

    
