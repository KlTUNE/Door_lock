from datetime import datetime

# ログファイルのパス
LOG_FILE = "./access.log"
# ログファイルの最大行数
MAX_LOG_LINES = 1000

# ログを記録する
def write_log(_from, status, message):
    with open(LOG_FILE, "r") as file:
        logs = file.readlines()
    if len(logs) > MAX_LOG_LINES: logs = logs[len(logs)+1-MAX_LOG_LINES:]
    dt_now = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
    logs.append(f"{_from} | {dt_now} | {status} | {message}\n")
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
    pass