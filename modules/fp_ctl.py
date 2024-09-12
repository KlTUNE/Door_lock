from pyfingerprint.pyfingerprint import PyFingerprint
import time

# 指紋センサーのセットアップ&初期化
def init_fp_module():
    try:
        MODULE_PATH = '/dev/serial0'
        f = PyFingerprint(MODULE_PATH, 57600, 0xFFFFFFFF, 0x00000000)
        if ( f.verifyPassword() == False ): raise ValueError('指定された指紋センサーのパスワードが間違っています')
        print('センサー情報 : ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

        return f

    except Exception as e:
        print(f'指紋センサーを初期化できませんでした : {e}')
        return -1

### 指紋を検索
def search(f):
    try:
        if f.readImage() == False: return 999

        # 読み取った画像を特性に変換し、charbuffer1に格納
        f.convertImage(0x01)
        # 検索
        result = f.searchTemplate()
        # Index番号と一致度を取得(一致しない場合は-1)
        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber >= 0 ): print('#' + str(positionNumber) + '  一致度: ' + str(accuracyScore))
        return positionNumber

    except Exception as e:
        print(f'エラー : {e}')
        return -1

### 登録済みのindexを表示
def index(f):
    try:
        tableIndex = f.getTemplateIndex(0)
        TrueIndex = []
        for i in range(0, len(tableIndex)):
            if ( tableIndex[i]):
                print(f'#{str(i)}')
                TrueIndex.append(i)
        return TrueIndex

    except Exception as e:
        print(f'エラー : {e}')
        return []

### 指紋を削除
def delete(f):
    try:
        positionNumber = input('削除するIndex番号を入力してください: ')
        positionNumber = int(positionNumber)
        if ( f.deleteTemplate(positionNumber) == True ):
            print(f'削除しました #{positionNumber}')
            return True
        else :
            print(f'削除できませんでした #{positionNumber}')
            return False

    except Exception as e:
        print(f'エラー : {e}')
        return False

### 指紋を登録
def enroll(f):
    try:
        ## 指紋を検索
        positionNumber = search()

        if ( positionNumber >= 0 ):
            print(f'既に登録済みです #{str(positionNumber)}')
            exit(0)

        print('指を離してください...')
        # while ( f.readImage() == True ): pass
        time.sleep(2)
        print('もう一度指をセンサーにかざしてください...')
        while ( f.readImage() == False ): pass

        # 読み取った画像を特性に変換し、charbuffer2に格納
        f.convertImage(0x02)
        # charbufferを比較
        if ( f.compareCharacteristics() == 0 ): raise Exception('指紋が一致しません')
        # テンプレートの作成
        f.createTemplate()

        # テンプレートを保存
        positionNumber = f.storeTemplate()
        print(f'指紋は正常に登録されました #{str(positionNumber)}')
        return True

    except Exception as e:
        print(f'エラー : {e}')
        return False

if __name__ == "__main__":
    f = init_fp_module()
    enroll(f)
    # index(f)
    # search(f)
    delete(f)
    pass