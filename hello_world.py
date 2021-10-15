def mean(x):
    total = 0
    for number in x:
        total += number
    return total/len(x)

def main():
    y = [1,2,3]
    print(mean(y))

main()
