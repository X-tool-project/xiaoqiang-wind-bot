# TOKEN = 'AAHXCpdwD5Z3R6Kmk6JAIM_fBI-Wj32LtaA'
from telegram import Bot
import asyncio
from telegram import Update 
from telegram.ext import Application, CommandHandler, ContextTypes

from rss_fetcher import monitor_rss

# Set the RSS URL and the refresh interval
rss_url_bbc = "http://feeds.bbci.co.uk/news/rss.xml"
rss_url_ifanr= "http://www.ifanr.com/feed"

rss_url= rss_url_ifanr
refresh_interval = 15  # in seconds


TOKEN = '7016947851:AAHXCpdwD5Z3R6Kmk6JAIM_fBI-Wj32LtaA'

CHANNEL_ID = '@xiaoqiang2025'  # 你的频道ID，也可以是频道的数字ID


def escape_markdown_v2(text):
    # 转义Markdown V2中需要转义的特殊字符
    replacements = {
        '-': '\\-', '_': '\\_', '.': '\\.', '!': '\\!', '(': '\\(', ')': '\\)',
        '{': '\\{', '}': '\\}', '=': '\\=', '+': '\\+', '|': '\\|', '~': '\\~',
        '>': '\\>', '#': '\\#', '*': '\\*'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


async def send_message(rss_url,bot_token, chat_id,interval_seconds):
    bot = Bot(token=bot_token)
    last_checked = None
    while True:
        try:
            async for result in monitor_rss(rss_url,last_checked):
             if isinstance(result, float):
                last_checked = result
                print("Last checked:", last_checked)
             else:
                details = result
                #print("Details:", details)
                #print(details)  # 可选：用于调试
                #message = f"*{details['title']}*\n{details['summary']}\n[Read more]({details['link']})"
                title = details['title']
                # print(title) 
                summary = details['summary']
                # print(summary) 
                link = details['link']

                # html_message = '<a href="https://www.example.com">访问示例网站</a>'
                # html_message = f'<a href="{link}">{title}</a>'
                #print(link) 
                #message = f"[Read more]({details['link']})"
                message = f'<a href="{link}"><b>{title}</b></a>'
                #message = f"<b><u>{title}</u></b>\n<i>{summary}</i>\n[Read more]({link})"
            
                #print(message) 
                #print("\n\n") 

            #   print(message)  # 可选：用于调试
                await bot.send_message(chat_id, text=message,parse_mode='HTML')
                #await bot.send_message(chat_id, text=message,parse_mode='Markdown')

        except Exception as e:
            print(f"发送消息过程中出现错误: {e}")
       
    await asyncio.sleep(interval_seconds)


async def send_message_test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """向频道发送即时消息。"""
    message_text = "这是即时发送的消息11。"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message_text)   



async def initialize_app():
    # Initialization tasks
    pass

async def shutdown_app():
    # Cleanup tasks
    pass

async def main(rss_url,bot_token, chat_id) -> None:
    """主函数，设置命令处理器和启动机器人。"""
    # 创建应用实例
    #application = Application.builder().token(TOKEN).build()

    # 添加命令处理器，响应/start命令
    #application.add_handler(CommandHandler("start", send_message_test))
    # 添加命令处理器，响应/start命令

    #await initialize_app()
    await send_message(rss_url,TOKEN,CHANNEL_ID,3000)

    # 开始接收更新
    #application.run_polling()

     # Other tasks
    await shutdown_app()

  


if __name__ == "__main__":
    rss_url = rss_url_ifanr
    bot_token = TOKEN
    chat_id = CHANNEL_ID
    asyncio.run(main(rss_url, bot_token, chat_id))# TOKEN = 'AAHXCpdwD5Z3R6Kmk6JAIM_fBI-Wj32LtaA'
from telegram import Bot
import asyncio
from telegram import Update 
from telegram.ext import Application, CommandHandler, ContextTypes

from rss_fetcher import monitor_rss

# Set the RSS URL and the refresh interval
rss_url_bbc = "http://feeds.bbci.co.uk/news/rss.xml"
rss_url_ifanr= "http://www.ifanr.com/feedhttp://www.ifanr.com/feed"

rss_url= rss_url_ifanr
refresh_interval = 15  # in seconds


TOKEN = '7016947851:AAHXCpdwD5Z3R6Kmk6JAIM_fBI-Wj32LtaA'

CHANNEL_ID = '@xiaoqiang2025'  # 你的频道ID，也可以是频道的数字ID


def escape_markdown_v2(text):
    # 转义Markdown V2中需要转义的特殊字符
    replacements = {
        '-': '\\-', '_': '\\_', '.': '\\.', '!': '\\!', '(': '\\(', ')': '\\)',
        '{': '\\{', '}': '\\}', '=': '\\=', '+': '\\+', '|': '\\|', '~': '\\~',
        '>': '\\>', '#': '\\#', '*': '\\*'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


async def send_message(rss_url,bot_token, chat_id,interval_seconds):
    bot = Bot(token=bot_token)
    last_checked = None
    while True:
        try:
            async for result in monitor_rss(rss_url,last_checked):
             if isinstance(result, float):
                last_checked = result
                print("Last checked:", last_checked)
             else:
                details = result
                #print("Details:", details)
                #print(details)  # 可选：用于调试
                #message = f"*{details['title']}*\n{details['summary']}\n[Read more]({details['link']})"
                title = details['title']
                # print(title) 
                summary = details['summary']
                # print(summary) 
                link = details['link']

                # html_message = '<a href="https://www.example.com">访问示例网站</a>'
                # html_message = f'<a href="{link}">{title}</a>'
                #print(link) 
                #message = f"[Read more]({details['link']})"
                message = f'<a href="{link}"><b>{title}</b></a>'
                #message = f"<b><u>{title}</u></b>\n<i>{summary}</i>\n[Read more]({link})"
            
                #print(message) 
                #print("\n\n") 

            #   print(message)  # 可选：用于调试
                await bot.send_message(chat_id, text=message,parse_mode='HTML')
                #await bot.send_message(chat_id, text=message,parse_mode='Markdown')

        except Exception as e:
            print(f"发送消息过程中出现错误: {e}")
       
    await asyncio.sleep(interval_seconds)


async def send_message_test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """向频道发送即时消息。"""
    message_text = "这是即时发送的消息11。"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message_text)   



async def initialize_app():
    # Initialization tasks
    pass

async def shutdown_app():
    # Cleanup tasks
    pass

async def main(rss_url,bot_token, chat_id) -> None:
    """主函数，设置命令处理器和启动机器人。"""
    # 创建应用实例
    #application = Application.builder().token(TOKEN).build()

    # 添加命令处理器，响应/start命令
    #application.add_handler(CommandHandler("start", send_message_test))
    # 添加命令处理器，响应/start命令

    #await initialize_app()
    await send_message(rss_url,TOKEN,CHANNEL_ID,3000)

    # 开始接收更新
    #application.run_polling()

     # Other tasks
    await shutdown_app()

  


if __name__ == "__main__":
    rss_url = rss_url_ifanr
    bot_token = TOKEN
    chat_id = CHANNEL_ID
    asyncio.run(main(rss_url, bot_token, chat_id))