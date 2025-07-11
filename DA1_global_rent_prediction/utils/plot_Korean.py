# utils/plot_Korean.py


import matplotlib.pyplot as plt
import matplotlib as mpl

def set_korean_font():
    mpl.rcParams['font.family'] = 'Malgun Gothic'  # Windows 기준
    mpl.rcParams['axes.unicode_minus'] = False
