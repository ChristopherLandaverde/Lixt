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
CREATE TABLE IF NOT EXISTS `FLAPI`.`Grocery_list` (
  `id` VARCHAR(50) NULL DEFAULT NULL,
  `userID` VARCHAR(20) NULL DEFAULT NULL,
  `name` VARCHAR(50) NULL DEFAULT NULL,
  `created_at` DATE NULL DEFAULT NULL,
  `created_by` VARCHAR(50) NULL DEFAULT NULL,
  `last_edited` DATE NULL DEFAULT NULL,
  `last_edited_by` VARCHAR(50) NULL DEFAULT NULL,
  `time_updated` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `time_created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table FLAPI.items
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `FLAPI`.`items` (
  `id` VARCHAR(100) NOT NULL,
  `names` VARCHAR(100) NULL DEFAULT NULL,
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `names` (`names` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table FLAPI.Test_List
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `FLAPI`.`Test_List` (
  `ID` VARCHAR(255) NULL DEFAULT NULL,
  `UserID` INT NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `lastEdited` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `lastEditedBy` VARCHAR(255) NULL DEFAULT NULL,
  `createdAt` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `createdBy` VARCHAR(255) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table FLAPI.test_table
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `FLAPI`.`test_table` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stamp_created` TIMESTAMP NULL DEFAULT NULL,
  `stamp_updated` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `column_name` VARCHAR(250) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
SET FOREIGN_KEY_CHECKS = 1;
