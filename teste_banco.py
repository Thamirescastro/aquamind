# teste_banco.py
from src.db.crud import registrar_autocuidado, buscar_historico

print("Testando conexão e inserção...")
# Simulando alguém que bebeu 500ml, meditou, mas não alongou
novo_registro = registrar_autocuidado(500, True, False)
print("Inserido:", novo_registro)

print("\nBuscando histórico...")
historico = buscar_historico()
print("Histórico completo:", historico)
