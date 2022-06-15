
import math
from tkinter.tix import Tree

import matplotlib.pyplot as plt
import numpy as np
from sympy import LM

# 状態ベクトル
Cx = np.diag([0.5, 0.5, np.deg2rad(30.0)]) ** 2

# シミュレーションパラメータ
Q_sim = np.diag([0.2, np.deg2rad(1.0)]) ** 2
R_sim = np.diag([1.0, np.deg2rad(10.0)]) ** 2

DT = 0.1  # time tick [s]
SIM_TIME = 50.0
MAX_RANGE = 20.0
M_DIST_TH = 2.0
STATE_SIZE = 3
LM_SIZE = 2

show_animation = True


def main():
    print(__file__ + " start")
    
    time = 0.0

    # RFID positions [x. y]
    RFID = np.array()