def get_data(char_number):
    with open('file.txt', 'r') as f:
        return f.read(char_number)


def get_avg(int_number):
    data = get_data(int_number)
    numbers = [int(x) for x in data]
    return sum(numbers)/len(numbers)
