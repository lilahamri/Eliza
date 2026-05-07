import discord

# Noms des rôles considérés comme professeur
TEACHER_ROLES = ["professeur", "profeseur", "teacher", "prof", "admin", "administrateur", "staff", "Professeur"]

def is_teacher(member) -> bool:
    if not isinstance(member, discord.Member):
        return False
    
    for role in member.roles:
        if role.name.lower() in TEACHER_ROLES:
            return True
    return False

def get_teacher_roles_list() -> list:
    return TEACHER_ROLES.copy()

def add_teacher_role(role_name: str):
    if role_name.lower() not in TEACHER_ROLES:
        TEACHER_ROLES.append(role_name.lower())

def remove_teacher_role(role_name: str):
    if role_name.lower() in TEACHER_ROLES:
        TEACHER_ROLES.remove(role_name.lower())