'''

Este programa implementa um questionário interativo usando Customkinter uma bibioteca(lib) feita com base no tkinter
site da lib: https://customtkinter.tomschimansky.com/
github: https://github.com/TomSchimansky/CustomTkinter
DOC do tkinter: https://docs.python.org/3/library/tk.html

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


#__ Configuração das cores e estilos do projeto __#
COR_FUNDO = "#2b2b2b"
COR_TEXTO = "#ffffff"
COR_BOTAO = "#3a7ebf"
COR_BOTAO_HOVER = "#2a5d8f"
COR_TEXTO_BOTAO = "#ffffff"

# Configurações de fonte
FONTE_PADRAO = "Helvetica"
TAMANHO_FONTE_TITULO = 28
TAMANHO_FONTE_NORMAL = 20

# Configurações de estilo dos botões
CORNER_RADIUS = 10

# Numero de questões e tempo por questão
NUM_QUESTOES = 5
TEMPO_QUESTAO = 10

# Texto do titulo
TEXTO_INICIAL = "Questionario da apresentação"

# Arquivo json que vai ser utilizado para as perguntas
pergunta = pd.read_json(os.path.join(os.path.dirname(__file__), "pergunta.json"))

# Increase window size
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Adjust button sizes
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40

# O menu principal que vai ser a pagina raiz do projeto
class MenuPrincipal:
    # Quando a classe for chamada vai ser feito a configuração dela
    def __init__(self, master):
        self.master = master
        
        # Obtém as dimensões da tela do compuatador
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        # define a posicao da pagina 
        pos_x = (largura_tela // 2) - (WINDOW_WIDTH // 3)
        pos_y = (altura_tela // 3) - (WINDOW_HEIGHT // 3)
        self.master.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{pos_x}+{pos_y}")
        self.master.resizable(False, False)
        self.master.configure(bg=COR_FUNDO)

        # Título do menu
        self.lb_titulo = ctk.CTkLabel(self.master, text=f"{TEXTO_INICIAL}", 
                                      font=('Cooper Black', TAMANHO_FONTE_TITULO), text_color=COR_TEXTO)
        self.lb_titulo.place(relx=0.5, rely=0.2, anchor='center')

        # Configuração do botão do menu principal usando um discionario
        button_configs = {
            'width': BUTTON_WIDTH,
            'height': BUTTON_HEIGHT,
            'fg_color': COR_BOTAO,
            'text_color': COR_TEXTO_BOTAO,
            'hover_color': COR_BOTAO_HOVER,
            'font': (FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
            'corner_radius': CORNER_RADIUS
        }

        self.btn_iniciar = ctk.CTkButton(self.master, text='Iniciar', command=self.iniciar_questionario, **button_configs) # faz o desempacotamento do discionario declarado acima
        self.btn_iniciar.place(relx=0.5, rely=0.4, anchor='center')

        self.btn_configuracao = ctk.CTkButton(self.master, text='Configuração', command=self.abrir_configuracao, **button_configs)
        self.btn_configuracao.place(relx=0.5, rely=0.55, anchor='center')

        self.btn_aluno_aleatorio = ctk.CTkButton(self.master, text='Selecionar Aluno', command=self.abrir_selecao_aluno, **button_configs)
        self.btn_aluno_aleatorio.place(relx=0.5, rely=0.7, anchor='center')
        
        self.btn_sair = ctk.CTkButton(self.master, text='Sair', command=self.master.quit, **button_configs)
        self.btn_sair.place(relx=0.5, rely=0.85, anchor='center')

    # Limpa a janela atual e inicia o questionário
    def iniciar_questionario(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        Questionario(self.master)

        # Limpa a janela atual e abre a tela de configuração
    def abrir_configuracao(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        Configuracao(self.master)

    # Fução para a seleção dos alunos
    def abrir_selecao_aluno(self):
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        janela_width, janela_height = 500, 300
        pos_x = (largura_tela // 5) - (janela_width // 2)
        pos_y = (altura_tela // 3) - (janela_height // 3)
        janela_selecao = ctk.CTkToplevel(self.master)
        janela_selecao.title("Seleção de Aluno")
        janela_selecao.geometry(f"{janela_width}x{janela_height}+{pos_x}+{pos_y}")
        janela_selecao.resizable(False, False)
        janela_selecao.configure(fg_color=COR_FUNDO)

        # Carregar alunos do arquivo JSON
        alunos = pd.read_json(os.path.join(os.path.dirname(__file__), "alunos.json")).squeeze().tolist()

        label_aluno = ctk.CTkLabel(janela_selecao, text="", font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL), text_color=COR_TEXTO)
        label_aluno.place(relx=0.5, rely=0.3, anchor='center')

        def selecionar_aluno():
            for _ in range(20):  # Simula a roleta girando 20 vezes
                indice = randint(0, len(alunos) - 1)
                aluno = alunos[indice]
                label_aluno.configure(text=aluno)
                janela_selecao.update()
                time.sleep(0.1)
            
            # Depois de rodar 20 vezes seleciona o aluno final
            indice_final = randint(0, len(alunos) - 1)
            aluno_final = alunos[indice_final]
            label_aluno.configure(text=f"Aluno selecionado:\n{aluno_final}")

        btn_selecionar = ctk.CTkButton(janela_selecao, text="Selecionar", command=selecionar_aluno,
                                       fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                       hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                       corner_radius=CORNER_RADIUS)
        btn_selecionar.place(relx=0.5, rely=0.7, anchor='center')

# Pagina onde vai ficar as configurações de numero de questões e tempo por questão
class Configuracao:
    def __init__(self, master):
        self.master = master
        self.master.configure(fg_color=COR_FUNDO)

        # Título da página
        self.lb_titulo = ctk.CTkLabel(self.master, text="Configuração", 
                                      font=(FONTE_PADRAO, TAMANHO_FONTE_TITULO), text_color=COR_TEXTO)
        self.lb_titulo.place(relx=0.5, rely=0.2, anchor='center')

        # Label e entrada para o número de questões
        self.lb_num_questoes = ctk.CTkLabel(self.master, text="Número de questões:", 
                                            font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL), text_color=COR_TEXTO)
        self.lb_num_questoes.place(relx=0.3, rely=0.4, anchor='e')

        self.entry_num_questoes = ctk.CTkEntry(self.master, width=100, height=40, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL))
        self.entry_num_questoes.place(relx=0.35, rely=0.4, anchor='w')
        self.entry_num_questoes.insert(0, NUM_QUESTOES)

        # Label e entrada para o tempo por questão
        self.lb_tempo_questao = ctk.CTkLabel(self.master, text="Tempo por questão (segundos):", 
                                             font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL), text_color=COR_TEXTO)
        self.lb_tempo_questao.place(relx=0.3, rely=0.5, anchor='e')

        self.entry_tempo_questao = ctk.CTkEntry(self.master, width=100, height=40, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL))
        self.entry_tempo_questao.place(relx=0.35, rely=0.5, anchor='w')
        self.entry_tempo_questao.insert(0, TEMPO_QUESTAO)

        # Configuração do botão da pagina Configuração usando um discionario
        button_configs = {
            'width': BUTTON_WIDTH,
            'height': BUTTON_HEIGHT,
            'fg_color': COR_BOTAO,
            'text_color': COR_TEXTO_BOTAO,
            'hover_color': COR_BOTAO_HOVER,
            'font': (FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
            'corner_radius': CORNER_RADIUS
        }

        self.btn_salvar = ctk.CTkButton(self.master, text="Salvar", command=self.salvar_configuracao, **button_configs) # desempacotamento do discionario
        self.btn_salvar.place(relx=0.3, rely=0.7, anchor='center')

        self.btn_voltar = ctk.CTkButton(self.master, text="Voltar", command=self.voltar_menu, **button_configs)
        self.btn_voltar.place(relx=0.7, rely=0.7, anchor='center')

    # Função onde vai verificar se o tamanho indicado na entry é um numero valido
    # Se for valido ele salva como NUM_QUESTOES o controlador de numero de questões
    def salvar_configuracao(self):
        try:
            num_questoes = int(self.entry_num_questoes.get())
            tempo_questao = int(self.entry_tempo_questao.get())
            
            if 1 <= num_questoes <= len(pergunta) and tempo_questao > 0:
                global NUM_QUESTOES, TEMPO_QUESTAO
                NUM_QUESTOES = num_questoes
                TEMPO_QUESTAO = tempo_questao
                self.voltar_menu()
            else:
                if not (1 <= num_questoes <= len(pergunta)):
                    messagebox.showerror("Erro", f"O número de questões deve estar entre 1 e {len(pergunta)}")
                if tempo_questao <= 0:
                    messagebox.showerror("Erro", "O tempo por questão deve ser maior que 0 segundos")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos")

    def voltar_menu(self):
        # Limpa a janela e volta para o menu principal
        for widget in self.master.winfo_children():
            widget.destroy()
        MenuPrincipal(self.master)

# Classe onde vai ficar a janela onde serão respondidas as questões
class Questionario:
    def __init__(self, master):
        self.master = master
        self.master.configure(fg_color=COR_FUNDO)

	    #_ Criação da estrutura da pagina _#
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
                                         wraplength=WINDOW_WIDTH-40, justify="left",
                                         font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL))
        self.lb_enunciado.place(x=20, y=20)

        # Cria 5 radio button onde vai ficar as alternativas
        self.radio_var = ctk.IntVar(value=-1)
        self.radiob_alternativas = []
        for i in range(5):
            rb = ctk.CTkRadioButton(self.master, text="", variable=self.radio_var, value=i,
                                    text_color=COR_TEXTO, fg_color=COR_BOTAO,
                                    font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL))
            self.radiob_alternativas.append(rb)
            rb.place(x=20, y=100 + i*50)

        # Cria uma label para mostrar se a resposta está correta ou não
        self.lb_feedback = ctk.CTkLabel(self.master, text="", text_color=COR_TEXTO,
                                        font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL))
        self.lb_feedback.place(x=20, y=WINDOW_HEIGHT-200)

        # Cria uma barra de progresso para o temporizador
        self.progress_bar = ctk.CTkProgressBar(self.master, width=WINDOW_WIDTH-40, height= 20)
        self.progress_bar.place(x=20, y=WINDOW_HEIGHT-150)
        self.progress_bar.set(0)

        # Variável para controlar o temporizador
        self.timer = None
        self.is_running = True  # Nova variável para controlar se o questionário está ativo

        # Configuração do botão do Questionario usando um discionario
        button_configs = {
            'width': BUTTON_WIDTH,
            'height': BUTTON_HEIGHT,
            'fg_color': COR_BOTAO,
            'text_color': COR_TEXTO_BOTAO,
            'hover_color': COR_BOTAO_HOVER,
            'font': (FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
            'corner_radius': CORNER_RADIUS
        }

        self.btn_proximo = ctk.CTkButton(self.master, text="Próximo", command=self.pegar_resposta, **button_configs) # desempacotamento do discionario
        self.btn_proximo.place(x=WINDOW_WIDTH-20, y=WINDOW_HEIGHT-20, anchor='se')

        self.btn_sair = ctk.CTkButton(self.master, text="Sair", command=self.sair, **button_configs)
        self.btn_sair.place(x=20, y=WINDOW_HEIGHT-20, anchor='sw')

        # Atualiza a primeira questão
        self.atualizar_questao()

    # Gera uma lista de índices aleatórios únicos para não ser sequencia
    def gerar_indices_aleatorios(self):
        indices = []
        while len(indices) < self.num_questoes:
            indice = randint(0, len(pergunta) - 1)
            if indice not in indices:
                indices.append(indice)
        return indices

    # Usa o índice aleatório para selecionar a questão
    def atualizar_questao(self):
        indice_questao = self.indices_questoes[self.controle]
        self.lb_enunciado.configure(text=f"{self.controle+1}. {pergunta.loc[indice_questao, 'enunciado']}")
        for i, rb in enumerate(self.radiob_alternativas):
            rb.configure(text=pergunta.loc[indice_questao, "alternativas"][i])
        self.radio_var.set(value=-1)
        self.lb_feedback.configure(text="")
        self.btn_proximo.configure(text="Responder", command=self.pegar_resposta)
        self.iniciar_temporizador()

    # Cancela o temporizador anterior, se existir
    def iniciar_temporizador(self):
        if self.timer:
            self.master.after_cancel(self.timer)
        self.progress_bar.set(0)
        self.atualizar_temporizador()

    # Controla o temporizador e atualiza o progress bar
    def atualizar_temporizador(self):
        if not self.is_running:
            return

        valor_atual = self.progress_bar.get()
        if valor_atual < 1:
            try:
                self.progress_bar.set(valor_atual + 0.1/TEMPO_QUESTAO)   
                self.timer = self.master.after(100, self.atualizar_temporizador)  
            except Exception:
                # Se ocorrer um erro ao atualizar a progress bar, vai simplismente ingnorar
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

# Classe onde vai ficar a pagina final com o resulta de quantas questões foram acertadas
class PaginaResposta:
    def __init__(self, master, respostas):
        self.master = master
        self.master.configure(fg_color=COR_FUNDO)

        # Calcula o número de respostas corretas
        self.corretas = 0
        for indice_questao, resposta in respostas:
            if resposta != -1:  # Verifica se uma pergunta foi respondida porque -1 e o numero usado para definir vazio
                alternativa_selecionada = pergunta.loc[indice_questao, "alternativas"][resposta]
                if alternativa_selecionada == pergunta.loc[indice_questao, "correta"]:
                    self.corretas += 1

        # Título da página
        self.lb_titulo = ctk.CTkLabel(self.master, text="Resultados", 
                                      font=(FONTE_PADRAO, TAMANHO_FONTE_TITULO), text_color=COR_TEXTO)
        self.lb_titulo.place(relx=0.5, rely=0.3, anchor='center')

        # Mostra o resultado do questionario
        self.lb_resultado = ctk.CTkLabel(self.master, 
                                         text=f"Você acertou {self.corretas} de {len(respostas)} questões!",
                                         font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL), text_color=COR_TEXTO)
        self.lb_resultado.place(relx=0.5, rely=0.5, anchor='center')

        # Botão para voltar ao menu principal
        self.btn_voltar = ctk.CTkButton(self.master, text="Voltar ao Menu", command=self.voltar_menu,
                                        width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                                        fg_color=COR_BOTAO, text_color=COR_TEXTO_BOTAO,
                                        hover_color=COR_BOTAO_HOVER, font=(FONTE_PADRAO, TAMANHO_FONTE_NORMAL),
                                        corner_radius=CORNER_RADIUS)
        self.btn_voltar.place(relx=0.5, rely=0.7, anchor='center')

    # Limpa a janela e volta para o menu principal
    def voltar_menu(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        MenuPrincipal(self.master)

# Configuração da raiz do projeto onde vai ser criada a pagina
def mostrar_menu():
    app = ctk.CTk()
    app.configure(fg_color=COR_FUNDO)
    MenuPrincipal(app)
    app.mainloop()

if __name__ == "__main__":
    mostrar_menu()