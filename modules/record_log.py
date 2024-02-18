
LOG_FILE = "access.log"

def wite_log(log):
    with open("log.txt", "a") as file:
        file.write(log + "\n")
        file.close()

def read_berore_log():
    with open("log.txt", "r") as file:
        log = file.read()
        file.close()
        return log

def read_all_log():
    with open("log.txt", "r") as file:
        logs = file.readlines()
        file.close()
        return logs

if __name__ == "__main__":
    pass