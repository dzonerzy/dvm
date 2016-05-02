__author__ = 'dzonerzy'
from core.compiler import DVMCompiler
from core.vm import Dvm

a = DVMCompiler("tocompile.dasm")
a.compile()
VM = Dvm()
VM.vm_exec_mem(a.bytecode)


