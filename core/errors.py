__author__ = 'dzonerzy'

class VMBaseException(Exception):
    def __init__(self, arg):
        super(VMBaseException, self).__init__(arg)

class VMUnsupportedInstruction(VMBaseException):
    def __init__(self, opcode):
        super(VMBaseException, self).__init__("Unsupported instruction '%s'" % hex(opcode))

class VMNotImplementedInstruction(VMBaseException):
    def __init__(self, opcode):
        super(VMBaseException, self).__init__("Not implemented instruction '%s'" % hex(opcode))
