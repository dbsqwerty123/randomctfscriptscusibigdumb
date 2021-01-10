### Substitution Cipher
1) realise its not xor cus of the "{" so must be substitution cipher. 

2) https://www.boxentriq.com/code-breaking/cryptogram
3) ![image-20210110121457232](C:\Users\Sean\AppData\Roaming\Typora\typora-user-images\image-20210110121457232.png)


### XOR CHALL (xortools)
Xor tool https://github.com/hellman/xortool
1) run 

```bash
xortool -x <cyberchef base64 decoded file> -O <output dir>
```

2) cat files, try read english

3) open csv see this partial key ```xortool_out/376.out;b"N&CK'SC*MP"```

4) ![image-20210110121531060](C:\Users\Sean\AppData\Roaming\Typora\typora-user-images\image-20210110121531060.png)

5) looks like second char and 8th char is big gay. lets go use another cyberchef tab to xor it out.

6) looks like a conversation, so maybe instead of MY should be MR. 

7) now message xor key = encrypted. Since we have encrypted and message, we can do message encrypted xor message = key. 

8) so lets input base64.d(Axt) xor R ("r" being message) and we get AI (I is the one we want)

9) so now our key is ```NICK'SC*MP```

10) now to fix the 8th char, so we see this weird string "WATE7" which should be water. so....
base64(HGYHBh1) xor WATER gives us K'SCO. and "O" is the last char. 

So now our key is ```NICK'SCOMP```


### XOR CHALL 2 (math)
challenge:
```python
import base64
def enc(m):
    a=''.join([chr(13*(ord(m[i])^ord(m[i+4]))%128) for i in range(0,len(m)-4)])
    return base64.b64encode(a.encode())
```
SOLVE SCRIPT 
```python
import base64
encoded = base64.b64decode("AnBgdX0ZPysmDyByQxROHD45OQ0iVkI7L24kYnACXTA4QAo2WSo=")
a = "IRS{"
    a=''.join([chr(13*(ord(m[i])^ord(m[i+4]))%128) for i in range(0,len(m)-4)])
'''
if we also know the flag format duhh
if 13*ord(a[i]) ^ <brute force 128 numbers to see which map> = encoded[i], we know we correct
'''

for i in range(0,len(encoded)):
    for j in range(0,128): # brute force all possible chars from the mod
        if 13*(ord(a[i])^j)%128 == encoded[i]:
            a += chr(j) #since already have first 4 chars, dont need m[i+4]
print(a)

#proper method using idea of modular multiplicative inverse. 
print(encoded)

#Modular Multiplicative Inverse is 69          

for i in range(0,len(encoded)):
    first = (encoded[i] * 69)%128
    a += chr(first ^ ord(a[i]))
             
print(a)
```