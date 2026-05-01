import customtkinter as ctk
import subprocess
import os

class CompilerUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EZEQUIEL Compiler IDE - Punto 5")
        self.geometry("1100x700")

        # Configuración de columnas
        self.grid_columnconfigure(0, weight=1) # Editor
        self.grid_columnconfigure(1, weight=1) # Salidas
        self.grid_rowconfigure(1, weight=1)

        # 1. Título y Botón de Compilar
        self.btn_compile = ctk.CTkButton(self, text="COMPILAR PROYECTO", command=self.run_full_pipeline, fg_color="#2ecc71", hover_color="#27ae60")
        self.btn_compile.grid(row=0, column=0, columnspan=2, pady=15, padx=20, sticky="ew")

        # 2. Panel Izquierdo: Editor de Código
        self.lbl_editor = ctk.CTkLabel(self, text="Código Fuente (.src)", font=("Arial", 14, "bold"))
        self.lbl_editor.grid(row=1, column=0, sticky="nw", padx=25)
        
        self.txt_editor = ctk.CTkTextbox(self, font=("Consolas", 14))
        self.txt_editor.grid(row=1, column=0, padx=20, pady=(30, 20), sticky="nsew")

        # 3. Panel Derecho: Pestañas de Visualización (Fases del compilador)
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=1, column=1, padx=20, pady=(10, 20), sticky="nsew")
        
        self.tab_console = self.tabview.add("Consola/Errores")
        self.tab_tac = self.tabview.add("Código TAC")
        self.tab_llvm = self.tabview.add("LLVM IR")

        # Widgets de texto para cada fase
        self.txt_console = ctk.CTkTextbox(self.tab_console, font=("Consolas", 12))
        self.txt_console.pack(fill="both", expand=True)

        self.txt_tac = ctk.CTkTextbox(self.tab_tac, font=("Consolas", 12))
        self.txt_tac.pack(fill="both", expand=True)

        self.txt_llvm = ctk.CTkTextbox(self.tab_llvm, font=("Consolas", 12))
        self.txt_llvm.pack(fill="both", expand=True)

    def run_full_pipeline(self):
        # Guardar el código actual para que el pipeline lo procese
        content = self.txt_editor.get("1.0", "end")
        with open("input/programa.txt", "w", encoding="utf-8") as f:
            f.write(content)

        # Ejecutar el pipeline.py (Responsabilidad del Integrante 6)
        try:
            result = subprocess.run(['python3', 'pipeline.py'], capture_output=True, text=True)
            
            # Mostrar logs en la consola
            self.txt_console.delete("1.0", "end")
            self.txt_console.insert("1.0", result.stdout + "\n" + result.stderr)

            # Cargar los archivos generados por los integrantes 3 y 4
            self.load_phase_files()
        except Exception as e:
            self.txt_console.insert("end", f"\nError al conectar con el pipeline: {e}")

    def load_phase_files(self):
        # Leer TAC (Integrante 3)
        if os.path.exists("output.tac"):
            with open("output.tac", "r") as f:
                self.txt_tac.delete("1.0", "end")
                self.txt_tac.insert("1.0", f.read())
        
        # Leer LLVM (Integrante 4)
        if os.path.exists("output.ll"):
            with open("output.ll", "r") as f:
                self.txt_llvm.delete("1.0", "end")
                self.txt_llvm.insert("1.0", f.read())

if __name__ == "__main__":
    app = CompilerUI()
    app.mainloop()