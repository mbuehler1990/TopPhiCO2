
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from stl import mesh


def import_stl(File,Points,PolygonPoints,Surfaces):
    your_mesh = mesh.Mesh.from_file('some_file.stl')



    return your_mesh