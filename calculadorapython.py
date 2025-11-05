import tkinter as tk
from tkinter import ttk
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("380x550")
        self.root.resizable(False, False)
        
        # Cores do tema
        self.bg_color = "#202020"
        self.button_bg = "#323232"
        self.button_equals_bg = "#0078d4"
        self.text_color = "#ffffff"
        
        # Variáveis de controle
        self.expressao = ""
        self.display_var = tk.StringVar()
        self.display_historico = tk.StringVar()
        
        self.configurar_estilo()
        self.criar_interface()
    
    def configurar_estilo(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=self.bg_color, borderwidth=0)
        style.configure('TNotebook.Tab', 
                       background=self.bg_color, 
                       foreground=self.text_color,
                       padding=[20, 10],
                       borderwidth=0)
        style.map('TNotebook.Tab',
                 background=[('selected', self.bg_color)],
                 foreground=[('selected', '#0078d4')])
    
    def criar_interface(self):
        self.root.configure(bg=self.bg_color)
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill="both")
        
        # Display
        display_frame = tk.Frame(main_frame, bg=self.bg_color)
        display_frame.pack(fill="x", padx=0, pady=10)
        
        historico_label = tk.Label(
            display_frame,
            textvariable=self.display_historico,
            font=("Segoe UI", 12),
            bg=self.bg_color,
            fg="#cccccc",
            anchor="e",
            padx=20
        )
        historico_label.pack(fill="x", pady=5)
        
        display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Segoe UI", 36, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            anchor="e",
            padx=20
        )
        display.pack(fill="x", pady=10)
        self.display_var.set("0")
        
        # Abas
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(expand=True, fill="both", padx=0, pady=0)
        
        frame_basica = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(frame_basica, text="Padrão")
        self.criar_botoes_basicos(frame_basica)
        
        frame_cientifica = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(frame_cientifica, text="Científica")
        self.criar_botoes_cientificos(frame_cientifica)
    
    def criar_botao(self, parent, texto, comando, linha, coluna, colspan=1, cor_bg=None):
        if cor_bg is None:
            cor_bg = self.button_bg
        
        btn = tk.Button(
            parent,
            text=texto,
            font=("Segoe UI", 14),
            bg=cor_bg,
            fg=self.text_color,
            bd=0,
            relief="flat",
            activebackground="#3d3d3d",
            activeforeground=self.text_color,
            command=comando,
            cursor="hand2"
        )
        
        def on_enter(e):
            btn['background'] = '#3d3d3d'
        
        def on_leave(e):
            btn['background'] = cor_bg
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.grid(row=linha, column=coluna, columnspan=colspan, sticky="nsew", padx=2, pady=2, ipady=15)
        
        return btn
    
    def criar_botoes_basicos(self, frame):
        botoes = [
            [('%', 'special'), ('CE', 'special'), ('C', 'special'), ('⌫', 'special')],
            [('1/x', 'operator'), ('x²', 'operator'), ('√', 'operator'), ('÷', 'operator')],
            [('7', 'number'), ('8', 'number'), ('9', 'number'), ('×', 'operator')],
            [('4', 'number'), ('5', 'number'), ('6', 'number'), ('-', 'operator')],
            [('1', 'number'), ('2', 'number'), ('3', 'number'), ('+', 'operator')],
            [('±', 'number'), ('0', 'number'), ('.', 'number'), ('=', 'equals')]
        ]
        
        for i, linha in enumerate(botoes):
            for j, (texto, tipo) in enumerate(linha):
                cor_bg = self.button_equals_bg if tipo == 'equals' else self.button_bg
                self.criar_botao(frame, texto, lambda t=texto: self.processar_clique(t), 
                               i, j, cor_bg=cor_bg)
        
        for i in range(6):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            frame.grid_columnconfigure(j, weight=1)
    
    def criar_botoes_cientificos(self, frame):
        botoes = [
            [('(', 'operator'), (')', 'operator'), ('C', 'special'), ('⌫', 'special')],
            [('sin', 'function'), ('cos', 'function'), ('tan', 'function'), ('÷', 'operator')],
            [('ln', 'function'), ('log', 'function'), ('√', 'function'), ('×', 'operator')],
            [('π', 'function'), ('e', 'function'), ('x²', 'function'), ('-', 'operator')],
            [('7', 'number'), ('8', 'number'), ('9', 'number'), ('+', 'operator')],
            [('4', 'number'), ('5', 'number'), ('6', 'number'), ('x^y', 'function')],
            [('1', 'number'), ('2', 'number'), ('3', 'number'), ('n!', 'function')],
            [('±', 'number'), ('0', 'number'), ('.', 'number'), ('=', 'equals')]
        ]
        
        for i, linha in enumerate(botoes):
            for j, (texto, tipo) in enumerate(linha):
                cor_bg = self.button_equals_bg if tipo == 'equals' else self.button_bg
                self.criar_botao(frame, texto, lambda t=texto: self.processar_clique(t), 
                               i, j, cor_bg=cor_bg)
        
        for i in range(8):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            frame.grid_columnconfigure(j, weight=1)
    
    def processar_clique(self, valor):
        if valor == 'C':
            self.expressao = ""
            self.display_var.set("0")
            self.display_historico.set("")
        
        elif valor == 'CE':
            self.expressao = ""
            self.display_var.set("0")
        
        elif valor == '⌫':
            if self.expressao:
                self.expressao = self.expressao[:-1]
                self.display_var.set(self.expressao if self.expressao else "0")
        
        elif valor == '=':
            self.calcular()
        
        elif valor == '±':
            if self.expressao:
                if self.expressao[0] == '-':
                    self.expressao = self.expressao[1:]
                else:
                    self.expressao = '-' + self.expressao
                self.display_var.set(self.expressao)
        
        elif valor == '√':
            self.expressao += "sqrt("
            self.display_var.set(self.expressao)
        
        elif valor == 'x²':
            if self.expressao:
                self.expressao = f"({self.expressao})**2"
                self.calcular()
        
        elif valor == '1/x':
            if self.expressao:
                self.expressao = f"1/({self.expressao})"
                self.calcular()
        
        elif valor == 'x^y':
            self.expressao += "**"
            self.display_var.set(self.expressao)
        
        elif valor == 'sin':
            self.expressao += "sin("
            self.display_var.set(self.expressao)
        
        elif valor == 'cos':
            self.expressao += "cos("
            self.display_var.set(self.expressao)
        
        elif valor == 'tan':
            self.expressao += "tan("
            self.display_var.set(self.expressao)
        
        elif valor == 'ln':
            self.expressao += "log("
            self.display_var.set(self.expressao)
        
        elif valor == 'log':
            self.expressao += "log10("
            self.display_var.set(self.expressao)
        
        elif valor == 'n!':
            if self.expressao:
                self.expressao = f"factorial({self.expressao})"
                self.calcular()
        
        elif valor == 'π':
            self.expressao += "pi"
            self.display_var.set(self.expressao)
        
        elif valor == 'e':
            self.expressao += "e"
            self.display_var.set(self.expressao)
        
        elif valor == '÷':
            self.expressao += "/"
            self.display_var.set(self.expressao)
        
        elif valor == '×':
            self.expressao += "*"
            self.display_var.set(self.expressao)
        
        elif valor == '%':
            self.expressao += "/100*"
            self.display_var.set(self.expressao)
        
        else:
            if self.display_var.get() == "0" and valor not in ['+', '-', '*', '/']:
                self.expressao = str(valor)
            else:
                self.expressao += str(valor)
            self.display_var.set(self.expressao)
    
    def calcular(self):
        try:
            expressao_original = self.expressao
            expressao_processada = self.expressao
            
            # Substitui funções trigonométricas
            expressao_processada = expressao_processada.replace('sin(', 'math.sin(math.radians(')
            expressao_processada = expressao_processada.replace('cos(', 'math.cos(math.radians(')
            expressao_processada = expressao_processada.replace('tan(', 'math.tan(math.radians(')
            
            # Substitui funções matemáticas
            expressao_processada = expressao_processada.replace('sqrt(', 'math.sqrt(')
            expressao_processada = expressao_processada.replace('log(', 'math.log(')
            expressao_processada = expressao_processada.replace('log10(', 'math.log10(')
            expressao_processada = expressao_processada.replace('factorial(', 'math.factorial(int(')
            expressao_processada = expressao_processada.replace('pi', 'math.pi')
            expressao_processada = expressao_processada.replace('e', 'math.e')
            
            # Adiciona parênteses extras
            count_radians = expressao_processada.count('math.radians(')
            expressao_processada = expressao_processada.replace('math.radians(', 'math.radians((')
            expressao_processada += ')' * count_radians
            
            count_factorial = expressao_processada.count('math.factorial(int(')
            expressao_processada += '))' * count_factorial
            
            resultado = eval(expressao_processada)
            
            if isinstance(resultado, float):
                resultado = round(resultado, 10)
                resultado_str = f"{resultado:.10f}".rstrip('0').rstrip('.')
            else:
                resultado_str = str(resultado)
            
            self.display_historico.set(expressao_original + " =")
            self.display_var.set(resultado_str)
            self.expressao = resultado_str
        
        except ZeroDivisionError:
            self.display_var.set("Não é possível dividir por zero")
            self.expressao = ""
        
        except ValueError:
            self.display_var.set("Entrada inválida")
            self.expressao = ""
        
        except Exception:
            self.display_var.set("Erro")
            self.expressao = ""

def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()