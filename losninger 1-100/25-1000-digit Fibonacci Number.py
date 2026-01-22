# løst, https://projecteuler.net/problem=2

i = 2
fn1 = 1
fn2 = 1
while True:
    fn1, fn2 = fn2, fn1+fn2

    if len(str(fn1)) >= 1000:
        break

    i += 1

print(i)
# 4782