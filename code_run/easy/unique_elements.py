# https://coderun.yandex.ru/problem/exactly-one-occur
import sys
from collections import Counter


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    uniq = Counter(arr)
    print(sum(1 for x in uniq.values() if x == 1))
    # n = int(input())
    # arr = list(map(int, input().split()))
    # uniq = {}
    # for item in arr:
    #     if item not in uniq:
    #         uniq[item] = True
    #     else:
    #         uniq[item] = False
    # print(sum(1 for value in uniq.values() if value is True))


if __name__ == '__main__':
    main()
