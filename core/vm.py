__author__ = 'dzonerzy'
import sys
import time
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
    vcpuloop = 0
    vminstruction = 0
    start_time = time.time()

    def __init__(self, path=None):
        self.stats = self.vm_exec
        if path is not None and path != "":
            self._load(path)

    def _load(self, path):
        bc = file(path, "rb").read()
        self.mem = Memory(bc)

    def _single_step(self):
        params = []
        instruction = self.mem.ram[self.mem.bp]
        self.mem.inc_bp(1)
        for inst in self.opcodes.ops:
            self.vcpuloop += 1
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
                                self.mem.inc_bp(1)
                            params.append(tmp+"\x00")
                            self.mem.inc_bp(1)
                    else:
                        params.append(self.mem.ram[self.mem.bp])
                        self.mem.inc_bp(1)
                self.vminstruction += 1
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

    def vm_exec_mem(self, bytecode):
        self.mem = Memory(bytecode)
        self.vm_exec()

    def vm_exec_stats(self):
        tracer = trace.Trace(
            ignoredirs=[sys.prefix, sys.exec_prefix],
            trace=0,
            count=1)
        tracer.run('VM.stats()')
        r = tracer.results()
        instructions = 0
        for c in r.counts:
            if "memory.py" not in c[0]:
                instructions += r.counts[c]
        print "\nStats:\n[+] vCPU instructions: %s\n[+] VM loops: %s\n[+] VM exec instructions: %s\n[+] Exec time: %.3f secs" % \
              (instructions, self.vcpuloop, self.vminstruction, time.time()-self.start_time)
