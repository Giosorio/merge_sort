import random 

def merge_sort(list_):
    if len(list_) > 1:
        half = len(list_)//2
        left = list_[:half]
        right = list_[half:]
        
        # Print the process 
        # print(left, '*' * 5, right)

        # Recursive call in each half
        left = merge_sort(left)
        right = merge_sort(right)

        
        list_ = []
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                list_.append(left.pop(0))
            else:
                list_.append(right.pop(0))


        if len(left) > 0:
            list_ += left
        else:
            list_ += right
        
        
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