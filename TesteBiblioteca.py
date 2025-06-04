import sqlite3
import tkinter as tk
from tkinter import messagebox

# Banco de dados
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Tabelas auxiliares
cursor.execute("CREATE TABLE IF NOT EXISTS Editora (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS Categoria (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS Autor (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

# Tabela principal
cursor.execute("""
CREATE TABLE IF NOT EXISTS Livro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    subtitulo TEXT,
    ano_publicacao INTEGER NOT NULL,
    editora_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    autor_id INTEGER NOT NULL,
    idioma TEXT NOT NULL,
    resumo TEXT,
    FOREIGN KEY (editora_id) REFERENCES Editora(id),
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id),
    FOREIGN KEY (autor_id) REFERENCES Autor(id)
)
""")
conn.commit()

# Interface
janela = tk.Tk()
janela.title("Cadastro de Livros")
janela.geometry("500x500")

# Funções
def cadastrar():
    try:
        dados = {
            "Título": titulo.get(),
            "Subtítulo": subtitulo.get(),
            "Ano de Publicação": ano.get(),
            "ID Editora": editora.get(),
            "ID Categoria": categoria.get(),
            "ID Autor": autor.get(),
            "Idioma": idioma.get(),
            "Resumo": resumo.get("1.0", tk.END).strip()
        }

        with open("livros.txt", "a", encoding="utf-8") as f:
            f.write("\n--- Novo Livro ---\n")
            for campo, valor in dados.items():
                f.write(f"{campo}: {valor}\n")

        messagebox.showinfo("Sucesso", "Livro salvo no arquivo livros.txt!")
        limpar_campos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar: {e}")

def limpar_campos():
    for campo in [titulo, subtitulo, ano, editora, categoria, autor, idioma]:
        campo.delete(0, tk.END)
    resumo.delete("1.0", tk.END)

# Layout uniforme
LARGURA_CAMPO = 40

tk.Label(janela, text="Título:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
titulo = tk.Entry(janela, width=LARGURA_CAMPO)
titulo.grid(row=0, column=1, pady=5)

tk.Label(janela, text="Subtítulo:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
subtitulo = tk.Entry(janela, width=LARGURA_CAMPO)
subtitulo.grid(row=1, column=1, pady=5)

tk.Label(janela, text="Ano de Publicação:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
ano = tk.Entry(janela, width=LARGURA_CAMPO)
ano.grid(row=2, column=1, pady=5)

tk.Label(janela, text="ID da Editora:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
editora = tk.Entry(janela, width=LARGURA_CAMPO)
editora.grid(row=3, column=1, pady=5)

tk.Label(janela, text="ID da Categoria:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
categoria = tk.Entry(janela, width=LARGURA_CAMPO)
categoria.grid(row=4, column=1, pady=5)

tk.Label(janela, text="ID do Autor:").grid(row=5, column=0, sticky="e", padx=10, pady=5)
autor = tk.Entry(janela, width=LARGURA_CAMPO)
autor.grid(row=5, column=1, pady=5)

tk.Label(janela, text="Idioma:").grid(row=6, column=0, sticky="e", padx=10, pady=5)
idioma = tk.Entry(janela, width=LARGURA_CAMPO)
idioma.grid(row=6, column=1, pady=5)

tk.Label(janela, text="Resumo:").grid(row=7, column=0, sticky="ne", padx=10, pady=5)
resumo = tk.Text(janela, width=LARGURA_CAMPO, height=5)
resumo.grid(row=7, column=1, pady=5)

tk.Button(janela, text="Cadastrar Livro", width=30, command=cadastrar).grid(row=8, column=1, pady=15)

janela.mainloop()
