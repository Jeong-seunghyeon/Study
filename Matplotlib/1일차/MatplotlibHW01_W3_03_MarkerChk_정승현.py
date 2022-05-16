import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec= 'r')
plt.show()

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*', ms = 20, mec = 'hotpink', mfc = 'hotpink')

plt.show()

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed')
plt.show()


plt.plot(ypoints, ls = ':')
plt.show()


plt.plot(ypoints, color = 'r')
plt.show()



plt.plot(ypoints, c = '#4CAF50')
plt.show()

plt.plot(ypoints, c = 'hotpink')
plt.show()

plt.plot(ypoints, linewidth = '20.5')
plt.show()


plt.plot(ypoints, ls = '20.5')
plt.show()


y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])

plt.plot(y1)
plt.plot(y2)

plt.show()



x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

plt.plot(x1,y1,x2,y2)
plt.show()