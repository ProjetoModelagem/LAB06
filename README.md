# 📷 Processamento de Imagens

## 📌 Operações Morfológicas

Nesta etapa são realizadas operações que modificam a estrutura das imagens, com o objetivo de melhorar a representação visual e facilitar a análise posterior.

1. **Imagens intermediárias**:  
   ![Operações Morfológicas](https://github.com/user-attachments/assets/fdfa07f6-a29c-49ef-a6b8-5b129e03e720)

   As imagens representam, em ordem:
   - Original RGB, Blur, Escala de Cinza, Threshold  
   - Erosão, Dilatação, Abertura, Fechamento  
   - Gradiente Morfológico, TopHat, BlackHat  

### ✅ **Imagem Final Destacada (Fechamento Morfológico)**  

Esta imagem final mostra o resultado da operação de fechamento morfológico, utilizada principalmente para remover pequenos buracos e preencher regiões.

![Imagem Final - Fechamento](https://github.com/user-attachments/assets/69ba3602-2ac9-4c12-afba-14766d48bd4e)

---

## 📌 Espaço de Cores

Nesta etapa, a imagem original é convertida em diferentes espaços de cores para facilitar análises específicas de cor, luminosidade e saturação.

1. **Imagens intermediárias**:  
   ![Espaço de Cores](https://github.com/user-attachments/assets/cce26f1c-a8f2-4265-97e7-a8c9cf0c4920)

   As imagens representam, em ordem:
   - RGB (original), Cinza, HSV, HLS

### ✅ **Imagem Final Destacada (HSV)**  

A imagem final destaca o espaço HSV, que separa cor (Hue), saturação (Saturation) e valor de brilho (Value), facilitando a análise visual de áreas específicas.

![Imagem Final - HSV](https://github.com/user-attachments/assets/c8ed4962-7e92-4b4d-acf8-9c8436da3674)

---

## 📌 Detecção de Contornos

Nesta etapa, são destacadas as bordas e contornos relevantes na imagem, utilizando técnicas como Thresholding, suavização e o algoritmo Canny para detecção de bordas.

1. **Imagens intermediárias**:  
   ![Detecção de Contornos](https://github.com/user-attachments/assets/a9da85d7-3e2c-4b71-a771-e15b0612447d)


   As imagens representam, em ordem:
   - Original, Blur, Escala de Cinza, Canny sem Blur  
   - Canny com Blur, Threshold, Abertura Morfológica, Contornos Detectados

### ✅ **Imagem Final Destacada (Contornos)**  

A imagem final apresenta os contornos detectados, claramente destacados sobre a imagem original, facilitando análises de formas e objetos presentes.

![Imagem Final - Contornos](https://github.com/user-attachments/assets/f092755d-603b-422b-a6e7-956a5d4fdc7a)

