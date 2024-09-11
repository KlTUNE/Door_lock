from datetime import datetime
from pathlib import Path

# ログファイルのパス
LOG_FILE = "./access.log"
# ログファイルの最大行数
MAX_LOG_LINES = 1000

# ログを記録する
def write_log(_from, status, message):
    try:
        with open(LOG_FILE, "r") as file: logs = file.readlines()
    except FileNotFoundError:
        # ファイルが存在しない場合は作成する
        file_path_obj = Path(LOG_FILE)
        file_path_obj.touch()
        logs = []
    if len(logs) >= MAX_LOG_LINES: logs = logs[1:]
    dt_now = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
    log_message = f"{_from} | {dt_now} | {status} | {message}\n"
    print(log_message)
    logs.append(log_message)
    logs = ''.join(logs)
    with open(LOG_FILE, "w") as file:
        file.write(logs)

# 直前に記録されたログを読み込む
def read_before_log():
    return read_all_log()[-1]

# 全てのログを読み込む
def read_all_log():
    with open(LOG_FILE, "r") as file:
        logs = list(map(adjust_log, file.readlines()))
        return logs

# read_all_log()で使用されるmac用関数
def adjust_log(log):
    log = log.rstrip('\r\n')
    log = log.split(" | ")
    return log

if __name__ == "__main__":
    write_log("test", "OPEN", "SUCCESS")
    # print(read_before_log()[2])
    # file_path_obj = Path("./test.log")
    # file_path_obj.touch()
    pass
