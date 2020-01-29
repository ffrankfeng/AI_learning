### logistic回归
![1](https://github.com/fengf96/deeplearning.ai---notes/blob/master/DL1-2/0002.jpg?raw=true)
1. 用于二分分类的算法
2. 输出值经过sigmoid()函数，使输出值范围为（0，1）
    1. sigmoid(z)表达式：
        ```math
         \delta (z)=\frac{1}{1+e^{-z}}
        ```
    2. 笔记
    ![2](https://github.com/fengf96/deeplearning.ai---notes/blob/master/DL1-2/0005.jpg?raw=true)
    
### logistic回归损失函数
1. 误差平方损失函数回使得梯度下降无法找到最优解。
2.  损失函数：
    ```math
    l(\hat{y},y)=-ylog(\hat{y})+(1-y)log(1-\hat{y})
    ```
3. 成本函数：
    ```math
    J(w,b)=\frac{1}{m}\sum_{m}^{i=1}l(\hat{y})^{(i)},y^{(i)})
    ```
    
### 梯度下降法
w，b参数更新：
```math
    w=w-a\frac{dJ(w,b)}{dw}
    
    b=b-a\frac{dJ(w,b)}{db}
```

### 导数

### 计算图
1. 链式法则