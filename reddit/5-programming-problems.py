# coding: utf-8

"""
https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
Can you actually code anything?

For my Software Engineer position I'm usually expecting you to be able to code
something. I'm talking about real code here: I give you a problem, and you
write a solution for it using any programming language you feel confortable
with.

Do you think you can actually do this?

Here is the deal: if you can't solve the following 5 problems in less than
1 hour, you may want to revisit your resume. You might be great at doing
whatever you do today, but you need to stop calling yourself a "Software
Engineer" (or Programmer, or Computer Science specialist, or even maybe
    "Developer".) Stop lying to yourself, and take some time to re-focus
your priorities.

The 5 problems

(The following problems are ridiculously simple, but you'd be surprise to
    discover how many people struggle with them. To the point of not getting
    anything done at all. Seriously.)
"""


class Problem1(object):

    """Problem 1

    Write three functions that compute the sum of the numbers in a given list
    using a for-loop, a while-loop, and recursion.
    """

    def __init__(self, num_list):
        self.num_list = num_list

    def test(self):
        print 'for_loop:', self.for_loop(self.num_list)
        print 'while_loop:', self.while_loop(self.num_list)
        print 'recursion:', self.recursion(self.num_list)

    def for_loop(self, num_list):
        result = 0
        for x in num_list:
            result += x
        return result

    def while_loop(self, num_list):
        lst = num_list[:]
        result = 0
        while lst:
            x = lst.pop()
            result += x
        return result

    def recursion(self, num_list):
        if not num_list:
            return 0
        else:
            return num_list[0] + self.recursion(num_list[1:])


class Problem2(object):

    """Problem 2

    Write a function that combines two lists by alternatingly taking elements.
    For example: given the two lists [a, b, c] and [1, 2, 3],
    the function should return [a, 1, b, 2, c, 3].
    """

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def alternate_taking(self):
        from itertools import chain
        return list(chain(*zip(self.l1, self.l2)))

    def test(self):
        print 'alternate {} {}:'.format(self.l1, self.l2)
        print self.alternate_taking()


class Problem3(object):

    """Problem 3

    Write a function that computes the list of the first 100 Fibonacci numbers.
    By definition, the first two numbers in the Fibonacci sequence are 0 and
    1, and each subsequent number is the sum of the previous two. As an
    example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8,
    13, 21, and 34.
    """

    def __init__(self, num=10):
        self.result = []
        self.num = num
        self.this = 0
        self.next = 1
        self.calc()

    def calc(self):
        for i in range(self.num):
            self.result.append(self.next)
            self.this, self.next = self.next, self.this + self.next

    def test(self):
        print 'First 100 Fibonacci numbers: {}'.format(self.result)


class Problem4(object):

    """
    Problem 4

    Write a function that given a list of non negative integers, arranges them
    such that they form the largest possible number.
    For example, given [50, 2, 1, 9], the largest formed number is 95021.
    """

    def __init__(self, num_list):
        self.num_list = num_list
        self.str_list = map(str, num_list)

    def arrange(self):
        def compare(a, b):
            '''better form comparison'''
            return cmp(int(str(a) + str(b)), int(str(b) + str(a)))

        sorted_lst = sorted(self.str_list, cmp=compare, reverse=True)
        return int(''.join(sorted_lst))

    def permutation(self):
        from itertools import permutations
        all_possible_perms = (int(''.join(map(str, x)))
                              for x in permutations(self.num_list))
        return max(all_possible_perms)

    def test(self):
        print 'largest formed number: {} (sort by better form)'.format(self.arrange())
        print 'largest formed number: {} (permutation)'.format(self.permutation())


class Problem5(object):

    """
    Problem 5

    Write a program that outputs all possibilities to put + or - or nothing
    between the numbers 1, 2, ..., 9 (in this order) such that the result
    is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
    """

    def __init__(self, lst='123456789', num=100):
        self.lst = lst
        self.num = num
        self.result = []

    def f(self, pre, remain):
        if not remain:
            if eval(pre) == self.num:
                self.result.append(pre)
        else:
            self.f(pre + '+' + remain[0], remain[1:])
            self.f(pre + '-' + remain[0], remain[1:])
            self.f(pre + remain[0], remain[1:])

    def test(self):
        self.f(self.lst[0], self.lst[1:])
        for x in self.result:
            print x


def main():
    # p1 = Problem1([1, 2, 3, 4, 5])
    # p1.test()
    # p2 = Problem2(['a', 'b', 'c'], [1, 2, 3])
    # p2.test()
    # p3 = Problem3(100)
    # p3.test()
    # p4 = Problem4([501, 50, 2, 1, 9])
    # p4 = Problem4([56, 565655, 56565665])
    p4 = Problem4([9, 95, 959, 9585, 9595])
    # p4 = Problem4([4, 56, 5])
    # p4 = Problem4([4, 50, 5])
    # p4 = Problem4([50, 2, 1, 9])
    p4.test()
    # p5 = Problem5('123456789', 100)
    # p5.test()
    return 0


if __name__ == '__main__':
    main()
