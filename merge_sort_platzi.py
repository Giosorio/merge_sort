import random 

def merge_sort(list_):
    if len(list_) > 1:
        half = len(list_)//2
        left = list_[:half]
        right = list_[half:]
        
        # Print the process 
        # print(left, '*' * 5, right)

        # Recursive call in each half
        merge_sort(left)
        merge_sort(right)

        # Iterators to go through the left and right lists
        i = 0
        j = 0
        # Iterator for list_
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_[k] = left[i]
                i+=1
            else:
                list_[k] = right[j]
                j+=1
            
            k+=1

        while i < len(left):
            list_[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list_[k] = right[j]
            j+=1
            k+=1
        
        # Print the process 
        # print('left {}, right {}'.format(left, right))
        # print(list_)
        # print('-' * 5)

    return list_ 



if __name__ == '__main__':
    list_size = int(input('List size: '))

    list_ = [random.randint(0, 100) for i in range(list_size)]
    # list_ = [3, 41, 11, 84, 25]
    print(list_)
    print('-' * 5)

    list_ordered = merge_sort(list_)
    print(list_ordered)