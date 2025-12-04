def parse_input(file: str) -> list[int]:
    return [int(row) for row in open(file)]

def p1(input: list[int]) -> int:
    return sum(input)

def p2(input: list[int]) -> int:
    seen_frequencies: set[int] = set()
    idx, freq = 0, 0
    while freq not in seen_frequencies:
        seen_frequencies.add(freq)
        freq += input[idx%len(input)]
        idx += 1
    return freq

if __name__ == "__main__":
    input = parse_input("solutions/day01/input.txt")
    print(f"[P1] The resulting frequency is: {p1(input)}")
    print(f"[P2] The first duplicate frequency is: {p2(input)}")