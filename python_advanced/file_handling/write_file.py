#!/usr/bin/env python3
"""Module for writing files."""


def write_file(filename="", text=""):
    """Writes a string to file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
