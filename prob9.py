# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def is_pythagorean_triplet(x, y, z):
    return x < y < z and (x ** 2 + y ** 2) == z ** 2


def fulfills_sum(x, y, z):
    return x + y + z == 1000


def is_answer(x, y, z):
    return is_pythagorean_triplet(x, y, z) and fulfills_sum(x, y, z)


def main():
    for x in range(1, 1001):
        for y in range(x, 1001):
            for z in range(y, 1001):
                if (is_answer(x, y, z)):
                    print("Found answer: %d\ntriplet: %d %d %d" % (x * y * z, x, y, z))
                    return

if __name__ == '__main__':
    main()
