import customtkinter as ctk
import subprocess
import os
import difflib
import llvmlite.binding as llvm

# =====================================================================
# LÓGICA DEL BACKEND DE OPTIMIZACIÓN (ir_manual.py integrado)
# =====================================================================
def aplicar_pases_manuales(llvm_ir_string, lista_pases):
    """Aplica selectivamente los pases sobre el código LLVM IR."""
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    
    try:
        modulo = llvm.parse_assembly(llvm_ir_string)
        modulo.verify()
    except Exception as e:
        return f"Error de sintaxis en el LLVM IR original:\n{e}", False

    # Crear el Gestor de Pases de LLVM
    pass_manager = llvm.create_module_pass_manager()
    
    # Mapeo exacto de los pases solicitados en el enunciado a llvmlite
    for pase in lista_pases:
        p = pase.lower().strip()
        if p == "mem2reg":
            pass_manager.add_promote_memory_to_register_pass()
        elif p == "instcombine":
            pass_manager.add_instruction_combining_pass()
        elif p == "simplifycfg":
            pass_manager.add_cfg_simplification_pass()
        elif p == "dce":
            pass_manager.add_dead_code_elimination_pass()
        elif p == "inline":
            pass_manager.add_function_inlining_pass(275)
        elif p == "loop-unroll":
            pass_manager.add_loop_unroll_pass()
            
    pass_manager.run(modulo)
    return str(modulo), True

# =====================================================================
# INTERFAZ GRÁFICA DEL COMPILADOR ACTUALIZADA
# =====================================================================
class CompilerUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EZEQUIEL Compiler IDE - Con Módulo de Optimización Manual")
        self.geometry("1200x750")

        # Configuración de columnas globales
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
        self.tab_manual = self.tabview.add("Optimización Manual") # <- TU PESTAÑA DEL PUNTO 2

        # Widgets de texto para fases estándar
        self.txt_console = ctk.CTkTextbox(self.tab_console, font=("Consolas", 12))
        self.txt_console.pack(fill="both", expand=True)

        self.txt_tac = ctk.CTkTextbox(self.tab_tac, font=("Consolas", 12))
        self.txt_tac.pack(fill="both", expand=True)

        self.txt_llvm = ctk.CTkTextbox(self.tab_llvm, font=("Consolas", 12))
        self.txt_llvm.pack(fill="both", expand=True)

        # CONSTUCCIÓN INTERNA DE LA PESTAÑA: OPTIMIZACIÓN MANUAL
        self.setup_manual_optimization_tab()

    def setup_manual_optimization_tab(self):
        """Configura la estructura visual del panel interactivo de optimizaciones."""
        # Contenedor principal de la pestaña dividido en Controles (Izq) y Vista Diff (Der)
        self.tab_manual.columnconfigure(0, weight=0) # Barra de opciones (fija)
        self.tab_manual.columnconfigure(1, weight=1) # Diff e inputs (expandible)
        self.tab_manual.rowconfigure(0, weight=1)

        # --- SUBPANEL IZQUIERDO: CONTROLES ---
        self.frame_controles = ctk.CTkFrame(self.tab_manual, width=180)
        self.frame_controles.grid(row=0, column=0, padx=5, pady=5, sticky="nsw")
        
        lbl_pases = ctk.CTkLabel(self.frame_controles, text="Passes de LLVM", font=("Arial", 12, "bold"))
        lbl_pases.pack(padx=10, pady=5, anchor="w")

        # Diccionario para almacenar el estado booleano de los Checkboxes
        self.check_vars = {}
        pases_requeridos = ["mem2reg", "instcombine", "simplifycfg", "dce", "inline", "loop-unroll"]
        
        for pase in pases_requeridos:
            var = ctk.BooleanVar()
            cb = ctk.CTkCheckBox(self.frame_controles, text=pase, variable=var, font=("Consolas", 12))
            cb.pack(padx=15, pady=4, anchor="w")
            self.check_vars[pase] = var

        # Botones de Acción del módulo
        self.btn_opt_manual = ctk.CTkButton(self.frame_controles, text="Aplicar Passes", command=self.ejecutar_opt_manual, fg_color="#3498db")
        self.btn_opt_manual.pack(padx=10, pady=15, fill="x")

        self.btn_ejecutar_ir = ctk.CTkButton(self.frame_controles, text="Ejecutar IR (lli)", command=self.ejecutar_ir_jit, fg_color="#9b59b6")
        self.btn_ejecutar_ir.pack(padx=10, pady=5, fill="x")

        self.btn_exportar_ir = ctk.CTkButton(self.frame_controles, text="Exportar IR", command=self.exportar_ir_manual, fg_color="#e67e22")
        self.btn_exportar_ir.pack(padx=10, pady=5, fill="x")

        # --- SUBPANEL DERECHO: COMPARADOR DIFF (Lado a Lado) ---
        self.frame_diff = ctk.CTkFrame(self.tab_manual)
        self.frame_diff.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.frame_diff.columnconfigure(0, weight=1)
        self.frame_diff.columnconfigure(1, weight=1)
        self.frame_diff.rowconfigure(1, weight=1)

        # Encabezados de paneles
        lbl_orig = ctk.CTkLabel(self.frame_diff, text="IR Original (Sin Optimizar)", font=("Arial", 11, "bold"))
        lbl_orig.grid(row=0, column=0, pady=2, sticky="w", padx=10)
        
        lbl_mod = ctk.CTkLabel(self.frame_diff, text="IR Modificado (Optimizado)", font=("Arial", 11, "bold"))
        lbl_mod.grid(row=0, column=1, pady=2, sticky="w", padx=10)

        # Los dos cuadros de texto paralelos
        self.txt_diff_original = ctk.CTkTextbox(self.frame_diff, font=("Consolas", 11), wrap="none")
        self.txt_diff_original.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.txt_diff_optimizado = ctk.CTkTextbox(self.frame_diff, font=("Consolas", 11), wrap="none")
        self.txt_diff_optimizado.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        # Guardaremos internamente el último string optimizado exitosamente para re-ejecución
        self.current_optimized_ir = ""

    # =====================================================================
    # ACCIONES DEL MÓDULO MANUAL
    # =====================================================================
    def ejecutar_opt_manual(self):
        """Lee el IR original de la fase 5, corre los pases y genera el Diff visual."""
        # Obtener el IR que generó el backend sin optimizar
        ir_original = self.txt_llvm.get("1.0", "end-1c")
        if not ir_original.strip():
            self.txt_diff_original.delete("1.0", "end")
            self.txt_diff_original.insert("1.0", "⚠️ Primero debes 'COMPILAR PROYECTO' para generar un LLVM IR base.")
            return

        # Capturar qué pases están activos en los checkboxes
        pases_activos = [pase for pase, var in self.check_vars.items() if var.get()]
        
        # Ejecutar optimización
        ir_resultado, exito = aplicar_pases_manuales(ir_original, pases_activos)
        
        # Limpiar paneles de visualización
        self.txt_diff_original.delete("1.0", "end")
        self.txt_diff_optimizado.delete("1.0", "end")

        if not exito:
            # Si llvmlite falló parseando el código
            self.txt_diff_optimizado.insert("1.0", ir_resultado)
            return

        self.current_optimized_ir = ir_resultado

        # Renderizar en paneles con cálculo de Diferencias (Diff)
        lineas_orig = ir_original.splitlines()
        lineas_opt = ir_resultado.splitlines()

        # Usamos difflib para comparar secuencialmente
        differ = difflib.Differ()
        diff_resultado = list(differ.compare(lineas_orig, lineas_opt))

        # Reconstruir las vistas pintando las adiciones/sustracciones
        for linea in diff_resultado:
            if linea.startswith("  "):  # Línea idéntica
                self.txt_diff_original.insert("end", linea[2:] + "\n")
                self.txt_diff_optimizado.insert("end", linea[2:] + "\n")
            elif linea.startswith("- "): # Eliminado del original -> Pintamos ROJO
                self.txt_diff_original.insert("end", linea[2:] + "\n")
                # Tip de CustomTkinter/Tkinter: se pueden usar colores de texto insertando tags en texto puro si se desea,
                # para mantenerlo robusto y compatible, indicamos el cambio con un marcador visual claro o color.
            elif linea.startswith("+ "): # Añadido al optimizado -> Pintamos VERDE
                self.txt_diff_optimizado.insert("end", "[+] " + linea[2:] + "\n")

    def ejecutar_ir_jit(self):
        """Ejecuta el IR optimizado manualmente mediante la herramienta JIT 'lli'."""
        ir_a_correr = self.current_optimized_ir if self.current_optimized_ir else self.txt_llvm.get("1.0", "end-1c")
        if not ir_a_correr.striimport customtkinter as ctk
import subprocess
import os
import difflib
import llvmlite.binding as llvm

# =====================================================================
# LÓGICA DEL BACKEND DE OPTIMIZACIÓN (ir_manual.py integrado)
# =====================================================================
def aplicar_pases_manuales(llvm_ir_string, lista_pases):
    """Aplica selectivamente los pases sobre el código LLVM IR."""
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    
    try:
        modulo = llvm.parse_assembly(llvm_ir_string)
        modulo.verify()
    except Exception as e:
        return f"Error de sintaxis en el LLVM IR original:\n{e}", False

    # Crear el Gestor de Pases de LLVM
    pass_manager = llvm.create_module_pass_manager()
    
    # Mapeo exacto de los pases solicitados en el enunciado a llvmlite
    for pase in lista_pases:
        p = pase.lower().strip()
        if p == "mem2reg":
            pass_manager.add_promote_memory_to_register_pass()
        elif p == "instcombine":
            pass_manager.add_instruction_combining_pass()
        elif p == "simplifycfg":
            pass_manager.add_cfg_simplification_pass()
        elif p == "dce":
            pass_manager.add_dead_code_elimination_pass()
        elif p == "inline":
            pass_manager.add_function_inlining_pass(275)
        elif p == "loop-unroll":
            pass_manager.add_loop_unroll_pass()
            
    pass_manager.run(modulo)
    return str(modulo), True

# =====================================================================
# INTERFAZ GRÁFICA DEL COMPILADOR ACTUALIZADA
# =====================================================================
class CompilerUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EZEQUIEL Compiler IDE - Con Módulo de Optimización Manual")
        self.geometry("1200x750")

        # Configuración de columnas globales
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
        self.tab_manual = self.tabview.add("Optimización Manual") # <- TU PESTAÑA DEL PUNTO 2

        # Widgets de texto para fases estándar
        self.txt_console = ctk.CTkTextbox(self.tab_console, font=("Consolas", 12))
        self.txt_console.pack(fill="both", expand=True)

        self.txt_tac = ctk.CTkTextbox(self.tab_tac, font=("Consolas", 12))
        self.txt_tac.pack(fill="both", expand=True)

        self.txt_llvm = ctk.CTkTextbox(self.tab_llvm, font=("Consolas", 12))
        self.txt_llvm.pack(fill="both", expand=True)

        # CONSTUCCIÓN INTERNA DE LA PESTAÑA: OPTIMIZACIÓN MANUAL
        self.setup_manual_optimization_tab()

    def setup_manual_optimization_tab(self):
        """Configura la estructura visual del panel interactivo de optimizaciones."""
        # Contenedor principal de la pestaña dividido en Controles (Izq) y Vista Diff (Der)
        self.tab_manual.columnconfigure(0, weight=0) # Barra de opciones (fija)
        self.tab_manual.columnconfigure(1, weight=1) # Diff e inputs (expandible)
        self.tab_manual.rowconfigure(0, weight=1)

        # --- SUBPANEL IZQUIERDO: CONTROLES ---
        self.frame_controles = ctk.CTkFrame(self.tab_manual, width=180)
        self.frame_controles.grid(row=0, column=0, padx=5, pady=5, sticky="nsw")
        
        lbl_pases = ctk.CTkLabel(self.frame_controles, text="Passes de LLVM", font=("Arial", 12, "bold"))
        lbl_pases.pack(padx=10, pady=5, anchor="w")

        # Diccionario para almacenar el estado booleano de los Checkboxes
        self.check_vars = {}
        pases_requeridos = ["mem2reg", "instcombine", "simplifycfg", "dce", "inline", "loop-unroll"]
        
        for pase in pases_requeridos:
            var = ctk.BooleanVar()
            cb = ctk.CTkCheckBox(self.frame_controles, text=pase, variable=var, font=("Consolas", 12))
            cb.pack(padx=15, pady=4, anchor="w")
            self.check_vars[pase] = var

        # Botones de Acción del módulo
        self.btn_opt_manual = ctk.CTkButton(self.frame_controles, text="Aplicar Passes", command=self.ejecutar_opt_manual, fg_color="#3498db")
        self.btn_opt_manual.pack(padx=10, pady=15, fill="x")

        self.btn_ejecutar_ir = ctk.CTkButton(self.frame_controles, text="Ejecutar IR (lli)", command=self.ejecutar_ir_jit, fg_color="#9b59b6")
        self.btn_ejecutar_ir.pack(padx=10, pady=5, fill="x")

        self.btn_exportar_ir = ctk.CTkButton(self.frame_controles, text="Exportar IR", command=self.exportar_ir_manual, fg_color="#e67e22")
        self.btn_exportar_ir.pack(padx=10, pady=5, fill="x")

        # --- SUBPANEL DERECHO: COMPARADOR DIFF (Lado a Lado) ---
        self.frame_diff = ctk.CTkFrame(self.tab_manual)
        self.frame_diff.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.frame_diff.columnconfigure(0, weight=1)
        self.frame_diff.columnconfigure(1, weight=1)
        self.frame_diff.rowconfigure(1, weight=1)

        # Encabezados de paneles
        lbl_orig = ctk.CTkLabel(self.frame_diff, text="IR Original (Sin Optimizar)", font=("Arial", 11, "bold"))
        lbl_orig.grid(row=0, column=0, pady=2, sticky="w", padx=10)
        
        lbl_mod = ctk.CTkLabel(self.frame_diff, text="IR Modificado (Optimizado)", font=("Arial", 11, "bold"))
        lbl_mod.grid(row=0, column=1, pady=2, sticky="w", padx=10)

        # Los dos cuadros de texto paralelos
        self.txt_diff_original = ctk.CTkTextbox(self.frame_diff, font=("Consolas", 11), wrap="none")
        self.txt_diff_original.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.txt_diff_optimizado = ctk.CTkTextbox(self.frame_diff, font=("Consolas", 11), wrap="none")
        self.txt_diff_optimizado.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        # Guardaremos internamente el último string optimizado exitosamente para re-ejecución
        self.current_optimized_ir = ""

    # =====================================================================
    # ACCIONES DEL MÓDULO MANUAL
    # =====================================================================
    def ejecutar_opt_manual(self):
        """Lee el IR original de la fase 5, corre los pases y genera el Diff visual."""
        # Obtener el IR que generó el backend sin optimizar
        ir_original = self.txt_llvm.get("1.0", "end-1c")
        if not ir_original.strip():
            self.txt_diff_original.delete("1.0", "end")
            self.txt_diff_original.insert("1.0", "⚠️ Primero debes 'COMPILAR PROYECTO' para generar un LLVM IR base.")
            return

        # Capturar qué pases están activos en los checkboxes
        pases_activos = [pase for pase, var in self.check_vars.items() if var.get()]
        
        # Ejecutar optimización
        ir_resultado, exito = aplicar_pases_manuales(ir_original, pases_activos)
        
        # Limpiar paneles de visualización
        self.txt_diff_original.delete("1.0", "end")
        self.txt_diff_optimizado.delete("1.0", "end")

        if not exito:
            # Si llvmlite falló parseando el código
            self.txt_diff_optimizado.insert("1.0", ir_resultado)
            return

        self.current_optimized_ir = ir_resultado

        # Renderizar en paneles con cálculo de Diferencias (Diff)
        lineas_orig = ir_original.splitlines()
        lineas_opt = ir_resultado.splitlines()

        # Usamos difflib para comparar secuencialmente
        differ = difflib.Differ()
        diff_resultado = list(differ.compare(lineas_orig, lineas_opt))

        # Reconstruir las vistas pintando las adiciones/sustracciones
        for linea in diff_resultado:
            if linea.startswith("  "):  # Línea idéntica
                self.txt_diff_original.insert("end", linea[2:] + "\n")
                self.txt_diff_optimizado.insert("end", linea[2:] + "\n")
            elif linea.startswith("- "): # Eliminado del original -> Pintamos ROJO
                self.txt_diff_original.insert("end", linea[2:] + "\n")
                # Tip de CustomTkinter/Tkinter: se pueden usar colores de texto insertando tags en texto puro si se desea,
                # para mantenerlo robusto y compatible, indicamos el cambio con un marcador visual claro o color.
            elif linea.startswith("+ "): # Añadido al optimizado -> Pintamos VERDE
                self.txt_diff_optimizado.insert("end", "[+] " + linea[2:] + "\n")

    def ejecutar_ir_jit(self):
        """Ejecuta el IR optimizado manualmente mediante la herramienta JIT 'lli'."""
        ir_a_correr = self.current_optimized_ir if self.current_optimized_ir else self.txt_llvm.get("1.0", "end-1c")
        if not ir_a_correr.strip():
            return
            
        archivo_temp = "temp_manual_run.ll"
        with open(archivo_temp, "w", encoding="utf-8") as f:
            f.write(ir_a_correr)
            
        try:
            res = subprocess.run(["lli", archivo_temp], capture_output=True, text=True, timeout=5)
            # Cambiar a la pestaña de consola para ver el print() resultante
            self.tabview.set("Consola/Errores")
            self.txt_console.delete("1.0", "end")p():
            return
            
        archivo_temp = "temp_manual_run.ll"
        with open(archivo_temp, "w", encoding="utf-8") as f:
            f.write(ir_a_correr)
            
        try:
            res = subprocess.run(["lli", archivo_temp], capture_output=True, text=True, timeout=5)
            # Cambiar a la pestaña de consola para ver el print() resultante
            self.tabview.set("Consola/Errores")
            self.txt_console.delete("1.0", "end")