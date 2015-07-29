import math
num = 100
count = 0

for num_a in range(2, num + 1):
    for i in range(2, int(math.sqrt(num_a) + 1)):
        if num_a % i == 0:
            break
        else:
            num_b = num_a
            num_w = 0
            while num_b > 0:
                num_b /= 10
                num_w += 1
            if num_w == 1:
                count += 1
            elif num_w >= 2:
                w = 1
                while num_w > w:
                    num_x = int(num_b/10**w) + (num_b % 10**w) * (10**num_w-w)
                    w += 1
                    for num_c in range(2, int(math.sqrt(num_x) + 1)):
                        if num_x % num_c == 0:
                            w = num_w + 1
                            break
                    if w == num_w:
                        print num_a, num_b
                        count += 1
print count
