import os
# 获取当前工作目录
dir_path = os.getcwd()
# 遍历指定目录下的所有文件
for root, dirs, files in os.walk(dir_path):
    for file in files:
        # 只处理后缀为md、html、xml的文件
        if file.endswith('.md') or file.endswith('.html') or file.endswith('.xml'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('{{', '{% raw %}{{')
            content = content.replace('}}', '}}{% endraw %}')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'{file_path} 处理完毕！')