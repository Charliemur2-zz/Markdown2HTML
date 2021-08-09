#!/usr/bin/python3
""" Script that converts Markdown to HTML
    Args:
        First: name of the Markdown file.
        Second: output file name.
"""

import sys
import os


def markdownToHtml():
    if (len(sys.argv) < 3):
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not(os.path.isfile("./{}".format(md_file))):
        print("Missing {}".format(md_file), file=sys.stderr)
        exit(1)

    headings_md = ["###### ", "##### ", "#### ", "### ", "## ", "# "]
    headings_html = ["<h6>", "<h5>", "<h4>", "<h3>", "<h2>", "<h1>"]

    with open(md_file, "r") as f_in:
        with open(html_file, "w") as f_out:
            for line in f_in.read().split("\n"):
                for i in range(0, len(headings_md)):
                    if headings_md[i] in line:
                        new_line = line.replace(
                            headings_md[i], headings_html[i])
                        new_line += headings_html[i].replace("<", "</") + "\n"
                        f_out.write(new_line)
                        break

    exit(0)

if __name__ == "__main__":
    markdownToHtml()
