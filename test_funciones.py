from funciones import cifrar


def test_cifrar():
    resultado_1 = cifrar("ZigZag", 1)
    resultado_2 = cifrar(" JH BH", -1)
    # cesar3 = crea_cifrador(3)

    assert resultado_1 == " JH BH"
    assert resultado_2 == "ZIGZAG"
    # assert cesar3("ZigZag") == "CLJCDJ"