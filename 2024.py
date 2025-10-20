import pandas as pd

def load_data(source_data):
    df = pd.read_csv(source_data, sep=r'\s+', header=None, names=['a','b'], dtype=int)
    first_list, second_list = sorted(df['a'].tolist()), sorted(df['b'].tolist())
    return first_list, second_list

def day1_p1(source_data):
    data = load_data(source_data)
    total_diff = 0
    for i in range(len(data[0])):
        total_diff += abs(data[0][i] - data[1][i])
    return total_diff

def day1_p2(source_data):
    data = load_data(source_data)
    similarity_score = 0
    for i in range(len(data[0])):
        matches = len([j for j in data[1] if j == data[0][i]])
        if matches > 0:
            similarity_score += data[0][i] * matches
    return similarity_score

def main():
    
    print(f'Day 1 part 1 answer: {day1_p1("data/2024_1.txt")}')
    print(f'Day 1 part 2 answer: {day1_p2("data/2024_1.txt")}')

if __name__ == "__main__":
    main()