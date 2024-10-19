# https://coderun.yandex.ru/problem/exactly-one-occur
import sys
from collections import Counter


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    uniq = Counter(arr)
    print(sum(1 for x in uniq.values() if x == 1))


if __name__ == '__main__':
    main()
