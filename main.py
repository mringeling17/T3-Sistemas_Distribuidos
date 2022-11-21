import wikipedia as wiki
import os

artists = ["Bad Bunny", "Dua Lipa", "Ariana Grande", "Karol_G", "The Weeknd", "Justin Bieber", "Post Malone", "Ed Sheeran", "Taylor Swift", "Bizarrap"]
wiki.set_lang('es')
count = 1
folder = "./carpeta1/"
if not os.path.exists(folder):
    os.makedirs(folder)
    os.makedirs("./carpeta2/")
for i in artists:
    a = wiki.page(i)
    if count>5:
        folder = "./carpeta2/"
    with open(folder+str(count) + '.txt', 'w', encoding='utf-8') as f:
        f.write(a.content)
    count += 1

