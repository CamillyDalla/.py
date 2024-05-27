import tkinter as tk
from tkinter import messagebox

def coletar_informacao():
    nome = nome_entry.get()
    email = email_entry.get()
    comentario = comentario_entry.get()
    if nome and email and comentario:
        return nome, email, comentario
    else:
        messagebox.showerror("Erro", "Por favor, insira seu nome, e-mail e comentário.")

def coletar_avaliacao():
    try:
        avaliacao = int(avaliacao_entry.get())
        if 1 <= avaliacao <= 5:
            return avaliacao
        else:
            messagebox.showerror("Erro", "Por favor, insira um número entre 1 e 5.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def resposta_satisfacao(avaliacao):
    if avaliacao == 5:
        return "Excelente! Estamos muito felizes que você teve uma experiência ótima!"
    elif avaliacao == 4:
        return "Ficamos felizes que você teve uma boa experiência. Agradecemos pelo feedback!"
    elif avaliacao == 3:
        return "Obrigado pela sua avaliação. Vamos nos esforçar para melhorar."
    elif avaliacao == 2:
        return "Sentimos muito que sua experiência não foi satisfatória. Vamos melhorar."
    elif avaliacao == 1:
        return "Lamentamos saber que sua experiência foi ruim. Vamos trabalhar para melhorar."

def submit_avaliacao():
    informacoes = coletar_informacao()
    if informacoes:
        nome, email, comentario = informacoes
        avaliacao = coletar_avaliacao()
        if avaliacao:
            mensagem = resposta_satisfacao(avaliacao)
            messagebox.showinfo("Avaliação", f"Olá, {nome}! {mensagem}\nObrigado por nos avaliar, {email}. Sua avaliação foi registrada. Comentário: {comentario}\nAgradecemos seu feedback!")

# Criando a janela principal
root = tk.Tk()
root.title("Avaliação da Loja")

# Criando e posicionando os widgets
tk.Label(root, text="Nome:").grid(row=0, column=0)
nome_entry = tk.Entry(root)
nome_entry.grid(row=0, column=1)

tk.Label(root, text="E-mail:").grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

tk.Label(root, text="Avaliação (1-5):").grid(row=2, column=0)
avaliacao_entry = tk.Entry(root)
avaliacao_entry.grid(row=2, column=1)

tk.Label(root, text="Comentário:").grid(row=3, column=0)
comentario_entry = tk.Entry(root)
comentario_entry.grid(row=3, column=1)

submit_button = tk.Button(root, text="Enviar Avaliação", command=submit_avaliacao)
submit_button.grid(row=4, columnspan=2)

# Rodando a aplicação
root.mainloop()
