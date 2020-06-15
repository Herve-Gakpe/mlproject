# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest

def haversine() :
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) == 0.21901499328621418
