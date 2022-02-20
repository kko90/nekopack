from telethon import TelegramClient
import logging
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon import connection
from telethon import events
from telethon import utils
import asyncio
from telethon.tl.types import InputChannel
import aiocron
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.utils import pack_bot_file_id
import telethon
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest
import random
from telethon.tl.functions.photos import UploadProfilePhotoRequest ,DeletePhotosRequest
from telethon import functions ,types
from telethon.tl.functions.messages import DeleteMessagesRequest
import time
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel,InputMediaPoll, Poll, PollAnswer
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest
import json






len_message = []
len_remove = []
list_check = []

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
	level = logging.INFO)
logger = logging.getLogger(__name__)

started = []
admin_list = [879124022,1157849197]

admin_master = 879124022

api_id = 1710507

api_hash = 'a962c251bad15eafdb74d267b6d2eca7'

phone_number = '+989031601172'

client = TelegramClient(
	'dr', 
	api_id, 
	api_hash )

client.start()
client.parse_mode = "html"

def creat_database():
    try:
        channel_join = open("channel.json","x")
        edit_database = open("channel.json","a+")
        edit_database.write(json.dumps({"channel_id":"None","len_spam":"None","remove":"None"}))
        edit_database.close()
    except:
        pass

creat_database()

@aiocron.crontab('*/1 * * * *')
async def clear_list():
    len_message.clear()
    len_remove.clear()

@client.on(events.NewMessage(from_users = admin_list,pattern="-add"))
async def add_admin(event):
    database = open(f"channel.json","r")
    read_database = json.loads(database.read())
    channeL_id = read_database.get('channel_id')

    if channeL_id == "None":
        await event.reply("شما چنلی تنظیم نکردید\nبرای تنظیم چنل از دستور :\n-set + idchannel\nنمونه :\n-set -145445212145")
    else:
        try:
            get_id = int((event.raw_text).split(" ")[1])
            
            await client(functions.channels.EditAdminRequest(int(channeL_id),get_id,admin_rights=types.ChatAdminRights(post_messages=True),rank='some string here'))
            await event.reply("با موفقیت ادمین شد")
        except ValueError as e:
            await event.reply("چت آیدی اشتباه وارد شده است و یا کاربر داخل کانال عضو نیست و یا کانال اشتباه ست شده است")
        except telethon.errors.rpcerrorlist.ChatAdminRequiredError:
            await event.reply("من داخل تنظیم شده ادمین نیستم")
        except TypeError:
             await event.reply("چت آیدی اشتباه وارد شده است و یا کاربر داخل کانال عضو نیست و یا کانال اشتباه ست شده است")
        except :
            await event.reply("چت ایدی وارد شده نامعتبر است")
@client.on(events.NewMessage(from_users = admin_list,pattern="-sick"))
async def sick_admin(event):
    database = open(f"channel.json","r")
    read_database = json.loads(database.read())
    channeL_id = read_database.get('channel_id')
    if channeL_id == "None":
        await event.reply("شما چنلی تنظیم نکردید\nبرای تنظیم چنل از دستور :\n-set + idchannel\nنمونه :\n-set -145445212145")
    else:
        try:
            get_id = int((event.raw_text).split(" ")[1])
            await client(functions.channels.EditAdminRequest(int(channeL_id),get_id,admin_rights=types.ChatAdminRights(),rank='some string here'))
            await event.reply("با موفقیت صیک شد")
        except ValueError:
            await event.reply("چت آیدی اشتباه وارد شده است و یا کاربر داخل کانال عضو نیست و یا کانال اشتباه ست شده است")
        except telethon.errors.rpcerrorlist.ChatAdminRequiredError:
            await event.reply("من داخل تنظیم شده ادمین نیستم")
        except TypeError:
             await event.reply("چت آیدی اشتباه وارد شده است و یا کاربر داخل کانال عضو نیست و یا کانال اشتباه ست شده است")
        except :
            await event.reply("چت ایدی وارد شده نامعتبر است")
        
@client.on(events.NewMessage(from_users = admin_list,pattern="-set"))
async def set_channel(event):
    try:
        channel_id = int((event.raw_text).split(" ")[1])
        database = open(f"channel.json","r")
        read_database = json.loads(database.read())
        spam = read_database.get("len_spam")
        remove = read_database.get("remove")
        edit_database = open("channel.json","w")
        edit_database.write(json.dumps({"channel_id":f"{channel_id}","len_spam":spam,"remove":remove}))
        edit_database.close()
        await event.reply(f"چنل با موفقیت تنظیم شد\n{channel_id}")
    except ValueError:
        await event.reply("فقط عدد مورد قبول است")
    
@client.on(events.NewMessage(from_users = admin_list,pattern="-spam"))
async def set_channel(event):
    try:
        spam_len = int((event.raw_text).split(" ")[1])
        database = open(f"channel.json","r")
        read_database = json.loads(database.read())
        channel_id = read_database.get("channel_id")
        remove = read_database.get("remove")
        edit_database = open("channel.json","w")
        edit_database.write(json.dumps({"channel_id":channel_id,"len_spam":spam_len,"remove":remove}))
        edit_database.close()
        await event.reply(f"تعداد اسپم با موفقیت تنظیم شد\n{spam_len}")
    except ValueError:
        await event.reply("فقط عدد مورد قبول است")
    
@client.on(events.NewMessage(from_users = admin_list,pattern="-remove"))
async def set_channel(event):
    try:
        remove = int((event.raw_text).split(" ")[1])
        database = open(f"channel.json","r")
        read_database = json.loads(database.read())
        channel_id = read_database.get("channel_id")
        spam_len = read_database.get("len_spam")
        edit_database = open("channel.json","w")
        edit_database.write(json.dumps({"channel_id":channel_id,"len_spam":spam_len,"remove":remove}))
        edit_database.close()
        await event.reply(f"تعداد حذف ممبر با موفقیت تنظیم شد\n{remove}")
    except ValueError:
        await event.reply("فقط عدد مورد قبول است")
    
@client.on(events.NewMessage(from_users = admin_list,pattern="-status"))
async def set_channel(event):
    
    database = open(f"channel.json","r")
    read_database = json.loads(database.read())
    channel_id = read_database.get("channel_id")
    spam = read_database.get("len_spam")
    remove = read_database.get("remove")
    await event.reply(f"channel id : {channel_id}\nlen spam : {spam}\nlen remove : {remove}")    

@client.on(events.NewMessage())
async def handler(event): 
    if event.is_channel:
        database = open(f"channel.json","r")
        read_database = json.loads(database.read())
        channel_id = read_database.get("channel_id")
        spam = read_database.get("len_spam")
        
        if channel_id != "None" and event.chat_id == int(channel_id) and spam != "None":
            channel_id = int(channel_id)
            len_message.append(event.message.id)
            if len(len_message) == int(spam):
                list_admin_group = []
                async for i in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
                    list_admin_group.append((i).id)
                for i in list_admin_group:               
                    try:
                        await client(functions.channels.EditAdminRequest(int(channel_id),i,admin_rights=types.ChatAdminRights(),rank='some string here'))
                    except telethon.errors.rpcerrorlist.UserIdInvalidError:
                        pass
                    except telethon.errors.UserCreatorError:
                        pass
                await client(functions.channels.DeleteMessagesRequest(channel=channel_id,id=len_message))
                len_message.clear()
                await client.send_message(admin_master,"یه نفر اسپم زد همه رو ریمو کردم")

@client.on(events.NewMessage(from_users=admin_list,pattern="-rem-one"))
async def while_true(event):
        database = open(f"channel.json","r")
        read_database = json.loads(database.read())
        channel_id = read_database.get("channel_id")
        if len(list_check) == 0 and channel_id != "None":
            
            list_check.append(1)
            await event.reply("ضد اسپم شروع شد")
            while True:
                database = open(f"channel.json","r")
                read_database = json.loads(database.read())
                channel_id = read_database.get("channel_id")
                remove = read_database.get("remove")
                async for event in client.iter_admin_log(int(channel_id),ban=True,limit=1):
                    if event.id not in len_remove:
                        len_remove.append(event.id)
                if remove != "None" and len(len_remove) >= int(remove)+1:
                    list_admin_group = []
                    async for i in client.iter_participants(int(channel_id), filter=ChannelParticipantsAdmins):
                        list_admin_group.append((i).id)
                    for i in list_admin_group:               
                        try:
                            await client(functions.channels.EditAdminRequest(int(channel_id),i,admin_rights=types.ChatAdminRights(),rank='some string here'))
                        except telethon.errors.rpcerrorlist.UserIdInvalidError:
                            pass
                        except telethon.errors.UserCreatorError:
                            pass
                        except telethon.errors.rpcerrorlist.ChatAdminRequiredError:
                            pass
                    len_remove.clear()
                    await client.send_message(admin_master,"یه نفر ممبر حذف کرد همه رو ریمو کردم")
                await asyncio.sleep(1)
                list_check.clear()
                list_check.append(1)
        else:
            await event.reply("این فرایند از قبل استارت شده است")
    

clear_list.start()
asyncio.get_event_loop().run_forever()

client.run_until_disconnected()


connected()


