#import numpy as np
#a = np.arange(0,11,1) 
#print(2**a)            
#[   1    2    4    8   16   32   64  128  256  512 1024]


#x = np.array([3, 4, 5,6])
#a=3+ np.zeros(10,dtype=np.float)
#a[-1]=1.5
#print(a)
#Bài tập 2: Xây dựng mảng gồm 10 phần tử, trong đó 9 phần tử đầu bằng 3, phần tử cuối cùng bằng 1.5.


#a=[]
#for i in range(10):
 #   a.append(3) if i<9 else a.append(1.5)
#print(a)
#........................................................
''' 
import numpy as np
n=int(input())
print("n=",n)
b=-(n-4)/2 #  vd n=2, so phan tu=4 + 2*n,   [2 -1.5 -1 -0.5 0 -0.5 -1 -1.5] 
a=np.arange(2,b,-0.25)
b=list(range(1,n,2))
a[b]=-1
print(a[:n])       
Bài tập: Cho trước một số tự nhiên n. Tạo một mảng có n phần tử mà các phần tử có chỉ số chẵn (bắt đầu từ 0) là một cấp số cộng bắt đầu từ 2, công sai bằng -0.5; các phần tử có chỉ số lẻ bằng -1.
Ví dụ:
Với n=4, kết quả trả về là mảng [ 2. -1. 1.5 -1. ]. Với n=5, kết quả trả về là mảng [ 2. -1. 1.5 -1. 1. ].
.............................................................
'''
'''
import numpy as np
a=np.array([1,2,3])
b=[1,2,3]
a=np.arange(3)


b.insert(1,3)

print(np.argmax(a))
print(b)
print(len(a))
 '''
import numpy as np
a=np.array({1,12,2})
print(a)
