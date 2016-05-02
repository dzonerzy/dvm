__author__ = 'dzonerzy'
from core.opcodes import Opcodes, ReserverdBytes
from core.errors import VMUnsupportedInstruction, DVMCompilerWrongLabel

class DVMCompiler:
    opcodes = Opcodes()
    reservation = ReserverdBytes()
    path = None
    program = None
    bytecode = ""
    labels = []

    def __init__(self, path):
        self.path = path

    def _check_syntax(self):
        self.program = file(self.path).read().replace("\r", "").split("\n")
        for line in self.program:
            if line.startswith(":"):  # it's a label!
                pass
            else:
                try:
                    self.opcodes.ops[line.split(" ")[0]]
                except:
                    raise VMUnsupportedInstruction(line.split(" ")[0])
                finally:
                    return 1

    def _get_label_instructions(self, label):
        pass

    def _calculate_distance(self):
        pos = 0
        for line in self.program:
            line = line.split(" ")
            instruction, params = line[0], [l for l in line if l != line[0]]
            if not instruction.startswith(":") and not self._is_not_jump(instruction):
                    self.labels.append({"val": params[0], "pos": pos})
            pos += 1
        for lbl in self.labels:
            pos = self.program.index(lbl["val"])
            if pos > int(lbl["pos"]):
                c = 0
                iset = self.program[lbl["pos"]:pos+1]
                for i in iset:
                    if not i.startswith(":"):
                        i = i.split(" ")
                        inst, p = i[0], [l for l in i if l != i[0]]
                        c += self.opcodes.ops_size[self.opcodes.ops[inst]]+1
                for i in iset:
                    if not i.startswith(":"):
                        i = i.split(" ")
                        inst, p = i[0], [l for l in i if l != i[0]]
                        if not self._is_not_jump(inst) and p[0] == lbl["val"]:
                            self.program[self.program.index(" ".join(i))] = inst + " %s" % (c-2)
                    else:
                        self.program.remove(i)

            else:
                c = 0
                iset = self.program[pos:lbl["pos"]+1]
                for i in iset:
                    if not i.startswith(":"):
                        i = i.split(" ")
                        inst, p = i[0], [l for l in i if l != i[0]]
                        c += self.opcodes.ops_size[self.opcodes.ops[inst]]+1
                for i in iset:
                    if not i.startswith(":"):
                        i = i.split(" ")
                        inst, p = i[0], [l for l in i if l != i[0]]
                        if not self._is_not_jump(inst) and p[0] == lbl["val"]:
                            self.program[self.program.index(" ".join(i))] = inst + " %s" % c
                    else:
                        self.program.remove(i)

    def _is_not_jump(self, instruction):
        bytecode = self.opcodes.ops[instruction]
        if not 0xc0 <= bytecode <= 0xcf and bytecode != 0x1b and bytecode != 0x1a:
            return 1
        else:
            return 0

    def compile(self):
        self._check_syntax()
        self._calculate_distance()
        for line in self.program:
            line = line.split(" ")
            instruction, params = line[0], [l for l in line if l != line[0]]
            self.bytecode += chr(self.opcodes.ops[instruction])
            for p in params:
                try:
                    p = int(p)
                    self.bytecode += chr(p)
                except ValueError:
                        p = p.replace("\n", "") + "\x00"
                        for ch in p:
                            self.bytecode += ch

    def compile_and_run(self):
        pass

    def compile_and_save(self):
        pass
