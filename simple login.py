"""
Operadores Lógicos
and, or, not
in e not in
"""
a = ""
b = 0

nome = "Tiago Pimenta"
if "ti" not in nome:
    print("executei")
else:
    print("existe o texto")

    """
    Teste
    """
usuario = input("Nome de usuário: ")
senha = input("senha do usuário: ")

usuario_bd = "tiago"
senha_bd = "123"

if usuario_bd == usuario and senha_bd == senha:
    print("Voce esta logado")
else:
    print(" login ou senha incorreto")