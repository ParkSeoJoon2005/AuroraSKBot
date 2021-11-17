
  
"""
XIT License 2021
Copyright (c) 2021 Dihan Official
"""
import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from DaisyX import (DEV_USERS, pbot)
from DaisyX.utils import formatter




# Stats Module

async def bot_sys_stats():
    bot_uptime = ANYTIME
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
root@DihanOfficial:~$ Sophia
------------------
UPTIME: ANYTIME
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
------------------
"""
    return stats

