import html2markdown

# 读取 HTML 文件内容
with open('test.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 转换为 Markdown 格式
markdown_content = html2markdown.convert(html_content)

# 将转换后的 Markdown 内容保存到文件
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)
