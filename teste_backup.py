import os
from backup import backup


def teste_1_arquivo_de_backup_existe():
    
    """
    Teste para verificar se o programa funciona com o backup.parm
    
    """
    
    arq_backup = open('./Pendrive/backup.parm', 'w')
    arq_backup.close()
    
    assert backup() == True
    
    os.remove('./Pendrive/backup.parm')

def teste_2_arquivo_de_backup_nao_existe():
    
    """
    Verifica se o programa reclama da não existência do backup.parm
    
    """
    assert backup() == False

def teste_3_arquivos_para_backup_existem():
    
    """
    Teste para verificar se o programa está verificando a existência dos arquivos 
    descritos no backup.parm
    
    """
    
    arq_backup = open('./Pendrive/backup.parm', 'w')
    arq_backup.write('arq1.txt\narq2.txt\narq3.txt')
    arq_backup.close()
    
    arq1pd = open('./Pendrive/arq1.txt', 'w')
    arq1pd.close()
    arq2pd = open('./Pendrive/arq2.txt', 'w')
    arq2pd.close()
    arq3pd = open('./Pendrive/arq3.txt', 'w')
    arq3pd.close()
    
    arq1hd = open('./HD/arq1.txt', 'w')
    arq1hd.close()
    arq2hd = open('./HD/arq2.txt', 'w')
    arq2hd.close()
    arq3hd = open('./HD/arq3.txt', 'w')
    arq3hd.close()
    
    
    assert backup() == True
    
    os.remove('./Pendrive/backup.parm')
    os.remove('./Pendrive/arq1.txt')
    os.remove('./Pendrive/arq2.txt')
    os.remove('./Pendrive/arq3.txt')
    os.remove('./HD/arq1.txt')
    os.remove('./HD/arq2.txt')
    os.remove('./HD/arq3.txt')

def teste_4_arquivos_para_backup_nao_existem():
    
    """
    Teste para verificar se o programa está verificando a existência dos arquivos 
    descritos no backup.parm
    
    """
    
    arq_backup = open('./Pendrive/backup.parm', 'w')
    arq_backup.write('arq1.txt\narq2.txt\narq3.txt')
    arq_backup.close()
    
    arq1pd = open('./Pendrive/arq1.txt', 'w')
    arq1pd.close()
    arq2pd = open('./Pendrive/arq2.txt', 'w')
    arq2pd.close()
    arq3pd = open('./Pendrive/arq3.txt', 'w')
    arq3pd.close()
    
    arq1hd = open('./HD/arq1.txt', 'w')
    arq1hd.close()
    arq3hd = open('./HD/arq3.txt', 'w')
    arq3hd.close()
    
    
    assert backup() == False
    
    os.remove('./Pendrive/backup.parm')
    os.remove('./Pendrive/arq1.txt')
    os.remove('./Pendrive/arq2.txt')
    os.remove('./Pendrive/arq3.txt')
    os.remove('./HD/arq1.txt')
    os.remove('./HD/arq3.txt')

def teste_5_arquivos_para_backup_nao_existem():
    
    """
    Teste para verificar se o programa está verificando a existência dos arquivos 
    descritos no backup.parm
    
    """
    
    arq_backup = open('./Pendrive/backup.parm', 'w')
    arq_backup.write('arq1.txt\narq2.txt\narq3.txt')
    arq_backup.close()
    
    arq2pd = open('./Pendrive/arq2.txt', 'w')
    arq2pd.close()
    arq3pd = open('./Pendrive/arq3.txt', 'w')
    arq3pd.close()
    
    arq1hd = open('./HD/arq1.txt', 'w')
    arq1hd.close()
    arq2hd = open('./HD/arq2.txt', 'w')
    arq2hd.close()
    arq3hd = open('./HD/arq3.txt', 'w')
    arq3hd.close()
    
    
    assert backup() == False
    
    os.remove('./Pendrive/backup.parm')
    os.remove('./Pendrive/arq2.txt')
    os.remove('./Pendrive/arq3.txt')
    os.remove('./HD/arq1.txt')
    os.remove('./HD/arq2.txt')
    os.remove('./HD/arq3.txt')