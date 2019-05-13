#!/usr/bin/env python3
"""

"""
__author__ = "Aaron Steele"
__credits__ = ["Frederick Jansson"]
__version__ = "1.0"

import argparse
from build_model_tosca import *
from sol6_writer.Sol6Writer import Sol6Writer
import logging
logger = logging.getLogger(__name__)


class SolCon:
    def __init__(self):

        print("Starting SolCon (v{})...".format(__version__))

        self.desc = "NFVO SOL6 Converter (SolCon): Convert a SOL001 (TOSCA) YAML to SOL006 JSON"

        parser = argparse.ArgumentParser(description=self.desc)
        parser.add_argument('-f', '--file',
                            help="The TOSCA VNF YAML file to be processed")
        parser.add_argument('-o', '--output',
                            help="The output file for the converted VNF, outputs to stdout if not specified")
        parser.add_argument('-l', '--log-level',
                            choices=['DEBUG', 'INFO', 'WARNING'], default=logging.INFO,
                            help="Set the log level for standalone logging")
        parser.add_argument('-c', '--config',
                            help='Location to file with definitions for TOSCA types (YAML format)')
        args = parser.parse_args()
        # We can't use the logger before we set it up, so do that first
        setup_logger(args.log_level)

        file = args.file
        output = args.output
        config = args.config

        model_builder_tosca = BuildModelTosca(file, output, config)
        model_builder_tosca.build()

        model = model_builder_tosca.tosca_model
        writer = Sol6Writer(model)
        # TODO: Make this use absolute paths
        writer.write(output)


def setup_logger(log_level=logging.INFO):
    log_format = "%(levelname)s - %(message)s"
    log_filename = "solcon.log"

    logging.basicConfig(level=log_level, filename=log_filename, format=log_format)
    # Duplicate the output to the console as well as to a file
    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(console)


if __name__ == '__main__':
    SolCon()
