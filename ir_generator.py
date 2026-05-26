from llvmlite import ir


class IRGenerator:
    def __init__(self):
        self.module = ir.Module(name="programa")
        self.module.triple = "x86_64-pc-linux-gnu"  # 👈 SOLUCIÓN AL ERROR
        self.builder = None
        self.func = None
        self.variables = {}

    def create_main(self):
        func_type = ir.FunctionType(ir.IntType(32), [])
        self.func = ir.Function(self.module, func_type, name="main")

        block = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def declare_variable(self, name, value):
        int_type = ir.IntType(32)
        ptr = self.builder.alloca(int_type, name=name)
        self.builder.store(ir.Constant(int_type, value), ptr)
        self.variables[name] = ptr

    def load_variable(self, name):
        return self.builder.load(self.variables[name], name=name)

    def add(self, left, right):
        return self.builder.add(left, right)

    def sub(self, left, right):
        return self.builder.sub(left, right)

    def mul(self, left, right):
        return self.builder.mul(left, right)

    def div(self, left, right):
        return self.builder.sdiv(left, right)

    def finish(self):
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

    def save(self, filename="archivo.ll"):
        with open(filename, "w") as f:
            f.write(str(self.module))

if __name__ == "__main__":
    gen = IRGenerator()
    gen.create_main()

    # x = 5
    gen.declare_variable("x", 5)

    # x + 3
    x = gen.load_variable("x")
    result = gen.add(x, ir.Constant(ir.IntType(32), 3))

    gen.finish()
    gen.save("archivo.ll")