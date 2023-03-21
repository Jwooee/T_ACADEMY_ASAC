def calcBMI( height, weight):
    stdW = (height-100)*0.85
    obesity = weight/stdW*100
    return obesity

import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False 

