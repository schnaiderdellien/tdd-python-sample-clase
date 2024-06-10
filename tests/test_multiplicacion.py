# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import multiplicacion

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_multiplicacion(self):
        assert multiplicacion(1,2) == 2
        assert multiplicacion(5,2) == 10
