#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MNISTの手描き数字データをDLし,描画する.
http://qiita.com/kenmatsu4/items/7b8d24d4c5144a686412
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_mldata

# Scikit LearnをつかってMNISTの手書き数字データのダウンロード
# #HOME/scikit_learn_data/mldata/mnist-original.mat にキャッシュされる
print 'fetch MNIST dataset'
mnist = fetch_mldata('MNIST original')
# mnist.data : 70,000件の784次元ベクトルデータ
mnist.data   = mnist.data.astype(np.float32)
mnist.data  /= 255     # 0-1のデータに変換

"""
# mnist.target : 正解データ（教師データ）
mnist.target = mnist.target.astype(np.int32)
これは要らない
"""

# 手書き数字データを描画する関数
def draw_digit(data):
    size = 28
    plt.figure(figsize=(2.5, 3))

    X, Y = np.meshgrid(range(size),range(size))
    Z = data.reshape(size,size)   # convert from vector to 28x28 matrix
    Z = Z[::-1,:]             # flip vertical
    plt.xlim(0,27)
    plt.ylim(0,27)
    plt.pcolor(X, Y, Z)
    plt.gray()
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")

    plt.show()
# MNISTの手描き数字データを3つ適当に選択
draw_digit(mnist.data[5])
draw_digit(mnist.data[12345])
draw_digit(mnist.data[33456])
