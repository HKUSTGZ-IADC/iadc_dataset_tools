#!/usr/bin/python3
import os
import sys
import numpy as np

class Lidar():
  def __init__(self, lidar_name):
    self.lidar_name = lidar_name

  def __str__(self):
    return '{} Intrinsics:\n'.format(self.lidar_name)

if __name__ == '__main__':
  pass
