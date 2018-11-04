#!/usr/bin/env python3.6

import pytest
from hr import cli

@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_fails_without_arguments(parser):
    """
    Without a specified path the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_parser_export_flag(parser):
    """
    The flag is set to false by default if flag is present set it to true
    """
    args = parser.parse_args(['/some/path'])
    assert args.export == False

    args = parser.parse_args(['--export','/some/path'])
    assert args.export == True


def test_parser_succeeds_with_a_path(parser):
    """
    The parser will not exit if it receives a flag and path
    """
    args = parser.parse_args(['/some/path'])

    assert args.path == '/some/path'
