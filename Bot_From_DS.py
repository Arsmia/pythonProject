import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_messege(self, messege):
        print('Message from {0.author}: {0.content}'.format(messege))

client = MyClient()
client.run("OTE4MTA0MDgzMzM0ODQwMzUx.YbCZDw.Xh9gnBxT_v8Qkq4eIr603pui1VE")

