def parse_input(line):
    """
    delete duplicate inline characters like: ' ', '\t'
    :param line: str
    :return: str
    """
    res = []
    length = len(line)
    i = 0

    skip = [' ', '\t']
    while i < length:
        if line[i] not in skip:
            res.append(line[i])
            i += 1
        else:
            if line[i] == ' ':
                res.append(' ')
                i += 1
                while i < length and line[i] in skip:
                    i += 1

    return ''.join(res)
