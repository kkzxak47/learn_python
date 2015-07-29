# coding: utf-8


def fun(seq, idfun=lambda x: x):
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        result.append(marker)
    return result

print ''.join(fun('ACCBDRSEEEUOKO', lambda x: x.lower()))
