import discord
import asyncio

discord_channel_id = 0000000000000
discord_bot_token = "TOKEN"
discord_timeout = 60

class Client(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.loop.create_task(self.update_count_user_task())

    async def on_ready(self):
        print('Loged in as: {0}'.format(self.user))
        

    async def update_count_user_task(self):
        await self.wait_until_ready()
        while not self.is_closed():
            info_channel = self.get_channel(discord_channel_id)
            await info_channel.edit(name="new_name_channel")
            await asyncio.sleep(discord_timeout)

client = Client()
client.run(discord_bot_token)

