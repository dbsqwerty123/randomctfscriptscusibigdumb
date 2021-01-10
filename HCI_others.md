    I KINDA PRESUME WHOEVER READS THIS HAS BASIC UNDERSTANDING 


1) stegsolve/online tool

2) magic bytes fix

3) audio spectogram/base64 decode

4) base64 recursion/png

5) Linux Volatility. find flag.docx and base64 string. profit

6) PIL big gay. 
```python
import requests
from PIL import Image
import time


#section 1
s = requests.session()
r = s.get("http://challs.sieberrsec.tech:8129/test/A")
print(r.text)
i1 = r.text[348:375]
print(i1)
print(i1[6:-2])
f = open("1.jpg",'wb')
f.write(s.get('http://challs.sieberrsec.tech:8129' + i1).content)
f.close()
img = Image.open("1.jpg").load()

#compare every image pixels

#Assumption that img[0,0] = baseline
a1 = ""
for i in range(1080):
    for j in range(1080):
        if img[i,j] > img[0,0]:
            a1 = a1 + "1"
        elif img[i,j] < img[0,0]:
            a1 = a1 + "0"
print(a1)
r = s.post("http://challs.sieberrsec.tech:8129/submit/A", data={"answertext": a1, "ts": i1[6:-2]})


##chall 2
print(r.text)
i2a = r.text[1786:1813]
print(i2a)
r = s.get("http://challs.sieberrsec.tech:8129" + i2a)
print(r.text)
i2b = r.text[356:383]
print(i2b)
f = open("1.jpg",'wb')
f.write(s.get('http://challs.sieberrsec.tech:8129' + i2b).content)
f.close()
img = Image.open("1.jpg").load()

#make a freq dictionary to find the standard pixels
d2 = dict()
for i in range(2560):
    for j in range(1440):
        if img[i,j] in d2:
            d2[img[i,j]] = d2[img[i,j]] + 1
        else:
            d2[img[i,j]] = 1
print(d2)

#find the top and second top pixel, i.e the 2 standards.
tmp1 = max(d2.values())
tmp2 = min(d2.keys()) #Assign random key lmao
for k in d2.keys():
    if d2[k] != tmp1 and d2[k] > d2[tmp2]:
        tmp2 = k
#brainded, just find key instead of value/frequency
for k in d2.keys():
    if d2[k] == tmp1:
        tmp1 = k
        break
print(tmp1)
print(tmp2)

def similar(b, v):
    for i in range(3):
        if abs(v[i]-b[i]) > 1:
            return False
    return True

#compare and yeet to server
a2 = ""
for i in range(2560):
    for j in range(1440):
        if similar(tmp1, img[i,j]):
            if img[i,j] > tmp1:
                a2 = a2 + "1"
            elif img[i,j] < tmp1:
                a2 = a2 + "0"
        else:
            if img[i,j] > tmp2:
                a2 = a2 + "1"
            elif img[i,j] < tmp2:
                a2 = a2 + "0"
print(a2)

r = s.post("http://challs.sieberrsec.tech:8129/submit/B", data={"answertext": a2, "ts": i2b[6:-2]})
print(r.text)



#test/cases following the word document.


def test1(a, b):
    for i in range(3):
        if abs(a[i] - b[i]) <= 5 or abs(a[i] - b[i]) >= 10:
            return False
    return True

def test2(a, b):
    for i in range(3):
        if abs(a[i] - b[i]) == 0 or abs(a[i] - b[i]) > 5:
            return False
    return True

def test3(a, b):
    for i in range(3):
        if abs(a[i] - b[i]) <= 3 or abs(a[i] - b[i]) > 5:
            return False
    return True

def test4(a, b):
    for i in range(3):
        if abs(a[i] - b[i]) < 1 or abs(a[i] - b[i]) > 2:
            return False
    return True


i3a = r.text[1960:1987]
print(i3a)
r = s.get("http://challs.sieberrsec.tech:8129" + i3a)
print(r.text)
i3b = r.text[357:384]
print(i3b)
f = open("1.jpg",'wb')
f.write(s.get('http://challs.sieberrsec.tech:8129' + i3b + "0").content)
f.close()
f = open("2.jpg",'wb')
f.write(s.get('http://challs.sieberrsec.tech:8129' + i3b + "1").content)
f.close()
f = open("3.jpg",'wb')
f.write(s.get('http://challs.sieberrsec.tech:8129' + i3b + "2").content)
f.close()
img1 = Image.open("1.jpg").load()
img2 = Image.open("2.jpg").load()
a3 = ""
for i in range(1920):
    for j in range(1080):
        if test1(img1[i,j], img2[i,j]):
            a3 = a3 + "1"
        elif test2(img1[i,j], img2[i,j]):
            a3 = a3 + "0"
print(a3)
img3 = Image.open("3.jpg").load()
for i in range(1920):
    for j in range(1080):
        if test3(img1[i,j], img3[i,j]):
            a3 = a3 + "1"
        elif test4(img1[i,j], img3[i,j]):
            a3 = a3 + "0"
print(a3)

r = s.post("http://challs.sieberrsec.tech:8129/submit/C", data={"answertext": a3, "ts": i3b[6:-2]})
print(r.text)
```