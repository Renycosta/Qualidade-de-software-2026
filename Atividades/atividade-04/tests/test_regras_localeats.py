import pytest

from src.regras_localeats import quantidade_itens_valida


def test_quantidade_itens_valida():
    resultado = quantidade_itens_valida(5)

    assert resultado is True


def test_quantidade_itens_negativa():
    with pytest.raises(ValueError):
        quantidade_itens_valida(-1)