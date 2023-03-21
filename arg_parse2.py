import argparse  # 导入模块
parser = argparse.ArgumentParser()  # 创建对象
parser.add_argument('--Length', default=9, type=int, help='长度')
parser.add_argument('--Width', default=6, type=int, help='宽度')
args = parser.parse_args()
area = args.Length * args.Width
print('面积=', area)
