from quark_runtime import *

import test



def main():
    (test).go();
    ((test).test).go();
    t1 = test.Test();
    t2 = test.test.Test();
    (t1).go();
    (t2).go();


if __name__ == "__main__":
    main()
