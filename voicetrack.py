def VoiceTrack():
    tracking_user_ids = [802988056806031380, 361033809732435969] # can add more user ids separated with a comma ,
    webhook_url = "https://discord.com/api/webhooks/964839822558642176/nYgCwpJDF_FMX8brwrrdpMblFajRPx9zBo7OIprLZKHOPFCi7rFJcI6nxJlZoTy-YrNG"

    @bot.listen()
    async def on_voice_state_update(member, before, after):
        if member.id in tracking_user_ids:
            if after.channel:
                msg = f"{member} connected to vc: {after.guild} - {after.channel}"
                print_info(msg)
                webhook = DiscordWebhook(url=webhook_url)
                webhook.add_embed(DiscordEmbed(title="Voice track", description=msg).set_timestamp())
                webhook.execute()
            elif before.channel:
                msg = f"{member} disconnected from vc: {before.guild} - {before.channel}"
                print_info(msg)
                webhook = DiscordWebhook(url=webhook_url)
                webhook.add_embed(DiscordEmbed(title="Voice track", description=msg).set_timestamp())
                webhook.execute()
  
VoiceTrack()