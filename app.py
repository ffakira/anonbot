import discord
import json
import random

with open("config.json") as json_file:
	config = json.load(json_file)

client = discord.Client()


@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("!pin"):
		await message.channel.send(":pushpin: You have attempted to pin this message")

	if message.content.startswith("!test"):
		embed = discord.Embed(title="Current Admins and Moderators", description="Please don't send a DM to our fellow admins", color=0xFF00FF)
		embed.add_field(name="Photons", value="Just a dev.", inline=True)
		embed.add_field(name="Siggi", value="CubeBuilders\' owner", inline=True)
		embed.add_field(name="Keita", value="\u200b", inline=True)
		# embed.add_field(name="This is a test #2", value="This is nother hello", inline=False)
		await message.channel.send(embed=embed)

	if message.content.startswith("!lottery"):
		get_lotery = random.sample(range(1, 51), 6)
		temp_str = []
		get_lotery.sort()
		for i in get_lotery:
			temp_str.append(str(i))
		get_lotery = ' '.join(temp_str)
		await message.channel.send("Lotery generated: %s" % (get_lotery))
	
	# @todo: temporary debugging
	if message.content.startswith("!q"):
		await client.logout()

client.run(config["token"])