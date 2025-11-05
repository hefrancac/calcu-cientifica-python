# 🧮 Calculadora com Interface Gráfica

> Um projeto de calculadora de desktop com visual moderno e funcionalidades padrão e científicas.
> 
> Criado por: **Henrique França**



## 📝 Descrição

Este projeto é uma calculadora completa desenvolvida em **Python** com a biblioteca **Tkinter**. Ela apresenta uma interface de usuário limpa, em tema escuro (dark mode), e é organizada em abas para facilitar o uso, separando as operações básicas das científicas.

---

## ✨ Funcionalidades

A calculadora é dividida em duas seções principais:

### 1. 🖥️ Interface e Design

* **Tema Escuro Moderno:** Interface com cores escuras (`#202020`) para conforto visual.
* **Navegação por Abas:** Separação clara entre os modos "Padrão" e "Científica".
* **Display Duplo:**
    * Um display superior para o **histórico** da expressão (ex: `10 + 5 =`).
    * Um display principal para a **entrada atual** e o **resultado**.
* **Botões Interativos:** Efeito de *hover* (mudança de cor) ao passar o mouse sobre os botões.

### 2. 🔢 Calculadora Padrão

A aba "Padrão" oferece todas as operações aritméticas essenciais:

* **Operações Básicas:** Adição (`+`), Subtração (`-`), Multiplicação (`×`), Divisão (`÷`).
* **Controle:** `C` (Limpar tudo), `CE` (Limpar entrada atual), `⌫` (Apagar).
* **Funções Imediatas:**
    * **`%`**: Porcentagem.
    * **`1/x`**: Inverso de um número.
    * **`x²`**: Elevar ao quadrado.
    * **`√`**: Raiz quadrada.
    * **`±`**: Inverter o sinal do número.

### 3. 🔬 Calculadora Científica

A aba "Científica" expande as capacidades para incluir funções matemáticas avançadas:

* **Controle de Expressão:**
    * **`(`** e **`)`**: Adicionar parênteses para controlar a ordem das operações.
* **Funções Trigonométricas:**
    * `sin`, `cos`, `tan` (calculados em graus).
* **Funções Logarítmicas:**
    * **`ln`**: Logaritmo natural.
    * **`log`**: Logaritmo na base 10.
* **Potenciação e Raízes:**
    * **`x^y`**: Potência (ex: `2**3`).
    * **`x²`**: Quadrado.
    * **`√`**: Raiz quadrada.
* **Constantes:**
    * **`π`** (Pi).
    * **`e`** (Número de Euler).
* **Outras Funções:**
    * **`n!`**: Fatorial.
* **Gerenciamento de Erros:** A calculadora exibe mensagens de erro para entradas inválidas, como "Não é possível dividir por zero".

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Tkinter** (Biblioteca padrão do Python para GUI)
* **Módulo `math`** (Para as funções científicas)

---

## 🚀 Como Executar

1.  Certifique-se de ter o **Python 3** instalado em sua máquina.
2.  Salve o código acima em um arquivo chamado `calculadora.py`.
3.  Abra seu terminal ou prompt de comando.
4.  Navegue até o diretório onde você salvou o arquivo.
5.  Execute o comando:

    ```bash
    python calculadora.py
    ```

6.  A janela da calculadora será aberta.

---

## 👨‍💻 Autor

Este projeto foi desenvolvido e criado por:

**Henrique França**
