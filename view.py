import crypto
import Data_base
import time

def pontos():
    print("=" * 20 )

while True:
    try:
        pontos()    
        rsp = int(input('logar(digite 1)\ncadastrar(digite 2)\n'))
        pontos()

        if rsp == 1:
            email = str(input('Digite seu E-Mail: '))
            senha = str(input("Digite sua Senha: "))
            comparar = Data_base.ConsultarDados(email)
            if comparar is None:
                continue
            elif comparar == senha:
                print('você está logado')
                break
            else:
                print('sua senha está errada')
                continue
        
        elif rsp == 2:
            nome = str(input('Digite seu Nome: '))
            email = str(input('Digite seu E-Mail: '))
            senha = str(input('Digite sua Senha: '))
            senha_criptografada = crypto.encripta(senha)
            Data_base.AdicionarDados(nome, email, senha_criptografada)
            time.sleep(1.5)
            continue
        
        else:
            print('digite uma resposta valida')
    
    except KeyboardInterrupt:
        print('\no programa foi encerrado')
        break
    except ValueError:
        print('Você Digitou Algo Errado, Digite Apenas 1 Ou 2!')
