from quark_runtime import *

import pkg



def main():
    c = pkg.C();
    (c).event1();
    (c).event2();
    (c).run();


if __name__ == "__main__":
    main()