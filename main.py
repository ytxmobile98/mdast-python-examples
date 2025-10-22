import mdast
from pathlib import Path
from pprint import pprint

CURDIR = Path(__file__).parent

EXAMPLE_FILE = CURDIR / "docs" / "example.md"


def main():
    with open(EXAMPLE_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    parse_options = mdast.ParseOptions.gfm()
    output = mdast.md_to_ast(text, parse_options)
    pprint(output, sort_dicts=False)


if __name__ == "__main__":
    main()
