# %%

txt = "Meu novo arquivo de texto\n"

nome_arquivo = "historia_02.txt"

# w = novo arquivo / a = adicionar nova escrita
with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)