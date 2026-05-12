from src.hidratacao import calcular_agua

def test_temperatura_baixa():
    assert calcular_agua(15) == 2.0

def test_temperatura_media():
    assert calcular_agua(25) == 2.5

def test_temperatura_alta():
    assert calcular_agua(35) == 3.0