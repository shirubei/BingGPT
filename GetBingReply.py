import asyncio
from EdgeGPT import Chatbot

async def reply_BING(query):
	bot = Chatbot()
	response = await bot.ask(prompt = query)
	await bot.close()

	return response["item"]["messages"][1]["text"].replace('^', '') + '\n\n数据源:' 
	  + response["item"]["messages"][1]["adaptiveCards"][0]["body"][0]["text"].split("\n\n")[0].replace('"', '')
  
	reply = asyncio.run(reply_BING(msg))
	send_msg(reply, receiverid, room_id, nickname, 1)  #send_msg 通过websocket client发送消息给微X程序, 
          #具体参照https://github.com/cixingguangming55555/wechat-bot
