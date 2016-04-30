__author__ = 'dzonerzy'

class Memory:
    # large memory
    stack = []
    ram = []
    heap = []

    # pointers
    sp = 0
    bp = 0

    # registers (not used atm)
    dvmeax = [16]
    dvmebx = [16]
    dvmecx = [16]
    dvmedx = [16]

    # cpu flags
    ef = 0
    gf = 0
    sf = 0
    esf = 0
    egf = 0
    nef = 0

    # oldbp
    oldbp = 0

    def __init__(self, bytecode):
        for i in range(0, 4096):
            self.ram.append(0)
            self.stack.append(0)
        self._load_bytecode(bytecode)

    def _load_bytecode(self, bytecode):
        for _byte in bytecode:
            self.ram.insert(self.bp, ord(_byte))
            self.inc_bp()
        self.bp = 0

    def inc_bp(self):
        self.bp += 1

    def dec_bp(self):
        self.bp -= 1

    def inc_sp(self):
        self.sp += 1

    def dec_sp(self):
        self.sp -= 1