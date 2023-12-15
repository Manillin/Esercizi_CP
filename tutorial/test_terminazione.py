import time
import cv2
from discord_webhook import DiscordEmbed, DiscordWebhook

webhook_url = "https://discord.com/api/webhooks/1184788603470090320/jqkYHRC-y7P920AYLdB1e08g1WPLWzIcelEssk1tG23VXXE2kvgsNUQUhg5q7fYZ86hU"
try:
    l = []
    print('a')
    time.sleep(2)
    l[5] = 'ciao'
    print('\n\n\na')
except Exception as e:
    print(f"Errore: {e}")
    # Invia il webhook
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="ID",
                         description=f"Errore: {e}", color="ff0000")
    embed.set_author(name="Il bro Ferretty")
    embed.set_footer(text="TCP?")
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    # Termina lo script

    '''
    Ampliamento del bot:

    -Discord webhook per eccezioni -> check
    -Discord webhook per statistiche:
        .dopo n iterazioni: (elapsed time, punteggio, vantaggio in minuti, numero di iterazioni )
        .dopo n ore di gioco gentle termination con script endgame
        .postendgame webhook con stats sulla partita, simile al primo punto 
    -macro per farlo ripartire e iniziare una nuova partita dopo un timeout 
        .gestire il caso in cui la partita fallisca 
        .comunicare se la partita inizia correttamente
    
    
    
    '''
