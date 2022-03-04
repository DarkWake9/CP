
from math import log10
from matplotlib import pyplot as plt
arr = [2.37,
3.56,
4.20,
4.90,
6.02,
6.73,
7.21,
7.60,
9.66,
10.45,
10.65,
10.65,
10.65,
10.65,
10.65,
10.65,
10.65,
10.65,
10.65,
10.65,
10.65,
10.61,
10.45,
9.74,
9.39,
8.71,
8.00,
4.89,
2.28]
K = 1000
freq = [20,
30,
40,
50,
70,
80,
90,
100,
250,
500,
1*K ,
2 *K ,
5 *K ,
10 *K ,
20 *K ,
30 *K ,
40 *K ,
50 *K ,
60 *K ,
70 *K ,
80 *K ,
100 *K ,
200 *K ,
500 *K ,
600 *K ,
800 *K ,
1000 *K ,
2000 *K ,
3000 *K ,
]
res = [i/0.3 for i in arr]
logres = [float(20 * log10(i)) for i in res]
#for i in res:
  #  print(i)
#for i in logres:
 #   print(i)

plt.loglog(freq,logres)
plt.title("Frequency Response\nStop band                                                             Pass band                                                             Stop band")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain in dB")
plt.show()