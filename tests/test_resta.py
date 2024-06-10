# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import resta

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_resta(self):
        assert resta(5,2) == 3
        assert resta(-1,-2) == -3
        assert resta(-5,5) == 0
        assert resta(1,9) == -8