from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = "https://discord.com/api/webhooks/1184788603470090320/jqkYHRC-y7P920AYLdB1e08g1WPLWzIcelEssk1tG23VXXE2kvgsNUQUhg5q7fYZ86hU"


webhook = DiscordWebhook(url=webhook_url)

# create embed object for webhook
embed = DiscordEmbed(title="Checkpoint",
                     description="Script terminated... check terminal", color="03b2f8")

# set author
embed.set_author(name="Il bro Ferretty")

# set footer
embed.set_footer(text="TCP?")

# set timestamp (default is now) accepted types are int, float and datetime
embed.set_timestamp()

# add embed object to webhook
webhook.add_embed(embed)
response = webhook.execute()
