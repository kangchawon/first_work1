문1.
print("100")
print(100)
print(50+50)
print("50+50")      

문2.
print('%d/%d=%d'%(5,10,5/10))


문3.
print("%04d"%876)
print("%5s"%"CookBook")
print("%1.1f"%123.45)

문4.
print("{2:d}{0:d}{1:d}".format(111,222,333))

문5
print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("\b뒤로한칸이동\b연습")
print("\\역슬래시출력")
print("\'작은따옴표출력")
print("\"큰따옴표출력")

문6.
boolVar = True
intVar = 100
floatVar = 123.45
strVar = "안녕"
character = 1

boolVar, intVar, floatVar, strVar= True, 0, 0.0, ""
character 형식이  거리가 멈

문7.
num1=100
num1=num2=100
num1=num2=num3=100


문8.
a=b=10=c=d=20

10=c 차례에서 에러가 남, 상수에는 변수를 넣지 못함

문9.
value=0

b=bin(value)
h=hex(value)

print(b)
print(h)

value=2

b=bin(value)
h=hex(value)

print(b)
print(h)

value=7

b=bin(value)
h=hex(value)

print(b)
print(h)

value=11

b=bin(value)
h=hex(value)

print(b)
print(h)

value=16

b=bin(value)
h=hex(value)

print(b)
print(h)


value=0

b=format(value, 'b')
h=format(value, 'x')

print(b)
print(h)

value=2

b=format(value, 'b')
h=format(value, 'x')

print(b)
print(h)

value=7

b=format(value, 'b')
h=format(value, 'x')

print(b)
print(h)

value=11

b=format(value, 'b')
h=format(value, 'x')

print(b)
print(h)

value=16

b=format(value, 'b')
h=format(value, 'x')

print(b)
print(h)

문10.
b = int('0b0011', 2)
print(b)

b = int('0b01010', 2)
print(b)

h = int('0x11', 16)
print(h)

o = int('0o17', 8)
print(o)

문11.
b = int('0b1011', 2)
print(b)

h = int('0x1a', 16)
print(h)

문12.
value=1

h=hex(value)
o=oct(value)
b=bin(value)

print(h)
print(o)
print(b)

문13.
int('1002',2)

int('1008',8)

int('AAFG',16)

int('1001',2)

int('1007',8)

int('AAFF',16)

문14.
class(3.3)
정수형은 class 표현 안됨
int(3.3)
float(3.3)
boolVar = True, False, Null
불형에서 Null 은 정의 되지 않음
print(1+1)
print('hello world')
print("hello world")
작은따옴표, 큰따옴표는 문자, 문자열에 차이가 없음

문15.
num=12345678
hex_num=hex(12345678)
oct_num=oct(12345678)
bin_num=bin(12345678)

print("10진수==>", num)
print("16진수==>", hex_num)
print("8진수==>", oct_num)
print("2진수==>", bin_num)


