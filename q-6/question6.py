def duplicate(arr):
    slow = fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
        slow = arr[0]
        while slow!= fast:
            slow = arr[slow]
            fast = arr[fast]
        return slow
arr = eval(input("Enter list:"))
print("Duplicate number in array:", duplicate(arr))