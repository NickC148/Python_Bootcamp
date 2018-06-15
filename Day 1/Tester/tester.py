# To run, in the cmd enter the following
# python <filename>.py
# OR
# Navigate to the directory in the console
# Run python, and Import <filename>
# Then call <filename>.<function>(params)

# Ex:
# import tester
# tester.xxx(12)


def xxx(a):
    print 'I\'m going to lick these', a * \
        5, 'mother fucking snakes AND this mother fucking plane!'


def main():
    return xxx(12)


if __name__ == '__main__':
    main()
