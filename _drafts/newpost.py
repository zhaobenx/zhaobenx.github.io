import time

template = \
"""---
layout: post
title: {title}
tag: {tag}
comments: true
---
"""


def main():
    title = ''
    while not title:
        title = input("请输入文章标题:\n")
    file_name = input("请输入文件名称，空默认为标题:\n") or title
    tag = input("请输入标签 可为空:\n").split()
    date = time.strftime("%Y-%m-%d-", time.localtime())
    with open(date+file_name.replace(' ','-').replace('　','-') + ".md","w",encoding='utf8') as file:
        file.write(template.format(title=title,tag=tag))

    print("Done! Enjoy your writing!")


if __name__ == "__main__":
    main()