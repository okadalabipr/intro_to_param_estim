# 最適ちゃん
遺伝的アルゴリズムを用いたODEモデルのパラメータ最適化
***
![cfos](https://user-images.githubusercontent.com/31299606/50464653-81b02700-09d5-11e9-910a-e3e2dcbd4fdd.png)

 Points (blue diamonds, EGF; red squares, HRG) denote experimental data, solid lines denote simulations.

## モデル

- [Nakakuki, T. et al. Ligand-specific c-Fos expression emerges from the spatiotemporal control of ErbB network dynamics. Cell 141, 884–896 (2010).](https://www.cell.com/cell/fulltext/S0092-8674(10)00373-9)

## 使い方

0. [Anaconda3](https://www.anaconda.com/)をダウンロードする．
1. **Parameter search**
    - Jupyter Notebookでwork/runGA_jupyter.ipynbを開き，一番上の`%run -i script/run_ga1.py`と書かれたセルを実行する．更新された最良のパラメータセットはFitParamフォルダに格納される．設定した世代数の上限に達する or 許容誤差を下回るまで計算は実行される．一度中断した最適化計算を再開する場合は，その下の`%run -i script/run_ga2.py`と書かれたセルを実行する．
2. **Plot simulation results**
    - Jupyter Notebookでwork/runSim_jupyter.ipynbを開き，一番上のセルを実行するとその時点での最良のパラメータセットでのシミュレーション結果を表示する．

## インストール
    $ git clone https://github.com/u360665a/ODEParamEstim