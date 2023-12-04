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

class Game:
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    def __init__(self, text):
        #Game 80: 3 green, 13 red, 8 blue; 17 red, 9 blue; 7 blue, 1 green, 2 red; 8 red, 6 blue, 3 green; 1 red, 2 blue; 2 green, 4 blue, 10 red
        self.record = text
        self.id = self._parse_id(text)
        self.pos_cubes = self._parse_cubes(text)

    def _parse_id(self, text: str) -> int:
        """Extracts the game ID from a string"""
        game_id = int(text.split(":")[0].split(" ")[1])
        return game_id

    def _parse_cubes(self, text: str) -> dict:
        """Extracts the game cubes from a string and keeps the max of the given values"""
        max_game_cubes = dict(red = 0, green = 0, blue = 0)

        draws = text.split(":")[1].split(";")
        for draw in draws:
            cubes = draw.split(",")
            for cube in cubes:
                num, color = cube.strip().split(" ")
                if max_game_cubes[color] < int(num):
                    max_game_cubes[color] = int(num)

        return max_game_cubes

    def is_possible(self) -> bool:
        """Returns True if the game complies with the max cubes allowed"""
        return self.MAX_BLUE >= self.pos_cubes["blue"] and self.MAX_GREEN >= self.pos_cubes["green"] and self.MAX_RED >= self.pos_cubes["red"]
    
    def get_cube_pow(self) -> int:
        return self.pos_cubes["blue"] * self.pos_cubes["green"] * self.pos_cubes["red"]

def main() -> int:
    file_path = "./2023/02/games.txt"

    id_sum = 0
    pow_sum = 0

    file_reader = FileReader(file_path)

    for line in file_reader.read_lines():
        game = Game(line)
        pow_sum += game.get_cube_pow()
        if game.is_possible():
            id_sum += game.id

    print(f"The sum of all possible games ID's is: {id_sum}")
    print(f"The sum of all possible games POW is: {pow_sum}")
    return 0

if __name__ == '__main__':
    main()
