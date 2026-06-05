from llvmlite import ir


class IRGenerator:

    # //////////////////////////////////////////////////////////
    # CONSTRUCTOR
    # //////////////////////////////////////////////////////////

    def __init__(self):

        self.module = ir.Module(name="programa")
        self.module.triple = "x86_64-pc-linux-gnu"

        self.builder = None
        self.func = None

        self.variables = {}

        # LLVM V4

        self.labels = {}
        self.temporales = {}

    # //////////////////////////////////////////////////////////
    # MAIN
    # //////////////////////////////////////////////////////////

    def create_main(self):

        func_type = ir.FunctionType(
            ir.IntType(32),
            []
        )

        self.func = ir.Function(
            self.module,
            func_type,
            name="main"
        )

        block = self.func.append_basic_block(
            name="entry"
        )

        self.builder = ir.IRBuilder(block)

    # //////////////////////////////////////////////////////////
    # VARIABLES
    # //////////////////////////////////////////////////////////

    def declare_variable(self, name, value):

        int_type = ir.IntType(32)

        ptr = self.builder.alloca(
            int_type,
            name=name
        )

        self.builder.store(
            ir.Constant(int_type, value),
            ptr
        )

        self.variables[name] = ptr

        return ptr

    def load_variable(self, name):

        return self.builder.load(
            self.variables[name],
            name=name
        )

    # //////////////////////////////////////////////////////////
    # OPERACIONES ARITMÉTICAS
    # //////////////////////////////////////////////////////////

    def add(self, left, right):
        return self.builder.add(left, right)

    def sub(self, left, right):
        return self.builder.sub(left, right)

    def mul(self, left, right):
        return self.builder.mul(left, right)

    def div(self, left, right):
        return self.builder.sdiv(left, right)

    # //////////////////////////////////////////////////////////
    # COMPARACIONES
    # //////////////////////////////////////////////////////////

    def compare(self, op, left, right):

        operadores = {
            ">": ">",
            "<": "<",
            ">=": ">=",
            "<=": "<=",
            "==": "==",
            "!=": "!="
        }

        return self.builder.icmp_signed(
            operadores[op],
            left,
            right
        )

    # //////////////////////////////////////////////////////////
    # CASTING
    # //////////////////////////////////////////////////////////

    def int_to_float(self, valor):

        return self.builder.sitofp(
            valor,
            ir.FloatType()
        )

    def float_to_int(self, valor):

        return self.builder.fptosi(
            valor,
            ir.IntType(32)
        )

    # //////////////////////////////////////////////////////////
    # STRUCTS
    # //////////////////////////////////////////////////////////

    def create_struct(self, nombre, campos):

        struct_type = ir.LiteralStructType(
            campos
        )

        return struct_type

    # //////////////////////////////////////////////////////////
    # TAC -> LLVM
    # //////////////////////////////////////////////////////////

    def generate_from_tac(self, codigo_tac):

        self.create_main()

        lineas = codigo_tac.split("\n")

        for linea in lineas:

            linea = linea.strip()

            if not linea:
                continue

            print("LLVM <- TAC:", linea)

            # Aquí irá la traducción TAC -> LLVM

        self.finish()

    # //////////////////////////////////////////////////////////
    # FINALIZAR
    # //////////////////////////////////////////////////////////

    def finish(self):

        self.builder.ret(
            ir.Constant(
                ir.IntType(32),
                0
            )
        )

    # //////////////////////////////////////////////////////////
    # GUARDAR
    # //////////////////////////////////////////////////////////

    def save(self, filename="archivo.ll"):

        with open(filename, "w") as f:
            f.write(str(self.module))


# //////////////////////////////////////////////////////////
# PRUEBA LOCAL
# //////////////////////////////////////////////////////////

if __name__ == "__main__":

    gen = IRGenerator()

    gen.create_main()

    gen.declare_variable(
        "x",
        5
    )

    x = gen.load_variable("x")

    resultado = gen.add(
        x,
        ir.Constant(
            ir.IntType(32),
            3
        )
    )

    gen.finish()

    gen.save("archivo.ll")

    print("LLVM generado correctamente.")
