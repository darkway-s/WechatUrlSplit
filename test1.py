import argparse
from Url2Html import Url2Html
from StyleSlot import StyleSlot

parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('--url', type=str, default='https://mp.weixin.qq.com/s/OA0rTMFRDjivnlEBFQRKOw',
                    help='the url to be operated on')
parser.add_argument('--inputfile', type=str, default='test.html',
                    help='the name of the input file')
parser.add_argument('--outputfile', type=str, default='output.docx',
                    help='the name of the output file')
args = parser.parse_args()

url = args.url
inputfile = args.inputfile
outputfile = args.outputfile

uh = Url2Html()
s = uh.operate(url, mode=1)

# 保存到文件
with open(inputfile, 'w', encoding='utf-8') as f:
    f.write(s)

print('success!')
st = StyleSlot(s, outputfile)
print(st)
