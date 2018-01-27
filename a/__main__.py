import sys
from a.Helper import Helper
from a.A import A


def main():
    a = A()

    if len(sys.argv[1::]) > 0:
        a.run(sys.argv[1], sys.argv[2::])
    else:
        Helper(a.get_settings())


if __name__ == '__main__':
    main()