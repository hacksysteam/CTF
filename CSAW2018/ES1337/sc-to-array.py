import subprocess

assert subprocess.call(['/usr/bin/nasm', 'sc.asm', '-o', 'sc']) == 0
with open('sc', 'r') as fd:
  sc = fd.read()

print('const sc = [{}];'.format(', '.join('0x{:02x}'.format(ord(c)) for c in sc)))

