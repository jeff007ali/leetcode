def countElements(arr):
    ans = 0
    for i in arr:
        n = i + 1
        if n in arr:
            ans += 1

    return ans


print(countElements1([1,2,3]))
print(countElements([1,1,3,3,5,5,7,7]))
print(countElements([1,3,2,3,5,0]))
print(countElements([1,1,2,2]))