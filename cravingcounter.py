import os
import dbfunctions
from discord.ext import commands
from dotenv import load_dotenv

def main():
    try:
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')

        bot = commands.Bot(command_prefix='!')

        @bot.command(name='urge', aliases=["craving"], help = "Adds 1 to your counter of urges you overcame")
        async def urge_counter(ctx):
            message = ''
            member_id = ctx.message.author.id
            data = dbfunctions.get_member_data(member_id)
            if not data:
                dbfunctions.create_member((str(member_id), ctx.message.author.name, 1, 0))
                message = 'Way to start keeping track of your urges!'
            else:
                dbfunctions.update_member(member_id, 'urge')
                if (data[0] == 0):
                    message = 'You have now overcome your first urge!'
                else:
                    message = 'You have now overcome ' + str(data[0] + 1) + ' urges!'
            await ctx.send(message)

        @bot.command(name='saidno', help = "Adds 1 to your counter of times you've said no when you could've used")
        async def no_counter(ctx):
            message = ''
            member_id = ctx.message.author.id
            data = dbfunctions.get_member_data(member_id)
            if not data:
                dbfunctions.create_member((str(member_id), ctx.message.author.name, 0, 1))
                message = 'Way to start keeping track of the times you\'ve said no!'
            else:
                dbfunctions.update_member(member_id, 'saidno')
                if (data[1] == 0):
                    message = 'You said \'no\' when you had the opportunity to use for the first time! Nice going!'
                else:
                    message = 'You\'ve said \'no\' when you could\'ve used ' + str(data[1]) + ' times now!'
            await ctx.send(message)

        @bot.command(name='stats', help = "Check your stats!")
        async def check(ctx):
            message = ''
            member_id = ctx.message.author.id
            data = dbfunctions.get_member_data(member_id)
            if not data:
                message = 'Looks like you haven\'t started keeping track yet. How about now? Just send the !urge or !saidno command and let me do the rest!'
            else:
                message = 'You\'ve overcome ' + str(data[0]) + ' urges and you\'ve said \'no\' when you could\'ve used ' + str(data[1]) + ' times now!'
            await ctx.send(message)

        bot.run(TOKEN)

    except KeyboardInterrupt:
        bot.close()

main()
