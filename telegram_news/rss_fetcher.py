import feedparser
from bs4 import BeautifulSoup
import asyncio
from aiogram import Bot, Dispatcher, types
import time  # Ensure this line is added

async def fetch_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

async def extract_details(entry):
    title = entry.title
    link = entry.link
    summary = BeautifulSoup(entry.summary, features="html.parser").text
    published = entry.published

    return {
        'title': title,
        'link': link,
        'summary': summary,
        'published': published
    }

async def send_to_telegram(message, bot_token, chat_id):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
    await bot.close()

async def monitor_rss_interval(url, interval_seconds=300):
    last_checked = None

    while True:
        print("Checking for new entries...")
        entries = await fetch_feed(url)
        new_entries = [entry for entry in entries if last_checked is None or time.mktime(entry.published_parsed) > last_checked]

        if new_entries:
            last_checked = time.mktime(entries[0].published_parsed)
            for entry in new_entries:
                details = await extract_details(entry)
               # print(details)
               # message_text = "这是即时发送的消息11。"
               # await send_to_telegram(message_text, bot_token, chat_id)

               
                yield details  
               # await send_to_telegram(message, bot_token, chat_id)

        await asyncio.sleep(interval_seconds)



async def monitor_rss(url,last_checked):
   # last_checked = None
    
    print("Checking for new entries...")
    entries = await fetch_feed(url)
    new_entries = [entry for entry in entries if last_checked is None or time.mktime(entry.published_parsed) > last_checked]
    
    print(last_checked)
    
    if new_entries:
        last_checked = time.mktime(entries[0].published_parsed)
        yield last_checked  
        for entry in new_entries:
            details = await extract_details(entry)
            print(details)
            # message_text = "这是即时发送的消息11。"
            # await send_to_telegram(message_text, bot_token, chat_id)
            
            yield details 
            # await send_to_telegram(message, bot_token, chat_id)


if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    bot_token = sys.argv[2]
    chat_id = sys.argv[3]
    interval_seconds = int(sys.argv[4]) if len(sys.argv) > 4 else 300
    asyncio.run(monitor_rss(url, bot_token, chat_id, interval_seconds))
import feedparser
from bs4 import BeautifulSoup
import asyncio
from aiogram import Bot, Dispatcher, types
import time  # Ensure this line is added

async def fetch_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

async def extract_details(entry):
    title = entry.title
    link = entry.link
    summary = BeautifulSoup(entry.summary, features="html.parser").text
    published = entry.published

    return {
        'title': title,
        'link': link,
        'summary': summary,
        'published': published
    }

async def send_to_telegram(message, bot_token, chat_id):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
    await bot.close()

async def monitor_rss_interval(url, interval_seconds=300):
    last_checked = None

    while True:
        print("Checking for new entries...")
        entries = await fetch_feed(url)
        new_entries = [entry for entry in entries if last_checked is None or time.mktime(entry.published_parsed) > last_checked]

        if new_entries:
            last_checked = time.mktime(entries[0].published_parsed)
            for entry in new_entries:
                details = await extract_details(entry)
               # print(details)
               # message_text = "这是即时发送的消息11。"
               # await send_to_telegram(message_text, bot_token, chat_id)

               
                yield details  
               # await send_to_telegram(message, bot_token, chat_id)

        await asyncio.sleep(interval_seconds)



async def monitor_rss(url,last_checked):
   # last_checked = None
    
    print("Checking for new entries...")
    entries = await fetch_feed(url)
    new_entries = [entry for entry in entries if last_checked is None or time.mktime(entry.published_parsed) > last_checked]
    
    print(last_checked)
    
    if new_entries:
        last_checked = time.mktime(entries[0].published_parsed)
        yield last_checked  
        for entry in new_entries:
            details = await extract_details(entry)
            print(details)
            # message_text = "这是即时发送的消息11。"
            # await send_to_telegram(message_text, bot_token, chat_id)
            
            yield details 
            # await send_to_telegram(message, bot_token, chat_id)


if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    bot_token = sys.argv[2]
    chat_id = sys.argv[3]
    interval_seconds = int(sys.argv[4]) if len(sys.argv) > 4 else 300
    asyncio.run(monitor_rss(url, bot_token, chat_id, interval_seconds))
