import matplotlib as mp
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import pymysql

dbConnection = pymysql.connect('localhost','root','','imdb_scrape')
movies = pd.read_sql("SELECT * FROM movies", dbConnection)

pd.set_option('display.expand_frame_repr',False)

movies['votes'] = movies['votes'].astype(int)
movies['gross_income'] = movies['gross_income'].astype(float)
movies.sort_values(by='votes')

print(movies.describe().loc[['min','max'],['votes','gross_income']])

correlation = np.corrcoef(movies['votes'], movies['gross_income'])

def move_figure(f,x,y):
    backend = mp.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x,y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x,y))
    else:
        f.canvas.manager.window.move(x,y)

plt.style.use('seaborn')

fig1, ax1 = plt.subplots(1,1)

ax1.scatter(movies['votes'],movies['gross_income'],linewidth=1,alpha=0.75)
# ax1.plot(movies['votes'][:15],movies['gross_income'][:15],linewidth="1.5",marker='o')
# income = np.expand_dims(movies['gross_income'], axis=1)
# income = np.reshape((3,3,1))
# im = ax1.imshow(income,cmap='Blues')
# cbar = fig1.colorbar(im,ax=ax1)
# cbar.set_label('Gross Income Range')

ax1.set_title("Correlation of Votes and Gross Income")
ax1.set_xlabel("Votes")
ax1.set_ylabel("Gross Income")

ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.title.set_text('Correlation = ' + "{:.2f}".format(correlation[0,1]))

ax1.legend()

fig1.canvas.set_window_title("Correlation Plot")
fig1.set_figheight(6)
fig1.set_figwidth(8)

move_figure(fig1,300,60)
plt.tight_layout()
plt.show()