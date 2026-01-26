import threading

numbers = [1, 2, 3, 4, 5]
results = {}

def ComputeSum(nums):
    results['sum'] = sum(nums)

def ComputeProduct(nums):
    product = 1
    for num in nums:
        product *= num
    results['product'] = product

t1 = threading.Thread(target=ComputeSum, args=(numbers,))
t2 = threading.Thread(target=ComputeProduct, args=(numbers,))
t1.start()
t2.start()

t1.join()
t2.join()

print("Sum of elements:", results['sum'])
print("Product of elements:", results['product'])
