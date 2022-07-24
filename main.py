import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='$', help_command=None)

#If you ever get a discord request error, run kill 1 in the shell and it should fix it


@bot.event
async def on_ready():
    print("We logged in as {0.user}".format(bot))


@bot.command(name="problem")
async def problem(ctx):

    question = ctx.message.content[len('$problem'):].strip()
    mode = ctx.message.content.split()[-1]
    question = question.strip(mode)
    dm = await ctx.author.create_dm()

    if mode in ctx.message.content:
        if mode == "easy":
            with open('questions/easy.txt', 'a') as f:
                f.write(question + '\n\n')
            await ctx.send(f"New {mode} question added!")
        if mode == "medium":
            with open('questions/medium.txt', 'a') as f:
                f.write(question + '\n\n')
            await ctx.send(f"New {mode} question added!")
        if mode == "hard":
            with open('questions/hard.txt', 'a') as f:
                f.write(question + '\n\n')
            await ctx.send(f"New {mode} question added!")

        embed = discord.Embed(
            title="Thank You!",
            description=
            "Thank you for adding a question! It is very beneficial to other's because they are able to look at your question and solve it! This then helps then grow in their coding skills! Have fun learning!",
            color=discord.Color.blue())
        await dm.send(embed=embed)


@bot.command(name="q")
async def q(ctx):
    questions = ""
    difficulty = ctx.message.content.split()[-1]
    if difficulty == "easy":
        with open(f'questions/{difficulty}.txt', 'r') as f:
            for line in f:
                questions += line

                embed = discord.Embed(title="Easy Problems To Solve",
                                      description=questions,
                                      color=discord.Color.blue())
            await ctx.send(embed=embed)

    if difficulty == "medium":
        with open(f'questions/{difficulty}.txt', 'r') as f:
            for line in f:
                questions += line

                embed = discord.Embed(title="Medium Problems To Solve",
                                      description=questions,
                                      color=discord.Color.blue())
            await ctx.send(embed=embed)

    if difficulty == "hard":
        with open(f'questions/{difficulty}.txt', 'r') as f:
            for line in f:
                questions += line

                embed = discord.Embed(title="Hard Problems To Solve",
                                      description=questions,
                                      color=discord.Color.blue())
            await ctx.send(embed=embed)


@bot.command(name="help")
async def help(ctx):
    embed = discord.Embed(title="Python Bot Commands",
                          description="",
                          color=discord.Color.blue())

    embed.set_footer(
        text=
        "Remember to specify the difficulty of your problem when using `problem` or `q`"
    )
    embed.add_field(name="Commands", value="`problem`, `q`, `help`")
    embed.add_field(name="Difficulties", value="`easy`, `medium`, or `hard`")
    await ctx.send(embed=embed)


keep_alive()
bot.run(os.getenv('token'))
