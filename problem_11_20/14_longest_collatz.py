"""
Longest Collatz Sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:
    n->n/2 (n is even)
    n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Althought it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Note: Once the chain starts, the terms are allowed to go above one million.
"""


def collat_next(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (3 * num) + 1


def main():
    counts = {}
    counts[1] = 1
    for x in range(2, 1000000):
        count = 0
        number = x
        while number not in counts and number != 1:
            count += 1
            number = collat_next(number)
            if number in counts:
                count += counts[number]
        counts[x] = count
    print(max(counts, key=counts.get))


if __name__ == "__main__":
    main()
