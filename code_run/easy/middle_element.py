# https://coderun.yandex.ru/problem/median-out-of-three
import sys


def main():
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[1])


if __name__ == '__main__':
    main()
