#!/usr/bin/env python3
import os

from buildin import build_in
from utils import parse_input


def launch(args):
    pid = os.fork()
    if pid == 0:  # child process
        try:
            os.execvp(args[0], args)
        except FileNotFoundError:
            print('xsh: {}: Command not found'.format(args[0]))
    else:  # parent process
        os.waitpid(pid, os.WUNTRACED)
    return True


def execute(args):
    if not args[0]:
        return True
    # exec build in command first
    if args[0] in build_in:
        return build_in[args[0]](args)
    else:
        return launch(args)


def loop():
    status = True
    while status:
        line = parse_input(input('> ').strip())
        args = line.split(' ')  # args value sample: ['ls', '-la']
        status = execute(args)


def main():
    loop()


if __name__ == '__main__':
    main()
