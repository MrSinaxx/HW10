from typing import List
from contextlib import contextmanager

def process_data(input_str: str) -> str:
    return input_str.upper()

@contextmanager
def file_opener(file_path: str, mode: str):
    file = open(file_path, mode)
    try:
        yield file
    finally:
        file.close()

def main(input_file_path: str, output_file_path: str):
    with file_opener(input_file_path, 'r') as input_file:
        input_data = input_file.readlines()
    
    output_data = [process_data(line.strip()) for line in input_data]
    
    with file_opener(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(output_data))

if __name__ == "__main__":
    input_file_path = "input.txt"
    output_file_path = "output.txt"
    main(input_file_path, output_file_path)
