#this opens a file, then reads till who knows where, then xorrrrrrrrr it
from pwn import *
to_xor = open('<insert_image/file name>', 'rb').read()[:<insert till who knows what byte>]
xored = xor(to_xor, b'\xff')
f = open("<insert second file/who knows what>", "wb")
f.write(xored)
