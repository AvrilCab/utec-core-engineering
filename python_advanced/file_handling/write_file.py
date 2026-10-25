#!/usr/bin/env python3
"""Module for writing to text files."""


def write_file(filename="", text=""):
    """Writes a string to a text file (utf-8) and returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
