import time
import os
import 
## TODO:
# 1. loop to select post to publish
# 2. add date to the published post 
def main():
    
    date = time.strftime("%Y-%m-%d-", time.localtime())
    #with open(date+file_name.replace(' ','-').replace('　','-') + ".md","w",encoding='utf8') as file:
    #    file.write(template.format(title=title,tag=tag))

    #print("Done! Enjoy your writing!")
    post_extension = ('.md','.markdown','.html')
    posts = [f for f in os.listdir() if f.endswith(post_extension) ]

    if not os.path.isdir('../_posts'):
        os.makedirs('../_posts')
    for post in posts:
        print
       
    os.rename('')
    input()


if __name__ == "__main__":
    main()