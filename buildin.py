import os


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
    print('to do')
    return True


build_in = {'cd': xsh_cd, 'exit': xsh_exit, 'pwd': xsh_pwd, 'history': xsh_history}
