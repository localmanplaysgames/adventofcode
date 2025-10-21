from pathlib import Path

def load_data(source_data):
    return [list(map(int, line.split())) for line in Path(source_data).read_text().splitlines() if line.strip()]

def count_safe(source_data):
    data = load_data(source_data)
    return data

def main():
    print(count_safe('data/2024_2.txt'))

if __name__ == "__main__":
    main()