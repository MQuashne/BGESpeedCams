#!/usr/bin/python3

import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/pi/speed-camera/speed-cam.csv")
df.columns=['dateTime','speed','unit','path','x','y','width','height','area','direction','location']
df['dateTime'] = pd.to_datetime(df['dateTime'])
L2R = df.loc[df['direction'] =="L2R"]
R2L = df.loc[df['direction'] =="R2L"]

plt.style.use('default')
fig=plt.figure()
fig.suptitle('Parsonage Rd Traffic Speed')
ax=fig.add_subplot(111)
ax.scatter(L2R["dateTime"],L2R["speed"],c='#0000FF40')
ax.scatter(R2L["dateTime"],R2L["speed"],c='#ff800040')
ax.legend(["Left to Right","Right to Left"], loc='upper left',ncol=1,frameon=True)
ax.set_xlabel('Date and Time')
ax.set_ylabel('Speed (mph)')

figFile = "/home/pi/speed-camera/media/graphs/speed_scatter.png"
if os.path.isfile(figFile):
	os.remove(figFile)
plt.savefig(figFile)

source = "/home/pi/speed-camera/speed-cam.csv"
destination = "/home/pi/speed-camera/media/entries/speed-cam.csv"
dest = shutil.copyfile(source,destination)
print("Destination Path:", dest)
