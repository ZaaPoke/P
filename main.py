import time
import json
import aiohttp
import asyncio
from rich.console import Console

print("   _____             ____  _                   ")
print("  |__  /__ _  __ _  / ___|| |_ ___  _ __ ___   ")
print("    / // _` |/ _` | \___ \| __/ _ \| '__/ _ \  ")
print("   / /| (_| | (_| |  ___) | || (_) | | |  __/  ")
print("  /____\__,_|\__,_| |____/ \__\___/|_|  \___|  \n")
print("=================================================")
author = "Zaa レム"
print("Author : " + author)
script = "Auto Post Discord V2"
print("Script : " + script)
discord = "Zaa Store"
print("Discord Name : " + discord)
dcurl = "https://discord.gg/GU3kzPRask"
print("Discord Url : " + dcurl)
print("===========================================")
print('Dont Resell This Script')
print("===========================================\n")

time.sleep(3)
print("Running in :")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

# rich setup
console = Console()
def tprint(content: str) -> None:
    now = time.strftime('%r')
    console.print(f'[bold bright_black]~ {now} |[/] [navajo_white1]{content}')

# load config
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
jobs = config.get('jobs')


# functions
async def send_msg(session, channel_id, msg) -> None:
    '''Sends a message to a channel'''

    res = await session.post(
        f'https://discord.com/api/v9/channels/{channel_id}/messages',
        json={'content': msg}
    )

    if res.status != 200:
        tprint(f'[bold red]Failed to send message[/] to {channel_id}')
        return print(await res.text())

    
    tprint(f'[bold green]Sent message[/] to {channel_id}')

async def msg_worker(session, job) -> None:
    '''Calls send_msg with desired interval and channel ID repeatedly'''
    
    channel_id = job.get('channel_id')
    msg = job.get('message')

    while True:
        await send_msg(session, channel_id, msg)
        await asyncio.sleep(job.get('delay'))



async def main() -> None:

    async with aiohttp.ClientSession() as session:

        session.headers.update({
            'Authorization': token
        })

        await asyncio.gather(*[msg_worker(session, job) for job in jobs])

asyncio.run(main())
