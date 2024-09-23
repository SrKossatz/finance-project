from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# importar barra de progresso do ttk
from tkinter.ttk import Progressbar

# importar o modulo para plotar graficos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# importar modulo para criar calendario
from tkcalendar import Calendar, DateEntry
from datetime import date

from tkinter import messagebox as MessageBox

# Importar funções da view
from view import *


# ################# cores ###############
co0 = "#2e2d2b"  
co1 = "#feffff"  
co7 = "#3fbfb9"   
co2 = "#4fa882"  
co3 = "#38576b"  
co4 = "#403d3d"   
co5 = "#e06636"   
co6 = "#038cfc"   
co8 = "#263238"   
co9 = "#a9a9a9"   

# colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

# Criando frames
janela = Tk()
janela.title("Finanças")
janela.geometry("900x650")
janela.configure(bg=co9)
janela.resizable(False, False)

style = ttk.Style(janela)
style.theme_use('clam')



frame1 = Frame(janela, width=1043, height=50, bg=co1, relief='flat')
frame1.grid(row=0, column=0)

frame2 = Frame(janela, width=1043, height=361, bg=co1, pady=20, relief='raised')
frame2.grid(row=1, column=0, pady=3, padx=0, sticky=NSEW)

frame3 = Frame(janela, width=1043, height=300, bg=co1, relief='flat')
frame3.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

frame_grafico = Frame(frame2, width=580, height=250, bg=co2)
frame_grafico.place(x=415, y=5)


# Acessar a imagem
img = Image.open('img/python.webp')
img = img.resize((45, 45))
img = ImageTk.PhotoImage(img)

img_logo = Label(frame1, image=img, text=' Orçamento Pessoal', width=900, compound=LEFT, padx=5, relief='raised', anchor='nw', font=('Verdana 20 bold'), bg=co1, fg=co4)
img_logo.place(x=0, y=0)





# Back End - Funções_________________
global tree

def adicionar_categoria():
    nome = inserir_categoria.get()  # Obtém o nome da categoria do campo de texto
    
    if nome == '':
        MessageBox.showinfo('Erro', 'Preencha o campo')  # Valida se o campo está vazio
        return

    # Insere a nova categoria no banco de dados (renomeie a função para evitar o conflito)
    adicionar_categoria_no_bd(nome)
    
    MessageBox.showinfo('Sucesso', 'Categoria adicionada com sucesso')
    
    inserir_categoria.delete(0, END)  # Limpa o campo de entrada após a inserção
    
    # Pega os valores da categoria atualizados
    categorias = ver_categoria()  # Aqui usamos uma variável diferente do nome da função
    
    # Atualiza a lista de categorias no ComboBox
    lista_categorias = []
    
    for i in categorias:
        lista_categorias.append(i[1])  # Adiciona o nome da categoria à lista
    
    # Atualiza a combobox de categorias com a nova lista
    combo_categoria_despesas['values'] = lista_categorias

def adicionar_receita():
    nome = 'Receita'
    data = calendario_receita.get()  # Obtém a data da receita
    valor = valor_receitas.get()  # Obtém o valor da receita
    
    # Lista com os dados para inserção
    lista_inserir = [nome, data, valor]
    
    # Verifica se algum dos campos está vazio
    for i in lista_inserir:
        if i == '':
            MessageBox.showinfo('Erro', 'Preencha todos os campos')  # Mostra erro se houver campos vazios
            return
    
    # Chama a função correta para adicionar a receita ao banco de dados ou sistema de armazenamento
    adicionar_receita_no_bd(nome, data, valor)
    
    # Exibe uma mensagem de sucesso
    MessageBox.showinfo('Sucesso', 'Receita adicionada com sucesso')

    # Limpa os campos após a inserção
    valor_receitas.delete(0, END)
    calendario_receita.delete(0, END)
    
    mostrar_renda()  # Atualiza a tabela de renda
    percentual()  # Atualiza o percentual de gastos
    grafico_barra()  # Atualiza o gráfico de barras
    grafico_pizza()  # Atualiza o gráfico de pizza
    resumo()  # Atualiza o resumo

def adicionar_despesa():
  nome = combo_categoria_despesas.get()  # Obtém o nome da categoria da despesa
  data = calendario_despesa.get()  # Obtém a data da despesa
  valor = valor_despesas.get()  # Obtém o valor da despesa
  
  # Lista com os dados para inserção
  lista_inserir = [nome, data, valor]
  
  # Verifica se algum dos campos está vazio
  for i in lista_inserir:
      if i == '':
          MessageBox.showinfo('Erro', 'Preencha todos os campos')  # Mostra erro se houver campos vazios
          return

  adicionar_despesa_no_bd(nome, data, valor)  # Chama a função correta para adicionar a despesa ao banco de dados ou sistema de armazenamento
  
  MessageBox.showinfo('Sucesso', 'Despesa adicionada com sucesso')
  
  combo_categoria_despesas.set('')  # Limpa o campo de categoria
  valor_despesas.delete(0, END)  # Limpa o campo de valor
  calendario_despesa.delete(0, END)  # Limpa o campo de data
  
  mostrar_renda()  # Atualiza a tabela de renda
  percentual()  # Atualiza o percentual de gastos
  grafico_barra()  # Atualiza o gráfico de barras
  grafico_pizza()  # Atualiza o gráfico de pizza
  resumo()  # Atualiza o resumo

# FIM Back End - Funções_________________

# percentual de gastos

def percentual():
  label_barra = Label(frame2, text='Percentual de receita gasta', height=1, anchor=NW, font=('Verdana 12 bold'), bg=co1, fg=co4)
  label_barra.place(x=7, y=5)
  
  style = ttk.Style()
  style.theme_use('default')
  style.configure("black.Horizontal.TProgressbar",)
  style.configure('TProgressbar', thickness=20)
  
  valor = 50
  label_percentual = Label(frame2, text='{:,.2f}%'.format(valor), anchor=NW, font=('Verdana 12 bold'), bg=co1, fg=co4)
  label_percentual.place(x=200, y=35)
  
  bar = Progressbar(frame2, length=180, mode='determinate')
  bar.place(x=10, y=35)
  bar['value'] = 50
  

# grafico barra

def grafico_barra():
  lista_categorias = ['Renda', 'Despesas', 'Saldo']
  lista_valores = [500, 1000, 1500]
  
  figura = plt.Figure(figsize=(4, 3.45), dpi=60)
  ax = figura.add_subplot(111)
  # ax.autoscale(enable=True, axis='both', tight=None)
  ax.bar(lista_categorias, lista_valores,  color=['#FF5733', '#33FF57', '#3357FF'], width=0.9)

  c = 0
  for i in ax.patches:
      ax.text(i.get_x()-.001, i.get_height()+.5,
              str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
      c += 1

  ax.set_xticks(range(len(lista_categorias)))  # Define os ticks
  ax.set_xticklabels(lista_categorias, fontsize=16)  # Define os labels dos ticks
  
  ax.patch.set_facecolor('#ffffff')
  ax.spines['bottom'].set_color('#CCCCCC')
  ax.spines['bottom'].set_linewidth(1)
  ax.spines['right'].set_linewidth(0)
  ax.spines['top'].set_linewidth(0)
  ax.spines['left'].set_color('#CCCCCC')
  ax.spines['left'].set_linewidth(1)

  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.tick_params(bottom=False, left=False)
  ax.set_axisbelow(True)
  ax.yaxis.grid(False)
  ax.xaxis.grid(False)

  canva = FigureCanvasTkAgg(figura, frame2)
  canva.get_tk_widget().place(x=10, y=70)


def resumo():
  valor = [500, 1000, 1500]
  
  l_linha = Label(frame2, text='', width=150, height=1, anchor=NW, font=('Arial 1'))
  l_linha.place(x=309, y=52)
  l_sumario = Label(frame2, text='Renda Mensal      '.upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#000')
  l_sumario.place(x=309, y=35)
  l_sumario = Label(frame2, text='€ {:,.2f}'.format(valor[0]), anchor=NW, font=('Arial 12'), bg=co1, fg='#545454')
  l_sumario.place(x=309, y=70)
  
  l_linha = Label(frame2, text='', width=170, height=1, anchor=NW, font=('Arial 1'))
  l_linha.place(x=309, y=132)
  l_sumario = Label(frame2, text='Despesas Mensais      '.upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#000')
  l_sumario.place(x=309, y=115)
  l_sumario = Label(frame2, text='€ {:,.2f}'.format(valor[1]), anchor=NW, font=('Arial 12'), bg=co1, fg='#545454')
  l_sumario.place(x=309, y=150)
  
  l_linha = Label(frame2, text='', width=50, height=1, anchor=NW, font=('Arial 1'))
  l_linha.place(x=309, y=207)
  l_sumario = Label(frame2, text='Saldo'.upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#000')
  l_sumario.place(x=309, y=190)
  l_sumario = Label(frame2, text='€ {:,.2f}'.format(valor[1]), anchor=NW, font=('Arial 12'), bg=co1, fg='#545454')
  l_sumario.place(x=309, y=220)


# função grafico pizza

def grafico_pizza():
  
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)
    lista_valores = [345, 225, 534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    # Lista de cores personalizadas
    colors = ['#FF9999', '#66B3FF', '#99FF99']

    # Explode para destacar fatias
    explode = [0.05] * len(lista_categorias)  # Explode igual para todas as fatias

    # Gráfico de pizza
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.8),
           autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)

    # Legenda
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    # Exibir o gráfico na interface Tkinter
    canva_categoria = FigureCanvasTkAgg(figura, frame_grafico)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


grafico_barra()
percentual()  
resumo()
grafico_pizza()


# Criar frames dentro do frame3
frame3_1 = Frame(frame3, width=300, height=250, bg=co1)
frame3_1.grid(row=0, column=0)

frame3_2 = Frame(frame3, width=220, height=250, bg=co1)
frame3_2.grid(row=0, column=1, padx=5)

frame3_3 = Frame(frame3, width=220, height=250, bg=co1)
frame3_3.grid(row=0, column=2, padx=5)


# tabela renda mensal

titlo_tabela_renda = Label(frame2, text='Tabela Receitas e Despesas', anchor='nw', font=('Verdana 12 bold'), bg=co1, fg=co4)
titlo_tabela_renda.place(x=5, y=309)

# Função para mostrar a tabela de renda

def mostrar_renda():
    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela()

    global tree

    tree = ttk.Treeview(frame3_1, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame3_1, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame3_1, orient="horizontal", command=tree.xview)

    # Serve para rolar a tabela
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # Tamanhos das colunas
    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajustar a largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

mostrar_renda()

# ----------------------------Configurações de despesas--------------------------------
label_info = Label(frame3_2, text='Insira novas Despesas', font=('Verdana 10 bold'), bg=co1, fg=co4, anchor='nw')
label_info.place(x=10, y=10)

# categoria
label_categoria = Label(frame3_2, text='Categoria', font=('Ivy 10'), bg=co1, fg=co4, anchor='nw')
label_categoria.place(x=10, y=40)

# Aqui você chama a função que busca as categorias no banco de dados
categorias = ver_categoria()  # Chama a função que retorna as categorias do banco de dados

# Atualiza a lista de categorias com os valores obtidos
lista_categorias = []

for i in categorias:
    lista_categorias.append(i[1])  # Adiciona o nome da categoria à lista

# ComboBox de categorias
combo_categoria_despesas = ttk.Combobox(frame3_2, width=10, font=('Ivy 10'))
combo_categoria_despesas.place(x=110, y=41)

# Insere as categorias na combobox logo na inicialização
combo_categoria_despesas['values'] = lista_categorias


# Calendário Despesas
label_calendario_despesas = Label(frame3_2, text='Data', font=('Ivy 10'), bg=co1, fg=co4, anchor='nw')
label_calendario_despesas.place(x=10, y=70)
calendario_despesa = DateEntry(frame3_2, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy') 
calendario_despesa.place(x=110, y=71)

# Valor

label_valor_despesas = Label(frame3_2, text='Valor', font=('Ivy 10'), bg=co1, fg=co4, anchor='nw')
label_valor_despesas.place(x=10, y=100)
valor_despesas = Entry(frame3_2, width=12, font=('Ivy 10'), justify='left', relief='solid')
valor_despesas.place(x=110, y=101)

# Botão para adicionar despesas
img_button = Image.open('img/add.png')
img_button = img_button.resize((17, 17))
img_button = ImageTk.PhotoImage(img_button)

button_despesas = Button(frame3_2,command=adicionar_despesa, image=img_button, text=' Adicionar'.upper(), width=80, compound=LEFT, anchor='nw', font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
button_despesas.place(x=110, y=131)


# Botão excluir
label_excluir_categoria = Label(frame3_2, text='Excluir', font=('Ivy 10 bold'), bg=co1, fg=co4, anchor='nw')
label_excluir_categoria.place(x=10, y=190)

img_button_delete = Image.open('img/remove.png')
img_button_delete = img_button_delete.resize((17, 17))
img_button_delete = ImageTk.PhotoImage(img_button_delete)

button_delete = Button(frame3_2, image=img_button_delete, text=' Excluir'.upper(), width=80, compound=LEFT, anchor='nw', font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
button_delete.place(x=110, y=190)

# Configuração de Receitas
label_info = Label(frame3_3, text='Insira novas Receitas', font=('Verdana 10 bold'), bg=co1, fg=co4, anchor='nw')
label_info.place(x=10, y=10)

# Calendário Receitas
label_calendario_receitas = Label(frame3_3, text='Data', font=('Ivy 10'), bg=co1, fg=co4, anchor='nw')
label_calendario_receitas.place(x=10, y=40)
calendario_receita = DateEntry(frame3_3, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')  
calendario_receita.place(x=110, y=41)

# Valor Receitas

label_valor_receitas = Label(frame3_3, text='Valor', font=('Ivy 10'), bg=co1, fg=co4, anchor='nw')
label_valor_receitas.place(x=10, y=70)
valor_receitas = Entry(frame3_3, width=12, font=('Ivy 10'), justify='left', relief='solid')
valor_receitas.place(x=110, y=71)


# Botão para adicionar receitas
img_button_receitas = Image.open('img/add.png')
img_button_receitas = img_button_receitas.resize((17, 17))
img_button_receitas = ImageTk.PhotoImage(img_button_receitas)

button_receitas = Button(frame3_3, image=img_button_receitas,command=adicionar_receita, text=' Adicionar'.upper(), width=80, compound=LEFT, anchor='nw', font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
button_receitas.place(x=110, y=111)


# Configuração inserir nova categoria
label_info = Label(frame3_3, text='Categoria', font=('Ivy 10'), bg=co1, fg=co4, anchor='nw')
label_info.place(x=10, y=160)

inserir_categoria = Entry(frame3_3, width=12, font=('Ivy 10'), justify='left', relief='solid')
inserir_categoria.place(x=110, y=160)


# Botão inserir nova categoria
img_button_categoria = Image.open('img/add.png')
img_button_categoria = img_button_categoria.resize((17, 17))
img_button_categoria = ImageTk.PhotoImage(img_button_categoria)

button_categoria = Button(frame3_3, command=adicionar_categoria, image=img_button_categoria, text=' Adicionar'.upper(), width=80, compound=LEFT, anchor='nw', font=('Ivy 7'), bg=co1, fg=co0, overrelief=RIDGE)
button_categoria.place(x=110, y=190)








janela.mainloop()

