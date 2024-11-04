from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self,repository:UsuarioRepository)-> None:
        self.repository = repository

    def criar_usuario(self,nome:str,email:str,senha:str):
        try:
            usuario = Usuario(nome=nome,email=email,senha=senha)

            consultar_usuario = self.repository.listar_todos_usuarios(usuario.email)

            if consultar_usuario:
                print("Usuario ja existe")
                return
            
    def atualizar_usuario(self):
            try:
                 print("\Atualizando os dados do usuario...")

                 email_usuario = input("Informe o email do usuario:") 

                 usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email=email_usuario) 

                 if usuario_cadastrado:
                      usuario_cadastrado.nome = input("Digite seu nome:")
                      usuario_cadastrado.email = input("Digite seu email:")
                      usuario_cadastrado.senha= input ("Digite sua senha:")
                      self.repository.atualizar_usuario(usuario_cadastrado) 
                      print("Usuario atualizado com sucesso !")

                 else
                      print("Usuario não encontrado.")

            except TypeError as erro:
                 print(f"Erro ao atualizar o ususario: {erro}") 
            except Exception as                        

            self.repository.salvar_usuario(usuario)
            print("Usuario salvo com sucesso")
        except TypeError as erro:
            print("Erro ao salvar usuario:{erro}")            
        except Exception as erro:
            print("Ocorreu um erro inesperado:{erro}")            
    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()
