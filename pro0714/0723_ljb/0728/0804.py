#author_='xqh';
#date: 2021/8/4 11:22


if __name__ == '__main__':


    # str=input()
    #
    # arr=str.split(" ")
    # print(arr)
    # for i in range(len(arr)):
    #     arr[i]=int(arr[i])
    #
    # print(arr)

    arr=[1,2,2,3,3,3,4]

    # b=None
    # for a in arr:
    #     if a is not b:
    #         arr
    #     elif a is b:
    #         arr.remove(b)
    # print(arr)
    for i in range(1,len(arr)-1):
        if arr[i]==arr[i-1]:
            arr[i-1]=None
    print(arr)

    while True:
        if None not in arr:
            break
        arr.remove(None)

    print(arr)



