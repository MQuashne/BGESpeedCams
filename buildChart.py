#%%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("speed-cam.csv")
df.columns=['dateTime','speed','unit','path','x','y','width','height','area','direction','location']
df['dateTime'] = pd.to_datetime(df['dateTime'])
L2R = df.loc[df['direction'] =="L2R"]
R2L = df.loc[df['direction'] =="R2L"]
#%%
plt.style.use('seaborn')
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(L2R["dateTime"],L2R["speed"],c='#0000FF40')
ax.scatter(R2L["dateTime"],R2L["speed"],c='#ff800040')
ax.legend()
plt.savefig("speed_scatter.png")
# %%
print(df['dateTime'])
# %%
