# Python VM - DVM
Python VM with simple custom assembly code

This is just an experimental project, based on a custom VM implementation with some "standard" opcodes, many things are still not implemented so, if you want to add your custom opcode add it to <b>core/opcodes.py</b> and then implement it in <b>core/vcpu.py</b>.

Feel free to contribute :)

#Output

```
dzonerzy:dvm dzonerzy$ python dvm.py
DANIELONE

Stats:
[+] vCPU instructions: 3890
[+] VM loops: 879
[+] VM exec instructions: 60
[+] Exec time: 0.00928592681885 secs
```

\#dzonerzy
