import logging
logging.basicConfig(
    filename='array_duplicates.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def duplicate(arr):
    try:
        slow = fast = arr[0]
        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        logging.info(f"Duplicate number found: {slow}")
        return slow
    except Exception as e:
        logging.error(f"Error in finding duplicate: {e}")

arr = eval(input("Enter list:"))
print("Duplicate number in array:", duplicate(arr))
