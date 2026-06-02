import llvmlite.binding as llvm
import subprocess
import os

def aplicar_pases_manuales(llvm_ir_string, lista_pases):
    """
    Recibe el contenido de un archivo .ll (str) y una lista de pases elegidos.
    Aplica secuencialmente cada transformación y retorna el IR optimizado.
    """
    # Inicializar componentes de LLVM
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    
    try:
        # Parsear el código IR de entrada
        modulo = llvm.parse_assembly(llvm_ir_string)
        modulo.verify()
    except Exception as e:
        return f"Error de sintaxis en el LLVM IR original: {e}"

    # Crear el Pass Manager de LLVM para el módulo
    pass_manager = llvm.create_module_pass_manager()
    
    # Mapear los pases requeridos por el enunciado a las funciones de llvmlite
    # Requisito mínimo: mem2reg, instcombine, simplifycfg, dce, inline, loop-unroll
    for pase in lista_pases:
        p = pase.lower().strip()
        if p == "mem2reg":
            # Promueve memoria a registros (elimina allocas redundantes)
            pass_manager.add_promote_memory_to_register_pass()
        elif p == "instcombine":
            # Combinación de instrucciones
            pass_manager.add_instruction_combining_pass()
        elif p == "simplifycfg":
            # Simplificación del Grafo de Flujo de Control
            pass_manager.add_cfg_simplification_pass()
        elif p == "dce":
            # Eliminación de código muerto
            pass_manager.add_dead_code_elimination_pass()
        elif p == "inline":
            # Inlining de funciones (parámetro de umbral de peso)
            pass_manager.add_function_inlining_pass(275)
        elif p == "loop-unroll":
            # Desenrollado de ciclos
            pass_manager.add_loop_unroll_pass()
            
    # Ejecutar el Pass Manager sobre nuestro módulo parseado
    pass_manager.run(modulo)
    
    # Retornar el string del nuevo IR optimizado
    return str(modulo)

def ejecutar_ir(llvm_ir_string):
    """
    Ejecuta el IR utilizando el comando 'lli' de LLVM en WSL2 
    y captura la salida de consola para la interfaz.
    """
    archivo_temporal = "temp_manual_exec.ll"
    with open(archivo_temporal, "w", encoding="utf-8") as f:
        f.write(llvm_ir_string)
        
    try:
        # Ejecuta el interprete JIT de LLVM (lli)
        resultado = subprocess.run(
            ["lli", archivo_temporal],
            capture_output=True,
            text=True,
            timeout=5
        )
        salida = resultado.stdout
        errores = resultado.stderr
        return f"{salida}\n{errores}".strip()
    except subprocess.TimeoutExpired:
        return "Error: Tiempo de ejecución excedido (¿Ciclo infinito?)."
    except FileNotFoundError:
        return "Error: El comando 'lli' de LLVM no está instalado o disponible en el PATH de WSL2."
    finally:
        if os.path.exists(archivo_temporal):
            os.remove(archivo_temporal)