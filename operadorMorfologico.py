# pip install opencv-python matplotlib
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
import os

# Lista de imagens disponíveis na pasta
imagens_entrada = ['GIRAFA.jpeg', 'SATELITE.jpeg', 'AVIAO.jpeg']

for nome_img in imagens_entrada:
    print(f"Processando imagem: {nome_img}")

    # 1. Carregar imagem e converter para RGB
    img = cv2.imread(nome_img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 2. Aplicar filtro de ruído (blur)
    img_blur = cv2.blur(img, (5, 5))

    # 3. Converter para escala de cinza
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)

    # 4. Aplicar limiarização (threshold) para binarização
    a = img_gray.max()
    _, thresh = cv2.threshold(img_gray, a / 2 + 100, a, cv2.THRESH_BINARY_INV)

    # 5. Definir kernel para operações morfológicas
    kernel = np.ones((12, 12), np.uint8)

    # 6. Aplicar operações morfológicas
    img_dilate = cv2.dilate(thresh, kernel, iterations=1)
    img_erode = cv2.erode(thresh, kernel, iterations=1)
    img_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    img_close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    img_grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
    img_tophat = cv2.morphologyEx(thresh, cv2.MORPH_TOPHAT, kernel)
    img_blackhat = cv2.morphologyEx(thresh, cv2.MORPH_BLACKHAT, kernel)

    # 7. Organizar imagens para visualização intermediária
    imagens_intermedias = [
        ('Imagem original (RGB)', img),
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

    # 8. Plotar imagens intermediárias
    total = len(imagens_intermedias)
    colunas = math.ceil(math.sqrt(total))
    linhas = math.ceil(total / colunas)

    plt.figure(figsize=(15, 10))
    for i, (titulo, imagem) in enumerate(imagens_intermedias):
        plt.subplot(linhas, colunas, i + 1)
        plt.imshow(imagem, cmap='gray')
        plt.title(titulo, fontsize=9)
        plt.axis('off')
    plt.suptitle(f'Processamento Morfológico - {nome_img}', fontsize=14)
    plt.tight_layout()
    plt.show()

    # 9. Exibir imagem final destacada (Fechamento, por exemplo)
    plt.figure(figsize=(10, 8))
    plt.imshow(img_close, cmap='gray')
    plt.title(f"Imagem Final Destacada ({nome_img}) - Fechamento (Close)", fontsize=14)
    plt.axis('off')
    plt.show()
