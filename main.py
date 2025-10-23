import mdast
from pathlib import Path

CURDIR = Path(__file__).parent

EXAMPLE_FILE = CURDIR / "docs" / "example.md"


def process_nodes(ast: dict) -> list[str]:

    types: set[str] = set()

    def _process_nodes_and_add_types(obj: dict, level: int = 0):
        print(
            f"processing item, level: {level}, "
            f"type: {obj['type']}, "
            f"has children: {'children' in obj}, "
            f"value: \"{obj.get('value', '')}\", "
            f"start: {obj['position']['start']}, "
            f"end: {obj['position']['end']}"
        )

        types.add(obj["type"])

        if "children" in obj:
            for child in obj["children"]:
                _process_nodes_and_add_types(child, level + 1)

    _process_nodes_and_add_types(ast)
    return sorted(list(types))


def main():
    with open(EXAMPLE_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    config = mdast.ParseOptions.gfm()
    ast = mdast.md_to_ast(text, config)
    # print(ast)
    print("Collected types:", process_nodes(ast))


if __name__ == "__main__":
    main()
