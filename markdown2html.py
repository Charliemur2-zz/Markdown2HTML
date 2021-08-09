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

    mark_down = sys.argv[1]
    html = sys.argv[2]

    if not(os.path.isfile("./{}".format(mark_down))):
        print("Missing {}".format(mark_down), file=sys.stderr)
        exit(1)

    head_mark = ["###### ", "##### ", "#### ", "### ", "## ", "# "]
    head_html = ["<h6>", "<h5>", "<h4>", "<h3>", "<h2>", "<h1>"]

    with open(mark_down, "r") as f_in:
        with open(html , "w") as f_out:
            for line in f_in.read().split("\n"):
                for i in range(0, len(head_mark)):
                    if head_mark[i] in line:
                        new_line = line.replace(
                            head_mark[i], head_html[i])
                        new_line += head_html[i].replace("<", "</") + "\n"
                        f_out.write(new_line)
                        break

    exit(0)

if __name__ == "__main__":
    markdownToHtml()
