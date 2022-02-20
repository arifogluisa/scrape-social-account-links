def link_setter(links, url):
    reddit_link = 'No link'
    telegram_link = 'No link'
    discord_link = 'No link'
    medium_link = 'No link'
    pinterest_link = 'No link'

    for link in links:
        if "reddit.com" in link['href']:
            reddit_link = link['href']
        if "t.me" in link['href']:
            telegram_link = link['href']
        if "discord" in link['href'] or "chat" in link['href']:
            discord_link = link['href']
        if "medium.com" in link['href']:
            medium_link = link['href']
        if "pinterest.com" in link['href']:
            pinterest_link = link['href']

    return url, reddit_link, telegram_link, discord_link, medium_link, pinterest_link
