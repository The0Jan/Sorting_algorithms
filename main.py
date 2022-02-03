from Sorting import sort_bubble, sort_quick, sort_select
import matplotlib.pyplot as plt
import timeit

#function for creating the list of words
def get_words(amount):
    count = amount
    dictionary = []
    with open("pan_tadeusz.txt", encoding="utf8") as file:
        for line in file:
            for words in line.split():
                if count == 0:
                    break
                dictionary.append(words)
                count = count -1
    return dictionary

#function for drawing a graph
def draw_graph(times, amount, title):
    y = times
    x = amount
    plt.plot(x, y)
    plt.ylabel("Time")
    plt.xlabel("Amount of words")
    plt.title(title)
    plt.show
    plt.savefig(title + ".png")
    plt.close()

#function for creating a .txt file with the measurments
def create_file(times, amounts,sort_type, file_name = "results"):
    full_name = file_name + ".txt"
    indexes = len(times)
    with open(full_name, 'a+') as file:
        file.write(sort_type + '\n')
        for  index in range(0,indexes):
            current_amount = amounts[index] 
            current_time  = times[index]
            line = "Words given:" + str(current_amount) + '\t' + "Time:" + str(current_time) + '\n'
            file.write(line)

def create_results(algorithm, name_of_sort = ' ',max = 10000, increment = 500, ):
    amount= 0
    times =[]
    words = []
    print(name_of_sort)
    while amount < max:
        amount = amount + increment
        collection = get_words(amount)
        time = timeit.timeit(lambda:algorithm(collection), number = 1 )
        rounded = round(time, 4)
        times.append(rounded)
        words.append(amount)
        print('Number of words:',amount, ' Rounded_time:', rounded)
    print("\n ------------- \n")
    #These functions are used for creating the graph and adding the data to the .txt file
    #draw_graph(times, words, name_of_sort)
    #create_file(times, words, name_of_sort)

create_results(sort_quick, "Quick Sort")
create_results(sort_bubble, "Bubble Sort")
create_results(sort_select, "Selection Sort")

