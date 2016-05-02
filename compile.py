__author__ = 'dzonerzy'
from core.compiler import DVMCompiler
from core.vm import Dvm

a = DVMCompiler("tocompile.dasm")
a.compile_and_save()
VM = Dvm("tocompile.dasm.dvm")
VM.vm_exec_stats()
