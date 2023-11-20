import argparse
from ..logging import get_logger
from ..main import add_numbers


logger = get_logger(__name__)


def add_cli_add_arg_parser(sub_parsers) -> argparse._SubParsersAction:
    """
    Adds 'add' parser.

    Parameters
    ----------
    sub_parsers  :   An instance of argparse.ArgumentParser subparsers.

    Returns
    -------
    An instance of argparse.ArgumentParser subparsers.
    """
    parser = sub_parsers.add_parser('add', help='Adds two numbers.')
    parser._action_groups.pop()

    # Required arguments
    parser_required = parser.add_argument_group('required arguments')
    parser_required.add_argument(
        "--value_1",
        dest="value_1",
        type=int,
        required=True,
        help="Value 1."
    )
    parser_required.add_argument(
        "--value_2",
        dest="value_2",
        type=int,
        required=True,
        help="Value 2."
    )

    parser.set_defaults(which='add')
    return sub_parsers


def run_cli_add_from_parsed_args(args) -> None:
    """
    Run testpkg 'add' command using parameters from parsed arguments.

    Parameters
    ----------
    args    :   An instance of argparse.ArgumentParser with the following variables:
                value_1
                value_2
    """
    add_numbers(value_1=args.value_1, value_2=args.value_2)
