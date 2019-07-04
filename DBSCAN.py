'''
@author:lzp
@Algorithms:DBSCAN
'''
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
'''
说明：计算向量间距离
输入：向量A，向量B
输出：欧式距离
'''
def dist(vector1,vector2):
    return np.sqrt(np.sum(np.square(vector1-vector2)))
'''
说明：判断是否在ε-邻域中
'''
def eps_neighbor(vector1,vector2,eps):
    model=KNeighborsClassifier()
    return dist(vector1,vector2) < eps;
'''
说明：
'''
def DBSCAN(D, e, Minpts):
  #初始化核心对象集合T,聚类个数k,聚类集合C, 未访问集合P,
  T = set(); k = 0; C = []; P = set(D)
  for d in D:
    if len([ i for i in D if dist(d, i) <= e]) >= Minpts:
      T.add(d)
  #开始聚类
  while len(T):
    P_old = P
    o = list(T)[np.random.randint(0, len(T))]
    P = P - set(o)
    Q = []; Q.append(o)
    while len(Q):
      q = Q[0]
      Nq = [i for i in D if dist(q, i) <= e]
      if len(Nq) >= Minpts:
        S = P & set(Nq)
        Q += (list(S))
        P = P - S
      Q.remove(q)
    k += 1
    Ck = list(P_old - P)
    T = T - set(Ck)
    C.append(Ck)
  return C

