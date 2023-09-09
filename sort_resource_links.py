"""
    If you added a new resource to an existing resources.md or learning-material.md file, just run this script directly.
    If you added a new resources.md or learning-material.md file, add the path to the file to the RESOURCE_FILE_PATHS list
    below and then run this script.

    To run this script, open a terminal or command prompt and navigate to the directory that contains this script.

    If you're using a Mac or a Linux distribution, you can run this script from the terminal by typing the following command:
        python3 sort_resource_links.py
    If you're using Windows, you can run this script from the command prompt by typing the following command:
        python sort_resource_links.py

    Note 1: You must have Python 3 installed on your computer to run this script. If you don't have Python 3 installed,
    you can download it from https://www.python.org/downloads/. Make sure you download the version for your operating
    system (Windows, Mac, or Linux).

    Note 2: This script assumes that it is at the root of the repository. If you move this script to a different location,
    you will need to update the RESOURCE_FILE_PATHS list below to include the correct paths to the resources.md and
    learning-material.md files.
    
    Note 3: (FOR NOW) This script only works with Markdown files containing ONLY links, every link must be on a new line and
    must be in the following format:
        - [text](link)
    If you have any links in a different format, this script will not work properly. If you're not sure how to format a
    Markdown link, see https://www.markdownguide.org/basic-syntax/#links.
"""


import re


class MarkdownLink:
    """Represents a Markdown link with text and a URL.

    Attributes:
        text (str): The text associated with the link.
        link (str): The URL to which the link points.
    """

    def __init__(self, text, link):
        """Initializes a MarkdownLink instance with the provided text and link.

        Args:
            text (str): The text associated with the link.
            link (str): The URL to which the link points.
        """

        self.text = text
        self.link = link

    def __str__(self):
        """Returns a user-friendly string representation of the MarkdownLink instance.

        Returns:
            str: A formatted string in the Markdown link format, e.g., "[text](link)".
        """

        return f"[{self.text}]({self.link})"

    def __repr__(self):
        """
        Returns a formal string representation of the MarkdownLink instance.

        Returns:
            str: A formatted string that represents the MarkdownLink instance.
        """

        return f"- [{self.text}]({self.link})"

    def __lt__(self, other):
        """
        Compares two MarkdownLink instances based on their text attributes for sorting.

        Args:
            other (MarkdownLink): Another MarkdownLink instance to compare with.

        Returns:
            bool: True if this instance's text is less than the other instance's text; False otherwise.
        """

        return self.text < other.text

def extract_links_from_md_file(file_content):
    """
    Extracts Markdown links from the provided file content.

    Args:
        file_content (str): The content of a Markdown file as a string.

    Returns:
        list of MarkdownLink: A list of MarkdownLink objects representing the links found in the content.
    """

    links = []
    for line in file_content.splitlines():
        match = re.search(r"- \[(.*)\]\((.*)\)", line)  # Match lines like "- [text](link)"
        if match:
            text = match.group(1)
            link = match.group(2)
            links.append(MarkdownLink(text, link))
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
        new_file_content = "\n".join([repr(link) for link in links])

        # Write the new file content to the file
        with open(markdown_file_path, "w") as f:
            f.write(new_file_content)

        # Print a success message
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
    ]

    for resource_file_path in RESOURCE_FILE_PATHS:
        sort_links_in_md_file(resource_file_path)
