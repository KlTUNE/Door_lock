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

# 指紋を検索
def search():
    pass

# 登録済みのindexを表示
def index():
    try:
        tableIndex = f.getTemplateIndex(0)
        for i in range(0, len(tableIndex)):
            print('TemplateIndex #' + str(i) + ' is used: ' + str(tableIndex[i]))

    except Exception as e:
        print(f'エラー : {e}')
        exit(1)

# 指紋を削除
def delete():
    pass

# 指紋を登録
def enroll():
    pass

if __name__ == "__main__":
    # search()
    index()
    # delete()
    # enroll()
    pass