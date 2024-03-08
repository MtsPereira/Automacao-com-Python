#Passo a passo do projeto
#Passo 1: entrar no sistema da empresa 
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado
# pyautogui.hotkey("crtl", "v") -> combinação de teclas

#abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no site 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#dar uma pausa um pouco maior (3 segundos)
time.sleep(4)

#Passo 2: fazer login
pyautogui.click(x=-814, y=414) #< coloca aqui nos parenteses a posição
pyautogui.write("mp_07@gmail.com")

#escrever a senha
pyautogui.press("tab")
pyautogui.write("96857447")

#clicar no botão de logar 
pyautogui.click(x=-657, y=572) #< coloca aqui a posição 
time.sleep(3)



#Passo 3: importar a base de dados
import pandas as pd 
tabela = pd.read_csv("produtos.csv")
print(tabela)

#Passo 4: cadastrar 1 produto
#para cada linha da minha tabela
for linha in tabela.index:
    #clicar no 1 campo
    pyautogui.click(x=-926, y=294) #colocar aqui a posição
    
    #codigo do produto         coluna
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo) 
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha,"marca"])  
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha,"tipo"]) 
    pyautogui.press("tab")
    
    #categoria
    #str() string -> texto
    #str(1) -> 1 -> "1"
    pyautogui.write(str(tabela.loc[linha,"categoria"])) 
    pyautogui.press("tab")

    #preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"])) 
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))  
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

#Passo 5: repetir o processo de cadastro até acabar