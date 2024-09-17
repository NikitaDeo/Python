def sort_athletes(n, m, data, k):
    data_list = [line.split() for line in data]
    data_list.sort(key=lambda x: int(x[k]))
    for row in data_list:
        print(' '.join(row))
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    n, m = map(int, data[0].split())
    athlete_data = data[1:n+1]
    k = int(data[n+1])
    sort_athletes(n, m, athlete_data, k)