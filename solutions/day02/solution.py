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

def p2(input: list[str]) -> str:
    for id1 in input:
        for id2 in input:
            if id1 != id2:
                common_part = common_chars(id1, id2)
                if len(common_part) == len(id1)-1:
                    return common_part
    return ""

def common_chars(s1: str, s2: str) -> str:
    return "".join(ch for i, ch in enumerate(s1) if ch == s2[i])

if __name__ == "__main__":
    input = parse_input("solutions/day02/input.txt")
    print(f"[P1] The checksum is: {p1(input)}")
    print(f"[P2] The common letters are: {p2(input)}")