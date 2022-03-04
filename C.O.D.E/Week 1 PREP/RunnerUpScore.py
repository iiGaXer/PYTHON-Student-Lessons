if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    arr.sort()
    max_num = arr[-1]
    arr.remove(max_num)

    i = 0
    while i != len(arr):
        if max_num == arr[-1]:
            arr.remove(arr[-1])

        else:
            print(arr[-1])
            break

