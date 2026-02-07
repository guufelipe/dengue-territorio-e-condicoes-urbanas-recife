import pandas as pd

def tratar_dados_dengue(df):
    """
    Recebe o DataFrame concatenado de Dengue.
    Possui metadados completos (Notificação, Paciente, Sintomas, Classificação).
    """
    colunas_renomear = {
        # --- Notificação ---
        'num_notificacao': 'id_notificacao',
        'dt_notificacao': 'data_notificacao',
        'co_municipio_notificacao': 'cod_municipio_notificacao',
        'co_unidade_notificacao': 'cod_unidade_notificacao',
        
        # --- Paciente ---
        'dt_nascimento': 'paciente_nascimento',
        'tp_sexo': 'paciente_sexo',
        'tp_gestante': 'paciente_gestante',
        'tp_raca_cor': 'paciente_raca',
        'tp_zona_residencia': 'residencia_zona',
        'no_bairro_residencia': 'residencia_bairro',
        
        # --- Clínicos ---
        'febre': 'sintoma_febre',
        'mialgia': 'sintoma_mialgia',
        'cefaleia': 'sintoma_cefaleia',
        'exantema': 'sintoma_exantema',
        'vomito': 'sintoma_vomito',
        'nausea': 'sintoma_nausea',
        'dor_costas': 'sintoma_dor_costas',
        'conjutivite': 'sintoma_conjuntivite',
        'artrite': 'sintoma_artrite',
        'artralgia': 'sintoma_artralgia',
        
        # --- Classificação e Evolução ---
        'tp_classificacao_final': 'final_classificacao',
        'st_ocorreu_hospitalizacao': 'final_hospitalizacao',
        'tp_evolucao_caso': 'final_evolucao'
    }

    colunas_existentes = [col for col in colunas_renomear.keys() if col in df.columns]
    df_filtrado = df[colunas_existentes].copy()
    df_filtrado = df_filtrado.rename(columns=colunas_renomear)
    return df_filtrado

def tratar_dados_zika(df):
    """
    Recebe o DataFrame concatenado de Zika.
    Baseado no metadado fornecido: Apenas Notificação e Paciente disponíveis.
    """
    colunas_renomear = {
        # --- Notificação ---
        'num_notificacao': 'id_notificacao',
        'dt_notificacao': 'data_notificacao',
        'co_municipio_notificacao': 'cod_municipio_notificacao',
        'co_unidade_notificacao': 'cod_unidade_notificacao',
        
        # --- Paciente ---
        'dt_nascimento': 'paciente_nascimento',
        'tp_sexo': 'paciente_sexo',
        'tp_gestante': 'paciente_gestante',
        'tp_raca_cor': 'paciente_raca',
        'tp_zona_residencia': 'residencia_zona',
        'no_bairro_residencia': 'residencia_bairro'
    }

    colunas_existentes = [col for col in colunas_renomear.keys() if col in df.columns]
    df_filtrado = df[colunas_existentes].copy()
    df_filtrado = df_filtrado.rename(columns=colunas_renomear)
    return df_filtrado

def tratar_dados_chikungunya(df):
    """
    Recebe o DataFrame concatenado de Chikungunya.
    Baseado no metadado fornecido: Apenas Notificação e Paciente disponíveis.
    """
    colunas_renomear = {
        # --- Notificação ---
        'num_notificacao': 'id_notificacao',
        'dt_notificacao': 'data_notificacao',
        'co_municipio_notificacao': 'cod_municipio_notificacao',
        'co_unidade_notificacao': 'cod_unidade_notificacao',
        
        # --- Paciente ---
        'dt_nascimento': 'paciente_nascimento',
        'tp_sexo': 'paciente_sexo',
        'tp_gestante': 'paciente_gestante',
        'tp_raca_cor': 'paciente_raca',
        'tp_zona_residencia': 'residencia_zona',
        'no_bairro_residencia': 'residencia_bairro'
        
        # Nota: O metadado de Chikungunya fornecido lista colunas de transferência
        # administrativa (dt_transf, nu_lote), mas não lista sintomas ou 
        # classificação final. Portanto, não foram incluídos aqui.
    }

    # 1. Filtra apenas as colunas que existem no dicionário
    colunas_existentes = [col for col in colunas_renomear.keys() if col in df.columns]
    df_filtrado = df[colunas_existentes].copy()
    
    # 2. Renomeia as colunas
    df_filtrado = df_filtrado.rename(columns=colunas_renomear)

    return df_filtrado