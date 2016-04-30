__author__ = 'dzonerzy'
import sys
import trace
from core.memory import Memory
from core.opcodes import Opcodes, ReserverdBytes
from core.vcpu import vCPU
from core.errors import VMUnsupportedInstruction, VMNotImplementedInstruction

class Dvm:
    mem = None
    opcodes = Opcodes()
    reservation = ReserverdBytes()
    stats = None
    vcpu = vCPU()

    def __init__(self, path):
        self.stats = self.vm_exec
        self._load(path)

    def _load(self, path):
        bc = file(path, "rb").read()
        #bc = "\x7eNKXSOVYXO\x00\xbb\x0a\xfa\x00\xc0\x05\xde\x0a\xb0" \
        #     "\x1b\x09\xb1\xb1\xb1\xb1\xb1\xb1\xb1\xb1\xb1\x60\xff"
        self.mem = Memory(bc)

    def _single_step(self):
        params = []
        instruction = self.mem.ram[self.mem.bp]
        self.mem.inc_bp()
        for inst in self.opcodes.ops:
            if instruction == int(self.opcodes.ops[inst]):
                has_param = self.opcodes.ops_size[instruction]
                has_reservation = 0
                if instruction in self.opcodes.ops_reservation:
                    has_reservation = self.reservation.reserved[self.opcodes.ops_reservation[instruction]]
                for param in range(0, has_param):
                    if has_reservation:
                        if (has_reservation == 0x0f and param == range(0, has_param)[0]) or \
                                (has_reservation == 0x01 and param == range(0, has_param)[-1]):
                            tmp = ""
                            while self.mem.ram[self.mem.bp] != 0x00:
                                tmp += chr(self.mem.ram[self.mem.bp])
                                self.mem.inc_bp()
                            params.append(tmp+"\x00")
                            self.mem.inc_bp()
                    else:
                        params.append(self.mem.ram[self.mem.bp])
                        self.mem.inc_bp()
                return self._process_instruction(self.mem, instruction, params)
        raise VMUnsupportedInstruction(instruction)

    def _process_instruction(self, vm, inst, args):
        try:
            return self.vcpu.ops_func[inst](vm, args)
        except KeyError:
            raise VMNotImplementedInstruction(inst)

    def vm_exec(self):
        while self._single_step():
            pass

    def vm_exec_stats(self):
        tracer = trace.Trace(
            ignoredirs=[sys.prefix, sys.exec_prefix],
            trace=0,
            count=1)
        tracer.run('VM.stats()')
        r = tracer.results()
        cycle = 0
        for c in r.counts:
            if "memory.py" not in c[0]:
                cycle += r.counts[c]
        print "\nExecution ended with %s vCPU cycles" % cycle
