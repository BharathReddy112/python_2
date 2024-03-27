'''
&=  Performs Bitwise AND on operands and assign value to left operand	a &= b   
|=  Performs Bitwise OR on operands and assign value to left operand	a |= b    
^=  Performs Bitwise xOR on operands and assign value to left operand	a ^= b    
>>= Performs Bitwise right shift on operands and assign value to left operand	a >>= b     
<<= Performs Bitwise left shift on operands and assign value to left operand	a <<= b 
'''

a = 3
b = 5
# a = a & b 
a &= b
print(a)

# a = a | b 
a |= b
print(a)

# a = a ^ b 
a ^= b
print(a)

# a = a >> b 
a >>= b 
print(a)

# a = a << b 
a <<= b
print(a)

