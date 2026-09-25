# ============================================================
# EMPRESA: TudoWeb
# OBJETIVO: Pesquisa de Satisfação de Atendimento ao Cliente
# ============================================================

# Quantidade total de entrevistados (Altere para 50 na versão final)
TOTAL_ENTREVISTADOS = 50  # Configurado para 10 para realização dos testes

# Inicialização dos contadores
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0
print("=" * 50)
print("     PESQUISA DE SATISFAÇÃO - TUDOWEB     ")
print("=" * 50)

# Estrutura de repetição para coletar as respostas
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    # Loop para garantir uma opção válida
    while True:
        print("\nQual a sua opinião sobre o atendimento prestado?")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        
        opcao = input("Digite sua opção (1, 2 ou 3): ")

        # Estrutura de decisão para verificar a opinião
        if opcao == "1":
            qtd_excelente += 1
            break
        elif opcao == "2":
            qtd_bom += 1
            break
        elif opcao == "3":
            qtd_ruim += 1
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")

# ============================================================
# RELATÓRIO FINAL
# ============================================================
print("\n" + "=" * 50)
print("          RESULTADO DA PESQUISA DE SATISFAÇÃO          ")
print("=" * 50)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print(f"   Quantidade de respostas 'BOM': {qtd_bom}")
print(f"   Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print("=" * 50)