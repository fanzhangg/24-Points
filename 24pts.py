import random

from Game import *


def cal(a, b, c, d):
    a_ = str(a)
    b_ = str(b)
    c_ = str(c)
    d_ = str(d)
    perm = [[a_] + [b_] + [c_] + [d_], [a_] + [b_] + [d_] + [c_], [a_] + [c_] + [b_] + [d_], [a_] + [c_] + [d_] + [b_],
            [a_] + [d_] + [b_] + [c_], [a_] + [d_] + [c_] + [b_], [b_] + [a_] + [c_] + [d_], [b_] + [a_] + [d_] + [c_],
            [b_] + [c_] + [a_] + [d_], [b_] + [c_] + [d_] + [a_], [b_] + [d_] + [a_] + [c_], [b_] + [d_] + [c_] + [a_],
            [c_] + [a_] + [b_] + [d_], [c_] + [a_] + [d_] + [b_], [c_] + [b_] + [a_] + [d_], [c_] + [b_] + [d_] + [a_],
            [c_] + [d_] + [a_] + [b_], [c_] + [d_] + [b_] + [a_], [d_] + [a_] + [b_] + [c_], [d_] + [a_] + [c_] + [b_],
            [d_] + [b_] + [a_] + [c_], [d_] + [b_] + [c_] + [a_], [d_] + [c_] + [a_] + [b_], [d_] + [c_] + [b_] + [a_]]
    symbols_1 = ['+++', '*++', '+*+', '**+', '*+*', '***',
                 '-++', '/++', '-*+', '/*+', '/+*', '/**',
                 '+-+', '*-+', '+/+', '*/+', '*-*', '*/*',
                 '++-', '*+-', '+*-', '**-', '*+/', '**/',
                 '+--', '*--', '+/-', '*/-', '*-/', '*//',
                 '-+-', '/+-', '-*-', '/*-', '/+/', '/*/'
                 '--+', '/-+', '-/+', '//+', '/-*', '//*',
                 '---', '/--', '-/-', '//-', '/-/', '///']

    symbols_2 = ['*++', '/++', '*-+', '*+-', '*--', '/+-', '/-+', '/--']
    symbols_3 = ['*+*', '/+*', '*-*', '*+/', '*-/', '/+/', '/-*', '/-/']
    symbols_4 = ['+*+', '-*+', '+/+', '+*-', '+/-', '-*-', '-/+', '-/-']
    for nums in perm:
        for syms in symbols_1:
            exp = nums[0] + syms[0] + nums[1] + syms[1] + nums[2] + syms[2] + nums[3]
            try:
                eval(exp)
            except ZeroDivisionError:
                al = 1
            else:
                if eval(exp) == 24:
                    print(exp)
                    return True
    for nums in perm:
        for syms in symbols_2:
            exp = '(' + nums[0] + syms[0] + nums[1] + syms[1] + nums[2] + ')' + syms[2] + nums[3]
            try:
                eval(exp)
            except ZeroDivisionError:
                al = 1
            else:
                if eval(exp) == 24:
                    print(exp)
                    return True
        for syms in symbols_2:
            exp = nums[0] + syms[0] + '(' + nums[1] + syms[1] + nums[2] + syms[2] + nums[3] + ')'
            try:
                eval(exp)
            except ZeroDivisionError:
                al = 1
            else:
                if eval(exp) == 24:
                    print(exp)
                    return True
        for syms in symbols_4:
            exp = '(' + nums[0] + syms[0] + nums[1] + ')' + syms[1] + '(' + nums[2] + syms[2] + nums[3] + ')'
            try:
                eval(exp)
            except ZeroDivisionError:
                al = 1
            else:
                if eval(exp) == 24:
                    print(exp)
                    return True
        for syms in symbols_3:
            exp = nums[0] + syms[0] + '(' + nums[1] + syms[1] + nums[2] + syms[2] + nums[3] + ')'
            try:
                eval(exp)
            except ZeroDivisionError:
                al = 1
            else:
                if eval(exp) == 24:
                    print(exp)
                    return True
        for syms in symbols_3:
            exp = nums[0] + syms[0] + '(' + nums[1] + syms[1] + nums[2] + ')' + syms[2] + nums[3]
            try:
                eval(exp)
            except ZeroDivisionError:
                al = 1
            else:
                if eval(exp) == 24:
                    print(exp)
                    return True
    print("No solution")
    return False


if __name__ == '__main__':

    nums_collection = get_nums_collection(1000)

    test(nums_collection)


    count = 0

    # for nums in nums_collection:
    #     a = nums[0]
    #     b = nums[1]
    #     c = nums[2]
    #     d = nums[3]
    #
    #     if cal(a, b, c, d) is True:
    #         count += 1
    # print("Lv's Game: Number of Solutions : " + str(count))

