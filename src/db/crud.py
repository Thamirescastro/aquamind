from .database import supabase

def registrar_autocuidado(agua_ml: int, meditacao: bool, alongamento: bool):
    """
    Insere um novo registro diário de hidratação e autocuidado no banco.
    """
    dados = {
        "agua_ml": agua_ml,
        "meditacao_concluida": meditacao,
        "alongamento_concluido": alongamento
    }
    
    # O comando .execute() finaliza a operação no Supabase para Python
    resposta = supabase.table("registros_diarios").insert(dados).execute()
    return resposta.data

def buscar_historico():
    """
    Busca todos os registros para exibir na interface web.
    """
    resposta = supabase.table("registros_diarios").select("*").execute()
    return resposta.data