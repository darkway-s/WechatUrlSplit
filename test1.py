from Url2Html import Url2Html
from StyleSlot import StyleSlot


# url = "https://mp.weixin.qq.com/s/5z99-ykZ3qQgi1rK2AaGEg" 
url = "https://mp.weixin.qq.com/s/OA0rTMFRDjivnlEBFQRKOw"
inputfile = 'test.html'
outputfile = 'output.docx'

uh = Url2Html()
s = uh.operate(url, mode=1)
# 保存到文件
with open(inputfile, 'w', encoding='utf-8') as f:
    f.write(s)

print('success!')
st = StyleSlot(s, outputfile)
print(st)