# 📷 Processamento de Imagens

## 📌 Operações Morfológicas

Nesta etapa são realizadas operações que modificam a estrutura das imagens, com o objetivo de melhorar a representação visual e facilitar a análise posterior.

1. **Imagens intermediárias**:  
   ![Operações Morfológicas](https://github.com/user-attachments/assets/e1bc7c82-f8a4-4aed-9063-18778a29e768)

   As imagens representam, em ordem:
   - Original RGB, Blur, Escala de Cinza, Threshold  
   - Erosão, Dilatação, Abertura, Fechamento  
   - Gradiente Morfológico, TopHat, BlackHat  

### ✅ **Imagem Final Destacada (Fechamento Morfológico)**  

Esta imagem final mostra o resultado da operação de fechamento morfológico, utilizada principalmente para remover pequenos buracos e preencher regiões.

![Imagem Final - Fechamento](https://github.com/user-attachments/assets/eecd7cf9-81ec-4b89-82a3-f3399b57d1a3)

---

## 📌 Espaço de Cores

Nesta etapa, a imagem original é convertida em diferentes espaços de cores para facilitar análises específicas de cor, luminosidade e saturação.

1. **Imagens intermediárias**:  
   ![Espaço de Cores](https://github.com/user-attachments/assets/e83bff43-b8df-4c3e-a63b-bff3ee118a35)

   As imagens representam, em ordem:
   - RGB (original), Cinza, HSV, HLS

### ✅ **Imagem Final Destacada (HSV)**  

A imagem final destaca o espaço HSV, que separa cor (Hue), saturação (Saturation) e valor de brilho (Value), facilitando a análise visual de áreas específicas.

![Imagem Final - HSV](https://github.com/user-attachments/assets/7790c560-978e-4479-b692-214e83b18028)

---

## 📌 Detecção de Contornos

Nesta etapa, são destacadas as bordas e contornos relevantes na imagem, utilizando técnicas como Thresholding, suavização e o algoritmo Canny para detecção de bordas.

1. **Imagens intermediárias**:  
   ![Detecção de Contornos](https://github.com/user-attachments/assets/e006dbb1-3080-4459-b20f-cf880989bdb8)

   As imagens representam, em ordem:
   - Original, Blur, Escala de Cinza, Canny sem Blur  
   - Canny com Blur, Threshold, Abertura Morfológica, Contornos Detectados

### ✅ **Imagem Final Destacada (Contornos)**  

A imagem final apresenta os contornos detectados, claramente destacados sobre a imagem original, facilitando análises de formas e objetos presentes.

![Imagem Final - Contornos](https://github.com/user-attachments/assets/3f1e2b15-01c8-4c32-aa8b-5cad670e2755)
