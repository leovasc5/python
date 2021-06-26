soma = lambda x, y: x + y
mult = lambda a, b, c: (a+b)*c

print(soma(2, 4))
print(mult(6, 4, 2))

res = (lambda d, e: d+e)(3, 2)
print(res)

r = lambda f, func: f+func(f)
resultado = r(2, lambda f:f*f)
print(resultado)