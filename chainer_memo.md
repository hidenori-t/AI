# about chainer
ChainerはPreffered Networksが開発したニューラルネットワークを誤差伝播で学習するライブラリ.特徴は、「実際に Python のコードを用いて入力配列に何の処理が適用されたかだけを記憶しておき、それを誤差逆伝播の実行に使います」だそう。

# 参考

[Chainer Tutorial](http://docs.chainer.org/en/latest/tutorial/index.html)

[CUDAなしMacで、Chainer使ってCaffeモデルをインポートして画像認識させてみる](http://d.hatena.ne.jp/shi3z/20150711/1436566217)


[DeepLearningライブラリのChainerがすごい、らしい](http://cvl-robot.hateblo.jp/entry/2015/06/11/223928)

[PFN発のディープラーニングフレームワークchainerで画像分類をするよ(chainerでニューラルネット1)](http://hi-king.hatenablog.com/entry/2015/06/11/021144)

***
macbook で試した
```
pip install chainer
git clone https://github.com/pfnet/chainer.git
python chainer/examples/mnist/train_mnist.py
```
Chainerの順伝播型ニューラルネットワークでClassificationしてみる、という試み

# MNIST(Mixed National Institute of Standards and Technology)とは
[THE MNIST DATABASE of handwritten digits](http://yann.lecun.com/exdb/mnist/)
(手書き数字データベース)のトレーニング
MNISTとは28x28pxの60000枚の学習サンプル、10000枚のテストサンプルからなる手書き数字画像データベースです。ニューラルネットワークのベンチマーク的な立場で機械学習分野やDeepLearning分野で広く使われています。

``` output
('epoch', 20)
train mean loss=0.0486672781675, accuracy=0.985983343621
test  mean loss=0.0633980164513, accuracy=0.985000008941
```
test 予測誤差 train 訓練誤差 epoch データを何周したか
理想的には,訓練精度・予測精度がバランス良く上昇し,収束して欲しい
数10~100 epoch の間で目に見える程度,緩やかな指数関数的カーブが理想
予測精度が訓練精度のやや下で推移が理想
[ディープラーニングの過去と未来](http://www.slideshare.net/nlab_utokyo/20150414seminar)

train,test ともに 98.5% 出てる  
trainは学習に使用され、testの方は学習の評価に使用されます。
学習中にlossとaccuracyというものが表示されていると思います。
lossは予測と正解の一致が多くなると小さくなる値、
accuracyは正解率をそれぞれ意味します。なのでこれらの値の推移を見ていると学習が進んでいる様子が分かると思います。

# Chainerをアップグレード
```
$ sudo pip install chainer --upgrade
```
[機械学習ライブラリ Chainerの紹介](http://nonbiri-tereka.hatenablog.com/entry/2015/06/14/225706)
Weight Decayや学習アルゴリズムの設定ができます（SGDとか）
他にもCNNやRNNなども揃っているのでおそらく、基本的なネットワーク構築は簡単にできると思います。

# 各関数等を説明
Chainerの作法で,データは配列からChainerのVariableという型（クラス）のオブジェクトに変換して使う.

https://github.com/pfnet/chainer/blob/master/chainer/functions/softmax_cross_entropy.py にソフトマックス関数の出力値ykを用いて交差エントロピー関数が表現されている.
***
[【機械学習】ディープラーニング フレームワークChainerを試しながら解説してみる。](http://qiita.com/kenmatsu4/items/7b8d24d4c5144a686412)
を参考に精度と誤差をグラフ描画する!!

```
# 精度と誤差をグラフ描画??
plt.figure(figsize=(8,6))
plt.plot(range(len(train_acc)), train_acc)
plt.plot(range(len(test_acc)), test_acc)
plt.legend(["train_acc","test_acc"],loc=4)
plt.title("Accuracy of digit recognition.")
plt.plot()
```
error
```
Traceback (most recent call last):
  File "/Users/tatarahidenori/chainer/examples/mnist/train_mnist.py", line 176, in <module>
    plt.plot(range(len(train_acc)), train_acc)
NameError: name 'train_acc' is not defined
```
