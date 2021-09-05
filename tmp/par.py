import argparse

"""
default - コマンドラインに対応する引数が存在せず、さらに namespace オブジェクトにも存在しない場合に利用される値。
const - 一部の action と nargs の組み合わせで利用される定数。
"""

def func(x):
    return list(map(lambda y: y**2,x))

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=func,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))