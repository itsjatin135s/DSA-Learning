#reverse an array

def rev(arr):
    for i in range(0,int(len(arr)/2)):
        other = len(arr)-i-1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp
    print(arr)

#example

rev([1,2,3,4,5])