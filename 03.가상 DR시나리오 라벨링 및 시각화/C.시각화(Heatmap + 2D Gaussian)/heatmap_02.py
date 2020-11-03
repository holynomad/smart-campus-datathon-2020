#heatmap_02.py
# 참조: https://www.it-swarm.dev/ko/python/%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9C%84%EC%97%90-%ED%9E%88%ED%8A%B8-%EB%A7%B5/829748283/
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from PIL import Image
import pandas as pd

# https://stackoverflow.com/questions/21566379/fitting-a-2d-gaussian-function-using-scipy-optimize-curve-fit-valueerror-and-m
def twoD_Gaussian(xdata_tuple, amplitude, xo, yo, sigma_x, sigma_y, theta, offset):
    (x, y) = xdata_tuple
    xo = float(xo)
    yo = float(yo)
    a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
    b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
    c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
    g = offset + amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo)
                        + c*((y-yo)**2)))
    return g.ravel()

# using colormap : https://pythonkim.tistory.com/82
def transparent_cmap(start_level, end_level, cmap, N=255):
    #"Copy colormap and set alpha values"

    mycmap = cmap
    mycmap._init()
    #mycmap._lut[:,-1] = np.linspace(0, 0.8, N+4)
    mycmap._lut[:,-1] = np.linspace(start_level, end_level, N+4)
    return mycmap

#from pathlib import Path
#print(Path().absolute())

# read labelled & merged Dataset
df = pd.read_csv("labelled_all_merged_20200625_v1.6.csv", encoding = 'euc-kr')


# https://hogni.tistory.com/7
df_modified = df[["roomid", "datetime", "temp"]]

print(df_modified.head())

df_mod_202 = df_modified[df_modified['roomid'] == 202]

print(df_mod_202.head())

df_mod_202_pv = df_mod_202.pivot('roomid', 'datetime', 'temp')
#
print(df_mod_202_pv.head())
#

#Use base cmap to create transparent
# ref color range : https://pythonkim.tistory.com/82 (e.g. Blues, Greens, Reds, jet, coolwarm... )
mycmap_202 = transparent_cmap(0, 1, plt.cm.Reds)
mycmap_203 = transparent_cmap(0, 0.8, plt.cm.Blues)
mycmap_204 = transparent_cmap(0, 0.4, plt.cm.Blues)
mycmap_205 = transparent_cmap(0, 0.1, plt.cm.Reds)

# Import image and get x and y extents
I = Image.open('2F.png')
p = np.asarray(I).astype('float')
w, h = I.size
y, x = np.mgrid[0:h, 0:w]

#Plot image and overlay colormap
fig, ax = plt.subplots(1,1)
ax.imshow(I)
#Gauss = twoD_Gaussian((x, y), 1, .5*x.max(), .4*y.max(), .1*x.max(), .1*y.max(), 0, 3)

case_level = 20
offset = 0
amp = 5

sig_x_202 = 0.02
sig_y_202 = sig_x_202


# iterating over time-series
#for i in range(0, len(df_mod_202.index), 1):

i = 500
theta_202 = df_mod_202.loc[i, 'temp']

# twoD_Gaussian(xdata_tuple, amplitude, xo, yo, sigma_x, sigma_y, theta, offset):
Gauss202 = twoD_Gaussian((x, y), amp, .65*x.max(), .27*y.max(), sig_x_202*x.max(), sig_y_202*y.max(), 1, offset)
cb = ax.contourf(x, y, Gauss202.reshape(x.shape[0], y.shape[1]), case_level, cmap=mycmap_204)

sig_x_203 = 0.01
sig_y_203 = sig_x_203
theta_203 = df_mod_202.loc[i, 'temp']
wgt_sig_212 = 0.05


Gauss203 = twoD_Gaussian((x, y), amp, .68*x.max(), .35*y.max(), sig_x_203*x.max(), sig_y_203*y.max(), 2, offset)
cb = ax.contourf(x, y, Gauss203.reshape(x.shape[0], y.shape[1]), case_level, cmap=mycmap_204)
#plt.colorbar(cb203)

Gauss204 = twoD_Gaussian((x, y), amp, .7*x.max(), .63*y.max(), .03*x.max(), .03*y.max(), 3, offset)
cb = ax.contourf(x, y, Gauss204.reshape(x.shape[0], y.shape[1]), case_level, cmap=mycmap_203)

#theta_212 = df_mod_212.loc[i, 'covid_case']
#wgt_sig_212 = 0.05
x_212 = 0.48
y_212 = 0.63

Gauss212 = twoD_Gaussian((x, y), amp, x_212*x.max(), y_212*y.max(), wgt_sig_212*x.max(), wgt_sig_212*y.max(), theta_212, offset)
cb = ax.contourf(x, y, Gauss212.reshape(x.shape[0], y.shape[1]), case_level, cmap=mycmap_212)

plt.title("SK Future - 2F COVID risk map")
plt.colorbar(cb)
plt.show()
