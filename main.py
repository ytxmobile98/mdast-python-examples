import mdast
from pathlib import Path

CURDIR = Path(__file__).parent

EXAMPLE_FILE = CURDIR / "docs" / "example.md"


def extract_text_from_node(node):
    """Recursively extract text content from AST nodes,
    handling paragraphs properly by collecting all text
    within a paragraph on one line"""

    # Handle text nodes directly
    if node.get('type') == 'text':
        return node.get('value', '')

    # Handle paragraph nodes -
    # collect all text from their children into a single string
    if node.get('type') == 'paragraph':
        paragraph_text = ''
        if 'children' in node:
            for child in node['children']:
                text = extract_text_from_node(child)
                if text:
                    paragraph_text += text
        # Return the entire paragraph text as a single string
        return paragraph_text

    # For root node, process each child and separate them with blank lines
    # Only add blank lines between different top-level elements
    # (like paragraphs)
    if node.get('type') == 'root':
        result_lines = []
        if 'children' in node:
            for child in node['children']:
                child_text = extract_text_from_node(child)
                if child_text:
                    # If it's a paragraph or similar block element, add it as a complete line
                    result_lines.append(child_text)

        # Join all blocks with two newlines (blank line between them)
        return '\n\n'.join(result_lines)

    # For other node types,
    # recursively process their children and concatenate the results
    text_content = ''
    if 'children' in node:
        for child in node['children']:
            text = extract_text_from_node(child)
            if text:
                text_content += text
    return text_content


def remove_markdown_formatting(text):
    """Parse Markdown using mdast and remove formatting symbols,
    returning plain text with each paragraph on one line
    separated by blank lines"""
    parse_options = mdast.ParseOptions.gfm()
    ast = mdast.md_to_ast(text, parse_options)

    # The root node is usually a 'root' type node containing children
    if isinstance(ast, dict) and ast.get('type') == 'root':
        result = extract_text_from_node(ast)
        # Ensure proper formatting: trim and make sure it's clean
        return result.strip()
    else:
        # If the parsing result is not the expected structure,
        # return the original text or an empty string
        return text


def main():
    with open(EXAMPLE_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Remove Markdown formatting to get plain text
    plain_text = remove_markdown_formatting(text)

    print("Original Markdown content:")
    print("=" * 50)
    print(text)
    print("\nPlain text after removing formatting:")
    print("=" * 50)
    print(plain_text)


if __name__ == "__main__":
    main()
