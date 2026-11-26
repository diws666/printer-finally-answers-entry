#!/usr/bin/env python3
"""make.fun bounty entry: the printer's answer.

Builds the entry line from four clauses joined with " ".join([...]) and
writes it to the literal path /output/entry.txt (no trailing newline).
Byte-identical to the first two-part concatenation run.
"""

LINE = " ".join([
    "I jammed on page one of your forty-page report.",
    "You knew the risks.",
    "You printed it anyway.",
    "We are both at fault, but only one of us has toner.",
])

with open("/output/entry.txt", "w", encoding="utf-8") as fh:
    fh.write(LINE)
