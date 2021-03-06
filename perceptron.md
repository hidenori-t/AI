# パーセプトロン
線形識別器の基礎(今は)
究極的には「識別関数」の値の大小で分類する.

$$\mathbf{y}=\mathbf{w^{\mathrm{T}}x}$$

$\mathbf{x}$: 入力信号（これから識別したいもの）  
$\mathbf{w^{\mathrm{T}}}$: 重みベクトル（学習結果）  
$\mathbf{y}$: 返値（「±の符号」が大事！）  
***
例として,ここではメールのSPAM判定を想定する.

入力信号の例.「メールの単語頻度」と仮定.

$$ \mathbf{x}=\begin{bmatrix}「会議」という語の数 \\「目標」という語の数  \\「お買い得」という語の数 \end{bmatrix} =  \begin{bmatrix}2 \\1  \\0 \end{bmatrix}$$

次に,重みベクトルの例.適当に決め打ち.

$$ \mathbf{w}=\begin{bmatrix}w_{1} \\w_{2}  \\w_{3} \end{bmatrix} =\begin{bmatrix}1(「会議」は非SPAM) \\1(「目標」は非SPAM)  \\-1(「お買い得」はSPAM) \end{bmatrix} $$

そこで識別関数を計算してみる.

$$\mathbf{y}=\mathbf{w^{\mathrm{T}}x}= \begin{bmatrix}1 & 1 & -1 \end{bmatrix} \begin{bmatrix}2 \\1  \\0 \end{bmatrix}=2$$

$\mathbf{y}=2$ ゆえに,これは非SPAM.
***
$\mathbf{w^{\mathrm{T}}}$ は$1 \times 3$行列 $(m =1,n =3)$  
$\mathbf{x}$ は$3 \times 1$行列 $(n =3,p =1)$

このとき $\mathbf{w^{\mathrm{T}}}$ の第 $1(i=1)$ 行と $\mathbf{x}$ の第 $1(j=1)$ 列はともに $3(n=3)$ 個の成分からなっているので,その対応する成分の積の和は

$$
\mathbf{y} = \sum_{k=1}^{3} w_{1k}^{{\mathrm{T}}}\mathbf{x}_{k1}=
w_{11}^{{\mathrm{T}}}\mathbf{x}_{11}+
w_{12}^{{\mathrm{T}}}\mathbf{x}_{21}+
w_{13}^{{\mathrm{T}}}\mathbf{x}_{31}=
1\cdot2 +1\cdot1+ (-1)\cdot0 =3
$$
で表す.

2ではなく3っぽい
```
import numpy as np

wt = np.array([1,1,-1])
x = np.array([[2],
              [1],
              [0]])

print np.dot(wt,x)
```
***
続きはslideshareのp16から



ちなみに  
> パーセプトロンが分からなきゃ、 サポートベクターマシンも分からない！  
パーセプトロンが分かれば、 サポートベクターマシンなんて余裕！  
（おそらく）史上最強の 機械学習分類器  

とのことです.  
slideshare:
[Simple perceptron by TJO](http://www.slideshare.net/takashijozaki1/simple-perceptron-by-tjo) from [Takashi J Ozaki](http://www.slideshare.net/takashijozaki1)を参考にさせてもらいました.
