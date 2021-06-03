#! /usr/bin/python3

# for sibling imports
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from utils.data_mutations import raw_to_nn_data
from pathlib import Path

base_path = Path(__file__).parent
file_path = (base_path / "../data/raw_klines_data.m").resolve()
file_path2 = (base_path / "../data/nn_data.m").resolve()
raw_data = open(file_path, "r")
nn_data = open(file_path2, "w")

nn_str = raw_to_nn_data(raw_data.read())
nn_data.write(nn_str)