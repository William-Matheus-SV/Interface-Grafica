from tkinter import *
from datetime import *     

#Cadastro dos Protudos
produtos = {
    1: ("Óleo Lubrificante", 50.00),
    2: ("Filtro de Ar", 14.00),
    3: ("Filtro de Óleo", 25.00),
    4: ("Bateria", 498.90),
    5: ("Pneu Aro 15 Direction", 289.90),
    #6: ("Óleo Motor Sintético", 27.04),
    7:("Vela Ignição", 15.36),
    8:("Descarbonizante", 25.39),
    #9:("Filtro Injeção", 11.33),
    #10:("Abraçadeira Plástica", 1.05),
   #11:("Kit Correia Dentada + Tensor Onix 1.0 1.4 8V", 141.17),
    #12:("Tensor Cva", 106.90),
    #13:("Rolamento Roda Ts ( Kit )" , 59.37),
    #14:("Bateria", 562.04),
    #15:("Bateria Moto", 192.17),
    16:("Atuador Embreagem", 265.08),
    #17:("Disco de Freio Dt Ventilado", 150.30),
    18:("Lampada Polo Led", 7.35)
}
#Cadastro dos Serviços
servicos = {
    1:("Manutenção preventiva", 200.00),
    2:("Reparo nos freios", 100.00),
    3:("Verificação das baterias e sistema de ignição", 80.00),
    4:("Consertos na climatização do veículo", 150.00),
    5:("Alinhamento e Balanceamento dos Pneus", 70.00),
    6:("Revisão geral", 250.00),
    7:("Lavagem", 50.00),
    8:("Lavagem + Polimento", 80.00),
    9:("Lavagem + Polimento + Higienização interna e externa", 180.00)

}
#Mecânico Virtual
mecanico_virtual = {
    1:"Problemas nos freios",
    2:"Bateria descarregada",
    3:"Superaquecimento do motor",
    4:"Problemas de transmissão",
    5:"Fusíveis queimados",
    #6:"Luzes do painel piscando",
    #7:"Sistema de áudio com mau funcionamento",
    #8:"Vazamentos de óleo",
    #9:"Vazamentos de líquido de arrefecimento",
    10:"Pneus desgastados",
    11:"Molas quebradas",
    12:"Problemas na suspensão",
    #13:"Falha no sistema de ignição",
    14:"Problemas de alinhamento",
    #15:"Sensor de oxigênio defeituoso",
    #16:"Problemas de embreagem",
    #17:"Sistema de ar condicionado com mau funcionamento",
   #18:"Falha no sistema de direção assistida",
    19:"Não sei identificar"
    
}
#respostas Mecânico Virutal
respostas_mecanico_virtual = {
    1: "Verifique as pastilhas e discos de freio, pode haver desgaste excessivo.",
    2: "Recarregue ou substitua a bateria. Verifique o funcionamento do alternador e inspecione o sistema elétrico do veículo para identificar possíveis falhas.",
    3: "Confira o nível do líquido de arrefecimento, reparar vazamentos, substituir o termostato defeituoso e assegurar que o ventilador do radiador esteja funcionando corretamente.",
    4: "Pode ser desgaste na transmissão. Visite a uma unidade fisica e comunique ao mecânico especializado.",
    5: "Troque o fusível queimado e verifique a causa do problema elétrico.",
    #6: "Pode haver mau contato. Leve para um diagnóstico elétrico.",
    #7: "Verifique conexões e fusíveis. Pode ser falha no rádio ou sistema elétrico.",
    #8: "Será necessário identificar a origem do vazamento, realizar as substituições necessárias de juntas ou vedantes, e garantir que o motor esteja corretamente selado para evitar futuros vazamentos.",
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
#variaveis Globais 
vars_produtos = {}
vars_servicos = {}
carrinho = []
#Inicio das funções
def adicionar_ao_carrinho(vars_produtos, vars_servicos, janela):
    global carrinho
    
    
    #Para produtos entrarem no carrinho
    for codigo, var in vars_produtos.items():
         if var.get()== 1:
            carrinho.append((produtos[codigo][0], produtos[codigo][1]))#adiciona ao carrinho por nome e preço
    
    #Para serviços entrarem no carrinho
    for codigo, var in vars_servicos.items():
        if var.get() == 1:
           carrinho.append((servicos[codigo][0], servicos[codigo][1]))
        print("Itens adicionados ao carrinho:")
        
    for item in carrinho:
            print(f"{item[0]} - R${item[1]:.2f}")
            
    # Verifica se nenhum item foi selecionado
    if not any(var.get() for var in vars_produtos.values()) and not any(var.get() for var in vars_servicos.values()):
        Label(janela, text="Nenhum item selecionado", fg="red", font=("Arial", 12), bg="#F5F5F5").pack(pady=10)
        return
  
def mostrar_carrinho(janela):
    tela_de_resumo = Toplevel(janela)
    tela_de_resumo.title("Adicionado ao carrinho")
    
    # Cria o widget de texto
    text_widget = Text(tela_de_resumo, height=20, width=50, font=("Arial", 12))
    text_widget.pack(padx=10, pady=10)
            
    # Monta o texto do resumo
    if not carrinho:
      resumo_texto = "Carrinho vazio!"
    else:
      resumo_texto = ""
                
      total = 0
      for item in carrinho:
        resumo_texto += f"{item[0]} - R${item[1]:.2f}\n"
        total += item[1]
        
    resumo_texto += f"\nTotal: R${total:.2f}"
            
    # Insere o texto no widget
    text_widget.insert(END, resumo_texto)
    text_widget.config(state=DISABLED) 
                     
# Função que vamos chamar para fazer um resumo de nota fiscal
def gerar_resumo(nome_cliente, telefone_cliente):
    resumo = "------------------- Nota Fiscal ------------------- \n"
    resumo += f"Cliente: {nome_cliente}\n"
    resumo += f"Telefone: {telefone_cliente}\n"
    resumo += f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"

    if not carrinho:
        resumo += "\nCarrinho vazio!\n"
        return resumo

    resumo += "\nItens:\n"
    total = 0
    for nome_item, preco_item in carrinho:
        resumo += f"- {nome_item}: R$ {preco_item:.2f}\n"
        total += preco_item

    desconto = total * 0.10 if total > 200 else 0
    total_final = total - desconto

    resumo += "\n--------------------------------------------\n"
    resumo += f"💰Valor total dos itens: R${total:.2f}\n"
    resumo += f"✅Valor do desconto: R${desconto:.2f}\n"
    resumo += f"💰Valor final a ser pago: R${total_final:.2f}\n"
    resumo += f"🙏Obrigado pela sua compra. {nome_cliente}\n Volte sempre!\n"
    resumo += "----------------------------------------------\n"

    return resumo

def finalizar_compra(nome, telefone, carrinho):
    resumo_texto = gerar_resumo(nome, telefone)
    tela_final = Toplevel()
    tela_final.title("Resumo da Compra")

    text_widget = Text(tela_final, height=20, width=60, font=("Arial", 12))
    text_widget.pack(padx=10, pady=10)
    text_widget.insert(END, resumo_texto)
    text_widget.config(state=DISABLED)
    
    #Esvaziando o carrinho para uma nova compra
    carrinho.clear()
    
    


def mostrar_resposta(codigo):
    resposta = respostas_mecanico_virtual.get(codigo, "Sem resposta disponível.")
    janela_resposta = Toplevel()
    janela_resposta.title("Respostas do Mecânico Virtual")
    #janela para a resposta
    Label(janela_resposta, 
          text= resposta,
          font=("Arial", 14),
          wraplength=400, justify="left").pack(padx=30, pady=30)
    #Destroi a resposta na tela 
    Button(janela_resposta, text = "Fechar",
           command = janela_resposta.destroy).pack(pady=10)

#Iniciando a Interface
def iniciar_interface(): 
    janela=Tk()
    janela.geometry("800x650")
    janela.title("Auto-Peças Soluções Automobilísticas")
    janela.config(bg="#F5F5F5")
    
    
    # Função para limpar a tela
    def limpar_tela():
        for widget in janela.winfo_children():
            widget.destroy()
    #Função para fechar        
    def janela_destroy():
            janela.destroy()
    #Mensagem de Boas Vindas Tela Inicial
   
    Label(janela, text="Bem-vindo à Auto-Peças Soluções Automobilísticas",
          font=("Arial", 20, "bold"), 
          bg="#F5F5F5").pack(pady=20)
    #Janela solicitando nome 
    Label(janela, text="Digite seu nome:",
          font=("Arial", 16),
          bg="#F5F5F5").pack()
    #Coletando o nome 
    entrada_nome = Entry(janela, font=("Arial", 14))
    entrada_nome.pack(pady=10)
    #Janela solicitando telefone
    Label(janela, text="Digite seu telefone:",
            font=("Arial", 16),
            bg="#F5F5F5").pack()
    #Colentando o telefone
    entrada_telefone = Entry(janela, font=("Arial", 14))
    entrada_telefone.pack(pady=10)
    
    def mostrar_menu(nome, telefone):
        limpar_tela()
        Label(janela, text=f"Olá, {nome}- Escolha uma opção:", 
              font=("Arial", 18, "bold"),
              bg="#F5F5F5").pack(pady=20)

        Button(janela, text="🛒 Produtos", font=("Arial", 16), command=lambda:mostrar_produtos(nome, telefone)).pack(pady=10)
        Button(janela, text="🛠 Serviços", font=("Arial", 16), command=lambda:mostrar_servicos(nome, telefone)).pack(pady=10)
        Button(janela, text="🤖 Mecânico Virtual", font=("Arial", 16), command=lambda:mostrar_mecanico_virtual(nome, telefone)).pack(pady=10)
        Button(janela, text="✅ Finalizar compra", font=("Arial", 14),command=lambda: finalizar_compra(nome, telefone, carrinho)).pack(pady=10)
        Button(janela, text="❌ Sair", font=("Arial", 16), command=lambda:(janela_destroy(), iniciar_interface())).pack(pady=(0,10))

    #Testes para nome e telefone só passarem com valores validos do tipo String e Numeros inteiros respectivamente
    #Função do botão entrar
    def entrar ():
        nome = entrada_nome.get().strip() #Remove espaços antes e depois do nome.
        telefone = entrada_telefone.get().strip()
        #Condição para só aceitar Strings como valores para nome
        #isalpha para garantir que só terá strings e not nome para garantir que não seja um valor vazio.
        #not telefone.isdigit para não passar nenhum valor em telefone que não seja um número.
        if not nome or not nome.replace(" ", "").isalpha() or not telefone.isdigit(): 
            Label(janela, text="⚠️ Por favor, insira um nome e um telefone válido!",
                  fg="red",
                  font=("Arial", 12)).pack()
            return
    
        mostrar_menu(nome, telefone)
    #Botão de Entrar         
    botao_entrar = Button(janela, text="Entrar", font=("Arial", 14), command=entrar)
    botao_entrar.pack(pady=10)
            
    # Texto do menu Produtos - Serviços - Mecânico Virtual
    texto_menu = Label(janela, text="", font=("Arial", 14), bg="#F5F5F5")
    texto_menu.pack(pady=20)
    
    # Tela de Produtos
    #Função dos Produtos
    def mostrar_produtos(nome, telefone):
        limpar_tela()
        Label(janela, text="Produtos Disponivéis", 
              font=("Arial", 20, "bold"),
              bg="#F5F5F5" ).pack(pady=20)
        
        # Variável para armazenar os checkboxes
        vars_produtos={}
        for codigo, (nome_produto, preco_produto) in produtos.items():
            var = IntVar()
            botao_produto = Checkbutton(janela, text=f"{nome_produto} - R${preco_produto:.2f}",
                        variable = var,
                        font=("Arial", 14),
                        bg = "#F5F5F5",
                        anchor = "w")
            botao_produto.pack(anchor = "w")
            vars_produtos[codigo]= var
            
                            
        #Criando os botões dentro da função gerar resumo produtos
        #Botão 1 simula uma nota fiscal de produtos
        Button(janela, text ="Adicionar ao carrinho", font=("Arial", 14), command=lambda: [adicionar_ao_carrinho(vars_produtos, vars_servicos, janela), mostrar_carrinho(janela)]).pack(pady=5)
        #Botão 2 voltar a tela do Menu
        Button(janela, text="Voltar", font=("Arial", 14), command=lambda:mostrar_menu(nome, telefone)).pack(pady=20)
                    
    # Tela de Serviços
    def mostrar_servicos(nome, telefone):
        limpar_tela()
        Label(janela, text="Serviços Disponivéis", font=("Arial", 20, "bold"), 
              bg="#F5F5F5").pack(pady=20)
        #Variavel para armazenar os checkboxes
        vars_servicos = {}
        for codigo, (nome_servico, preco_servico) in servicos.items():
            var = IntVar()
            botao_servico = Checkbutton(janela, text=f"{nome_servico} - R${preco_servico:.2f}",
                                        variable= var,
                                        font=("Arial", 14),
                                        bg = "#F5F5F5",
                                        anchor = "w")
            botao_servico.pack(anchor = "w")
            vars_servicos[codigo] = var      
                      
        #Criando os botões dentro da função gerar resumo dos serviços
        #Botão 1 simula uma nota fiscal de serviços
        Button(janela, text ="Adicionar ao carrinho", font=("Arial", 14), command=lambda: [adicionar_ao_carrinho(vars_produtos, vars_servicos, janela), mostrar_carrinho(janela)]).pack(pady=5)
        #Botão 2 voltar a tela do Menu
        Button(janela, text="Voltar", font=("Arial", 14), command=lambda:mostrar_menu(nome, telefone)).pack(pady=20)
                     


# Tela do Mecânico Virtual
    def mostrar_mecanico_virtual(nome, telefone):
        limpar_tela()
        Label(janela, text=" Selecione o problema do veículo: ", font=("Arial", 20, "bold"), 
              bg="#F5F5F5").pack(pady=20)
        
        #Variavel que vai ser a escolha do radiobutton
        escolha = IntVar(value=0)
        #Criando o Radiobutton
        for codigo, problema in mecanico_virtual.items():
            Radiobutton(janela, 
                        text=problema, 
                        variable=escolha,
                        value=codigo,
                        font=("Arial", 14),
                        anchor="w",
                        justify="left").pack(anchor="w", padx = 20)
            
        Button(janela, text="Ver resposta",
               font=("Arial",14),
               command=lambda: mostrar_resposta(escolha.get())).pack(pady=10)  
          
        Button(janela, text = "Voltar", 
               font=("Arial", 14), 
               command =lambda: mostrar_menu(nome, telefone)).pack(pady=20)
        



    janela.mainloop()
    
iniciar_interface()    