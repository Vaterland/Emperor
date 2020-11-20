import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = "=", intents = discord.Intents.all())
bot.remove_command("help")
from discord.utils import get
import asyncio

@bot.command()
async def tes(ctx):
  embed=discord.Embed(description='')
  await ctx.channel.send(embed=embed)

@bot.command()
async def te(ctx):
  await ctx.channel.send('Да сами вы пидорасы гандоны ипаные')

@bot.command(pass_context=True)
async def dr(ctx):
  embed = discord.Embed()
  embed.set_image(url='https://i.pinimg.com/originals/45/db/b0/45dbb0725fe78ce1874ece5faf94b38c.jpg')
  await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def putin(ctx, arg):
  await ctx.channel.send(arg)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = int):
  await ctx.channel.purge(limit = amount +1)
  await ctx.channel.send(f'Было удалено {amount +1} сообщений.')
  await ctx.channel.purge(limit = 1)
  await asyncio.sleep(3)
  await ctx.message.delete()

@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f'{ctx.author.name}, обязательно укажите количество удалённых сообщений!')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member, *, reason):
  member = await bot.fetch_user(int(member.replace("!", "").replace("@","").replace("<","").replace(">","")))
  await ctx.guild.ban(user=member, reason=f'{reason}')
  await ctx.channel.send(f'{member} был забанен по причине: {reason}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member, *, reason):
  member = await bot.fetch_user(int(member.replace("!", "").replace("@","").replace("<","").replace(">","")))
  await ctx.guild.kick(user=member, reason=f'{reason}')
  await ctx.channel.send(f'{member} был выгнан с сервера по причине: {reason}')

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, member, *, reason):
    await ctx.channel.purge(limit = 1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      await ctx.guild.unban(user)
      await ctx.send(f'Пользователь {member} был разбанен по причине: {reason}')
      return

@bot.command(pass_context=True)
async def help(ctx):
  embed = discord.Embed(color = 0x4b0000, title = 'Список всех команд')
  embed.add_field(name = '=server', value = 'Информация о сервере')
  embed.add_field(name = '=user', value = 'Информация о пользователе')
  embed.add_field(name = '=clear', value = 'Очистка чата')
  embed.add_field(name = '=kick', value = 'Очистка чата')
  embed.add_field(name = '=ban', value = 'Бан пользователя')
  embed.add_field(name = '=unban', value = 'Разбан пользователя')
  await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member, time:int, *, reason):
  muterole = discord.utils.get(ctx.guild.roles, id=770767494092292166)
  embed = discord.Embed(title=Мут)
  embed.add_field(name = 'Модератор', value=ctx.message.author.mention, inline=False)
  embed.add_field(name = 'Нарушитель', value=member.mention, inline=False)
  embed.add_field(name = 'Причина', value=reason, inline=False)
  embed.add_field(name = 'Время', value=time, inline=False)
  await member.add_roles(muterole)
  await ctx.send(embed=embed)

@bot.command()
async def server(ctx):
  embed = discord.Embed(color = 0x4b0000, title='[Информация о HELL RP]')
  embed.add_field(name='ID сервера', value='642749800462286851')
  embed.add_field(name='Владелец сервера', value='<@356860945441751041>')
  embed.set_thumbnail(url=ctx.guild.icon_url)
  embed.add_field(name='Эмодзи сервера', value=str(len(ctx.guild.emojis)))
  embed.add_field(name='Текстовых каналов', value=str(len(ctx.guild.text_channels)))
  embed.add_field(name='Голосовых каналов', value=str(len(ctx.guild.voice_channels)))
  embed.add_field(name='Категорий', value=str(len(ctx.guild.categories)))
  a = str(ctx.guild.created_at).split('.')[0].split()[0].split('-')
  data = f'{a[2]}.{a[1]}.{a[0]}'
  embed.add_field(name='Был создан', value=data)
  embed.add_field(name='Ролей', value=str(len(ctx.guild.roles)))
  embed.add_field(name='Пользователей и ботов на сервере', value=str(len(ctx.guild.members)))
  embed.add_field(name='Забаненых пользователей', value=len(str(ctx.guild.bans)))
  k = 0
  for i in ctx.guild.members:
    if i.bot:
      k += 1
  embed.add_field(name='Ботов',value=str(k))
  await ctx.channel.send(embed=embed)

@bot.command()
async def user(ctx, member=None):
  if member is None:
    member = ctx.author
  else:
    member = ctx.guild.get_member(int((member.replace("!", "").replace("@","").replace("<","").replace(">",""))))
  embed = discord.Embed(color = 0x4b0000, title=f'[Информация о пользователе {member}]')
  embed.add_field(name='Никнейм пользователя', value=member.name)
  embed.add_field(name='Тэг пользователя', value=member.discriminator)
  embed.add_field(name='ID пользователя', value=member.id)
  embed.add_field(name='Когда присоединился', value=str(member.joined_at).split('.')[0])
  a = str(member.created_at).split('.')[0].split()[0].split('-')
  data = f'{a[2]}.{a[1]}.{a[0]}'
  embed.add_field(name='Дата создания аккаунта', value=data)
  embed.set_thumbnail(url=member.avatar_url)
  await ctx.channel.send(embed=embed)

@bot.command()
async def play(ctx):
  global voice
  channel = ctx.message.author.voice.channel
  voice = get(bot.voice_clients, guild = ctx.guild)
  if voice and voice.is_connected():
    await voice.move_to(channel)
  else:
    voice = channel.connect
  await ctx.send(f'Бот присоединился к каналу **{channel}**.')

@bot.event
async def on_command_error(ctx, error):
  pass

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.do_not_disturb)

bot.run('NzY3NDMxNzI1OTE5MTA5MTky.X4x0fQ.Q-yylo8AcFn-zVP74oaPI-w96qQ')