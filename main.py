#!/usr/bin/env python3
import os

from buildin import build_in
from process import sub_process
from utils import parse_input, parse_args


def execute(args_list):
    length = len(args_list)
    std_in, std_out = os.dup(0), os.dup(1)
    tmp_in = os.dup(std_in)

    for i in range(length):
        os.dup2(tmp_in, 0)
        os.close(tmp_in)
        if i == length - 1:
            tmp_out = os.dup(std_out)
        else:
            tmp_in, tmp_out = os.pipe()
        os.dup2(tmp_out, 1)
        os.close(tmp_out)

        args = args_list[i]
        if not args[0]:
            return True
        # exec build in command first
        if args[0] in build_in:
            return False if not build_in[args[0]](args) else None
        else:
            sub_process(args)
    os.dup2(std_in, 0)
    os.dup2(std_out, 1)
    os.close(std_in)
    os.close(std_out)
    return True


def loop():
    status = True
    while status:
        prompt = os.getcwd() + ' > '
        line = parse_input(input(prompt).strip())
        args = line.split(' ')  # args value sample: ['ls', '-la']
        args_list = parse_args(args)
        status = execute(args_list)


def main():
    loop()


if __name__ == '__main__':
    main()
