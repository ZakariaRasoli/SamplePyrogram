
# import psutil
# import platform
# from datetime import datetime

# def get_size(bytes, suffix="B"):
#     factor = 1024
#     for unit in ["", "K", "M", "G", "T", "P"]:
#         if bytes < factor:
#             return f"{bytes:.2f}{unit}{suffix}"
#         bytes /= factor

# # print(platform.uname())
  
# # Memory usage
# # Calling psutil.cpu_precent() for 4 seconds
# # print('The CPU usage is: ', psutil.cpu_percent())

# # print("RAM memory % used:", round((psutil.virtual_memory()[2]/psutil.virtual_memory()[0]) * 100, 2))
# print("="*40, "System Information", "="*40)
# uname = platform.uname()
# print(f"System: {uname.system}")
# print(f"Node Name: {uname.node}")
# print(f"Release: {uname.release}")
# print(f"Version: {uname.version}")
# print(f"Machine: {uname.machine}")
# print(f"Processor: {uname.processor}")

# # Boot Time
# print("="*40, "Boot Time", "="*40)
# boot_time_timestamp = psutil.boot_time()
# bt = datetime.fromtimestamp(boot_time_timestamp)
# print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# # let's print CPU information
# print("="*40, "CPU Info", "="*40)
# # number of cores
# print("Physical cores:", psutil.cpu_count(logical=False))
# print("Total cores:", psutil.cpu_count(logical=True))
# # CPU frequencies
# cpufreq = psutil.cpu_freq()
# print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
# print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
# print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# # CPU usage
# print("CPU Usage Per Core:")
# for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
#     print(f"Core {i}: {percentage}%")
# print(f"Total CPU Usage: {psutil.cpu_percent()}%")

# # Memory Information
# print("="*40, "Memory Information", "="*40)
# # get the memory details
# svmem = psutil.virtual_memory()
# print(f"Total: {get_size(svmem.total)}")
# print(f"Available: {get_size(svmem.available)}")
# print(f"Used: {get_size(svmem.used)}")
# print(f"Percentage: {svmem.percent}%")
# print("="*20, "SWAP", "="*20)
# # get the swap memory details (if exists)
# swap = psutil.swap_memory()
# print(f"Total: {get_size(swap.total)}")
# print(f"Free: {get_size(swap.free)}")
# print(f"Used: {get_size(swap.used)}")
# print(f"Percentage: {swap.percent}%")

# # Disk Information
# print("="*40, "Disk Information", "="*40)
# print("Partitions and Usage:")
# # get all disk partitions
# partitions = psutil.disk_partitions()
# for partition in partitions:
#     print(f"=== Device: {partition.device} ===")
#     print(f"  Mountpoint: {partition.mountpoint}")
#     print(f"  File system type: {partition.fstype}")
#     try:
#         partition_usage = psutil.disk_usage(partition.mountpoint)
#     except PermissionError:
#         # this can be catched due to the disk that
#         # isn't ready
#         continue
#     print(f"  Total Size: {get_size(partition_usage.total)}")
#     print(f"  Used: {get_size(partition_usage.used)}")
#     print(f"  Free: {get_size(partition_usage.free)}")
#     print(f"  Percentage: {partition_usage.percent}%")
# # get IO statistics since boot
# disk_io = psutil.disk_io_counters()
# print(f"Total read: {get_size(disk_io.read_bytes)}")
# print(f"Total write: {get_size(disk_io.write_bytes)}")

# # Network information
# print("="*40, "Network Information", "="*40)
# # get all network interfaces (virtual and physical)
# if_addrs = psutil.net_if_addrs()
# for interface_name, interface_addresses in if_addrs.items():
#     for address in interface_addresses:
#         print(f"=== Interface: {interface_name} ===")
#         if str(address.family) == 'AddressFamily.AF_INET':
#             print(f"  IP Address: {address.address}")
#             print(f"  Netmask: {address.netmask}")
#             print(f"  Broadcast IP: {address.broadcast}")
#         elif str(address.family) == 'AddressFamily.AF_PACKET':
#             print(f"  MAC Address: {address.address}")
#             print(f"  Netmask: {address.netmask}")
#             print(f"  Broadcast MAC: {address.broadcast}")
# # get IO statistics since boot
# net_io = psutil.net_io_counters()
# print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
# print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

# from pyrogram.handlers import *


# def messageHandler(app, admins):
#     async def dump(client, message):
#         chat = message.chat
#         chat_id = chat.id
        
#         from_user = message.from_user
#         from_id = from_user.id

#         text = message.text
#         if str(from_id) in admins:
#             await app.send_message(chat_id, message)

#             if text == '/stop':
#                 await app.send_message(chat_id, "Bye.")
#                 await app.stop()
        

#     myHandler = MessageHandler(dump)
#     app.add_handler(myHandler)



# from pyrogram.handlers import *


# def messageHandler(app, admins):
#     async def dump(client, message):
#         text = fromId = fromName = None
#             text   = message.text
#             chatId = message.chat.id
#             chat_type   = message.chat.type
#             reply  = message.reply_to_message_id
    
#         if str(chat_type) != 'ChatType.CHANNEL':
#             from_user = message.from_user
#             fromId    = from_user.id
#             fromName  = from_user.first_name

#             if str(fromId) in admins:
#                 await app.send_message('-1001718852657', message)
#                 if text == '/himen':
                    
#                 #await app.stop()
#             if text == '/memory':
#                 import psutil
#                 await app.send_message(chatId, psutil.virtual_memory()[2])
#                 print()

#     myHandler = MessageHandler(dump)
#     app.add_handler(myHandler)

# import psutil

# print(psutil.virtual_memory())


# message = "  "

# if (len(message) / 4096) >= 1:
#     for i in range(int(float(len(message) / 4096))):
#         for message in message[i:i+4096]:
#             i = i + 4096
#             await app.send_message(chat_id, message)
# else:
#     await app.send_message(chat_id, message)


# print((len(message) / 4096) >= 1)


# import pytz
# import os, psutil
# # for t in pytz.all_timezones:
# #     print(t)
# def get_size(bytes, suffix="B"):
#     factor = 1024
#     for unit in ["", "K", "M", "G", "T", "P"]:
#         if bytes < factor:
#             return f"{bytes:.2f}{unit}{suffix}"
#         bytes /= factor

# process = psutil.Process(os.getpid())
# print(get_size(process.memory_info().rss))


# import re

# msg = '''hElp_12524'''
# # regex = r'^[\/\#\!\.]?help *(?:[\n\s]*)(.*)'
# # regex = r'^[\/\#\!\.\](runner) *(?:[\n\s]*)(.*)$'
# regex = r'^help_(.*)'
# print(re.findall(regex, msg, re.U|re.S|re.I)[0])
import os, shutil
path = 'test.py'
f_name = os.path.basename(path)
print(shutil.move(path, 'queue/' + f_name))
