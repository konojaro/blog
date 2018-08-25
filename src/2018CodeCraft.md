
# 2018华为软件精英挑战赛 赛后总结

![logo](http://codecraft.devcloud.huaweicloud.com/static/app/img/GeneralIntro/banner-2.jpg)

我队初赛的成绩是江山赛区第35名，以倒数第二的身份晋级本赛区复赛。

说来惭愧，最后是靠调参才冲了一波分，幸运地拿到了绿卡。比赛期间由于做的时间比较赶，并且和其他队伍没太多交流，所以对问题的认识有很多不到位的地方，现在回过头来看，这个问题本身是一个经典的时序问题，可以提炼出一套通用的思路供其他类似问题作为参考。

---

比赛官网： [这里](http://codecraft.devcloud.huaweicloud.com/home/Detail)

问题分为两部分：预测与装箱。显示通过对历史虚拟机实例请求的分析，预测未来一段时间实例的需求量，并找到一个接近最优的分配策略。

具体的问题及数据描述最近比较忙往后再补上，如有需要请参见官网。以下内容主要讲讲我们比赛时的做法，以及介绍一些别队赛后总结中提到的做法。

## 一、数据处理
### 数据预处理

首先以天为单位统计每种flavor的每日被请求的数量。如
```
flavor 1
2018-01-01 3
2018-02-02 2
...

flavor 2
...
```
### 数据清洗
可能出现某天是节假日，且flavor请求特别多的情况，这种数据属于异常点需要做处理。那么怎样认定数据是否是异常点？我们采用的方式是 **$\mu + 3 \delta$**, 当请求超过$\mu + 3 \delta$ 则认为当日数据异常。对于出现异常点的日子，要么直接去除，要么得重新填数，填数的方式可以非常多样，比赛中就直接设为$\mu + 3 \delta$。

这是上异常点的处理方式。训练数据中0出现的频率比较高，所以就没有下异常点的说法了。记得有一篇分享里说，据他们肉眼观察，存在某一天或者连续多天所有flavor的请求都是0的情况，可能是服务器检修。这种情况显然也属于异常点，需要处理。

另一种大家都使用的去噪方式是**箱型图**，而且据说效果拔群，随便什么模型只要一上箱型图结果都会有显著提升。目测箱型图的结果会比 $\mu + 3 \delta$ 要好。关于箱型图的介绍可以参考[这里](https://blog.csdn.net/clairliu/article/details/79217546)。

除了去噪之外，我们还加上了**平滑**，分别是三点平滑、五点平滑、七点平滑，意思是某点数据取两侧包括自己在内的三点、五点、七点的均值，加上平滑之后分数一定的提升。最后提交的版本用了三点平滑。

## 二、预测模型

### 线性回归 / 自回归

比赛数据是时序数据，没什么可以直接拿出来当特征的，所以拿前n天的数据作为特征，然后batch梯度下降求解。这个好像也叫做自回归吧。但是第n+1天的请求真的和前n天是线性关系吗？至少我感觉名次特别好的应该都不会是用线性回归来做的，除非他们发现了一些更加本质的高阶特征。

### 局部加权线性回归

局部加权线性回归考虑到更近的样本点的影响力更大，所以在目标函数里做了加权处理。

### 指数平滑

> 周期性判断： 自相关系数 傅里叶频谱


## 三、分配
使用**模拟退火法**进行装箱。

当得到预测结果后，我们会



