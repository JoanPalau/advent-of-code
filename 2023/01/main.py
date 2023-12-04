class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_lines(self) -> str:
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    yield line.rstrip('\n')
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def get_calibration_number(line: str) -> int:
    tens = units = None
    sub_start = sub_end = 0

    for index, element in enumerate(line):
        if element.isdigit():
            if tens is None:
                tens = units = element
            else:
                units = element
            sub_start = sub_end = index
        else:
            sub_end = index
            # REMEMBER: when getting a sub_str, the intervals are [ )
            number = get_number_from_string(line[sub_start:sub_end + 1])
            if number is not None:
                if tens is None:
                    tens = units = number
                else:
                    units = number
                sub_start = sub_end = index

    return int(tens + units) if tens is not None else 0

def get_number_from_string(string) -> str | None:
    word_map = dict(zero="0", one="1", two="2", three="3", four="4", five="5", six="6", seven="7", eight="8", nine="9")

    for key, _ in word_map.items():
        if is_word_contained(string, key):
            return word_map[key]
    return None

def is_word_contained(string, word) -> bool:
    word_length = len(word)
    for i in range(len(string) - word_length + 1):
        if string[i:i + word_length] == word:
            return True
    return False

def main() -> int:
    file_path = "./2023/01/input.txt"
    result = 0

    file_reader = FileReader(file_path)

    for line in file_reader.read_lines():
        result += get_calibration_number(line)

    print(f"The sum of all calibration numbers is: {result}")
    return 0

if __name__ == '__main__':
    main()
