# 导包
import yaml


# 获取文件流 并调用load解析
def read_yaml():
    with open("../data/data.yaml", "r", encoding="utf-8") as f:
        return yaml.load(f)


if __name__ == "__main__":
    print(read_yaml())
