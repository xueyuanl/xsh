import os
import subprocess

from buildin import build_in


def sub_exec(args):
    try:
        os.execvp(args[0], args)
    except FileNotFoundError:
        print('xsh: {}: Command not found'.format(args[0]))
        exit()  # still in child process, needs an extra exit()


def pipeline_subprocess(args_list):
    """
    this is a version which implement shell pipeline function using subprocess package
    :param args_list: [['ls', '-ls'], ['grep', '11']]
    :return: bool
    """
    length = len(args_list)
    s_in = os.dup(0)
    s_out = os.dup(1)
    fdin = os.dup(s_in)
    for i in range(length):
        os.dup2(fdin, 0)
        os.close(fdin)
        if i == length - 1:
            fdout = os.dup(s_out)
        else:
            fdin, fdout = os.pipe()
        os.dup2(fdout, 1)
        os.close(fdout)

        args = args_list[i]
        if not args[0]:
            return True
        # exec build in command first
        if args[0] in build_in:
            build_in[args[0]](args)
        else:
            subprocess.run(args)
            # return launch(args)
    os.dup2(s_in, 0)
    os.dup2(s_out, 1)
    os.close(s_in)
    os.close(s_out)
    return True