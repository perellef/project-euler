# løst, https://projecteuler.net/problem=2

s = 0

fn1 = 1
fn2 = 2
while True:
    fn1, fn2 = fn2, fn1+fn2

    if fn2 > 4000000:
        break
    if fn2 % 2 == 0:
        s += fn2

print(s)
# 4613730