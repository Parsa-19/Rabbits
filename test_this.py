import sys
import getopt



def main(argv):
    opts, args = getopt.getopt(argv, 'w:h:i')
    print(args)
    print(opts)
    for op, ar in opts:
        if op == '-w':
            print(ar)
        elif op == '-i':
            print("explenation")
        elif op == '-h':
            print(ar)
        else:
            print(f"there is no option {op}!!!")


main(sys.argv[1:])