import Examen2

# Prueba para el método ObtieneValencia
def test_obtiene_valencia():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneValencia(55522)
    assert resultado == 3

# Prueba para el método DivisibleTempo
def test_divisible_tempo():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.DivisibleTempo(15)
    assert resultado == [1, 3, 5, 15]


# Prueba para el método ObtieneMasBailable
def test_obtiene_mas_bailable():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneMasBailable([0.2, 0.1, 0.5, 0.3])
    assert resultado == 0.5


# Prueba para el método VerificaListaCanciones
def test_verifica_lista_canciones():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.VerificaListaCanciones(["Rock Thing", "Deadlocked", "Hydra"])
    assert resultado
