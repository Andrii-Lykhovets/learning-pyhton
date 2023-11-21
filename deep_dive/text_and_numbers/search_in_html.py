import urllib.request

if __name__ == "__main__":
    page = urllib.request.urlopen('https://github.com/Andrii-Lykhovets')
    text = page.read().decode('utf8')

    description_start = text.find('meta property="og:description"') + 40
    description_end = text.find('" /><meta property="profile:username"')
    description = text[description_start:description_end]

    print(description)
