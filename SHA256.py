#functions
def shift_right(x,shift):
    x =str(x)
    dec1 = int(x,2)
    out = dec1 >> shift
    binOut = bin(out)
    return binOut.replace("0b","").zfill(len(x))


def rotate_right(x,d):
    Rfirst = x[0 : len(x)-d]
    Rsecond = x[len(x)-d : ]
    value=Rsecond+Rfirst
    return value

def choose(x, y, z):
    decx = int(x,2)
    decy = int(y,2)
    decz = int(z,2)
    value = decz ^ (decx & (decy ^ decz))
    binOut = bin(value)
    return binOut.replace("0b","").zfill(len(x))
def majority(x, y, z):
    decx = int(x,2)
    decy = int(y,2)
    decz = int(z,2)
    value = ((decx | decy) & decz) | (decx & decy)
    binOut = bin(value)
    return binOut.replace("0b","").zfill(len(x))

def sigma0(x):
    # ROTR 7(x) ⊕ ROTR 18(x) ⊕ SHR3(x)

    a=rotate_right(x, 7)
    b=rotate_right(x, 18)
    c=shift_right(x, 3)
    inta=int(a,2)
    intb=int(b,2)
    intc=int(c,2)
    value=inta^intb^intc
    binOut = bin(value)
    binOut= binOut.replace("0b","")
    return binOut.zfill(len(x))

def sigma1(x):
    a=rotate_right(x, 17)
    b=rotate_right(x, 19)
    c=shift_right(x, 10)
    inta=int(a,2)
    intb=int(b,2)
    intc=int(c,2)
    value=inta^intb^intc
    binOut = bin(value)
    binOut= binOut.replace("0b","")
    return binOut.zfill(len(x))
    # ROTR 17(x) ⊕ ROTR 19(x) ⊕ SHR10(x)



def gamma0(x):
    # ROTR 2(x) ⊕ ROTR 13(x) ⊕ ROTR22(x)

    a=rotate_right(x, 2)
    b=rotate_right(x, 13)
    c=rotate_right(x, 22)
    inta=int(a,2)
    intb=int(b,2)
    intc=int(c,2)
    value=inta^intb^intc
    binOut = bin(value)
    binOut= binOut.replace("0b","")
    return binOut.zfill(len(x))


def gamma1(x):
    # ROTR 6(x) ⊕ ROTR 11(x) ⊕ ROTR25(x)
    a=rotate_right(x, 6)
    b=rotate_right(x, 11)
    c=rotate_right(x, 25)
    inta=int(a,2)
    intb=int(b,2)
    intc=int(c,2)
    value=inta^intb^intc
    binOut = bin(value)
    binOut= binOut.replace("0b","")
    return binOut.zfill(len(x))

def binary_add(x,y):
    sum = bin(int(x, 2) + int(y, 2))
    sum=sum.replace("0b","")
    sum=sum.zfill(32)
    res=""
    rev_res=""
    for i in range(0, 32):
        res = res + sum[-(i+1)]

    for i in range (0,32):
        rev_res=rev_res+res[-(i+1)]

    return rev_res
def binary_add4(w,x,y,z):
    sum = bin(int(w, 2) + int(x, 2)+int(y, 2)+int(z, 2))
    sum=sum.replace("0b","")
    sum=sum.zfill(32)
    res=""
    rev_res=""
    for i in range(0, 32):
        res = res + sum[-(i+1)]
    for i in range (0,32):
        rev_res=rev_res+res[-(i+1)]
    return rev_res
#starting of sha 256

##padding
message = input("enter the message")
phrase_size=len(message)*8
phrase_size_in_bin=bin(phrase_size)
phrase_size_in_bin=phrase_size_in_bin.replace("0b","")
binmessage= ''.join(format(ord(i), '08b') for i in message) # converts messgage into binary
binmessage= binmessage.ljust(len(binmessage)+1, '1') #adds 1 at the end of the string before padding
binmessage= binmessage.ljust(448, '0')
if len(phrase_size_in_bin)!=64:
    phrase_size_in_bin= phrase_size_in_bin.rjust(64, '0')

binmessage= binmessage+phrase_size_in_bin #addition of phrase size in binary at the end of padded messag
print(len(binmessage))
print(binmessage)

## message schedule
n = 32
chunks = [binmessage[i:i+n] for i in range(0, len(binmessage), n)] #splitting the 512 bit message into chunks of 32 bits
w0=chunks[0]
w1=chunks[1]
w2=chunks[2]
w3=chunks[3]
w4=chunks[4]
w5=chunks[5]
w6=chunks[6]
w7=chunks[7]
w8=chunks[8]
w9=chunks[9]
w10=chunks[10]
w11=chunks[11]
w12=chunks[12]
w13=chunks[13]
w14=chunks[14]
w15=chunks[15]
w16=binary_add4(sigma1(w14),w9,sigma0(w1),w0)
w17=binary_add4(sigma1(w15),w10,sigma0(w2),w1)
w18=binary_add4(sigma1(w16),w11,sigma0(w3),w2)
w19=binary_add4(sigma1(w17),w12,sigma0(w4),w3)
w20=binary_add4(sigma1(w18),w13,sigma0(w5),w4)
w21=binary_add4(sigma1(w19),w14,sigma0(w6),w5)
w22=binary_add4(sigma1(w20),w15,sigma0(w7),w6)
w23=binary_add4(sigma1(w21),w16,sigma0(w8),w7)
w24=binary_add4(sigma1(w22),w17,sigma0(w9),w8)
w25=binary_add4(sigma1(w23),w18,sigma0(w10),w9)
w26=binary_add4(sigma1(w24),w19,sigma0(w11),w10)
w27=binary_add4(sigma1(w25),w20,sigma0(w12),w11)
w28=binary_add4(sigma1(w26),w21,sigma0(w13),w12)
w29=binary_add4(sigma1(w27),w22,sigma0(w14),w13)
w30=binary_add4(sigma1(w28),w23,sigma0(w15),w14)
w31=binary_add4(sigma1(w29),w24,sigma0(w16),w15)
w32=binary_add4(sigma1(w30),w25,sigma0(w17),w16)
w33=binary_add4(sigma1(w31),w26,sigma0(w18),w17)
w34=binary_add4(sigma1(w32),w27,sigma0(w19),w18)
w35=binary_add4(sigma1(w33),w28,sigma0(w20),w19)
w36=binary_add4(sigma1(w34),w29,sigma0(w21),w20)
w37=binary_add4(sigma1(w35),w30,sigma0(w22),w21)
w38=binary_add4(sigma1(w36),w31,sigma0(w23),w22)
w39=binary_add4(sigma1(w37),w32,sigma0(w24),w23)
w40=binary_add4(sigma1(w38),w33,sigma0(w25),w24)
w41=binary_add4(sigma1(w39),w34,sigma0(w26),w25)
w42=binary_add4(sigma1(w40),w35,sigma0(w27),w26)
w43=binary_add4(sigma1(w41),w36,sigma0(w28),w27)
w44=binary_add4(sigma1(w42),w37,sigma0(w29),w28)
w45=binary_add4(sigma1(w43),w38,sigma0(w30),w29)
w46=binary_add4(sigma1(w44),w39,sigma0(w31),w30)
w47=binary_add4(sigma1(w45),w40,sigma0(w32),w31)
w48=binary_add4(sigma1(w46),w41,sigma0(w33),w32)
w49=binary_add4(sigma1(w47),w42,sigma0(w34),w33)
w50=binary_add4(sigma1(w48),w43,sigma0(w35),w34)
w51=binary_add4(sigma1(w49),w44,sigma0(w36),w35)
w52=binary_add4(sigma1(w50),w45,sigma0(w37),w36)
w53=binary_add4(sigma1(w51),w46,sigma0(w38),w37)
w54=binary_add4(sigma1(w52),w47,sigma0(w39),w38)
w55=binary_add4(sigma1(w53),w48,sigma0(w40),w39)
w56=binary_add4(sigma1(w54),w49,sigma0(w41),w40)
w57=binary_add4(sigma1(w55),w50,sigma0(w42),w41)
w58=binary_add4(sigma1(w56),w51,sigma0(w43),w42)
w59=binary_add4(sigma1(w57),w52,sigma0(w44),w43)
w60=binary_add4(sigma1(w58),w53,sigma0(w45),w44)
w61=binary_add4(sigma1(w59),w54,sigma0(w46),w45)
w62=binary_add4(sigma1(w60),w55,sigma0(w47),w46)
w63=binary_add4(sigma1(w61),w56,sigma0(w48),w47)

print(w63)


#compression
#h0 (intital hash values)
a="01101010000010011110011001100111"
b="10111011011001111010111010000101"
c="00111100011011101111001101110010"
d="10100101010011111111010100111010"
e="01010001000011100101001001111111"
f="10011011000001010110100010001100"
g="00011111100000111101100110101011"
h="01011011111000001100110100011001"


k0="01000010100010100010111110011000"
#wo
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k0,w0)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)

#w1
k1="01110001001101110100010010010001"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k1,w1)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w2
k2="01000010100010100010111110011000"

add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k2,w3)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w3
k3="11101001101101011101101110100101"

add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k3,w3)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w4
k4="00111001010101101100001001011011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k4,w4)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w5
k5="01011001111100010001000111110001"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k5,w5)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w6
k6="10010010001111111000001010100100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k6,w6)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w7
k7="1010101100011100010111101"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k7,w7)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w8
k8="11011000000001111010101010011000"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k8,w8)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w9
k9="00010010100000110101101100000001"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k9,w9)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w10
k10="00100100001100011000010110111110"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k0,w10)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w11
k11="01010101000011000111110111000011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k0,w11)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w12
k12="01110010101111100101110101110100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k12,w12)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w13
k13="10000000110111101011000111111110"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k0,w13)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w14
k14="10011011110111000000011010100111"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k14,w14)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w15
k15="11000001100110111111000101110100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k15,w15)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w16
k16="11100100100110110110100111000001"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k16,w16)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w17
k17="11101111101111100100011110000110"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k17,w17)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w18
k18="00001111110000011001110111000110"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k18,w18)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w19
k19="00100100000011001010000111001100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k19,w19)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w20
k20="00101101111010010010110001101111"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k20,w20)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w21
k21="01001010011101001000010010101010"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k21,w21)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w22
k22="01011100101100001010100111011100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k22,w22)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w23
k23="01110110111110011000100011011010"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k23,w23)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w24
k24="10011000001111100101000101010010"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k24,w24)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w25
k25="10101000001100011100011001101101"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k25,w25)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w26
k26="10110000000000110010011111001000"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k26,w26)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w27
k27="10111111010110010111111111000111"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k27,w27)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w28
k28="11000110111000000000101111110011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k28,w28)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w29
k29="11010101101001111001000101000111"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k29,w29)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w30
k30="00000110110010100110001101010001"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k30,w30)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w31
k31="0001010000101001001010010110011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k31,w31)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w32
k32="00100111101101110000101010000101"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k32,w31)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w33
k33="00101110000110110010000100111000"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k33,w32)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w34
k34="01001101001011000110110111111100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k34,w34)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w35
k35="01010011001110000000110100010011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k35,w35)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w36
k36="01100101000010100111001101010100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k36,w36)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w37
k37="01110110011010100000101010111011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k37,w37)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w38
k38="10000001110000101100100100101110"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k38,w38)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w39
k39="10010010011100100010110010000101"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k39,w39)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w40
k40="10100010101111111110100010100001"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k40,w40)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w41
k41="10101000000110100110011001001011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k41,w41)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w42
k42="11000010010010111000101101110000"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k42,w42)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w43
k43="11000111011011000101000110100011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k43,w43)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w44
k44="11010001100100101110100000011001"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k44,w44)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w45
k45="11010110100110010000011000100100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k45,w45)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w46
k46="11110100000011100011010110000101"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k46,w46)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w47
k47="00010000011010101010000001110000"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k47,w47)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w48
k48="00011001101001001100000100010110"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k48,w48)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w49
k49="00011110001101110110110000001000"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k32,w49)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w50
k50="00100111010010000111011101001100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k50,w50)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w51
k51="00110100101100001011110010110101"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k51,w51)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w52
k52="00111001000111000000110010110011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k52,w52)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w53
k53="01001110110110001010101001001010"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k53,w53)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w54
k54="01011011100111001100101001001111"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k54,w54)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w55
k55="01101000001011100110111111110011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k55,w55)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w56
k56="01110100100011111000001011101110"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k56,w56)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w57
k57="01111000101001010110001101101111"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k57,w57)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w58
k58="10000100110010000111100000010100"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k58,w58)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w59
k59="10001100110001110000001000001000"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k59,w59)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w60
k60="10010000101111101111111111111010"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k60,w60)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w61
k61="10100100010100000110110011101011"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k61,w61)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w62
k62="10111110111110011010001111110111"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k62,w62)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)
#w63
k63="11000110011100010111100011110010"
add1=binary_add(sigma1(e),choose(e,f,g))
add2=binary_add(k63,w63)
add3=binary_add(add1,add2)
add4=binary_add(h,add3)
T1=add4
T2=binary_add(sigma0(a),majority(a,b,c))
#shifiting and addition of t values
h=g
g=f
f=e
e=d
d=c
c=b
b=a
a=""
a=binary_add(T1,T2)
e=binary_add(e,T1)

## end of compression

A="01101010000010011110011001100111"
B="10111011011001111010111010000101"
C="00111100011011101111001101110010"
D="10100101010011111111010100111010"
E="01010001000011100101001001111111"
F="10011011000001010110100010001100"
G="00011111100000111101100110101011"
H="01011011111000001100110100011001"
H1A=binary_add(A,a)
H1B=binary_add(B,b)
H1C=binary_add(C,c)
H1D=binary_add(D,d)
H1E=binary_add(E,e)
H1F=binary_add(F,f)
H1G=binary_add(G,g)
H1H=binary_add(H,h)
print(H1A)
hashed_message=hex(int(H1A,2)).replace("0x","")#hex(int(H1B,2))+hex(int(H1C,2))+hex(int(H1D,2))+hex(int(H1E,2))+hex(int(H1F,2))+hex(int(H1G,2))+hex(int(H1H,2))
print(hashed_message)