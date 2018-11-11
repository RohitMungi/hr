from argparse import Action,ArgumentParser


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('path', help = "Path to inventory.json file")
    parser.add_argument('--export', '-e',
            help="Export users to a json file",
            action='store_true'
            )
    return parser

def main():
    from hr import inventory,users

    args= create_parser().parse_args()

    if args.export:
        inventory.dump(args.path)
    else:
        users_info = inventory.load(args.path)
        user.sync(users_info)
