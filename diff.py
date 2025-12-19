#!/usr/bin/env python

from diff_as_git.differ import FileDifferentiator
from diff_as_git.utilities import Document
import sys

if __name__ == '__main__':
    doc1 = Document(sys.argv[1])
    doc2 = Document(sys.argv[2])
    differ = FileDifferentiator()
    differ.diff(doc1, doc2)
    print("removed: ", differ.removed)
    print("added", differ.added)
