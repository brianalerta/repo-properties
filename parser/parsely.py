#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from pathlib import Path
from PyPDF2 import PdfFileReader
import tabula

ROOT = str(Path('.').resolve())


def extract_information(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()

    print(datetime.strptime(information.get('/ModDate'), 'D:%Y%m%d%H%M%SZ'))

    return information


def tabl(path):
    tables = tabula.read_pdf(path, pages="all", multiple_tables=True)
    print(tables)


if __name__ == '__main__':
    tabl(os.path.join(ROOT, 'raw', 'ucpb', '2020',
                      '02', '19',
                      'UCPB_Repossessed_Vehicles_20200219.pdf'))
    # print(ROOT)
