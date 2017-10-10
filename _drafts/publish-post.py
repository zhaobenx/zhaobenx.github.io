import time
import os
# TODO:
# 1. loop to select post to publish -done
# 2. add date to the published post -done


def main():

    post_extension = ('.md', '.markdown', '.html')
    
    
    date = time.strftime("%Y-%m-%d-", time.localtime())
    posts = [f for f in os.listdir() if f.endswith(post_extension)]

    if not os.path.isdir('../_posts'):
        os.makedirs('../_posts')

    print("All post:\n")
    for i, post in enumerate(posts):
        print('[{}]'.format(i), '\t', post)

    num = input("Please input the post number(like 1):\n")
    try:
        post = posts[int(num)]
    except Exception as e:
        print("Wrong number")
        # print(e)
    else:
        os.rename(post, '../_posts/' + date + post)
        # print(post)
        input("Successful")


if __name__ == "__main__":
    main()
