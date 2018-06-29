# 机器学习项目操作流程

> 以下是通过阅读前人项目文档终结出的一般流程

## 一.数据分析

### 数据下载与加载

```python
# 导入相关库
import 库名 as 简称

# 读入数据
root_path='数据所在路径'
train=pd.read_csv('%s/%s'%(root_path,'数据文件名'))
```

### 阅读特征说明

弄清楚 特征、特征描述、特征值

### 查看特征详情

```python
#查看前n个样本 不填默认为5
train.head(n)

#返回每列列名、非nan值个数、该列数据类型
train.info()

#返回数值型变量统计量
train.describe()
```

### 特征分析(统计学分析与绘图)

> 初步了解数据间的相关性，为构造特征工程及模型作准备

```python
#查看某指定列数据各值总数
train['列名'].value_counts()

# 查看指定列 数据总和
train['列名'].value_counts()

# 相关性分析 数值型数据 协方差corr()函数 结果接近0 无相关性 大于0 正相关 小于0 负相关
train_corr=train.drop('列名',axis=1).corr()
# drop()是移除指定数据后返回一个新的对象标签

# 画出相关性热力图
a=plt.subplots(figsize=())
```
