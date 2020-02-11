import os

from constants import HISTORY


def xsh_cd(args):
    try:
        os.chdir(args[1])
    except IndexError:
        os.chdir(os.environ['HOME'])
    except FileNotFoundError:
        print('xsh: No such file or directory: \'{}\''.format(args[1]))
    return True


def xsh_pwd(args):
    print(os.getcwd())
    return True


def xsh_exit(args):
    return False


def xsh_history(args):
    history_path = os.path.join(os.environ['HOME'], HISTORY)
    with open(history_path, 'r') as f:
        for line in f:
            print(line.strip())
    return True


build_in = {'cd': xsh_cd, 'exit': xsh_exit, 'pwd': xsh_pwd, 'history': xsh_history}
