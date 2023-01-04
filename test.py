# Tests file for doctest
if __name__ == "__main__":
    import doctest, os
    doctest.testfile("./tests/test_interface.txt")
    os.system('python3 -m test.py -v')
