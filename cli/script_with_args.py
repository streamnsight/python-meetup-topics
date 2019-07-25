#!./.venv/bin/python

import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This is my test script with arguments')

    # positional argument
    # '?' means 0 or 1
    # '+' means 1 or more
    # '*' means 0 or more
    # default is output if no argument is passed
    parser.add_argument('bar', nargs='*', default='one', help='bar help')

    # const is output if no argument is passed but the flag is defined
    parser.add_argument('-f', '--foo', nargs='?', const='nothing', default='foo', help='foo help')

    parser.add_argument('-m', '--move', choices=['rock', 'paper', 'scissors'])

    args = parser.parse_args()

    print(args)