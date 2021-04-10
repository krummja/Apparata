from __future__ import annotations

from .parser import Parser
from .lexer import Lexer


class Generator:
    """Transformation engine for Graph objects."""

    def generate_from_file(self, file_name: str, report: bool = False) -> Parser:
        grammar_file = open(file_name, 'r')
        parser = self.parse_grammar_file(grammar_file.read())
        grammar_file.close()

        if report:
            self.generate_report(parser)

        return parser

    def parse_grammar_file(self, grammar_file) -> Parser:
        parser = Parser(Lexer(grammar_file))
        parser.parse()
        return parser

    def generate_report(self, file):

        print("======================================================")
        print("GRAPH DATA")
        print("")

        for node, prop_dict in file.nodes.items():
            print("")
            print(f"{node}".upper())
            print("============================")
            for prop, value in prop_dict.items():
                print(f"{prop} : {value}")

        for (n, m), prop_dict in file.edges.items():
            print("")
            print(f"{n}".upper() + "  ->  " + f"{m}".upper())
            print("============================")
            for prop, value in prop_dict.items():
                print(f"{prop} : {value}")

        print("")
        print(f"Nodes: {file.node_count}")
        print(f"Edges: {file.edge_count}")
        print("")
        print("======================================================")
