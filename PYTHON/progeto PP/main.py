'''

Este programa implementa um questionário interativo usando Customkinter uma bibioteca(lib) motificada com base no tkinter
site da lib: https://customtkinter.tomschimansky.com/
github: https://github.com/TomSchimansky/CustomTkinter


Antes de começa digite esse comando no terminal para vai baixar os requisitos necessário: 
     pip install -r requisitos.txt  


#__Estrutura do algoritimo__#
- MenuPrincipal
A classe onde vai ficar o loop principal, onde todas as outras paginas levam para essa

- Configuração 
A classe Onde eu configuro a quantidade e tempo das questões 

- Questionario
A classe onde a parte principal do programa fica, onde serão mostradas o questionario

- PaginaResposta
A classe onde no final do questionario vai mostrar o resultado de quantas questões foram respondidas e quantas foram acertadas

'''

import customtkinter as ctk
import pandas as pd

from tkinter import messagebox
from random import randint
import time
import os

# Configuração das cores e estilos do projeto
COR_FUNDO = "#2b2b2b"
COR_TEXTO = "#ffffff"
COR_BOTAO = "#3a7ebf"
COR_BOTAO_HOVER = "#2a5d8f"
COR_TEXTO_BOTAO = "#ffffff"  

# Configurações de fonte
FONTE_PADRAO = "Helvetica"
TAMANHO_FONTE_TITULO = 24
TAMANHO_FONTE_NORMAL = 14

# Configurações de estilo dos botões
CORNER_RADIUS = 10

# Numero de questões e tempo por questão
NUM_QUESTOES = 5
TEMPO_QUESTAO = 5 

# Arquivo json que vai ser utilizado
pergunta = pd.read_json(os.path.join(os.path.dirname(__file__), "pergunta.json"))

# O menu principal que vai ser a pagina raiz do projeto
class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.geometry("820x420")
        self.master.resizable(False, False)
        self.master.configure(bg=COR_FUNDO)

        # Centraliza a janela na tela
        self.centralizar_janela()

        # Título do menu
        self.lb_titulo = ctk.CTkLabel(self.master, text="Menu Principal", 
                                      font=("Helvetica", 24), text_color=COR_TEXTO)
        self.lb_titulo.place(relx=0.5, rely=0.2, anchor='center')

        # Cria botões para iniciar o questionário, configuração e sair
        self.btn_iniciar = ctk.CTkButton(self.master, text='Iniciar', command=self.iniciar_questionario,
                                         fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                         hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                         corner_radius=CORNER_RADIUS)
        self.btn_iniciar.place(relx=0.5, rely=0.4, anchor='center')

        self.btn_configuracao = ctk.CTkButton(self.master, text='Configuração', command=self.abrir_configuracao,
                                              fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                              hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                              corner_radius=CORNER_RADIUS)
        self.btn_configuracao.place(relx=0.5, rely=0.5, anchor='center')

        self.btn_sair = ctk.CTkButton(self.master, text='Sair', command=self.master.quit,
                                      fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                      hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                      corner_radius=CORNER_RADIUS)
        self.btn_sair.place(relx=0.5, rely=0.6, anchor='center')

        # Novo botão para selecionar aluno aleatório
        self.btn_aluno_aleatorio = ctk.CTkButton(self.master, text='Selecionar Aluno', command=self.abrir_selecao_aluno,
                                                 fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                                 hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                                 corner_radius=CORNER_RADIUS)
        self.btn_aluno_aleatorio.place(relx=0.5, rely=0.7, anchor='center')

    def centralizar_janela(self):
        # Obtém as dimensões da tela
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        # Calcula a posição para centralizar
        pos_x = (largura_tela // 2) - (820 // 2)
        pos_y = (altura_tela // 2) - (420 // 2)

        # Define a geometria da janela
        self.master.geometry(f"820x420+{pos_x}+{pos_y}")

    def iniciar_questionario(self):
        # Limpa a janela atual e inicia o questionário
        for widget in self.master.winfo_children():
            widget.destroy()
        Questionario(self.master)

    def abrir_configuracao(self):
        # Limpa a janela atual e abre a tela de configuração
        for widget in self.master.winfo_children():
            widget.destroy()
        Configuracao(self.master)

    def abrir_selecao_aluno(self):
        janela_selecao = ctk.CTkToplevel(self.master)
        janela_selecao.title("Seleção de Aluno")
        janela_selecao.geometry("400x200")
        janela_selecao.configure(bg=COR_FUNDO)

        # Carregar alunos do arquivo JSON
        alunos = pd.read_json("alunos.json").squeeze().tolist()

        label_aluno = ctk.CTkLabel(janela_selecao, text="", font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL), text_color=COR_TEXTO)
        label_aluno.place(relx=0.5, rely=0.3, anchor='center')

        def selecionar_aluno():
            for _ in range(20):  # Simula a roleta girando 20 vezes
                indice = randint(0, len(alunos) - 1)
                aluno = alunos[indice]
                label_aluno.configure(text=aluno)
                janela_selecao.update()
                time.sleep(0.1)
            
            # Seleciona o aluno final
            indice_final = randint(0, len(alunos) - 1)
            aluno_final = alunos[indice_final]
            label_aluno.configure(text=f"Aluno selecionado:\n{aluno_final}")

        btn_selecionar = ctk.CTkButton(janela_selecao, text="Selecionar", command=selecionar_aluno,
                                       fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                       hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                       corner_radius=CORNER_RADIUS)
        btn_selecionar.place(relx=0.5, rely=0.7, anchor='center')

class Configuracao:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg=COR_FUNDO)

        # Título da página
        self.lb_titulo = ctk.CTkLabel(self.master, text="Configuração", 
                                      font=("Helvetica", 24), text_color=COR_TEXTO)
        self.lb_titulo.place(relx=0.5, rely=0.2, anchor='center')

        # Label e entrada para o número de questões
        self.lb_num_questoes = ctk.CTkLabel(self.master, text="Número de questões:", 
                                            text_color=COR_TEXTO)
        self.lb_num_questoes.place(relx=0.3, rely=0.4, anchor='e')

        self.entry_num_questoes = ctk.CTkEntry(self.master, width=50)
        self.entry_num_questoes.place(relx=0.35, rely=0.4, anchor='w')
        self.entry_num_questoes.insert(0, NUM_QUESTOES)  # Valor padrão

        # Botão para salvar configuração
        self.btn_salvar = ctk.CTkButton(self.master, text="Salvar", command=self.salvar_configuracao,
                                        fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                        hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                        corner_radius=CORNER_RADIUS)
        self.btn_salvar.place(relx=0.4, rely=0.6, anchor='center')

        # Botão para voltar ao menu principal
        self.btn_voltar = ctk.CTkButton(self.master, text="Voltar", command=self.voltar_menu,
                                        fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                        hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                        corner_radius=CORNER_RADIUS)
        self.btn_voltar.place(relx=0.6, rely=0.6, anchor='center')

    def salvar_configuracao(self):
        try:
            num_questoes = int(self.entry_num_questoes.get())
            if 1 <= num_questoes <= len(pergunta):
                global NUM_QUESTOES
                NUM_QUESTOES = num_questoes
                self.voltar_menu()
            else:
                messagebox.showerror("Erro", f"O número de questões deve estar entre 1 e {len(pergunta)}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido")

    def voltar_menu(self):
        # Limpa a janela e volta para o menu principal
        for widget in self.master.winfo_children():
            widget.destroy()
        MenuPrincipal(self.master)

class Questionario:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg=COR_FUNDO)

        # Variável que vai controlar as questões
        self.controle = 0

        # Um array que vai receber as respostas do usuário
        self.respostas = []

        # Use NUM_QUESTOES para limitar o número de questões
        self.num_questoes = min(NUM_QUESTOES, len(pergunta))

        # Cria uma lista de índices aleatórios para as questões
        self.indices_questoes = self.gerar_indices_aleatorios()

        # Cria um label que vai ser usado como enunciado da questão
        self.lb_enunciado = ctk.CTkLabel(self.master, text="", text_color=COR_TEXTO, 
                                         wraplength=780, justify="left")
        self.lb_enunciado.place(x=20, y=20)

        # Cria um radio button que vai receber as respostas das questões
        self.radio_var = ctk.IntVar(value=-1)
        self.radiob_alternativas = []
        for i in range(5):
            rb = ctk.CTkRadioButton(self.master, text="", variable=self.radio_var, value=i,
                                    text_color=COR_TEXTO, fg_color=COR_BOTAO)
            self.radiob_alternativas.append(rb)
            rb.place(x=20, y=80 + i*30)

        # Cria uma label para mostrar se a resposta está correta ou não
        self.lb_feedback = ctk.CTkLabel(self.master, text="", text_color=COR_TEXTO)
        self.lb_feedback.place(x=20, y=240)

        # Cria uma barra de progresso para o temporizador
        self.progress_bar = ctk.CTkProgressBar(self.master, width=780)
        self.progress_bar.place(x=20, y=280)
        self.progress_bar.set(0)

        # Variável para controlar o temporizador
        self.timer = None
        self.is_running = True  # Nova variável para controlar se o questionário está ativo

        # Cria botões para a próxima página e para sair
        self.btn_proximo = ctk.CTkButton(self.master, text="Próximo", command=self.pegar_resposta,
                                         fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                         hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                         corner_radius=CORNER_RADIUS)
        self.btn_proximo.place(x=720, y=400, anchor='se')

        self.btn_sair = ctk.CTkButton(self.master, text="Sair", command=self.sair,
                                      fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                      hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                      corner_radius=CORNER_RADIUS)
        self.btn_sair.place(x=100, y=400, anchor='sw')

        # Atualiza a primeira questão
        self.atualizar_questao()

    def gerar_indices_aleatorios(self):
        # Gera uma lista de índices aleatórios únicos
        indices = []
        while len(indices) < self.num_questoes:
            indice = randint(0, len(pergunta) - 1)
            if indice not in indices:
                indices.append(indice)
        return indices

    def atualizar_questao(self):
        # Usa o índice aleatório para selecionar a questão
        indice_questao = self.indices_questoes[self.controle]
        self.lb_enunciado.configure(text=f"{self.controle+1}. {pergunta.loc[indice_questao, 'enunciado']}")
        for i, rb in enumerate(self.radiob_alternativas):
            rb.configure(text=pergunta.loc[indice_questao, "alternativas"][i])
        self.radio_var.set(value=-1)
        self.lb_feedback.configure(text="")
        self.btn_proximo.configure(text="Responder", command=self.pegar_resposta)
        self.iniciar_temporizador()

    def iniciar_temporizador(self):
        # Cancela o temporizador anterior, se existir
        if self.timer:
            self.master.after_cancel(self.timer)
        self.progress_bar.set(0)
        self.atualizar_temporizador()

    def atualizar_temporizador(self):
        if not self.is_running:
            return

        valor_atual = self.progress_bar.get()
        if valor_atual < 1:
            try:
                self.progress_bar.set(valor_atual + 0.1/TEMPO_QUESTAO)   
                self.timer = self.master.after(100, self.atualizar_temporizador)  
            except Exception:
                # Se ocorrer um erro ao atualizar a barra de progresso, apenas ignore
                pass
        else:
            self.pegar_resposta(tempo_esgotado=True)

    def pegar_resposta(self, tempo_esgotado=False):
        if self.timer:
            self.master.after_cancel(self.timer)
            self.timer = None

        if tempo_esgotado:
            resposta_selecionada = -1
        else:
            resposta_selecionada = self.radio_var.get()
            if resposta_selecionada == -1:
                messagebox.showwarning("Aviso", "Por favor, selecione uma alternativa antes de prosseguir.")
                self.iniciar_temporizador()  
                return

        # Verifica a resposta e mostra o feedback
        indice_questao = self.indices_questoes[self.controle]
        resposta_correta = pergunta.loc[indice_questao, "correta"]

        if resposta_selecionada != -1:
            alternativa_selecionada = pergunta.loc[indice_questao, "alternativas"][resposta_selecionada]
            if alternativa_selecionada == resposta_correta:
                self.lb_feedback.configure(text="Resposta correta!", text_color="green")
            else:
                self.lb_feedback.configure(text=f"Resposta incorreta. A resposta correta era: {resposta_correta}", text_color="red")
        else:
            self.lb_feedback.configure(text="Tempo esgotado! Nenhuma resposta selecionada.", text_color="orange")

        self.respostas.append((indice_questao, resposta_selecionada))
        self.btn_proximo.configure(text="Próxima questão", command=self.proxima_questao)

    def proxima_questao(self):
        self.controle += 1
        if self.controle < self.num_questoes:
            self.atualizar_questao()
        else:
            self.is_running = False  # Marca o questionário como inativo
            self.mostrar_resultados()

    def mostrar_resultados(self):
        self.is_running = False  # Garante que o questionário está marcado como inativo
        # Cancela o temporizador se ainda estiver ativo
        if self.timer:
            self.master.after_cancel(self.timer)
            self.timer = None
        # Limpa a janela atual e mostra os resultados
        for widget in self.master.winfo_children():
            widget.destroy()
        PaginaResposta(self.master, self.respostas)

    def sair(self):
        self.is_running = False  # Marca o questionário como inativo
        # Cancela o temporizador se ainda estiver ativo
        if self.timer:
            self.master.after_cancel(self.timer)
            self.timer = None
        # Limpa a janela e volta para o menu principal
        for widget in self.master.winfo_children():
            widget.destroy()
        MenuPrincipal(self.master)

class PaginaResposta:
    def __init__(self, master, respostas):
        self.master = master
        self.master.configure(bg=COR_FUNDO)

        # Calcula o número de respostas corretas
        self.corretas = 0
        for indice_questao, resposta in respostas:
            if resposta != -1:  # Verifica se uma resposta foi selecionada
                alternativa_selecionada = pergunta.loc[indice_questao, "alternativas"][resposta]
                if alternativa_selecionada == pergunta.loc[indice_questao, "correta"]:
                    self.corretas += 1

        # Título da página
        self.lb_titulo = ctk.CTkLabel(self.master, text="Resultados", 
                                      font=("Helvetica", 24), text_color=COR_TEXTO)
        self.lb_titulo.place(relx=0.5, rely=0.2, anchor='center')

        # Mostra o resultado
        self.lb_resultado = ctk.CTkLabel(self.master, 
                                         text=f"Você acertou {self.corretas} de {len(respostas)} questões!",
                                         font=("Helvetica", 18), text_color=COR_TEXTO)
        self.lb_resultado.place(relx=0.5, rely=0.4, anchor='center')

        # Botão para voltar ao menu principal
        self.btn_voltar = ctk.CTkButton(self.master, text="Voltar ao Menu", command=self.voltar_menu,
                                        fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                        hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                        corner_radius=CORNER_RADIUS)
        self.btn_voltar.place(relx=0.5, rely=0.6, anchor='center')

    def voltar_menu(self):
        # Limpa a janela e volta para o menu principal
        for widget in self.master.winfo_children():
            widget.destroy()
        MenuPrincipal(self.master)

# Configuração da raiz do projeto onde vai ser criada a pagina
def mostrar_menu():
    app = ctk.CTk()
    app.configure(bg=COR_FUNDO)
    MenuPrincipal(app)
    app.mainloop()

if __name__ == "__main__":
    mostrar_menu()