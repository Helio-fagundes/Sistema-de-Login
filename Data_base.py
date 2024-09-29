import pymysql.cursors
import crypto
con = pymysql.connect(

    host="localhost",
    user="root",
    password="",
    port=3306,
    charset="utf8mb4",
    database="login",
    cursorclass = pymysql.cursors.DictCursor

)
def AdicionarDados(nome, email, senha):
    try:
        with con.cursor() as cursor:
            query = """
            INSERT INTO cadastros (nome, email, senha)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (nome, email, senha)) 
            con.commit()
            print("cadastrado com sucesso")
    
    except pymysql.err.IntegrityError as e:
        if 'Duplicate entry' in str(e):
            print(f'Erro: O e-mail "{email}" já está cadastrado. Tente outro.')
        else:
            print(f'O código apresenta um erro de integridade: {e}')
    except Exception as e:
        print(f'o codigo apresenta o erro {e}')
        
    finally:
        cursor.close()

def ConsultarDados(email):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM cadastros WHERE email = '{email}'")
            resultado = cursor.fetchone()
            if resultado is None:
                print('seu email está errado')
            else:
                senha_pronta = crypto.decripta(resultado['senha'])
                con.commit()
                return senha_pronta
    except Exception as e:
        print(f'erro {e} verificado')
    finally:
        cursor.close()
    
