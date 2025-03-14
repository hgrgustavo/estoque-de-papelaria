-- MySQL Script generated by MySQL Workbench
-- Fri Feb 28 15:09:01 2025
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema database_estoque_papelaria
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema database_estoque_papelaria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `database_estoque_papelaria` ;
USE `database_estoque_papelaria` ;

-- -----------------------------------------------------
-- Table `database_estoque_papelaria`.`livros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_estoque_papelaria`.`livros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `título` VARCHAR(45) NOT NULL,
  `isbn` VARCHAR(17) NOT NULL,
  `edição` VARCHAR(45) NOT NULL,
  `editora` VARCHAR(45) NOT NULL,
  `ano_publicação` YEAR NOT NULL,
  `preço_capa` DOUBLE(10,2) NOT NULL,
  `categoria` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_estoque_papelaria`.`autores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_estoque_papelaria`.`autores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome_completo` VARCHAR(45) NOT NULL,
  `nacionalidade` VARCHAR(45) NOT NULL,
  `biografia` TEXT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_estoque_papelaria`.`estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_estoque_papelaria`.`estoque` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data_entrada` DATE NOT NULL,
  `data_saida` DATE NOT NULL,
  `livros_id` INT NOT NULL,
  PRIMARY KEY (`id`, `livros_id`),
  INDEX `fk_estoque_livros_idx` (`livros_id` ASC) VISIBLE,
  CONSTRAINT `fk_estoque_livros`
    FOREIGN KEY (`livros_id`)
    REFERENCES `database_estoque_papelaria`.`livros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_estoque_papelaria`.`livros_has_autores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_estoque_papelaria`.`livros_has_autores` (
  `livros_id` INT NOT NULL,
  `autores_id` INT NOT NULL,
  PRIMARY KEY (`livros_id`, `autores_id`),
  INDEX `fk_livros_has_autores_autores1_idx` (`autores_id` ASC) VISIBLE,
  INDEX `fk_livros_has_autores_livros1_idx` (`livros_id` ASC) VISIBLE,
  CONSTRAINT `fk_livros_has_autores_livros1`
    FOREIGN KEY (`livros_id`)
    REFERENCES `database_estoque_papelaria`.`livros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livros_has_autores_autores1`
    FOREIGN KEY (`autores_id`)
    REFERENCES `database_estoque_papelaria`.`autores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
