import os
from datetime import * 
print("Bem vindo à Auto Peças Soluções Automobilisticas\n")

# Cadastro dos produtos  
produtos = [
    {"nome": "Pneu", "preco": 80.00},
    {"nome": "Bateria", "preco": 200.00},
    {"nome": "Óleo", "preco": 60.00},
    {"nome": "Filtro de ar", "preco": 45.00},
    {"nome": "Velas de ignição", "preco": 70.00},
    {"nome": "Disco de freio", "preco": 150.00},
    {"nome": "Pastilha de freio", "preco": 120.00},
    {"nome": "Radiador", "preco": 350.00},
    {"nome": "Amortecedor", "preco": 250.00},
    {"nome": "Correia dentada", "preco": 180.00},
    {"nome": "Embreagem", "preco": 400.00},
    {"nome": "Farol dianteiro", "preco": 220.00},
    {"nome": "Lanterna traseira", "preco": 150.00},
    {"nome": "Retrovisor", "preco": 90.00},
    {"nome": "Parachoque", "preco": 300.00},
    {"nome": "Escapamento", "preco": 280.00},
    {"nome": "Alternador", "preco": 500.00},
    {"nome": "Motor de arranque", "preco": 450.00},
    {"nome": "Sensor ABS", "preco": 200.00},
    {"nome": "Filtro de combustível", "preco": 65.00},
    {"nome": "Kit suspensão", "preco": 600.00}
]
# Cadastro de serviços
servicos = [
    {"nome":"Troca de pneu  ", "preco": 80.00},
    {"nome":"Troca de bateria  ", "preco": 150.00},
    {"nome":"Troca de óleo  ", "preco": 120.00},
    {"nome":"Limpeza do filtro de ar  ", "preco": 90.00},
    {"nome":"Revisão periódica (check-up geral)  ", "preco": 350.00},
    {"nome":"Alinhamento e balanceamento  ", "preco": 200.00},
    {"nome":"Troca de pastilha de freio  ", "preco": 180.00},
    {"nome":"Higienização do ar-condicionado  ", "preco": 250.00},
    {"nome":"Diagnóstico eletrônico (Scanner automotivo)  ", "preco": 159.99},
    {"nome":"Instalação de acessórios (Som, película, trava elétrica)  ", "preco": 149.99}
]
# Mecânico Virtual
mecanico_virtual = {
    1:"Problemas nos freios",
    2:"Bateria descarregada",
    3:"Superaquecimento do motor",
    4:"Problemas de transmissão",
    5:"Fusíveis queimados",
    6:"Luzes do painel piscando",
    7:"Sistema de áudio com mau funcionamento",
    8:"Vazamentos de óleo",
    9:"Vazamentos de líquido de arrefecimento",
    10:"Pneus desgastados",
    11:"Molas quebradas",
    12:"Problemas na suspensão",
    13:"Falha no sistema de ignição",
    14:"Problemas de alinhamento",
    15:"Sensor de oxigênio defeituoso",
    16:"Problemas de embreagem",
    17:"Sistema de ar condicionado com mau funcionamento",
    18:"Falha no sistema de direção assistida",
    19:"Não sei identificar",
    20:"Sair"
    
}
 # respostas Mecânico Virutal
respostas_mecanico_virtual = {
    1: "Verifique as pastilhas e discos de freio, pode haver desgaste excessivo.",
    2: "Recarregue ou substitua a bateria. Verifique o funcionamento do alternador e inspecione o sistema elétrico do veículo para identificar possíveis falhas.",
    3: "Confira o nível do líquido de arrefecimento, reparar vazamentos, substituir o termostato defeituoso e assegurar que o ventilador do radiador esteja funcionando corretamente.",
    4: "Pode ser desgaste na transmissão. Visite a uma unidade fisica e comunique ao mecânico especializado.",
    5: "Troque o fusível queimado e verifique a causa do problema elétrico.",
    6: "Pode haver mau contato. Leve para um diagnóstico elétrico.",
    7: "Verifique conexões e fusíveis. Pode ser falha no rádio ou sistema elétrico.",
    8: "Será necessário identificar a origem do vazamento, realizar as substituições necessárias de juntas ou vedantes, e garantir que o motor esteja corretamente selado para evitar futuros vazamentos.",
    9: "Cheque mangueiras, radiador e bomba d’água para evitar superaquecimento.",
    10: "Troque os pneus desgastados e verifique alinhamento.",
    11: "As molas estão comprometidas. Recomenda-se substituição imediata.",
    12: "Problemas na suspensão. Pode afetar a estabilidade, procure uma oficina.",
    13: "Falha na ignição. Pode ser vela ou bobina, faça uma revisão elétrica.",
    14: "Veículo desalinhado. Faça alinhamento e balanceamento.",
    15: "Sensor de oxigênio com defeito. Necessário diagnóstico eletrônico.",
    16: "Embreagem com problemas. Verifique desgaste e ajuste do sistema.",
    17: "Ar condicionado com falha. Pode faltar gás ou haver falha no compressor.",
    18: "Direção assistida com falha. Pode ser bomba hidráulica ou sistema elétrico.",
    19: "Recomendamos levar o veículo para uma avaliação completa."

}
carrinho = []
# Cadastro inicial do usuário
resposta = "N"
while True:
    while resposta.upper() != "S":
        nome = input("Digite o seu nome: ").strip()
        telefone = (input("Digite um número de telefone válido: ")).strip()
        if not nome or not nome.replace(" ", "").isalpha() or not telefone.isdigit():
            print("Nome deve conter apenas letras e telefone apenas números!")
            continue
        print("\nSeus dados são:")
        print("Nome:", nome)
        print("Telefone:", telefone)
        resposta = input("Está correto? (S/N): ").strip().upper() #strip retira espaços e upper converte tudo para maisculo
        if resposta not in ["S", "N"]:
            print("\nDigite apenas S para sim ou N para não.\n")
        
    os.system("cls")

    # Tela principal
    while True:
        print("\nBoas vindas ao nosso estabelecimento, como podemos ajudá-lo?")
        print("1 - Produtos")
        print("2 - Serviços")
        print("3 - Mecânico Virtual")
        print("4 - Sair do sistema")

        try:
            decisao = int(input("Escolha uma opção: "))
        except ValueError:
            print("⚠️ Digite um número válido.")
            continue

        # Produtos
        if decisao == 1: 
            print("\n--- Lista de Produtos Disponíveis ---")
            for i, produto in enumerate(produtos, start=1):
                print(f"{i} - {produto['nome']} - R${produto['preco']:.2f}")
                
            while True:
                try:
                    opcao = int(input("Digite o número do produto desejado (0 para voltar): "))
                except ValueError:
                    print("⚠️ Digite um número válido.")
                    continue

                if opcao == 0:
                    break
                elif 1 <= opcao <= len(produtos):
                    carrinho.append(produtos[opcao - 1])
                    print("✅ Produto adicionado:", produtos[opcao - 1]["nome"])
                else:
                    print("⚠️ Opção inválida, tente novamente.")
        # Serviços           
        elif decisao == 2:  
            print("\n--- Lista de Serviços Disponíveis ---")
            for i, servico in enumerate(servicos, start=1):
                print(f"{i} - {servico['nome']}  R${servico['preco']:.2f}")
                
            while True:    
                try:
                    opcao = int(input("Digite o número do serviço desejado (0 para voltar): "))
                except ValueError:
                    print("⚠️ Digite apenas números.")
                    continue

                if opcao == 0:
                    break
                elif 1 <= opcao <= len(servicos):
                    carrinho.append(servicos[opcao - 1])
                    print("✅ Serviço adicionado:", servicos[opcao - 1]["nome"])
                else:
                    print("⚠️ Opção inválida, tente novamente.")
                    
        #Mecânico Virtual           
        elif decisao == 3:
            print("\nBem vindo ao Mecânico Virtual")
            
            while True:
                print("Escolha o problema que mais se aproxima do seu carro:\n")
        
                # Mostrando as perguntas
                for codigo, descricao in mecanico_virtual.items():
                    print(f"{codigo} - {descricao}")
                
                escolha_mecanico = input("\nDigite o número correspondente: ").strip()
                
                #Verifica se a escolha é válida 
                if escolha_mecanico.isdigit():
                    escolha_mecanico= int(escolha_mecanico)
                    #Saída do  Mecânico
                    if escolha_mecanico == 20:
                        print("\nEncerrando Mecânico Virtual...\n")
                        break
                    if escolha_mecanico in respostas_mecanico_virtual:
                        print(f"\nResposta: {respostas_mecanico_virtual[escolha_mecanico]}\n")
                    else:
                        print("⚠️ Opção inválida, tente novamente")
                        continue
                else:
                    print("\n⚠️ Digite apenas números")        
                    continue
                
        elif decisao == 4:
            print("\nSistema encerrado.")
            exit()
            break
                
        # mostrar carrinho e total só no final da seleção
        if decisao in [1, 2]:
            if carrinho:
                print("\n🛒 Itens no carrinho:")
                for item in carrinho:
                    print(f"- {item['nome']} - R${item['preco']:.2f}")
                    
                # Perguntar ação final
                while True:
                    print("\nO que deseja fazer?")
                    print("1 - Finalizar compra")
                    print("2 - Voltar à tela inicial")
                    print("3 - Sair do sistema")
                    escolha_final = input("Digite a opção desejada: ")
                    
                    if escolha_final == "1":
                        os.system("cls") 
                        somaprodutos = sum(item["preco"] for item in carrinho)
                        if somaprodutos > 200:
                            desconto = somaprodutos * 0.10
                            total_com_desconto = somaprodutos - desconto
                            print("\n📋 Dados do Cliente:")
                            print("Nome:", nome)
                            print("Telefone:", telefone)
                            print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                            
                            if carrinho:
                                print("\n🛒 Itens no carrinho:")
                                for item in carrinho:
                                    print(f"- {item['nome']} - R${item['preco']:.2f}")
                            print(f"\n💰 Valor da compra: R${somaprodutos:.2f}")
                            if desconto > 0:
                                print(f"✅ Desconto aplicado: R${desconto:.2f}")
                                print(f"💰 Total a pagar com desconto: R${total_com_desconto:.2f}")
                        #else:
                        # print(f"\n💰 Valor total a pagar: R${total_com_desconto:.2f}")

                        # Mostrar dados do cliente junto com a compra
                        print("\n🙏 Obrigado pela sua compra,", nome)
                        print("Volte sempre!")
                        exit()
                        break
                    elif escolha_final == "2":
                        os.system("cls")                   
                        break  # volta ao menu principal
                        
                    elif escolha_final == "3":
                        print("\nSistema encerrado.")
                        exit()
                    else:
                        print("⚠️ Opção inválida, tente novamente.")
            else:
                print("\n⚠️ Nenhum item foi selecionado.")