import sys

if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
    result = text[::-1].swapcase()
    print(result)
