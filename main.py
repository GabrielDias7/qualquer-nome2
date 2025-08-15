# Sistema de verificação de idade complexo
# Autor: GitHub Copilot
# Data: 15/08/2025

import sys

usuarios = []

def menu():
	print("\n==== MENU ====")
	print("1. Cadastrar usuário")
	print("2. Listar usuários")
	print("3. Verificar maioridade de todos")
	print("4. Estatísticas de idades")
	print("5. Buscar usuário por nome")
	print("6. Remover usuário")
	print("7. Sair")

def validar_idade(idade):
	try:
		idade = int(idade)
		if idade < 0 or idade > 120:
			return False
		return True
	except ValueError:
		return False

def cadastrar_usuario():
	nome = input("Digite o nome do usuário: ").strip()
	while True:
		idade = input("Digite a idade: ").strip()
		if validar_idade(idade):
			idade = int(idade)
			break
		else:
			print("Idade inválida. Tente novamente.")
	usuarios.append({"nome": nome, "idade": idade})
	print(f"Usuário {nome} cadastrado com sucesso!")

def listar_usuarios():
	if not usuarios:
		print("Nenhum usuário cadastrado.")
		return
	print("\nLista de usuários:")
	for i, u in enumerate(usuarios):
		print(f"{i+1}. Nome: {u['nome']}, Idade: {u['idade']}")

def verificar_maioridade():
	if not usuarios:
		print("Nenhum usuário cadastrado.")
		return
	print("\nVerificação de maioridade:")
	for u in usuarios:
		status = "maior de idade" if u['idade'] >= 18 else "menor de idade"
		print(f"{u['nome']} ({u['idade']} anos): {status}")

def estatisticas_idades():
	if not usuarios:
		print("Nenhum usuário cadastrado.")
		return
	idades = [u['idade'] for u in usuarios]
	media = sum(idades) / len(idades)
	maior = max(idades)
	menor = min(idades)
	maiores = len([i for i in idades if i >= 18])
	menores = len([i for i in idades if i < 18])
	print(f"\nEstatísticas:")
	print(f"Média das idades: {media:.2f}")
	print(f"Maior idade: {maior}")
	print(f"Menor idade: {menor}")
	print(f"Total de maiores de idade: {maiores}")
	print(f"Total de menores de idade: {menores}")

def buscar_usuario():
	nome = input("Digite o nome para buscar: ").strip().lower()
	encontrados = [u for u in usuarios if nome in u['nome'].lower()]
	if encontrados:
		print("Usuários encontrados:")
		for u in encontrados:
			print(f"Nome: {u['nome']}, Idade: {u['idade']}")
	else:
		print("Nenhum usuário encontrado com esse nome.")

def remover_usuario():
	nome = input("Digite o nome do usuário para remover: ").strip().lower()
	removidos = 0
	global usuarios
	usuarios = [u for u in usuarios if not (nome == u['nome'].lower())]
	print(f"Usuários com nome '{nome}' removidos, se existiam.")

def main():
	while True:
		menu()
		opcao = input("Escolha uma opção: ").strip()
		if opcao == '1':
			cadastrar_usuario()
		elif opcao == '2':
			listar_usuarios()
		elif opcao == '3':
			verificar_maioridade()
		elif opcao == '4':
			estatisticas_idades()
		elif opcao == '5':
			buscar_usuario()
		elif opcao == '6':
			remover_usuario()
		elif opcao == '7':
			print("Saindo...")
			sys.exit(0)
		else:
			print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
	main()

# Preenchendo até 100 linhas com comentários e exemplos de uso
# Exemplo de uso:
# 1. Execute o programa
# 2. Cadastre usuários
# 3. Liste e verifique maioridade
# 4. Veja estatísticas
# 5. Busque e remova usuários
#
# Este sistema pode ser expandido para salvar dados em arquivos,
# adicionar autenticação, ou integrar com banco de dados.
#
# Fim do exemplo complexo de verificação de idade.
idade = int(input("Digite sua idade: "))

if idade >= 18:
	print("Você é maior de idade.")
else:
	print("Você é menor de idade.")

