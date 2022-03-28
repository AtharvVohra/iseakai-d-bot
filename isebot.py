# Isekai'd playtest bot
import lightbulb
import math, sys, random
# might switch to numpy uniform dist or poisson/gaussian dis if clock time random lib is not good enough

DICE = [0, 1, 1, 1, 2, 2]

bot = lightbulb.BotApp(token='', default_enabled_guilds=(931625225672617984))

@bot.command
@lightbulb.command('summon', 'Summons bot')
@lightbulb.implements(lightbulb.SlashCommand)
async def summon_bot(context):
	await context.respond('IseBot has been summoned to another world')

@bot.command
@lightbulb.option('spice', 'number of spice dice to roll', type=int)
@lightbulb.option('substance', 'number of substance dice to roll', type=int)
@lightbulb.option('style', 'number of style dice to roll', type=int)
@lightbulb.command('roll', 'Rolls Isedice, enter number of dice rolled for sty/sub/spice')
@lightbulb.implements(lightbulb.SlashCommand)
async def roll_dice(context):
	stytotal = 0 
	subtotal = 0
	spitotal = 0
	for i in range(context.options.style):
		stytotal += random.choice(DICE)
	for i in range(context.options.substance):
		subtotal += random.choice(DICE)
	for i in range(context.options.spice):
		spitotal += random.choice(DICE)

	returnstring = 'Roll Results: '+str(stytotal)+' Style, '+str(subtotal)+' Substance, '+str(spitotal)+' Spice'
	await context.respond(returnstring)

bot.run()