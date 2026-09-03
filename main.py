import math
import numpy as np
import matplotlib.pyplot as plt
'''
#4.3.1
data = np.random.rand(100)
print("Среднее:", round(np.mean(data), 4))
print("Медиана:", round(np.median(data), 4))
plt.scatter(range(100), data)
plt.title("Диаграмма рассеяния")
plt.show()
'''
#лошок
'''
#4.3.2
x = range(1, 11)
f = [math.sqrt(1+math.exp(math.sqrt(i)+math.cos(i**2)))/abs(1-math.sin(i)**3)+math.log(abs(2*i)) for i in x]
plt.plot(list(x), f)
plt.scatter(list(x)[:5], f[:5], color='black')
plt.show()
'''

'''
#4.3.3
import numpy as np
import matplotlib.pyplot as plt
from numpy import trapezoid as trapz
x = np.arange(0, 11, 1)
y = np.abs(np.cos(x * np.exp(np.cos(x) + np.log(x + 1))))
area = trapz(y, x)
print("Площадь:", round(area, 4))
plt.fill_between(x, y, alpha=0.3)
plt.plot(x, y)
plt.title(f'Площадь = {area:.4f}')
plt.show()
'''

'''
#4.3.4
m = range(1,13)
apple = [131.96,127.79,122.15,131.46,124.61,136.96,145.86,151.83,141.50,149.80,165.30,177.57]
microsoft = [231.96,232.38,235.77,252.18,249.68,270.90,286.54,301.88,281.92,331.62,330.59,336.32]
google = [1835.74,2070.07,2068.63,2410.12,2406.32,2541.01,2704.42,2909.24,2789.61,2953.94,2948.37,2893.59]
plt.subplot(3,1,1); plt.plot(m,apple); plt.title('Apple')
plt.subplot(3,1,2); plt.plot(m,microsoft); plt.title('Microsoft')
plt.subplot(3,1,3); plt.plot(m,google); plt.title('Google')
plt.tight_layout()
plt.show()
'''
'''
#4.3.5
import math
x,y = float(input("x: ")),float(input("y: "))
for name,val in [('+',x+y),('-',x-y),('*',x*y),('/',x/y if y else 'err'),('e^(x+y)',math.exp(x+y)),('sin',math.sin(x+y)),('cos',math.cos(x+y)),('x^y',x**y)]:
    print(f"{name} = {val}")
'''