import re


class MarkdownLink:
    """Represents a Markdown link with text and a URL.

    Attributes:
        title (str): The title of the section in which the link appears.
        text (str): The text associated with the link.
        link (str): The URL to which the link points.
    """

    def __init__(self, title, text, link):
        """Initializes a MarkdownLink instance with the provided text and link.

        Args:
            title (str): The title of the section in which the link appears.
            text (str): The text associated with the link.
            link (str): The URL to which the link points.
        """

        self.title = title
        self.text = text
        self.link = link

    def __str__(self):
        """Returns a user-friendly string representation of the MarkdownLink instance.

        Returns:
            str: A formatted string in the Markdown link format, e.g., "[text](link)".
        """

        return f"{self.title} / [{self.text}]({self.link})"

    def __repr__(self):
        """
        Returns a formal string representation of the MarkdownLink instance.

        Returns:
            str: A formatted string that represents the MarkdownLink instance.
        """

        return f"- [{self.text}]({self.link})"

    def __lt__(self, other):
        """
        Compares two MarkdownLink instances based on their title and text attributes for sorting.

        Args:
            other (MarkdownLink): Another MarkdownLink instance to compare with.

        Returns:
            bool: True if this instance's text is less than the other instance's text; False otherwise.
        """

        return (self.title == other.title and self.text.lower() < other.text.lower())

def extract_links_from_md_file(file_content):
    """
    Extracts Markdown links from the provided file content.

    Args:
        file_content (str): The content of a Markdown file as a string.

    Returns:
        list of MarkdownLink: A list of MarkdownLink objects representing the links found in the content.
    """

    links = []
    current_title = None

    for line in file_content.splitlines():
        title_match = re.match(r"####\s+(.*)", line)  # Match titles (assumes #### title format)
        if title_match:
            current_title = title_match.group(1)
        else:
            link_match = re.search(r"- \[(.*)\]\((.*)\)", line)  # Match lines like "- [text](link)"
            if link_match:
                text = link_match.group(1)
                link = link_match.group(2)
                links.append(MarkdownLink(current_title, text, link))

    return links

def sort_links_in_md_file(markdown_file_path):
    """
    Sorts Markdown links in a Markdown file alphabetically by their link text.

    Args:
        markdown_file_path (str): The path to the Markdown file to be sorted.

    Prints:
        str: A success message indicating that the links in the file have been sorted.
    """

    try:
        with open(markdown_file_path, "r") as f:
            file_content = f.read()

        # Extract the links from the file content and sort them
        links = extract_links_from_md_file(file_content)
        links.sort()

        # Create the new file content
        new_file_content = ""
        current_title = None
        for link in links:
            if link.title != current_title:
                if current_title is not None:
                    new_file_content += "\n"
                current_title = link.title
                new_file_content += f"#### {current_title}\n\n"
            new_file_content += f"{repr(link)}\n"

        # Write the new file content to the file
        with open(markdown_file_path, "w") as f:
            f.write(new_file_content)

        print(f"Links in {markdown_file_path} sorted successfully")

    # Handle errors
    except FileNotFoundError:
        print(f"File {markdown_file_path} not found")

    except PermissionError:
        print(f"Permission denied to open {markdown_file_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    RESOURCE_FILE_PATHS = [
        "printf/resources.md",
        "simple-shell/learning-material.md",
        "dsa/resources/resources.md",
    ]

    for resource_file_path in RESOURCE_FILE_PATHS:
        sort_links_in_md_file(resource_file_path)
