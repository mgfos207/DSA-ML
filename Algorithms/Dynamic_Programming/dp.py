def main():
    test = [[1, 2, 3],
    [3, 6, 8],
    [1, 1, 3]]

    n_cols, n_rows = len(test[0]), len(test)
    h_map = dict()
    def rec(r, c):
        if r >= len(test) or c >= len(test[0]):
            return float('inf')

        if (r, c) in h_map:
            return h_map[(r,c)]
        val = test[r][c]

        ans = min(rec(r +1, c) + val, rec(r, c+1) + val)
        h_map[(r, c)] = ans
        print(r, c)
        return ans

    ans = rec(0, 0)
    print(h_map)

if __name__ == "__main__":
    main()