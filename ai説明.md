* 説明出来る程度にAIを噛み砕く

モチベーション
* 結局,自分は働かずに,他人よりも賢いAIを奴隷として使いたいだけでは?*
* 自分か自分以上の賢い人を作る.


# 仕組み
# 必要なモデル

関数との関係
概念の説明

w(重み),b(バイアス)の目標に対する調節が学習である.

目標をいかに正しく設定するか
目標が間違っていたら,学習は時間の無駄になる.
目標を調節するのはフィードバックに対する関数を用いて調節する.
未来の目標は過去のデータしかないので,微分を使うことで調節していく.

自己符号化器によって,人間が教えなくても,機械が自分で学ぶようになった.

# コンピュータ将棋を例に「評価関数」のモデルをシンプルに書く
# モデルの定義
W^t = 重み , x = 特徴(駒の種類,数,位置関係,王将の危険度等の要素),入力  
f(x{n}) = W^t_{1} * x_{1} + W^t_{2} * x_{2} +...+W^t_{n} * x_{n} + b{n},
重みベクトル W と,特徴,入力ベクトル x の積に,バイアス bと一緒に加算したものが,1つのユニット(神経細胞)に入力される.
入力に対して,出力する際に関数で処理する.

モデルを作る上で最も重要なのがWの調整で,あらかじめ決めたWがどの程度適合しているかを統計的手法による検証を繰り返す.
では,統計的手法とは?

# 順伝播型ニューラルネットワーク FFNN

入力に,活性化関数を掛けたものが出力になる

# 変数は,x, w, b, 活性化関数

なぜ,入力を出力に変えるたるに活性化関数で処理する必要があるのか?確率で表現するため?

ロジスティック関数の説明

過学習防止にDropout
