import cryptocode

def encripta(senha_nova):
    senhacrypto = cryptocode.encrypt(senha_nova, 'rouba meu sistema agora')
    return senhacrypto

def decripta(senha_cadastrada):
    cripto_cadastrada = cryptocode.decrypt(senha_cadastrada, 'rouba meu sistema agora')
    return cripto_cadastrada
