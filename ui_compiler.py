import customtkinter as ctk
import subprocess
import os

class CompilerUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EZEQUIEL Compiler IDE - Punto 5")
        self.geometry("1100x700")

        # Configuración de columnas
        self.grid_columnconfigure(0, weight=1)  # Editor
        self.grid_columnconfigure(1, weight=1)  # Salidas
        self.grid_rowconfigure(1, weight=1)

        # Botón compilar
        self.btn_compile = ctk.CTkButton(
            self,
            text="COMPILAR PROYECTO",
            command=self.run_full_pipeline,
            fg_color="#2ecc71",
            hover_color="#27ae60"
        )
        self.btn_compile.grid(row=0, column=0, columnspan=2, pady=15, padx=20, sticky="ew")

        # Editor
        self.lbl_editor = ctk.CTkLabel(self, text="Código Fuente (.src)", font=("Arial", 14, "bold"))
        self.lbl_editor.grid(row=1, column=0, sticky="nw", padx=25)

        self.txt_editor = ctk.CTkTextbox(self, font=("Consolas", 14))
        self.txt_editor.grid(row=1, column=0, padx=20, pady=(30, 20), sticky="nsew")

        # Tabs
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=1, column=1, padx=20, pady=(10, 20), sticky="nsew")

        self.tab_console = self.tabview.add("Consola / Errores")
        self.tab_tac = self.tabview.add("Código TAC")
        self.tab_llvm = self.tabview.add("LLVM IR")

        # Consola
        self.txt_console = ctk.CTkTextbox(self.tab_console, font=("Consolas", 12))
        self.txt_console.pack(fill="both", expand=True)

        # TAC
        self.txt_tac = ctk.CTkTextbox(self.tab_tac, font=("Consolas", 12))
        self.txt_tac.pack(fill="both", expand=True)

        # LLVM
        self.txt_llvm = ctk.CTkTextbox(self.tab_llvm, font=("Consolas", 12))
        self.txt_llvm.pack(fill="both", expand=True)

    def run_full_pipeline(self):
        # Guardar código en archivo de entrada
        content = self.txt_editor.get("1.0", "end")

        os.makedirs("input", exist_ok=True)

        with open("input/programa.txt", "w", encoding="utf-8") as f:
            f.write(content)

        # Ejecutar pipeline
        try:
            result = subprocess.run(
                ['python', 'pipeline.py'],
                capture_output=True,
                text=True
            )

            # Mostrar salida en consola
            self.txt_console.delete("1.0", "end")
            self.txt_console.insert("1.0", result.stdout + "\n" + result.stderr)

            # Cargar archivos generados
            self.load_phase_files()

        except Exception as e:
            self.txt_console.insert("end", f"\nError al ejecutar pipeline: {e}")

    def load_phase_files(self):
        os.makedirs("output", exist_ok=True)

        # TAC
        tac_path = "output/programa.tac"
        if os.path.exists(tac_path):
            with open(tac_path, "r", encoding="utf-8") as f:
                self.txt_tac.delete("1.0", "end")
                self.txt_tac.insert("1.0", f.read())
        else:
            self.txt_tac.delete("1.0", "end")
            self.txt_tac.insert("1.0", "No se generó archivo TAC.")

        # LLVM
        llvm_path = "output/programa.ll"
        if os.path.exists(llvm_path):
            with open(llvm_path, "r", encoding="utf-8") as f:
                self.txt_llvm.delete("1.0", "end")
                self.txt_llvm.insert("1.0", f.read())
        else:
            self.txt_llvm.delete("1.0", "end")
            self.txt_llvm.insert("1.0", "No se generó archivo LLVM IR.")


if __name__ == "__main__":
    app = CompilerUI()
    app.mainloop()