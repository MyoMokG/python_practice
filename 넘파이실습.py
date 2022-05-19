import numpy as np


print("=====[문제1]=====")
num_arr = np.arange(1,21)

print("배열:", num_arr)
print("역순:", num_arr[::-1]) # 역순
print("합:", num_arr.sum()) # 합

num_rearr = num_arr.reshape(5,4)
print("2차배열:\n", num_rearr)


print("=====[문제2]=====")
n_arr = np.arange(25).reshape(5,5)
print(n_arr)
print("첫 번째 데이터:", n_arr[0,0])
print("마지막 데이터:", n_arr[4][4])
print("마지막 인덱스는 -1로 써도 됩니다.",n_arr[-1][-1])

print("슬라이싱 연습 1:\n", n_arr[0:2]) # 0행 이상 2행 미만
print("슬라이싱 연습 2:\n", n_arr[2:]) # 2행 이상
print("슬라이싱 연습 3:\n", n_arr[:, ::2]) #전체 행(디폴트 1칸씩 이동), 전체 열(2칸씩 이동)
print("슬라이싱 연습 4:\n", n_arr[::2, ::2]) #전체 행(2칸씩 이동), 전체 열(2칸씩 이동)
print("슬라이싱 및 리쉐이프 연습:\n", n_arr[0:2].reshape(5,2)) 
