import pytest
from feriados.FeriadosAPI import FeriadoAPI


class TestFeriadoAPI:
    def test_instanciar_objeto(self):
        objeto = FeriadoAPI(2022)
        assert objeto._ano, 2022
        assert type(objeto.feriados) == list
        assert len(objeto.feriados) == 11

    def test_str_repr(self):
        objeto = FeriadoAPI(2023)
        msg = 'Feriados de 2023'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_str_repr2(self):
        objeto = FeriadoAPI(2022)
        msg = 'Feriados de 2022'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_properties(self):
        objeto = FeriadoAPI(2022)
        assert objeto.ano == '2022'
