"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def main():
    reg_a = 1
    reg_b = 2
    reg_temp = 0
    sum = 0
    while reg_a < 4000000:
        # Register A holds the value of the current number upon first entry
        if (reg_a % 2 == 0):
            sum += reg_a
        reg_temp = reg_a + reg_b
        reg_a = reg_b
        reg_b = reg_temp
    print("Sum of even Fibonacci numbers up to 4,000,000: " + str(sum))


if __name__ == "__main__":
    main()
