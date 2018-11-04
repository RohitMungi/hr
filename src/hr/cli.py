from argparse import Action,ArgumentParser


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('path', help = "Path to inventory.json file")
    parser.add_argument('--export', '-e',
            help="Export users to a json file",
            action='store_true'
            )
    return parser

