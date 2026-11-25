#!/usr/bin/env python3
"""Print the Fix Human Sleep patch-note entry."""

import pathlib


def load_note(path="entry.txt"):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    return " ".join(text.split())


def deliver(note):
    print(note)


def main():
    deliver(load_note())


if __name__ == "__main__":
    main()
