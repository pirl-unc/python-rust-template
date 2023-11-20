import argparse
import testpkg
from .cli_add import *


def init_arg_parser():
    """
    Initialize the input argument parser.

    Returns
    -------
    argparse.ArgumentParser object
    argparse.ArgumentParser subparsers object
    """
    arg_parser = argparse.ArgumentParser(
        description="testpkg: Test package for integrating rust and python."
    )
    arg_parser.add_argument(
        '--version', '-v',
        action='version',
        version='%(prog)s version ' + str(testpkg.__version__)
    )
    sub_parsers = arg_parser.add_subparsers(help='Test package sub-commands.')
    return arg_parser, sub_parsers


def run():
    # Step 1. Initialize argument parser
    arg_parser, sub_parsers = init_arg_parser()
    sub_parsers = add_cli_add_arg_parser(sub_parsers=sub_parsers)           # add
    args = arg_parser.parse_args()

    # Step 2. Execute function based on CLI arguments
    if args.which == 'add':
        run_cli_add_from_parsed_args(args=args)
    else:
        raise Exception("Invalid command: %s" % args.which)
