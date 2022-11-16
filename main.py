import wikipedia as wiki

artists = ["Bad Bunny", "Dua Lipa", "Ariana Grande", "Karol_G", "The Weeknd", "Justin Bieber", "Post Malone", "Ed Sheeran", "Taylor Swift", "Bizarrap"]
wiki.set_lang('es')
for i in artists:
    a = wiki.page(i)
    with open(i+'.txt', 'w', encoding='utf-8') as f:
        f.write(a.content)

