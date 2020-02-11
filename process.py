import os
import subprocess
import sys

from buildin import build_in


def sub_exec(args):
    try:
        os.execvp(args[0], args)
    except FileNotFoundError:
        print('xsh: {}: Command not found'.format(args[0]))
        exit()  # still in child process, needs an extra exit()


def sub_process(args):
    try:
        subprocess.run(args)
    except FileNotFoundError:
        print('xsh: {}: Command not found'.format(args[0]))


def execute_bak(args_list):
    length = len(args_list)
    if length == 1:  # no pipeline case
        args = args_list[0]
        if not args[0]:
            return True
        # exec build in command first
        if args[0] in build_in:
            return build_in[args[0]](args)
        else:
            pid = os.fork()
            sub_exec(args) if pid == 0 else os.waitpid(pid, os.WUNTRACED)
            return True
    else:
        new_in, new_out = 0, 0
        old_in, old_out = 0, 0
        for i in range(length):
            if i < length - 1:  # if not the last command, create pipe
                new_in, new_out = os.pipe()

            pid = os.fork()
            if pid == 0:
                if i < length - 1:
                    os.dup2(new_out, sys.stdout.fileno())  # point current out to new pipe out
                    os.close(new_out)
                    os.close(new_in)  # do not need it, close
                if i > 0:
                    os.dup2(old_in, sys.stdin.fileno())  # point current in to new pipe in, to get prev command out
                    os.close(old_in)
                    os.close(old_out)  # do not need it, close
                args = args_list[i]
                sub_exec(args)
            else:  # in father process
                if i > 0:
                    os.close(old_out)
                    os.close(old_in)
                if i < length - 1:  # if not the last command, copy the pipeline, prepare for next child process
                    old_in, old_out = new_in, new_out

                os.waitpid(pid, os.WUNTRACED)
    return True
