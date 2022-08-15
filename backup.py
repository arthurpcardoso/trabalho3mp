import os

def backup():
    """Função backup
    
    Analisa os aquivos que precisam ser espelhdos através da tabela
    de decisão.

    Returns:
        boll: Retorna True se o backup foi bem sucedido, falso se
        não foi bem sucedido
    """
    
    try:
        assert os.path.exists('./Pendrive/backup.parm') == True
    except AssertionError:
        return False
    
    arq_backup = open('./Pendrive/backup.parm')
    lista_arquivos = arq_backup.read().splitlines()
    
    for arq in lista_arquivos:
        try:
            assert os.path.exists(f'./Pendrive/{arq}') == True
            assert os.path.exists(f'./HD/{arq}') == True
        except AssertionError:
            return False
    
    return True