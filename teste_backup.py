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

def teste_1_arquivo_de_backup_existe():
    
    """
    Verifica se o programa reclama da não existência do backup.parm
    
    """
    assert backup() == False