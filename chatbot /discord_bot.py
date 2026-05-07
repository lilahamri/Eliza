import discord
from config import DISCORD_TOKEN
from roles import is_teacher, TEACHER_ROLES, add_teacher_role, remove_teacher_role
from history import reset_history
from lm import ask_lm_studio

# Configuration Discord
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("=" * 50)
    print(f"✅ Bot Discord prêt : {client.user}")
    print(f"👨‍🏫 Rôles professeurs reconnus : {TEACHER_ROLES}")
    print("🤖 Le bot répond à tous les messages")
    print("=" * 50)

@client.event
async def on_member_join(member):
    for channel in member.guild.text_channels:
        if channel.name in ("général", "general", "bienvenue", "welcome"):
            await channel.send(f"Bienvenue {member.mention} ! 👋 Envoie-moi un message, je te répondrai ! 📚")
            break

@client.event
async def on_message(message):
    # Ignorer les messages du bot lui-même
    if message.author == client.user:
        return

    content = message.content.strip()
    content_lower = content.lower()

    # Salutations
    if content_lower in ("bonjour", "salut", "hello", "coucou", "cc", "slt", "cava", "ca va"):
        await message.channel.send(f"Bonjour {message.author.mention} ! 👋 En quoi puis-je t'aider ?")
        return
    
    # !examen
    if content_lower == "!examen":
        await message.channel.send(f"📝 {message.author.mention} Quel sujet veux-tu pour ton examen ? (maths, français, histoire, etc.)")
        return

    # !exercice
    if content_lower == "!exercice":
        await message.channel.send(f"📚 {message.author.mention} Quel sujet veux-tu pour ton exercice ? (maths, français, histoire, etc.)")
        return
    
    # !reset
    if content_lower == "!reset":
        reset_history(message.author.id, is_teacher(message.author))
        await message.channel.send(f"🔄 {message.author.mention} Conversation réinitialisée !")
        return

    # !mode
    if content_lower == "!mode":
        if is_teacher(message.author):
            await message.channel.send(f"👨‍🏫 {message.author.mention} Tu es en **mode Professeur**")
        else:
            await message.channel.send(f"👨‍🎓 {message.author.mention} Tu es en **mode Élève**")
        return

    # !roles
    if content_lower == "!roles":
        roles_list = ", ".join(TEACHER_ROLES)
        await message.channel.send(f"📋 **Rôles professeurs reconnus :** `{roles_list}`")
        return

    # !aide
    if content_lower == "!aide":
        if is_teacher(message.author):
            await message.channel.send(
                "📖 **Commandes Professeur :**\n"
                "`!examen` — Génère un examen avec corrigé\n"
                "`!exercice` — Génère un exercice avec corrigé\n"
                "`!reset` — Réinitialise la conversation\n"
                "`!mode` — Affiche ton mode\n"
                "`!roles` — Liste des rôles professeurs\n"
                "`!aide` — Affiche cette aide\n\n"
                "💬 Envoie-moi n'importe quelle question scolaire !"
            )
        else:
            await message.channel.send(
                "📖 **Commandes Élève :**\n"
                "`!examen` — Génère un quiz d'entraînement\n"
                "`!exercice` — Génère un exercice guidé\n"
                "`!reset` — Réinitialise la conversation\n"
                "`!mode` — Affiche ton mode\n"
                "`!aide` — Affiche cette aide\n\n"
                "💬 Envoie-moi n'importe quelle question scolaire !"
            )
        return

    # Commandes admin
    if hasattr(message.author, 'guild_permissions') and message.author.guild_permissions.administrator:
        if content_lower.startswith("!addrole"):
            parts = content.split()
            if len(parts) >= 2:
                add_teacher_role(parts[1])
                await message.channel.send(f"✅ Rôle `{parts[1]}` ajouté à la liste des professeurs !")
            else:
                await message.channel.send("❌ Utilisation: `!addrole nom_du_role`")
            return
        
        if content_lower.startswith("!removerole"):
            parts = content.split()
            if len(parts) >= 2:
                remove_teacher_role(parts[1])
                await message.channel.send(f"✅ Rôle `{parts[1]}` retiré de la liste des professeurs !")
            else:
                await message.channel.send("❌ Utilisation: `!removerole nom_du_role`")
            return

    # Ignorer les messages trop courts
    if len(content) < 2:
        return
    
    # Ignorer les commandes non reconnues qui commencent par !
    if content.startswith('!'):
        return
    
    teacher_mode = is_teacher(message.author)
    
    async with message.channel.typing():
        response = await ask_lm_studio(message.author.id, content, teacher_mode)
    
    if teacher_mode:
        await message.channel.send(f"👨‍🏫 **Professeur** {message.author.mention}\n{response}")
    else:
        await message.channel.send(f"👨‍🎓 **Élève** {message.author.mention}\n{response}")

def run_bot():
    """Lance le bot Discord"""
    client.run(DISCORD_TOKEN)