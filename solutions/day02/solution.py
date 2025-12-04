def parse_input(file: str) -> list[str]:
    return [row.rstrip() for row in open(file)]

def p1(input: list[str]) -> int:
    double_count, triple_count = 0, 0
    for s in input:
        freqs: dict[str, int] = {}
        for ch in set(s):
            freqs[ch] = s.count(ch)
        double, triple = False, False
        for cnt in freqs.values():
            double = True if cnt == 2 else double
            triple = True if cnt == 3 else triple
        double_count = double_count+1 if double else double_count
        triple_count = triple_count+1 if triple else triple_count
    return double_count*triple_count

if __name__ == "__main__":
    input = parse_input("solutions/day02/input.txt")
    print(f"[P1] The checksum is: {p1(input)}")