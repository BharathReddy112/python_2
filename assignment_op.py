'''
=   Assign value of right side of expression to left side operand	x = y + z 
+=  Add and Assign: Add right side operand with left side operand and then assign to left operand	a += b   
-=  Subtract AND: Subtract right operand from left operand and then assign to left operand: True if both operands are equal	a -= b  
*=  Multiply AND: Multiply right operand with left operand and then assign to left operand	a *= b     
/=  Divide AND: Divide left operand with right operand and then assign to left operand	a /= b
%=  Modulus AND: Takes modulus using left and right operands and assign result to left operand	a %= b  
//= Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a //= b   
**= Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a **= b     
'''

a = 3
b = 5
  
c = a + b  
print(c)

# a = a + b 
a += b 
print(a)

# a = a - b 
a -= b 
print(a)

# a = a * b 
a *= b 
print(a)

# a = a / b 
a /= b 
print(a)

# a = a % b 
a %= b  
print(a)

# a = a // b 
a //= b  
print(a)

# a = a ** b 
a **= b
print(a)

