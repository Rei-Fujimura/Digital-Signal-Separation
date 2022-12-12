###############################################################################
# 課題　電気マニア（デジタル信号処理）用Pythonコード
###############################################################################

#==============================================================================
# ライブラリインポート
#==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks

#==============================================================================
# 微分計算
#==============================================================================
Data = pd.read_csv(r"C:\Users\norir\Desktop\課題用.csv")
x = Data.to_numpy().T[0]
y = Data.to_numpy().T[1]
print(x,y)
dy = np.gradient(y)
 
#==============================================================================
# グラフ
#==============================================================================

# ピーク検出
peaks, _ = find_peaks(abs(dy), height=0.25,rel_height=0.5,distance=5)
print(peaks)

# 微分対象波形
plt.plot(x, y, 'r-', label='wave')
plt.plot(x, y, 'r.')
 
# 微分波形
plt.plot(x, abs(dy), 'b-', label='differential')
plt.plot(x, abs(dy), 'b.')
plt.plot(peaks, abs(dy)[peaks], "x", color = "orange", markersize=10) 
# グラフのタイトル・目盛設定
plt.title("Differential")
 
# 凡例の位置設定
plt.legend(loc='upper left')
 
# 罫線
plt.grid(which='major', color='black', linestyle='-')
plt.grid(which='minor', color='black', linestyle='-')
 
# 軸ラベル
plt.xlabel('x')
plt.ylabel('y')
 
file_name = 'differential.jpg'
plt.savefig(file_name)
plt.show()

width = peaks[1]-peaks[0]
print("width:", width)