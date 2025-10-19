import pandas as pd

def main():
    
    source_data = "data/2024_day1.txt"
    df = pd.read_csv(source_data, sep='\s+', header=None, names=['a','b'], dtype=int)
    first_list, second_list = sorted(df['a'].tolist()), sorted(df['b'].tolist())

    total_diff = 0
    print(f'List lengths = a: {len(first_list)}, b: {len(second_list)}')
    for i in range(len(first_list)):
        total_diff += abs(first_list[i] - second_list[i])
    
    print(total_diff)

if __name__ == "__main__":
    main()