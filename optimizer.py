class Optimizer:

    def __init__(self):
        pass

    def dead_code_elimination(self, ir_code):
        return ir_code

    def constant_folding(self, ir_code):
        return ir_code

    def function_inlining(self, ir_code):
        return ir_code

    def loop_unrolling(self, ir_code):
        return ir_code

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

        optimized_ir = original_ir

        optimized_ir = self.constant_folding(
            optimized_ir
        )

        optimized_ir = self.dead_code_elimination(
            optimized_ir
        )

        optimized_ir = self.function_inlining(
            optimized_ir
        )

        optimized_ir = self.loop_unrolling(
            optimized_ir
        )

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(optimized_ir)

        after = self.count_instructions(
            optimized_ir
        )

        reduction = 0

        if before > 0:
            reduction = (
                (before - after)
                / before
            ) * 100

        return {
            "before": before,
            "after": after,
            "reduction": round(reduction, 2)
        }
