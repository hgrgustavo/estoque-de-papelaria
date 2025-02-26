
CREATE SCHEMA IF NOT EXISTS `database_estoque_papelaria` ;
USE `database_estoque_papelaria` ;

-- -----------------------------------------------------
-- Table `database_estoque_papelaria`.`cadastro_livros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_estoque_papelaria`.`cadastro_livros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `isbn` VARCHAR(13) NOT NULL,
  `edicao` VARCHAR(255) NOT NULL,
  `editora` VARCHAR(255) NOT NULL,
  `ano_publicacao` YEAR NOT NULL,
  `preco_capa` FLOAT NOT NULL,
  `categoria` VARCHAR(255) NOT NULL,
  `autores` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_estoque_papelaria`.`cadastro_autores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_estoque_papelaria`.`cadastro_autores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome_completo` VARCHAR(255) NOT NULL,
  `nacionalidade` VARCHAR(255) NOT NULL,
  `biografia` VARCHAR(1000) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_estoque_papelaria`.`controle_estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_estoque_papelaria`.`controle_estoque` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quantidade_livros` INT NOT NULL,
  `controle_estoquecol` INT NOT NULL,
  `data_entrada_livro` DATE NOT NULL,
  `data_saida_livro` DATE NOT NULL,
  `cadastro_livros_id` INT NOT NULL,
  PRIMARY KEY (`id`, `cadastro_livros_id`),
  INDEX `fk_controle_estoque_cadastro_livros1_idx` (`cadastro_livros_id` ASC) VISIBLE,
  CONSTRAINT `fk_controle_estoque_cadastro_livros1`
    FOREIGN KEY (`cadastro_livros_id`)
    REFERENCES `database_estoque_papelaria`.`cadastro_livros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_estoque_papelaria`.`cadastro_livros_has_cadastro_autores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_estoque_papelaria`.`cadastro_livros_has_cadastro_autores` (
  `cadastro_livros_id` INT NOT NULL,
  `cadastro_autores_id` INT NOT NULL,
  PRIMARY KEY (`cadastro_livros_id`, `cadastro_autores_id`),
  INDEX `fk_cadastro_livros_has_cadastro_autores_cadastro_autores1_idx` (`cadastro_autores_id` ASC) VISIBLE,
  INDEX `fk_cadastro_livros_has_cadastro_autores_cadastro_livros1_idx` (`cadastro_livros_id` ASC) VISIBLE,
  CONSTRAINT `fk_cadastro_livros_has_cadastro_autores_cadastro_livros1`
    FOREIGN KEY (`cadastro_livros_id`)
    REFERENCES `database_estoque_papelaria`.`cadastro_livros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cadastro_livros_has_cadastro_autores_cadastro_autores1`
    FOREIGN KEY (`cadastro_autores_id`)
    REFERENCES `database_estoque_papelaria`.`cadastro_autores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
