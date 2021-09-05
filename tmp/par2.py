import argparse
from libs.config import Config, get_config

def get_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="semantic classification",
        usage="python3 train.py",
        description="""
        This module demonstrates classification.
        """,
        add_help=True,
    )
    parser.add_argument("config", type=str, help="path of a config file")
    return parser.parse_args()

a=get_parser()
print(a)
print(a.config)
b=libs.config.get_config(a.config)
print(b.ora)