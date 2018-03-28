
# numpy部分函数介绍
> 本文记录了我在使用numpy过程中用到的函数


```python
from numpy import *
```

## shape
shape函数的功能是查看矩阵或者数组的维数
***

建立一个3X3的单位矩阵a,a.shape=(3,3)，表示3行3列


```python
a=eye(3)
```


```python
a
```




    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])




```python
a.shape
```




    (3, 3)



建立一个4x3的矩阵b,shape[0]=4 shape[1]=3 


```python
b=array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
```


```python
b
```




    array([[ 1,  2,  3],
           [ 4,  5,  6],
           [ 7,  8,  9],
           [10, 11, 12]])




```python
b.shape[0]
```




    4




```python
b.shape[1]
```




    3



## tile
tile函数的功能是重复某个数组。比如tile(A,n)，功能是将数组A重复n次，构成一个新的数组。
***

建立一个数组a,用tile方法来创建数组b


```python
a=[0,1,2]
```


```python
b=tile(a,2)
```


```python
b
```




    array([0, 1, 2, 0, 1, 2])




```python
b=tile(a,(2,1))
```


```python
b
```




    array([[0, 1, 2],
           [0, 1, 2]])

