# パス追加用にsysをインポート
import sys
# matlabAPIのパスを追加
sys.path.append('C:\Program Files/MATLAB/R2022a/extern/engines/python/extern/engines/python/build/lib/')
# モジュールをインポート
import matlab.engine

# matlabエンジンをスタート
eng = matlab.engine.start_matlab()
# 自分のスクリプトに引数を渡して戻り値を変数に格納
res = eng.triarea(1.0, 5.0)
# 結果を出力
print(res)
eng.quit()