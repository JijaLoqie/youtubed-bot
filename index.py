import os
import sys
import loguru

from aiogram import Bot, Dispatcher, executor, types
import aiohttp

import exceptions
from youtube_handler import Youtubed


logger = loguru.logger
logger.add(sys.stderr, level="INFO")

API_TOKEN = "6669346721:AAEHGv1QM9zlfEr8vS1YFRfPFGRTqB1xA00"
PROXY_URL = "PROXY_URL"
PROXY_AUTH = aiohttp.BasicAuth(
    login="TELEGRAM PROXY LOGIN",
    password="TELEGRAM PROXY PASSWORD"
)

bot = Bot(token=API_TOKEN)
# bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)

dp = Dispatcher(bot)


def auth(func):
    
	async def wrapper(message):
		if message['from']['id'] == 123:
			return await message.reply("Ты не Слава, не Дима и не Саша!", reply=False)
		return await func(message)
	


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply(
		"Привет!\n\n"
		"/video <link> <quality>- загрузить сюда видосик\n"
		"\t\t\tquality=[max, min] - качество видосика - по умолчанию максимальное\n\n"
		"/music <link> - загрузить сюда музычку с ютуба\n"
	, reply=False)

@dp.message_handler(commands=['video', 'Video'])
async def video(message: types.Message):
	args = message.get_args().split()

	youtube = Youtubed(link=args[0])
	if (len(args) > 1):
		youtube.download(type='mp4', quality=args[1])
	else:
		youtube.download(type='mp4')
		

	await bot.send_video(message.chat.id, open(f'data/{youtube.title}.mp4', 'rb'))

	# await youtube.clear()
	# await message.reply(
	# 	"Лови видосик\n"
	# , reply=False)


@dp.message_handler(commands=['music', 'Music'])
async def music(message: types.Message):
	args = message.get_args().split()

	youtube = Youtubed(link=args[0])
	youtube.download(type='mp3')

	await bot.send_audio(message.chat.id, open(f'data/{youtube.title}.mp3', 'rb'))

	# await youtube.clear()

	# await message.reply(
	# 	"Лови музычку\n"
	# , reply=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
