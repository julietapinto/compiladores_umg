import customtkinter as ctk
import subprocess
import os

class CompilerUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EZEQUIEL Compiler IDE - Fase Final (Punto 5)")
        self.geometry("1300x750")

        # Distribución de la ventana en 3 columnas principales 
        self.grid_columnconfigure(0, weight=2)  # Editor Código Fuente
        self.grid_columnconfigure(1, weight=3)  # Pestañas de Salida automáticas y Diff
        self.grid_columnconfigure(2, weight=2)  # Panel de IR Manual
        self.grid_rowconfigure(1, weight=1)

        # Botón principal de compilación automática
        self.btn_compile = ctk.CTkButton(
            self,
            text="COMPILAR PROYECTO COMPLETO",
            command=self.run_full_pipeline,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            font=("Arial", 13, "bold")
        )
        self.btn_compile.grid(row=0, column=0, columnspan=3, pady=15, padx=20, sticky="ew")

        # ==========================================
        # COLUMNA 0: EDITOR DE CÓDIGO FUENTE 
        # ==========================================
        self.lbl_editor = ctk.CTkLabel(self, text="Código Fuente (.src)", font=("Arial", 14, "bold"))
        self.lbl_editor.grid(row=1, column=0, sticky="nw", padx=25)

        self.txt_editor = ctk.CTkTextbox(self, font=("Consolas", 14))
        self.txt_editor.grid(row=1, column=0, padx=(20, 10), pady=(30, 20), sticky="nsew")

        # ==========================================
        # COLUMNA 1: PESTAÑAS (TABS) DE SALIDA AUTOMÁTICA Y DIFF 
        # ==========================================
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=1, column=1, padx=10, pady=(10, 20), sticky="nsew")

        self.tab_console = self.tabview.add("Consola / Errores") 
        self.tab_tac = self.tabview.add("Código TAC") 
        self.tab_llvm = self.tabview.add("LLVM IR") 
        self.tab_llvm_opt = self.tabview.add("LLVM Optimizado O3") 
        self.tab_diff = self.tabview.add("Comparador Diff (Visual)") 

        # Configurar áreas de texto en las pestañas automáticas 
        self.txt_console = ctk.CTkTextbox(self.tab_console, font=("Consolas", 12))
        self.txt_console.pack(fill="both", expand=True)

        self.txt_tac = ctk.CTkTextbox(self.tab_tac, font=("Consolas", 12))
        self.txt_tac.pack(fill="both", expand=True)

        self.txt_llvm = ctk.CTkTextbox(self.tab_llvm, font=("Consolas", 12))
        self.txt_llvm.pack(fill="both", expand=True)

        self.txt_llvm_opt = ctk.CTkTextbox(self.tab_llvm_opt, font=("Consolas", 12))
        self.txt_llvm_opt.pack(fill="both", expand=True)

        # INTERFAZ DEL COMPARADOR DIFF INTERNO 
        self.frame_diff_split = ctk.CTkFrame(self.tab_diff, fg_color="transparent")
        self.frame_diff_split.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.frame_diff_split.grid_columnconfigure(0, weight=1)
        self.frame_diff_split.grid_columnconfigure(1, weight=1)
        self.frame_diff_split.grid_rowconfigure(1, weight=1)

        # Sub-títulos del Diff 
        self.lbl_diff_izq = ctk.CTkLabel(self.frame_diff_split, text="LLVM IR Original", font=("Arial", 11, "bold"), text_color="#3498db")
        self.lbl_diff_izq.grid(row=0, column=0, sticky="w", padx=5)
        
        self.lbl_diff_der = ctk.CTkLabel(self.frame_diff_split, text="LLVM IR Optimizado Manual", font=("Arial", 11, "bold"), text_color="#2ecc71")
        self.lbl_diff_der.grid(row=0, column=1, sticky="w", padx=5)

        # Cuadros de texto en paralelo 
        self.txt_diff_original = ctk.CTkTextbox(self.frame_diff_split, font=("Consolas", 11))
        self.txt_diff_original.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.txt_diff_manual = ctk.CTkTextbox(self.frame_diff_split, font=("Consolas", 11))
        self.txt_diff_manual.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        # ==========================================
        # COLUMNA 2: PANEL DE OPTIMIZACIÓN IR MANUAL 
        # ==========================================
        self.frame_manual = ctk.CTkFrame(self)
        self.frame_manual.grid(row=1, column=2, padx=(10, 20), pady=(15, 20), sticky="nsew")
        
        self.lbl_manual = ctk.CTkLabel(self.frame_manual, text="Panel IR Manual", font=("Arial", 14, "bold")) 
        self.lbl_manual.pack(pady=15, padx=15, anchor="w")

        self.lbl_instruccion = ctk.CTkLabel(
            self.frame_manual, 
            text="Selecciona los passes a aplicar:", 
            font=("Arial", 12, "italic"),
            text_color="#95a5a6"
        )
        self.lbl_instruccion.pack(pady=(0, 10), padx=15, anchor="w")

        # Diccionario para almacenar el estado de cada Checkbox 
        self.passes_vars = {
            "mem2reg": ctk.BooleanVar(value=False),      
            "instcombine": ctk.BooleanVar(value=False),  
            "simplifycfg": ctk.BooleanVar(value=False),  
            "dce": ctk.BooleanVar(value=False),          
            "inline": ctk.BooleanVar(value=False),        
            "loop-unroll": ctk.BooleanVar(value=False)   
        }

        # Creación dinámica de los Checkboxes 
        for pass_name, var in self.passes_vars.items():
            chk = ctk.CTkCheckBox(
                self.frame_manual, 
                text=f"-{pass_name}", 
                variable=var,
                font=("Consolas", 13)
            )
            chk.pack(pady=8, padx=25, anchor="w")

        # Botón para ejecutar la optimización manual 
        self.btn_run_manual = ctk.CTkButton(
            self.frame_manual,
            text="APLICAR PASSES SELECCIONADOS",
            command=self.run_manual_optimization,
            fg_color="#3498db",
            hover_color="#2980b9",
            font=("Arial", 12, "bold")
        )
        self.btn_run_manual.pack(pady=(25, 10), padx=20, fill="x")

        # Botón para exportar el IR Optimizado Manualmente 
        self.btn_export_manual = ctk.CTkButton(
            self.frame_manual,
            text="EXPORTAR IR OPTIMIZADO",
            command=self.export_manual_ir,
            fg_color="#e67e22",
            hover_color="#d35400",
            font=("Arial", 12, "bold")
        )
        self.btn_export_manual.pack(pady=5, padx=20, fill="x")

    def run_full_pipeline(self): 
        content = self.txt_editor.get("1.0", "end-1c")
        os.makedirs("input", exist_ok=True)

        with open("input/programa.txt", "w", encoding="utf-8") as f:
            f.write(content)

        try:
            result = subprocess.run(
                ['python3', 'pipeline.py'],
                capture_output=True,
                text=True
            )

            self.txt_console.delete("1.0", "end")
            self.txt_console.insert("1.0", result.stdout + "\n" + result.stderr)

            self.load_phase_files()

        except Exception as e:
            self.txt_console.insert("end", f"\nError al ejecutar pipeline: {e}")

    def run_manual_optimization(self): 
        llvm_path = "output/programa.ll"
        manual_opt_path = "output/programa.manual.ll"
        
        if not os.path.exists(llvm_path):
            self.txt_console.delete("1.0", "end")
            self.txt_console.insert("1.0", "[Error] No se puede optimizar: Primero debes darle al botón 'COMPILAR PROYECTO COMPLETO' para generar el código LLVM IR base.")
            self.tabview.set("Consola / Errores")
            return

        activos = [name for name, var in self.passes_vars.items() if var.get()] 
        
        if not activos:
            self.txt_console.delete("1.0", "end")
            self.txt_console.insert("1.0", "[Alerta] Por favor, selecciona al menos un pass del panel derecho antes de aplicar la optimización.")
            self.tabview.set("Consola / Errores")
            return

        comando_opt = ["opt", "-S"]
        for pass_name in activos:
            comando_opt.append(f"-{pass_name}")
        
        comando_opt.extend([llvm_path, "-o", manual_opt_path])

        try:
            self.txt_console.delete("1.0", "end")
            self.txt_console.insert("1.0", f"Ejecutando optimización manual en LLVM...\nComando: {' '.join(comando_opt)}\n\n")
            
            result = subprocess.run(
                comando_opt,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                self.txt_console.insert("end", "¡Optimización manual completada con éxito!\nRevisa la pestaña 'Comparador Diff (Visual)' para ver los cambios.")
                
                # Cargar datos en el comparador visual lado a lado 
                if os.path.exists(llvm_path):
                    with open(llvm_path, "r", encoding="utf-8") as f_orig:
                        self.txt_diff_original.delete("1.0", "end")
                        self.txt_diff_original.insert("1.0", f_orig.read())
                        
                if os.path.exists(manual_opt_path):
                    with open(manual_opt_path, "r", encoding="utf-8") as f_opt:
                        self.txt_diff_manual.delete("1.0", "end")
                        self.txt_diff_manual.insert("1.0", f_opt.read())
                
                # Mover el foco automáticamente a la pestaña Diff  
                self.tabview.set("Comparador Diff (Visual)")
            else:
                self.txt_console.insert("end", f"[Error en opt]:\n{result.stderr}")
                self.tabview.set("Consola / Errores")

        except Exception as e:
            self.txt_console.insert("end", f"\nError crítico al ejecutar el comando 'opt': {e}")
            self.tabview.set("Consola / Errores")

    def export_manual_ir(self): 
        manual_opt_path = "output/programa.manual.ll"
        
        if not os.path.exists(manual_opt_path):
            self.txt_console.delete("1.0", "end")
            self.txt_console.insert("1.0", "[Error] No hay ninguna optimización manual guardada para exportar. Primero selecciona tus passes y dale a 'APLICAR'.")
            self.tabview.set("Consola / Errores")
            return

        try:
            ruta_exportada = "output/codigo_optimizado_manual.ll"
            
            with open(manual_opt_path, "r", encoding="utf-8") as origen:
                contenido = origen.read()
                
            with open(ruta_exportada, "w", encoding="utf-8") as destino:
                destino.write(contenido)
                
            self.txt_console.delete("1.0", "end")
            self.txt_console.insert("1.0", f"¡Archivo exportado exitosamente!\n\nSe guardó en: {os.path.abspath(ruta_exportada)}")
            self.tabview.set("Consola / Errores")
            
        except Exception as e:
            self.txt_console.insert("end", f"\nError al exportar el archivo: {e}")

    def load_phase_files(self):
        os.makedirs("output", exist_ok=True)

        # TAC
        tac_path = "output/programa.tac"
        self.txt_tac.delete("1.0", "end")
        if os.path.exists(tac_path):
            with open(tac_path, "r", encoding="utf-8") as f:
                self.txt_tac.insert("1.0", f.read())
        else:
            self.txt_tac.insert("1.0", "No se generó archivo TAC.")

        # LLVM Original
        llvm_path = "output/programa.ll"
        self.txt_llvm.delete("1.0", "end")
        if os.path.exists(llvm_path):
            with open(llvm_path, "r", encoding="utf-8") as f:
                self.txt_llvm.insert("1.0", f.read())
        else:
            self.txt_llvm.insert("1.0", "No se generó archivo LLVM IR.")

        # LLVM Optimizado O3
        opt_path = "output/programa.opt.ll"
        self.txt_llvm_opt.delete("1.0", "end")
        if os.path.exists(opt_path):
            with open(opt_path, "r", encoding="utf-8") as f:
                self.txt_llvm_opt.insert("1.0", f.read())
        else:
            self.txt_llvm_opt.insert("1.0", "No se generó archivo LLVM Optimizado O3.")

if __name__ == "__main__":
    app = CompilerUI()
    app.mainloop()