import time
from twitchio.ext import commands

class MeuBot(commands.Bot):
    def __init__(self):
        super().__init__(token='SEU_TOKEN', prefix='!', initial_channels=['CANAL_DA_TWITCH'])

    async def event_ready(self):
        print(f'Bot conectado como {self.nick}')
        while True:
            await self.connected_channels[0].send("Estou no apoio! 🚀")
            time.sleep(600)  # Espera 10 minutos antes de repetir

bot = MeuBot()
bot.run()