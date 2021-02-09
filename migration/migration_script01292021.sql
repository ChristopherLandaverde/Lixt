-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: FLAPI
-- Source Schemata: FLAPI
-- Created: Thu Jan 21 15:59:18 2021
-- Workbench Version: 8.0.22
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema FLAPI
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `FLAPI` ;
CREATE SCHEMA IF NOT EXISTS `FLAPI` ;

-- ----------------------------------------------------------------------------
-- Table FLAPI.groclist
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `FLAPI`.`Grocery_List` (
  `ID` VARCHAR(50) NULL DEFAULT NULL,
  `userID` VARCHAR(20) NULL DEFAULT NULL,
  `name` VARCHAR(50) NULL DEFAULT NULL,
  `createdAt` DATE NULL DEFAULT NULL,
  `createdBy` VARCHAR(50) NULL DEFAULT NULL,
  `lastEdited` DATE NULL DEFAULT NULL,
  `lastEditedBy` VARCHAR(50) NULL DEFAULT NULL,
  `timeUpdated` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `timeCreated` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

USE FLAPI;

DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `updatsxe_USERID` BEFORE INSERT ON `Grocery_list` FOR EACH ROW BEGIN
   IF !(new.userID <=> new.createdBy) THEN
      SET new.userID := new.createdBy;
   END IF;
END */;;
DELIMITER ;

DELIMITER //
CREATE TRIGGER new_USERID BEFORE INSERT ON Grocery_list
FOR EACH ROW
BEGIN
   IF !(new.userID <=> new.lastEditedBy) THEN
      SET new.lastEditedBy := new.userID;
   END IF;
END;//
DELIMITER ;

ALTER TABLE GROCERY_LIST DROP LastEdited;
alter table Grocery_List drop column createdAt;
Alter table Grocery_list rename column timeUpdated to lastEdited;


-- ----------------------------------------------------------------------------
-- Table FLAPI.items
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `FLAPI`.`items`;

-- ----------------------------------------------------------------------------
-- Table FLAPI.Test_List
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `FLAPI`.`Test_List`;
-- ----------------------------------------------------------------------------
-- Table FLAPI.test_table
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `FLAPI`.`test_table`;
