import re
from pprint import pprint


def strip_comments(code):
    # see Bite description
    pattern = re.compile(r'\s*("""(.*?[\n]*)*"""|( {2}| {0})# .*)', flags=re.MULTILINE)
    return re.sub(pattern, '', code)