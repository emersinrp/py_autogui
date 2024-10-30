import pyautogui
import random
import time

def evitar_suspensao(intervalo=30):
    largura, altura = pyautogui.size()

    print("Iniciando a automação para evitar suspensão... Pressione Ctrl+C para parar.")
    
    try:
        while True:
            x = random.randint(0, largura - 1)
            y = random.randint(0, altura - 1)
            
            pyautogui.moveTo(x, y, duration=0.5)
            
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nAutomação encerrada pelo usuário.")

# Executa a função com um intervalo de 30 segundos
evitar_suspensao(intervalo=30)