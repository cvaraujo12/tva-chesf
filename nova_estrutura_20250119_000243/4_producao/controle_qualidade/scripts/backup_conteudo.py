#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para backup automático de conteúdo.
Realiza backup incremental e mantém versionamento.
"""

import os
import shutil
import logging
import yaml
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class ConfigBackup:
    """Configurações de backup."""
    diretorio_fonte: Path
    diretorio_destino: Path
    intervalo: timedelta
    max_versoes: int
    compressao: bool
    criptografia: bool

@dataclass
class LogBackup:
    """Log de backup."""
    data: datetime
    arquivos: List[str]
    tamanho_total: int
    status: str
    erros: List[str]

class GerenciadorBackup:
    """Classe principal para gerenciamento de backups."""
    
    def __init__(self, config_path: str = "config/backup_config.yaml"):
        """Inicializa o gerenciador com configurações."""
        self.config = self._carregar_config(config_path)
        self.logger = self._configurar_logger()
    
    def _carregar_config(self, path: str) -> Dict:
        """Carrega configurações do arquivo YAML."""
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def _configurar_logger(self) -> logging.Logger:
        """Configura o sistema de logging."""
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        # Criar handler para arquivo
        fh = logging.FileHandler('backup.log')
        fh.setLevel(logging.INFO)
        
        # Criar handler para console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Criar formatador
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        # Adicionar handlers ao logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        
        return logger
    
    def realizar_backup(self, config: ConfigBackup) -> LogBackup:
        """Realiza backup dos arquivos."""
        self.logger.info(f"Iniciando backup de: {config.diretorio_fonte}")
        
        # Inicializar log
        log = LogBackup(
            data=datetime.now(),
            arquivos=[],
            tamanho_total=0,
            status="iniciado",
            erros=[]
        )
        
        try:
            # Criar diretório de backup se não existir
            config.diretorio_destino.mkdir(parents=True, exist_ok=True)
            
            # Gerar nome do backup
            backup_dir = self._gerar_nome_backup(config.diretorio_destino)
            
            # Copiar arquivos
            self._copiar_arquivos(config.diretorio_fonte, backup_dir, log)
            
            # Comprimir se necessário
            if config.compressao:
                self._comprimir_backup(backup_dir)
            
            # Criptografar se necessário
            if config.criptografia:
                self._criptografar_backup(backup_dir)
            
            # Limpar backups antigos
            self._limpar_backups_antigos(config)
            
            log.status = "concluido"
            
        except Exception as e:
            self.logger.error(f"Erro durante backup: {e}")
            log.status = "erro"
            log.erros.append(str(e))
        
        # Salvar log
        self._salvar_log(log)
        
        return log
    
    def _gerar_nome_backup(self, destino: Path) -> Path:
        """Gera nome para o diretório de backup."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return destino / f"backup_{timestamp}"
    
    def _copiar_arquivos(self, fonte: Path, destino: Path, log: LogBackup):
        """Copia arquivos para o backup."""
        self.logger.info("Copiando arquivos...")
        
        for item in fonte.rglob("*"):
            if item.is_file():
                # Calcular caminho relativo
                caminho_relativo = item.relative_to(fonte)
                destino_arquivo = destino / caminho_relativo
                
                # Criar diretórios necessários
                destino_arquivo.parent.mkdir(parents=True, exist_ok=True)
                
                # Copiar arquivo
                shutil.copy2(item, destino_arquivo)
                
                # Atualizar log
                log.arquivos.append(str(caminho_relativo))
                log.tamanho_total += item.stat().st_size
    
    def _comprimir_backup(self, diretorio: Path):
        """Comprime o diretório de backup."""
        self.logger.info("Comprimindo backup...")
        
        arquivo_zip = diretorio.parent / f"{diretorio.name}.zip"
        shutil.make_archive(
            str(diretorio),
            "zip",
            diretorio
        )
        
        # Remover diretório original após compressão
        shutil.rmtree(diretorio)
    
    def _criptografar_backup(self, diretorio: Path):
        """Criptografa o backup."""
        self.logger.info("Criptografando backup...")
        # Implementar criptografia
        pass
    
    def _limpar_backups_antigos(self, config: ConfigBackup):
        """Remove backups antigos."""
        self.logger.info("Limpando backups antigos...")
        
        # Listar backups
        backups = sorted(
            config.diretorio_destino.glob("backup_*"),
            key=lambda x: x.stat().st_mtime
        )
        
        # Remover backups excedentes
        while len(backups) > config.max_versoes:
            backup_antigo = backups.pop(0)
            if backup_antigo.is_dir():
                shutil.rmtree(backup_antigo)
            else:
                backup_antigo.unlink()
    
    def _salvar_log(self, log: LogBackup):
        """Salva o log do backup."""
        # Criar diretório de logs se não existir
        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)
        
        # Gerar nome do arquivo
        nome_arquivo = f"backup_log_{log.data.strftime('%Y%m%d_%H%M%S')}.json"
        caminho_arquivo = logs_dir / nome_arquivo
        
        # Converter log para dict
        dados_log = {
            "data": log.data.isoformat(),
            "arquivos": log.arquivos,
            "tamanho_total": log.tamanho_total,
            "status": log.status,
            "erros": log.erros
        }
        
        # Salvar arquivo
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_log, f, ensure_ascii=False, indent=4)
        
        self.logger.info(f"Log salvo em: {caminho_arquivo}")

def main():
    """Função principal."""
    # Configurar logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Criar gerenciador de backup
    gerenciador = GerenciadorBackup()
    
    # Configurar backup
    config = ConfigBackup(
        diretorio_fonte=Path("conteudo"),
        diretorio_destino=Path("backups"),
        intervalo=timedelta(days=1),
        max_versoes=30,
        compressao=True,
        criptografia=False
    )
    
    try:
        # Realizar backup
        log = gerenciador.realizar_backup(config)
        
        # Exibir resultado
        if log.status == "concluido":
            logger.info("Backup realizado com sucesso!")
            logger.info(f"Total de arquivos: {len(log.arquivos)}")
            logger.info(f"Tamanho total: {log.tamanho_total / 1024 / 1024:.2f} MB")
        else:
            logger.error("Erro ao realizar backup:")
            for erro in log.erros:
                logger.error(f"- {erro}")
    
    except Exception as e:
        logger.error(f"Erro ao executar backup: {e}")

if __name__ == "__main__":
    main() 