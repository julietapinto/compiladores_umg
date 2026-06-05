# //////////////////////////////////////////////////////////
# PROYECTO FINAL COMPILADORES
# FASE 7 - OPTIMIZADOR O3
# INTEGRANTE 4
# //////////////////////////////////////////////////////////

class Optimizer:

    def __init__(self):
        pass

    def count_instructions(self, ir_code):

        total = 0

        for line in ir_code.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith(";"):
                continue

            total += 1

        return total

    def optimize(self, input_file, output_file):

        with open(input_file, "r", encoding="utf-8") as f:
            original_ir = f.read()

        before = self.count_instructions(original_ir)

        # //////////////////////////////////////////////////////
        # O3 PLACEHOLDER
        # //////////////////////////////////////////////////////

        optimized_ir = original_ir

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(optimized_ir)

        after = self.count_instructions(optimized_ir)

        reduction = 0

        if before > 0:
            reduction = ((before - after) / before) * 100

        return {
            "before": before,
            "after": after,
            "reduction": round(reduction, 2)
        }
