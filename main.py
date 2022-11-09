def main():
    print("Hello World!")
    if False:
        print("hej")

    (lambda f, n: f(f, n))(lambda f, n: [(not n % 3 and "fizz" or "") + (not n % 5 and "buzz" or "") or n] + f(f, n+1) if n <= 100 else [], 1)

if __name__ == "__main__":
    main()
