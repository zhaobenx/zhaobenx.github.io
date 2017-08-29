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
    tag = input("请输入标签 可为空:\n").split()
    date = time.strftime("%Y-%m-%d-", time.localtime())
    with open(date+title.replace(' ','-').replace('　','-') + ".md","w",encoding='utf8') as file:
        file.write(template.format(title=title,tag=tag))

    print("Done! Enjoy your writing!")


if __name__ == "__main__":
    main()