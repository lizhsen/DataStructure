#coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    str_lin = str(sys.stdin.readline().strip())
    alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    Alist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    out_come = ''
    for i in str_lin:
        if i == 'z':
            out_come += 'a'
        elif i == 'Z':
            out_come += 'A'
        elif i in alist:
            for j in range(len(alist)-1):
                if i == alist[j]:
                    out_come += alist[j+1]
                else:
                    pass
        elif i in Alist:
            for j in range(len(alist) - 1):
                if i == Alist[j]:
                    out_come += Alist[j+1]
                else:
                    pass
        else:
            out_come += i
    print out_come
