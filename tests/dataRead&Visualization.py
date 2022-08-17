import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog
f=filedialog.askopenfile(mode="rb",title="请打开记录的inner或out文件",initialdir="./../logs")
arr=__import__("pickle").load(f)
print(len(arr))
arr2=np.arange(0,len(arr)*3,3)
plt.plot(arr2,arr,label="delay")
plt.legend()
plt.xlabel("second")
plt.ylabel("ms")
plt.show()
