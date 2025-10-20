import pandas as pd

def day1(source_data):
    df = pd.read_csv(source_data, sep=r'\s+', header=None, names=['a','b'], dtype=int)
    first_list, second_list = sorted(df['a'].tolist()), sorted(df['b'].tolist())
    total_diff = 0
    for i in range(len(first_list)):
        total_diff += abs(first_list[i] - second_list[i])
    return total_diff

def main():
    
    print(f'Day 1 answer: {day1("data/2024_1.txt")}')

if __name__ == "__main__":
    main()