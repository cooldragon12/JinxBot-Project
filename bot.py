import discord
from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix='>>') # Prefix for commands

# initialize prompt
@client.event
async def on_ready():
    print('We are ready to go')


# Start o coding




# For Greetings 
@client.listen('on_message')
async def greeter(message):
    list_msg = [ f"How are you?  {message.author.mention}", f"Hi!!, {message.author.mention}", f"Good Day!!, {message.author.mention}",f"Kamusta, {message.author.mention}"]
    msg = random.choices(list_msg)
    if message.content.find('ello') != -1:
        await message.channel.send(f'{" ".join( repr(e) for e in msg )}')
    # if message.content.find('Good Morning') != -1:
    #     msg = f'Good Morning!! {message.author.mention}''

    #     await message.channel.send(msg)
# Commands to call startswith'.'


@client.command(aliases=['secret','sec'], pass_context=True)
async def secret_messeges(ctx, channel, *args):
    cont = 0
    message = ' '.join(args)
    for i in client.get_all_channels():
        if channel in i.name:
            cont += i.id

    print(f'{str(cont)}')
    channel_get = client.get_channel(cont)
    await channel_get.send(message)
    # await .delete_message(message)

# Need API for the games, need pa iimprove
# Call ".sts" or ".st" or ".s?"
@client.command(aliases=['sts','st','s?'])
async def status(ctx, userid, game):
    response_un = ['Sorry this game stats is unavailable at the moment', 'Try again later', 'Try other game, it might work', 'Kung ayaw sayo wag nalang']
    if game == 'Valorant':
        await ctx.send(f'The {game}, {random.choices(response_un)}')
    elif game == 'CSGO':
        await ctx.send(f'The {game}, {random.choices(response_un)}')
    # await ctx.send(f'userid: {userid} in {game}')


# Rollete and dice
# Call ".roll" or ".rl"
@client.command(aliases=['roll','rl'])
async def rollette(ctx, add):
    included_user = []
    prefixes = ['Your turn', 'I choose you', "You're next", 'How about you']
    # member_name, member_discriminator = member.split('#')
    users = client.get_all_members()
    if add == 'all' or add == '*':
        for user in users:
            if user.status != discord.Status.offline:
                included_user.append(f'{user.name}#{user.discriminator}')
    # if add == 'add':
    #     if (member_name, member_discriminator) in (users.name,user.discriminator):
    #         included_user.append(member_name+"#"+member_discriminator)
    # chosen = random.randrange(0, len(included_user))
    await ctx.send(f'{random.choices(included_user)} {random.choices(prefixes)}')

# The key to access
client.run('ODAzMjI0MTA5MjQwMjg3MjYy.YA6qvg.m4cxIKIafJBN6C4D7rW4buhC_Lo')