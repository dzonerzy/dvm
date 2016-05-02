__author__ = 'dzonerzy'

class vCPU:
    ops_func = dict({})

    def __init__(self):
        self.ops_func.update({0x7e: self.CSTRSP,
                              0xff: self.EXT,
                              0xdd: self.INCBSP,
                              0xde: self.DECBSP,
                              0xba: self.AGSP,
                              0xbb: self.TOSP,
                              0x60: self.SSP,
                              0xcf: self.SSDD,
                              0xfa: self.CB,
                              0xb0: self.INCSP,
                              0xb1: self.DECSP,
                              0x1a: self.SA,
                              0x1b: self.SD,
                              0xc0: self.SSU,
                              0x90: self.LICSP,
                              })

    def SSP(self, vmem, params):
        tmp = ""
        while vmem.stack[vmem.sp] != 0:
            tmp += chr(vmem.stack[vmem.sp])
            vmem.inc_sp(1)
        print tmp
        vmem.inc_sp(1)
        return 1

    def TOSP(self, vmem, params):
        vmem.dec_sp(params[0])
        return 1

    def AGSP(self, vmem, params):
        #vmem.sp += param[0]
        vmem.inc_sp(params[0])
        return 1

    def CSTRSP(self, vmem, params):
        for ch in params[0]:
            vmem.stack.insert(vmem.sp, ord(ch))
            vmem.inc_sp(1)
        return 1

    def EXT(self, vmem, params):
        return 0

    def INCBSP(self, vmem, params):
        vmem.stack[vmem.sp] = (vmem.stack[vmem.sp]+params[0])
        return 1

    def DECBSP(self, vmem, params):
        vmem.stack[vmem.sp] = (vmem.stack[vmem.sp]-params[0])
        return 1

    def SSDD(self, vmem, params):
        if vmem.nef:
            vmem.dec_bp(params[0])
        return 1

    def SSU(self, vmem, params):
        if vmem.ef:
            vmem.inc_bp(params[0])
        return 1

    def CB(self, vmem, params):
        val = vmem.stack[vmem.sp]
        vmem.gf, vmem.eq, vmem.sf, vmem.egf, vmem.esf, vmem.nef = 0, 0, 0, 0, 0, 0
        if val > params[0]:
            vmem.gf = 1
        if val == params[0]:
            vmem.ef = 1
        if val < params[0]:
            vmem.sf = 1
        if val >= params[0]:
            vmem.egf = 1
        if val <= params[0]:
            vmem.esf = 1
        if val != params[0]:
            vmem.nef = 1
        return 1

    def INCSP(self, vmem, params):
        vmem.inc_sp(params[0])
        return 1

    def DECSP(self, vmem, params):
        vmem.dec_sp(params[0])
        return 1

    def SA(self, vmem, params):
        vmem.inc_bp(params[0])
        return 1

    def SD(self, vmem, params):
        vmem.dec_bp(params[0])
        return 1

    def LICSP(self, vmem, params):
        tocpy = raw_input()
        for ch in tocpy+"\x00":
            vmem.stack[vmem.sp] = ord(ch)
            vmem.inc_sp(1)
        return 1

