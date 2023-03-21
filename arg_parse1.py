import argparse  # 导入模块
parser = argparse.ArgumentParser()  # 创建对象
parser.add_argument('--length', default=9, type=int, help='长度')
args = parser.parse_args()
print('长度=', args.length)
