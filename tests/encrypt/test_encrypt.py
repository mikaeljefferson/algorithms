from challenges.challenge_encrypt_message import encrypt_message
import pytest

def test_encrypt_message():
    
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("xesq", "dele")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(22, 666)
    assert encrypt_message("teste", 10) == "etset"
    assert encrypt_message("teste", 3) == "set_et"
    assert encrypt_message("teste", 2) == "ets_et"