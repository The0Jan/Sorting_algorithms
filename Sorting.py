
def sort_bubble(list_of_objects):
    for times_now in range(len(list_of_objects)-1,0,-1):
        for word in range(times_now):
            if list_of_objects[word] > list_of_objects[word+1]:
                temporary = list_of_objects[word+1]
                list_of_objects[word+1] = list_of_objects[word]
                list_of_objects[word] = temporary
    
def sort_select(list_of_objects):
    for words in range(0, len(list_of_objects)):
        temp_smallest = list_of_objects[words]
        index_of_smallest = words
        for current_word in range(words, len(list_of_objects)):
            if temp_smallest > list_of_objects[current_word]:
                temp_smallest  = list_of_objects[current_word]
                index_of_smallest = current_word
            if current_word == len(list_of_objects)-1:
                list_of_objects[index_of_smallest] = list_of_objects[words]
                list_of_objects[words] = temp_smallest

def divide_and_conquer(array, beginning, end):
    if end - beginning > 0:
        pivot = array[end]
        small_index = beginning
        for numbers in range(beginning, end):
            if array[numbers] <= pivot:
                # switching elements
                temp = array[numbers]
                array[numbers] = array[small_index]
                array[small_index] = temp
                small_index = small_index + 1

        #switching  the pivot with the first element bigger than it
        temp = array[small_index]
        array[small_index] = array[end]
        array[end] = temp

        #now the left and right side of the pivot
        divide_and_conquer(array, beginning, small_index-1)
        divide_and_conquer(array, small_index+1, end)

def sort_quick(array):
    last_index = len(array) -1
    divide_and_conquer(array, 0, last_index)










