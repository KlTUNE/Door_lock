from pyfingerprint.pyfingerprint import PyFingerprint
import time, hashlib

# 指紋センサーのセットアップ&初期化
try:
    MODULE_PATH = '/dev/serial0'
    f = PyFingerprint(MODULE_PATH, 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ): raise ValueError('指定された指紋センサーのパスワードが間違っています')
    print('センサー情報 : ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

except Exception as e:
    print(f'指紋センサーを初期化できませんでした : {e}')
    exit(1)

### 指紋を検索
def search():
    try:
        print('指をセンサーにかざしてください...')
        while ( f.readImage() == False ): pass

        # 読み取った画像を特性に変換し、文字バッファ1に格納
        f.convertImage(0x01)
        # 検索
        result = f.searchTemplate()
        # Index番号と一致度を取得
        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            print('不一致')
            exit(0)
        else:
            print('一致 Index番号#' + str(positionNumber))
            print('一致度: ' + str(accuracyScore))

    except Exception as e:
        print(f'エラー : {e}')
        exit(1)

### 登録済みのindexを表示
def index():
    try:
        tableIndex = f.getTemplateIndex(0)
        for i in range(0, len(tableIndex)):
            print('#' + str(i) + ' is used: ' + str(tableIndex[i]))

    except Exception as e:
        print(f'エラー : {e}')
        exit(1)

### 指紋を削除
def delete():
    pass

### 指紋を登録
def enroll():
    pass

if __name__ == "__main__":
    search()
    # index()
    # delete()
    # enroll()
    pass