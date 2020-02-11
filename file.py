import os

from constants import HISTORY


def add_history(line):
    if not line:
        return
    history_path = os.path.join(os.environ['HOME'], HISTORY)
    fd = os.open(history_path, os.O_WRONLY | os.O_APPEND)
    os.write(fd, b'%b\n' % line.encode())
    os.close(fd)
