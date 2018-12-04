%Parameter Estimation for ODE models
<<<<<<< HEAD
=======
%Copyright 2018 Hiroaki Imoto.
>>>>>>> 11c2345cb5d3dd4c81d1b5d483e29567b6b016c0

%MODEL: NF-kB model[1]
%EXPERIMENTAL DATA: nuclear NF-kB signal intensity (Measured by Mr. Michida)

%Parameter values were searched by genetic algorithm with Unimodal Normal Distribution Crossover[2] and Minimal Generation Gap[3].

①ファイル・関数の説明
・Figure
    図が入る．
・Fitparam
    パラメータ探索で結果が更新されるとここに入る．
・GA
    GAによるパラメータ探索，ODEソルバー，誤差の計算等に必要な関数
・PaperOptimization
    論文

・setParamConst.py
    定数のパラメータ(x)の名前およびその値
・setVarEnum.py
    変数(y)の名前
・diffeq.py
    微分方程式
・experimental_data.py
    フィッティングに使用する実験データ
・initialValues.py
    モデルの初期値(y0)
・getFitness.py
    シミュレーション結果と実験値の誤差(fit)を定量化
・setSearchParam.py
    最適化の対象となるパラメータ
・runGA.py
    GAによる探索を開始する．パラメータの探索範囲をここに記述．
・runSim.py
    （GAによって得られたパラメータセットでの）数値シミュレーション


②実行方法
<<<<<<< HEAD
    0. Anaconda(Python3.x version)を https://www.anaconda.com/download/ よりダウンロードする．
=======
    0. Anaconda(Python3.x version)をhttps://www.anaconda.com/download/ よりダウンロードする．
    
    1. Jupyter NotebookでrunGA.ipynbを開き，[%run -i runGA.py]と書かれたセルを実行する．計算中は誤差が小さくなっていく様子が表示される．計算は世代数の上限に達するか，許容誤差を下回るまでずっと実行される．Generation: 1000くらいまで計算すれば十分（だいぶ時間がかかります）．
    
    
    2. runSim.ipynbを開き，[%run -i runSim.py]と書かれたセルを実行する．
        
>>>>>>> 11c2345cb5d3dd4c81d1b5d483e29567b6b016c0

    1. Jupyter NotebookでrunGA.ipynbを開き，[%run -i runGA.py]と書かれたセルを実行する．計算中は誤差が小さくなっていく様子が表示される．計算は世代数の上限に達するか，許容誤差を下回るまでずっと実行される．Generation: 1000くらいまで計算すれば十分（だいぶ時間がかかります）．


    2. runSim.ipynbを開き，[%run -i runSim.py]と書かれたセルを実行する．


Reference:
    [1]Oppelt A, Kaschek D, Huppelschoten S, Sison-Young R, Zhang F, Buck-Wiese M et al. Model-based identification of TNFα-induced IKKβ-mediated and IκBα-mediated regulation of NFκB signal transduction as a tool to quantify the impact of drug-induced liver injury compounds. npj Syst Biol Appl 2018; 4: 23.

    [2]Ono I., Kita H., Kobayashi S.. A robust real-coded genetic algorithm using unimodal normal distribution crossover augmented by uniform crossover: effects of self-adaptation of crossover probabilities. in Proceedings of the 1st Annual Conference on Genetic and Evolutionary Computation 1, 496–503 (1999).
<<<<<<< HEAD

    [3]Sato, H., Ono, I. & Kobayashi, S. A new generation alternation model of genetic algorithms and its assesment. J. Jpn Soc. Artif. Intell. 12, 734–744 (1997).
=======
    
    [3]Sato, H., Ono, I. & Kobayashi, S. A new generation alternation model of genetic algorithms and its assesment. J. Jpn Soc. Artif. Intell. 12, 734–744 (1997).
>>>>>>> 11c2345cb5d3dd4c81d1b5d483e29567b6b016c0
