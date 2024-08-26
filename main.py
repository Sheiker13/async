import multiprocessing


def square_number(number, result_list, index):

    result_list[index] = number * number

def compute_squares(numbers):
    manager = multiprocessing.Manager()
    result_list = manager.list([0] * len(numbers))

    processes = []


    for i, number in enumerate(numbers):
        process = multiprocessing.Process(target=square_number, args=(number, result_list, i))
        processes.append(process)
        process.start()


    for process in processes:
        process.join()

    return list(result_list)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    squares = compute_squares(numbers)
    print(squares)
