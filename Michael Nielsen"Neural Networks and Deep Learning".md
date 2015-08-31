# [Michael Nielsen](http://michaelnielsen.org/): 『[Neural Networks and Deep Learning](http://nnadl-ja.github.io/nnadl_site_ja/index.html)』,2014
訳: [「ニューラルネットワークと深層学習」翻訳プロジェクト](https://github.com/nnadl-ja/nnadl_site_ja)より
<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/3.0/88x31.png" /></a><br />この 作品 は <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">クリエイティブ・コモンズ 表示 - 非営利 3.0 非移植 ライセンスの下に提供されています。</a>

## CHAPTER 1
# [パーセプトロン](http://nnadl-ja.github.io/nnadl_site_ja/chap1.html#perceptrons)
NANDゲートの万能性（それさえあればどんな関数でも計算できるという性質）から,パーセプトロンもまた万能.  
とりあえず,パーセプトロンは理解しているのでこのままにする.

# [シグモイドニューロン](http://nnadl-ja.github.io/nnadl_site_ja/chap1.html#sigmoid_neurons)

新しいタイプの人工ニューロン

パーセプトロンと似ているが,シグモイドニューロンの重みやバイアスに微小な変化を与えたとき,それに応じて生じる出力の変化も微小なものに留まるように調整されている.  
このことは、シグモイドニューロンで構成されているニューラルネットワークの学習を可能にする,決定的な違いとなる.  
パーセプトロンと同じく,シグモイドニューロンは$x_1, x_2,\ldots$といった入力を取りこむ.

しかし、これらの入力値は、単に$0$や$1$だけではなく、$0$から$1$<em>の間</em>のあらゆる値をとりこめる.

パーセプトロンと同じく,シグモイドニューロンはそれぞれの入力に対して,重み($w_1, w_2,\ldots$)を持ち,またニューロン全体に対するバイアスと呼ばれる値($b$)を持っている.しかし,出力は$0$や$1$だけではなく,
代わりに出力としては$\sigma(w \cdot x+b)$という値をとる.  

$\sigma$はシグモイド関数
( = <em>ロジスティック関数</em>と呼び,この新しいニューロンを<em>ロジスティック・ニューロン</em>と呼ぶことがある.
こちらの用語を使うニューラルネット研究者も大勢いる.岡谷貴之 :『[深層学習](http://amzn.to/1hMiOjZ)』講談社, 2015.によると,シグモイド関数にロジスティック関数は包含されるようだ)と呼ばれ,ニューラルネットでよく使われているアクティベーション関数である.  
次の式で定義される：

$$\begin{eqnarray}
  \sigma(z) \equiv \frac{1}{1+e^{-z}}.
\end{eqnarray}$$

パーセプトロンとの共通点を理解するため,  
$z = w \cdot x + b$を大きな正の数とする.  
すると,  
$e^{-z} \approx 0$,つまり$\sigma(z) \approx 1$となる.  

言い換えると  
$z = w \cdot x+b$を大きな数であるとき,  
シグモイドニューロンの出力はほぼ$1$となり,パーセプトロンと同じになる.

逆に,  
$z = w \cdot x+b$を大きな負の数とする.  
すると,  
$e^{-z} \rightarrow \infty$,つまり$\sigma(z) \approx 0$となる.

言い換えると  
$z = w \cdot x +b$を大きな負の数であるとき,  
シグモイドニューロンの出力はほぼ$0$となり,パーセプトロンと同じになる.


ただし, $w \cdot x+b$がそこまで大きな数でない場合はパーセプトロンと同じにはなならない.
