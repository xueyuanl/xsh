#!/usr/bin/env python3

import os


def execute(args):
    pid = os.fork()

    if pid == 0:  # child process
        os.execvp(args[0], args)
    else:
        os.waitpid(pid, os.WUNTRACED)
    return True


def loop():
    status = True
    while status:
        line = input('> ')
        args = line.split(' ')
        status = execute(args)


def main():
    loop()
    return True


if __name__ == '__main__':
    main()
