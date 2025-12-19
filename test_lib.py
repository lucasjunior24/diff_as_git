#!/usr/bin/env python

from diff_as_git.differ import FileDifferentiator
from diff_as_git.utilities import Document, Line

def create_line(filepath: str):
    liness: list[Line] = []
    for num, line in enumerate(filepath.split('\n')):
        liness.append(Line(num, line))
    return liness

class DocumentFile(Document):
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def lines(self):
        return create_line(self.filepath)
    
file_a = "Ahs, ssss \ndistinctly I\n remember it was\n in the bleak Decembe\nr And each separate d\ning ember wrought its ghos\nt upo\nn the floor. \n \sas "
file_b = "Assh, ss \ndistinctly I\n remember it was\n in\n the bleak December\n testajdp lpadlsapdlaps\n And each separa\nte dying \nember wrought its ghost upon the\n floor.\n | test added"

if __name__ == '__main__':
    doc1 = DocumentFile(file_b)
    doc2 = DocumentFile(file_a)

    differ = FileDifferentiator()
    differ.diff(doc1, doc2)
    print(differ.removed)
    print(differ.added)
