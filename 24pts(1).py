import random
from Twenty_Four import Game


def tran(s):
    if s == '+':
        a = 1

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
    symbols_1 = ['+++', '*++', '+*+', '**+', '*+*', '***', '++*', '+**',
                 '-++', '/++', '-*+', '/*+', '/+*', '/**', '-+*', '-**',
                 '+-+', '*-+', '+/+', '*/+', '*-*', '*/*', '+-*', '+/*',
                 '++-', '*+-', '+*-', '**-', '*+/', '**/', '++/', '+*/',
                 '*--', '*/-', '*-/',
                 '-*-', '/*-', '-*/',
                 '/-*', '--*', '-/*',
                 '//-', '/-/'
                 ]
    for nums in perm:
        for syms in symbols_1:
            exp = nums[0] + syms[0] + nums[1] + syms[1] + nums[2] + syms[2] + nums[3]
            if eval(exp) == 24:
                    print(exp)
                    return True
        for syms in symbols_1:
            exp = nums[0] + syms[0] + '(' + nums[1] + syms[1] + nums[2] + syms[2] + nums[3] + ')'
            if eval(nums[1] + syms[1] + nums[2] + syms[2] + nums[3]) != 0:
                if eval(exp) == 24:
                        print(exp)
                        return True
        for syms in symbols_1:
            exp = '(' + nums[0] + syms[0] + nums[1] + ')' + syms[1] + '(' + nums[2] + syms[2] + nums[3] + ')'
            if eval(nums[2] + syms[2] + nums[3]) != 0 or syms[1] != '/':
                if eval(exp) == 24:
                    print(exp)
                    return True
        for syms in symbols_1:
            exp = nums[0] + syms[0] + '(' + nums[1] + syms[1] + nums[2] + ')' + syms[2] + nums[3]
            if eval(nums[1] + syms[1] + nums[2]) != 0:
                if eval(exp) == 24:
                        print(exp)
                        return True
        for syms in symbols_1:
            exp = '(' + nums[0] + syms[0] + nums[1] + ')' + syms[1] + nums[2] + syms[2] + nums[3]
            if eval(exp) == 24:
                    print(exp)
                    return True
    print("No solution")


    return 0


if __name__ == '__main__':

    # nums_collection = get_nums_collection(1000)
    #
    # test(nums_collection)
    #
    # count = 0
    #
    # for i in nums_collection:
    #     a = i[0]
    #     b = i[1]
    #     c = i[2]
    #     d = i[3]
    #
    #     if cal(a, b, c, d) != 0:
    #         count += 1
    #
    #
    # print("lv's Game has"+str(count)+"solutions")

    if __name__ == "__main__":
        count = 1
        for a in range(1, 11):
            for b in range(1, 11):
                for c in range(1, 11):
                    for d in range(1, 11):
                        print("Given numbers : " + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d))
                        if cal(a, b, c, d) is True:

                            count += 1
        print("Number of Solutions : " + str(count))

# if __name__ == '__main__':
#     i = 0
#     count = 0
#     li = [0,0,0,0,0]
#     dic = {'+++':0, '*++':0, '+*+':0, '**+':0, '*+*':0, '***':0, '++*':0, '+**':0,
#            '-++':0, '/++':0, '-*+':0, '/*+':0, '/+*':0, '/**':0, '-+*':0, '-**':0,
#            '+-+':0, '*-+':0, '+/+':0, '*/+':0, '*-*':0, '*/*':0, '+-*':0, '+/*':0,
#                  '++-':0, '*+-':0, '+*-':0, '**-':0, '*+/':0, '**/':0, '++/':0, '+*/':0,
#                  '+--':0, '*--':0, '+/-':0, '*/-':0, '*-/':0, '*//':0, '+-/':0, '+//':0,
#                  '-+-':0, '/+-':0, '-*-':0, '/*-':0, '/+/':0, '/*/':0, '-+/':0, '-*/':0,
#                  '--+':0, '/-+':0, '-/+':0, '//+':0, '/-*':0, '//*':0, '--*':0, '-/*':0,
#                  '---':0, '/--':0, '-/-':0, '//-':0, '/-/':0, '///':0, '--/':0, '-//':0
#            }
#     while i < 1000:
#         a = random.randint(1, 10)
#         b = random.randint(1, 10)
#         c = random.randint(1, 10)
#         d = random.randint(1, 10)
#         print("Given numbers : " + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d))
#         m = cal(a, b, c, d)
#         if m != 0:
#             li[m-1] += 1
#             count += 1
#         i += 1
#     print("Number of Solutions : " + str(count))
#     print(li)

    # for a in range(1, 11):
    #     for b in range(1, 11):
    #         for c in range(1, 11):
    #             for d in range(1, 11):
    #                 print("Given numbers : " + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d))
    #                 m = cal(a, b, c, d)
    #                 if m in dic:
    #                     count += 1
    #                     dic[m] += 1
    # print("Number of Solutions : " + str(count))
    # print(dic)
