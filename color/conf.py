from color.color_const import *


class Color(object):
    def __init__(self):
        pass

    @staticmethod
    def color(s, color_scheme):
        """
        for reference: https://misc.flogisoft.com/bash/tip_colors_and_formatting
        :param s: str to color
        :param color_scheme: refer it in `color_const.py`
        :return: colored str
        """
        pre = '\033['
        post = '\033[0m'
        return '{}{};{};{}m{}{}'.format(pre, color_scheme[0], color_scheme[1], color_scheme[2], s, post)

    def prompt(self, s):
        return self.color(s, (format_dic['default'], foreground_dic['blue'], background_dic['default']))


color = Color()
