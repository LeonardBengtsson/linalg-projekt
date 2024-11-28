import os
from typing import Optional, Any

import numpy

import urllib
from urllib.request import OpenerDirector

import openpyxl
from openpyxl.workbook import Workbook


def fetch_workbook_from_url(url: str, path: str) -> Optional[Workbook]:
    if not os.path.isfile(path):
        directory: str = os.path.dirname(path)
        if not os.path.isdir(directory):
            os.makedirs(directory)

        opener: OpenerDirector = urllib.request.build_opener()
        opener.addheaders = [('User-agent', '')]
        urllib.request.install_opener(opener)
        try:
            urllib.request.urlretrieve(url, path)
        except:
            return None
    if not os.path.isfile(path):
        return None
    return openpyxl.open(path, read_only=True)


def load_matrix(path: str) -> Optional[numpy.ndarray[Any, Any]]:
    if not os.path.isfile(path):
        return None
    return numpy.loadtxt(path)


def save_matrix(path: str, matrix: numpy.ndarray[Any, Any], float_numbers: bool = False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if float_numbers:
        numpy.savetxt(path, matrix, fmt='%f')
    else:
        numpy.savetxt(path, matrix)