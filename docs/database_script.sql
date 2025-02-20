

CREATE DATABASE IF NOT EXISTS `database_estoque_papelaria` DEFAULT CHARACTER SET utf8 ;
USE `database_estoque_papelaria` ;

-- -----------------------------------------------------
-- Table `livros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `livros` (
  `id` INT NOT NULL,
  `titulo` VARCHAR(255) NOT NULL,
  `isbn` VARCHAR(255) NOT NULL,
  `edicao` VARCHAR(255) NOT NULL,
  `editora` VARCHAR(255) NOT NULL,
  `ano_publicacao` YEAR NOT NULL,
  `preco_capa` FLOAT NOT NULL,
  `ano_publicacao` DATE NOT NULL,
  `categoria` VARCHAR(255) NOT NULL,
  `autores` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`));
  
-- -----------------------------------------------------
-- Table `autores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `autores` (
  `id` INT NOT NULL,
  `nome_completo` VARCHAR(255) NOT NULL,
  `nacionalidade` VARCHAR(255) NOT NULL,
  `biografia` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`));

-- -----------------------------------------------------
-- Table `estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estoque` (
  `id` INT NOT NULL,
  `quantidade_livros` BIGINT NOT NULL,
  `data_entrada` DATE NOT NULL,
  `data_saida` DATE NOT NULL,
  `livros_id` INT NOT NULL,
  PRIMARY KEY (`id`, `livros_id`),
  INDEX `fk_estoque_livros1_idx` (`livros_id` ASC) VISIBLE,
  CONSTRAINT `fk_estoque_livros1`
    FOREIGN KEY (`livros_id`)
    REFERENCES `livros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `livros_has_autores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `livros_has_autores` (
  `livros_id` INT NOT NULL,
  `autores_id` INT NOT NULL,
  PRIMARY KEY (`livros_id`, `autores_id`),
  INDEX `fk_livros_has_autores_autores1_idx` (`autores_id` ASC) VISIBLE,
  INDEX `fk_livros_has_autores_livros_idx` (`livros_id` ASC) VISIBLE,
  CONSTRAINT `fk_livros_has_autores_livros`
    FOREIGN KEY (`livros_id`)
    REFERENCES `livros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livros_has_autores_autores1`livros_has_autores
    FOREIGN KEY (`autores_id`)
    REFERENCES `autores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
