# %%

A = 1
B = 5

print(A)
print(B)

# %%
C = A
A = B
B = C

print(A)
print(B)

# %%

A, B = B, A

print(A)
print(B)

# %%
a, b, *resto = 1, 2, 3, 4, 5

print(a, b, resto)

# %%
def soma(a, *args):
    total = a + sum(args)
    return total

soma(1, 2, 4, 7, 4)

# %%
def soma_quatro(a,b,c,d):
    return a+b+c+d

values = [1,2,3,4]
soma_quatro(*values)