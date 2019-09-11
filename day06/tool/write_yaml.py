# 导包
import yaml

# 数据准备
data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

# 需求：将data写入data目录下 write.yaml
with open("../data/write.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True)
