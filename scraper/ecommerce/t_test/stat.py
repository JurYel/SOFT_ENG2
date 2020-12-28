import matplotlib as mp
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import pymysql
from scipy import stats

dbConnection = pymysql.connect('localhost','root','','ecommerce_db')
lazada = pd.read_sql("SELECT * FROM lazada", dbConnection)
shopee = pd.read_sql("SELECT * FROM shopee", dbConnection)
ids = pd.read_sql("SELECT id FROM lazada", dbConnection)


pd.set_option('display.expand_frame_repr',False)

lazada['price'] = lazada['price'].astype(float)
shopee['price'] = shopee['price'].astype(float)
lazada['price_log'] = np.log10(lazada['price'])
shopee['price_log'] = np.log10(shopee['price'])

print(lazada.describe().loc[['min','max'],['price']])
print(shopee.describe().loc[['min','max'],['price']])

# Lazada Calculations
print("Lazada Stats: ")
la_mean = lazada['price_log'].mean()
la_std = np.std(lazada['price_log'])
la_stderr = la_std / np.sqrt(len(lazada['price_log']))

print("Mean(Lazada): {:.3f}".format(lazada['price_log'].mean()))
print("Standard Dev(Lazada): %f" % (np.std(lazada['price_log'])))
print("Standard Error(Lazada): {:.3f}".format(la_std / np.sqrt(len(lazada['price_log']))))

print("--------------")
print("Shopee Stats: ")
# Shopee Calculations

sh_mean = shopee['price_log'][:40].mean()
sh_std = np.std(shopee['price_log'][:40])
sh_stderr = sh_std / np.sqrt(len(shopee['price_log'][:40]))

print("Mean(Shopee): {:.3f}".format(sh_mean))
print("Standard Dev(Shopee): %f" % (sh_std))
print("Standard Error(Shopee): {:.3f}".format(sh_stderr))

sed = np.sqrt(la_stderr**2 + sh_stderr**2)
print("Standard Error Difference: {:.3f}".format(sed))

t_stat = (sh_mean - la_mean) / sed

print("T-Stat: {:.3f}".format(t_stat))

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

ax1.plot(shopee['id'][:40], shopee['price'][:40], color='tab:red', linewidth='1.5',marker='o')
ax1.set_xlabel('Products')
ax1.set_ylabel('Shopee Prices', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()

ax2.plot(lazada['id'], lazada['price'], color='tab:blue',linewidth='1.5',marker='o')
ax2.set_ylabel('Lazada Price',color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

ax1.set_yscale('log')
ax2.set_yscale('log')

ax1.title.set_text('Mean(Lazada) = ' + "{:.3f}".format(lazada['price_log'].mean()) + 
                " | " + "Mean(Shopee) = " + "{:.3f}".format(shopee['price_log'][:40].mean()))

fig1.canvas.set_window_title("Lazada vs Shopee")
fig1.set_figheight(6)
fig1.set_figwidth(8)

move_figure(fig1,300,60)
plt.tight_layout()
plt.show()

