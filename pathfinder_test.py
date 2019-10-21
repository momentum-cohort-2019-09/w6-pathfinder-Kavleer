import pytest
from pathfinder import *



def test_true_is_true():
  assert "true" == "true"

def test_source_file():
  assert source_file != None

def test_min_elevation():
  assert min_elevation([100,10,30,40]) == 10

def test_max_elevation():
  assert max_elevation([100,10,30,40]) == 100

def test_avg_elevation():
  assert avg_elevation([100,10,30,40]) == 45

def test_determine_source_file_height():
  data = """1 2 3
4 5 6
7 8 9"""
  assert determine_source_file_height(data) == 3

