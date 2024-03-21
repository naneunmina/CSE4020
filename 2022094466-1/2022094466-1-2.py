import numpy as np

M = np.arange(2,27)

print(M) #2부터 26까지의 1차원 배열
print("")
M_reshaped = M.reshape(5,5)
print(M_reshaped) #위 배열을 5by5로 변경
print("")
M_reshaped[1:-1, 1:-1] = 0
print(M_reshaped) #inner를 0으로
print("")
M_squre = M_reshaped@M_reshaped
print(M_squre) #행렬곱
print("")
V = M_squre[0, :]
print(np.sqrt(V@V)) #첫번째 행의 벡터 크기