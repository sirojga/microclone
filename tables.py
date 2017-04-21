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
        "CREATE TABLE IF NOT EXISTS `chem_plant_gr` ("
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
        "`ph` FLOAT(11) NOT NULL DEFAULT '0',"
        "`date` DATE NULL DEFAULT NULL,"
        "PRIMARY KEY (`id`),"
        "INDEX `fk_product_1_idx` (`medium_id` ASC),"
        "CONSTRAINT `fk_product_1`"
        "   FOREIGN KEY (`medium_id`)"
        "   REFERENCES `medium` (`id`)"
        "   ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB")

queries={"join_chem":"SELECT chem.id, chem.name, chem_amount.amount, chem_amount.date "
                     "FROM chem "
                     "INNER JOIN chem_amount on chem.id=chem_amount.chem_id "
                     "ORDER BY chem.id ASC",
         
         "join_pgr":"SELECT plant_gr.id, plant_gr.name, "
                     "CONCAT (chem.name,' : ' ,chem_plant_gr.amount)as 'reagents mg/l' "
                     "FROM plant_gr "
                     "INNER JOIN chem_plant_gr ON chem_plant_gr.pgr_id=plant_gr.id "
                     "INNER JOIN chem ON chem_plant_gr.chem_id=chem.id  "
                     "ORDER BY plant_gr.id ASC",

         
         "join_pgr2":"SELECT plant_gr.id, plant_gr.name, "
                     "GROUP_CONCAT(DISTINCT chem.name, ' : ', chem_plant_gr.amount ORDER BY plant_gr.name ASC SEPARATOR ', ' )as 'reagents mg/l' "
                     "FROM plant_gr "
                     "INNER JOIN chem_plant_gr ON chem_plant_gr.pgr_id=plant_gr.id "
                     "INNER JOIN chem ON chem_plant_gr.chem_id=chem.id  "
                     "GROUP BY plant_gr.id;",
         
         "join_pgr_name":"SELECT plant_gr.id, plant_gr.name, chem.name as chem_name, chem_plant_gr.amount "
                         "FROM plant_gr "
                         "INNER JOIN chem_plant_gr ON chem_plant_gr.pgr_id=plant_gr.id "
                         "INNER JOIN chem ON chem_plant_gr.chem_id=chem.id  "
                         "WHERE plant_gr.name='{}' "
                         "ORDER BY plant_gr.id ASC",
         
         "join_horm":"SELECT hormones.id, hormones.name, hormones_amount.amount,hormones_amount.date "
                     "FROM hormones "
                     "INNER JOIN hormones_amount ON hormones_amount.horm_id=hormones.id "
                     "ORDER BY hormones.id ASC",
         
         "join_medium":"SELECT medium.id, medium.name,  "
                        "GROUP_CONCAT(DISTINCT plant_gr.name,': ', plant_gr_medium.amount ORDER BY plant_gr.name ASC SEPARATOR ', ' )as pgrs, "
                        "GROUP_CONCAT(DISTINCT hormones.name,': ', hormones_medium.amount ORDER BY hormones.name ASC SEPARATOR ', ' )as horms, "
                        "GROUP_CONCAT(DISTINCT chem.name,': ', chem_medium.amount ORDER BY chem.name ASC SEPARATOR ', ' )as chems " 
                        "FROM medium "
                        "INNER JOIN plant_gr_medium ON plant_gr_medium.medium_id=medium.id "
                        "INNER JOIN plant_gr ON plant_gr_medium.plant_gr_id=plant_gr.id "
                        "INNER JOIN hormones_medium ON hormones_medium.medium_id=medium.id "
                        "INNER JOIN hormones ON hormones_medium.hormones_id=hormones.id "
                        "INNER JOIN chem_medium ON chem_medium.medium_id=medium.id "
                        "INNER JOIN chem ON chem_medium.chem_id=chem.id "
                        "GROUP BY medium.id;",
         
        "join_medium_name":"SELECT medium.id, medium.name,  "
                        "GROUP_CONCAT(DISTINCT plant_gr.name,': ', plant_gr_medium.amount ORDER BY plant_gr.name ASC SEPARATOR ', ' )as pgrs, "
                        "GROUP_CONCAT(DISTINCT hormones.name,': ', hormones_medium.amount ORDER BY hormones.name ASC SEPARATOR ', ' )as horms, "
                        "GROUP_CONCAT(DISTINCT chem.name,': ', chem_medium.amount ORDER BY chem.name ASC SEPARATOR ', ' )as chems " 
                        "FROM medium "
                        "INNER JOIN plant_gr_medium ON plant_gr_medium.medium_id=medium.id "
                        "INNER JOIN plant_gr ON plant_gr_medium.plant_gr_id=plant_gr.id "
                        "INNER JOIN hormones_medium ON hormones_medium.medium_id=medium.id "
                        "INNER JOIN hormones ON hormones_medium.hormones_id=hormones.id "
                        "INNER JOIN chem_medium ON chem_medium.medium_id=medium.id "
                        "INNER JOIN chem ON chem_medium.chem_id=chem.id "
                        "WHERE medium.name='{}' "
                        "GROUP BY medium.id;",

         
         "join_product":"SELECT product.id, medium.name, product.amount,product.ph,product.date "
                        "FROM product "
                        "INNER JOIN medium ON product.medium_id=medium.id "
                        "ORDER BY product.id ASC",
         
         "sum_p":"SELECT medium.id, SUM(product.amount)  "
                        "FROM product "
                        "INNER JOIN medium ON product.medium_id=medium.id "
                        "GROUP BY medium.id ",
         
         "sum_mc":"SELECT medium_id, chem_id, amount FROM chem_medium;",
         "sum_mh":"SELECT medium_id, hormones_id,  amount FROM hormones_medium;",
         "sum_mp":"SELECT medium_id, plant_gr_id, amount FROM plant_gr_medium;",
         "sum_pc":"SELECT pgr_id, chem_id,amount FROM chem_plant_gr;",
         "rest_c":"SELECT chem.id, chem.name, sum(chem_amount.amount) as 'amount' "
                     "FROM chem "
                     "INNER JOIN chem_amount on chem.id=chem_amount.chem_id "
                     "GROUP BY chem.id "
                     "ORDER BY chem.id ASC ",
         
         "rest_h":"SELECT hormones.id, hormones.name, sum(hormones_amount.amount) "
                     "FROM hormones "
                     "INNER JOIN hormones_amount ON hormones_amount.horm_id=hormones.id "
                     "GROUP BY hormones.id "
                     "ORDER BY hormones.id ASC",
         "show_tables":"SHOW TABLES",

        }


