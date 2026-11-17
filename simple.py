# Calculate total price with tax
def calc(x, y):
    return x + (x * y)

def main():
    a = 100
    b = 0.2
    print("Total:", calc(a, b))

    c = 200
    d = 0.2
    print("Total:", calc(c, d))

def run():
    main()

if __name__ == "__main__":
    run()
