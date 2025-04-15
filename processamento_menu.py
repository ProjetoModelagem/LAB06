# Como rodar o código: 
# No terminal digite: python processamento_menu.py

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import sys

# Lista de imagens disponíveis
imagens_disponiveis = ["GIRAFA.jpeg", "SATELITE.jpeg", "AVIAO.jpeg"]

# Obter caminho absoluto universal da pasta atual
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

def aguardar_e_sair():
    print("🟡 Pressione qualquer tecla para voltar ao menu.")
    plt.waitforbuttonpress()
    plt.close()

def mostrar_imagens(titulo, lista_imgs):
    total = len(lista_imgs)
    colunas = math.ceil(math.sqrt(total))
    linhas = math.ceil(total / colunas)
    plt.figure(figsize=(15, 10))
    for i, (desc, img) in enumerate(lista_imgs):
        plt.subplot(linhas, colunas, i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(desc, fontsize=9)
        plt.axis('off')
    plt.suptitle(titulo, fontsize=14)
    plt.tight_layout()
    plt.show(block=False)
    aguardar_e_sair()

def destacar_imagem(titulo, imagem):
    plt.figure(figsize=(10, 8))
    plt.imshow(imagem, cmap='gray')
    plt.title(titulo, fontsize=14)
    plt.axis('off')
    plt.show(block=False)
    aguardar_e_sair()

def carregar_imagem(nome_img):
    caminho_img = os.path.join(PASTA_ATUAL, nome_img)
    img = cv2.imread(caminho_img)
    if img is None:
        print(f"❌ Erro ao carregar {caminho_img}. Verifique a imagem.")
        sys.exit(1)
    return img

def operacoes_morfologicas(img_nome):
    img = carregar_imagem(img_nome)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_blur = cv2.blur(img, (5, 5))
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)
    a = img_gray.max()
    _, thresh = cv2.threshold(img_gray, a/2 + 100, a, cv2.THRESH_BINARY_INV)
    kernel = np.ones((12, 12), np.uint8)

    img_dilate = cv2.dilate(thresh, kernel, iterations=1)
    img_erode = cv2.erode(thresh, kernel, iterations=1)
    img_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    img_close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    img_grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
    img_tophat = cv2.morphologyEx(thresh, cv2.MORPH_TOPHAT, kernel)
    img_blackhat = cv2.morphologyEx(thresh, cv2.MORPH_BLACKHAT, kernel)

    imagens = [
        ('Original RGB', img),
        ('Blur', img_blur),
        ('Cinza', img_gray),
        ('Threshold', thresh),
        ('Erosão', img_erode),
        ('Dilatação', img_dilate),
        ('Abertura (Open)', img_open),
        ('Fechamento (Close)', img_close),
        ('Gradiente', img_grad),
        ('TopHat', img_tophat),
        ('BlackHat', img_blackhat)
    ]

    mostrar_imagens(f'Morfologia - {img_nome}', imagens)
    destacar_imagem(f'Fechamento (Final) - {img_nome}', img_close)

def espaco_cores(img_nome):
    img = carregar_imagem(img_nome)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    imagens = [
        ('RGB', img_rgb),
        ('Cinza', img_gray),
        ('HSV', img_hsv),
        ('HLS', img_hls)
    ]

    mostrar_imagens(f'Espaço de Cores - {img_nome}', imagens)
    destacar_imagem(f'Final: HSV - {img_nome}', img_hsv)

def contornos(img_nome):
    img = carregar_imagem(img_nome)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    a = img_gray.max()
    _, thresh = cv2.threshold(img_gray, a / 2 * 1.7, a, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5, 5), np.uint8)
    thresh_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    img_blur = cv2.blur(img_gray, ksize=(5, 5))
    edges_gray = cv2.Canny(img_gray, a/2, a/2)
    edges_blur = cv2.Canny(img_blur, a/2, a/2)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    img_copy = img.copy()
    final = cv2.drawContours(img_copy, contours, -1, (255, 0, 0), 2)

    imagens = [
        ('Original', img),
        ('Blur', img_blur),
        ('Cinza', img_gray),
        ('Canny sem Blur', edges_gray),
        ('Canny com Blur', edges_blur),
        ('Threshold', thresh),
        ('Open', thresh_open),
        ('Contornos', final)
    ]

    mostrar_imagens(f'Contornos - {img_nome}', imagens)
    destacar_imagem(f'Final: Contornos - {img_nome}', final)

def menu():
    while True:
        print("\n📷 PROCESSAMENTO DE IMAGENS - MENU")
        print("1. Operações Morfológicas")
        print("2. Espaço de Cores")
        print("3. Contornos")
        print("4. Sair")
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '4':
            print("Encerrando...")
            break
        if opcao not in ['1', '2', '3']:
            print("Opção inválida.")
            continue

        print("\nImagens disponíveis:")
        for i, nome in enumerate(imagens_disponiveis, 1):
            print(f"{i}. {nome}")
        escolha = input("Escolha a imagem (1-3): ")

        if escolha not in ['1', '2', '3']:
            print("Imagem inválida.")
            continue

        img_escolhida = imagens_disponiveis[int(escolha)-1]

        if opcao == '1': operacoes_morfologicas(img_escolhida)
        if opcao == '2': espaco_cores(img_escolhida)
        if opcao == '3': contornos(img_escolhida)

if __name__ == "__main__":
    menu()