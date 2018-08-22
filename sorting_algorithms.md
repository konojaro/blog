
# Sorting Algorithms

## 排序算法

![img](https://michaelyou.github.io/img/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95.png)

### 快速排序
平均时间：$O(n \log n)$

辅助空间：$O(n \log n)$

最好情况：$O(n \log n)$

最坏情况：$O(n^2)$ 数组已经有序（正序、逆序）

稳定性：不稳定

### 归并排序
平均时间：$O(n \log n)$

辅助空间：$O(n)$

最好情况：$O(n \log n)$

最坏情况：$O(n \log n)$

稳定性：稳定

### 堆排序
平均时间：$O(n \log n)$

辅助空间：$O(1)$

最好情况：$O(n \log n)$

最坏情况：$O(n \log n)$

稳定性：不稳定

### 冒泡排序
平均时间：$O(n^2)$

辅助空间：$O(1)$

最好情况：$O(n)$ 数组正序

最坏情况：$O(n^2)$ 数组逆序

稳定性：稳定（排序中只交换相邻位置的元素，两个数相等时不交换）

### 选择排序
平均时间：$O(n^2)$

辅助空间：$O(1)$

最好情况：$O(n^2)$

最坏情况：$O(n^2)$ 数组逆序

稳定性：不稳定


### 直接插入排序
平均时间：$O(n^2)$

辅助空间：$O(1)$

最好情况：$O(n)$ 数组正序

最坏情况：$O(n^2)$ 数组逆序

稳定性：稳定

### Shell排序
平均时间：$O(n \log n)$

辅助空间：$O(1)$

最好情况：$O(n \log n)$

最坏情况：$O(n \log n)$

稳定性：不稳定

## 快速排序


```python
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        
        # Separately sort elements before
        # partition and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print (arr)
quicksort(arr, 0, len(arr) - 1)
print (arr)
```

    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

## 归并排序


```python
def merge(arr, low, mid, high):
    temp = [0] * (high - low + 1)
    i, j, k = low, mid + 1, 0
    # 较小值放入temp
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    # 处理较长部分   
    while i <= mid:
        temp[k] = arr[i]
        k += 1; i += 1
        
    while j <= high:
        temp[k] = arr[j]
        k += 1; j += 1
    # 替换原数组
    for k in range(len(temp)):
        arr[low + k] = temp[k]

def mergesort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)
        
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print (arr)
mergesort(arr, 0, len(arr) - 1)
print (arr)
```

    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

## 堆排序


```python
# To heapify subtree rooted at index i
# n is size of heap
def heapify(arr, n, i):
    largest = i     # Initialize largest as root
    l = 2 * i + 1    # left = 2*i+1
    r = 2 * i + 2    # right = 2*i+2
    
    # See if left child of root exists and
    # is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
    
    # See if right child of root exists and
    # is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Heapify the root
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    
    # Build a maxheap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    
    # One by one extract elements
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
arr = [1,4,2,3,6,5,1]
print (arr)
heapSort(arr)
print (arr)
```

    [1, 4, 2, 3, 6, 5, 1]
    [1, 1, 2, 3, 4, 5, 6]
    

## 冒泡排序


```python
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n - 1):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

                
arr = [1,4,2,3,6,5,1]
print (arr)
bubbleSort(arr)
print (arr)
```

    [1, 4, 2, 3, 6, 5, 1]
    [1, 1, 2, 3, 4, 5, 6]
    

**Optimized Implementation:**

The above function always runs O(n^2) time even if the array is sorted. It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.


```python
# An optimized version of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already
        #  in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to
            # n-i-1. Swap if the element 
            # found is greater than the
            # next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
         
        print (arr)
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
            
arr = [1,4,2,3,6,5,1]
print (arr)
bubbleSort(arr)
print (arr)
```

    [1, 4, 2, 3, 6, 5, 1]
    [1, 2, 3, 4, 5, 1, 6]
    [1, 2, 3, 4, 1, 5, 6]
    [1, 2, 3, 1, 4, 5, 6]
    [1, 2, 1, 3, 4, 5, 6]
    [1, 1, 2, 3, 4, 5, 6]
    [1, 1, 2, 3, 4, 5, 6]
    [1, 1, 2, 3, 4, 5, 6]
    

## 选择排序


```python
def selectionSort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        
        # Find the minimum element in remaining unsorted array
        min_idx = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
arr = [1,4,2,3,6,5,1]
print (arr)
selectionSort(arr)
print (arr)     
```

    [1, 4, 2, 3, 6, 5, 1]
    [1, 1, 2, 3, 4, 5, 6]
    

## 直接插入排序
![image.png](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/insertionsort.png)
```
insertionSort(arr, n)
Loop from i = 1 to n-1.
……a) Pick element arr[i] and insert it into sorted sequence arr[0…i-1]
```


```python
def insertionSort(arr):
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [1,4,2,3,6,5,1]
print (arr)
insertionSort(arr)
print (arr)      
```

    [1, 4, 2, 3, 6, 5, 1]
    [1, 4, 2, 3, 6, 5, 1]
    [1, 2, 4, 3, 6, 5, 1]
    [1, 2, 3, 4, 6, 5, 1]
    [1, 2, 3, 4, 6, 5, 1]
    [1, 2, 3, 4, 5, 6, 1]
    [1, 1, 2, 3, 4, 5, 6]
    [1, 1, 2, 3, 4, 5, 6]
    

## 希尔排序
改良的直接插入排序


```python
def shellSort(arr):
    
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] =  temp

        gap //= 2
    
arr = [1,4,2,3,6,5,1]
print (arr)
shellSort(arr)
print (arr)  
```

    [1, 4, 2, 3, 6, 5, 1]
    [1, 1, 2, 3, 4, 5, 6]
    
