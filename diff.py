#!/usr/bin/env python

from diff_as_git.Differ import Differ
from diff_as_git.utilities import Document
import sys

if __name__ == '__main__':
    doc1 = Document(sys.argv[1])
    doc2 = Document(sys.argv[2])

    Differ.diff(doc1, doc2)
