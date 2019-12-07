import numpy as np
import matplotlib.pyplot as plt

def data_generate():
    rng=np.random.RandomState(1)
    #numpy.random.randn(d0, d1, …, dn)是從常態分配中返回一個或多個值 
    x=10*rng.rand(50)
    #numpy.random.rand(d0, d1, …, dn)的數值會產生在(0,1)之間
    y=2*x-5+rng.randn(50)

    return x,y

def train(x,y):
    learning_rate=0.0001
    #經過3000次的調整參數
    n_iterations=3000

    #隨機定義參數值
    theta = np.random.randn(2,1)
    #如同最小平方法,必須加入截距項
    x=np.concatenate((np.ones((x.shape[0],1)),x[:,np.newaxis]),axis=1)
    y=y[:,np.newaxis]
    #來畫點不一樣風格的圖吧
    plt.style.use('fivethirtyeight')
    
def draw( x,y):
    print(x,y)
    plt.scatter(x,y,s=100)
    plt.xlabel('x',fontsize=20)
    plt.ylabel('y',fontsize=20,rotation=0)
    plt.show()

if __name__ == "__main__":
    x,y = data_generate()
    train(x,y)
    
    