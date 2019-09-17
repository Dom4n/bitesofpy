from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    Blog = namedtuple('Blog', list(dict_.keys()))
    nt = Blog(**dict_)
    return nt


def nt2json(nt: namedtuple):
    return json.dumps(nt._asdict(), default=str)
