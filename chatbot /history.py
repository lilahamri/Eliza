student_conversation_history: dict[int, list[dict]] = {}
teacher_conversation_history: dict[int, list[dict]] = {}

def get_history_dict(user_id: int, is_teacher_mode: bool) -> dict[int, list[dict]]:
    return teacher_conversation_history if is_teacher_mode else student_conversation_history

def get_history(user_id: int, is_teacher_mode: bool) -> list[dict]:
    history_dict = get_history_dict(user_id, is_teacher_mode)
    return history_dict.get(user_id, [])

def init_history(user_id: int, is_teacher_mode: bool, system_prompt: str):
    history_dict = get_history_dict(user_id, is_teacher_mode)
    if user_id not in history_dict:
        history_dict[user_id] = [{"role": "system", "content": system_prompt}]

def add_to_history(user_id: int, is_teacher_mode: bool, role: str, content: str):
    history_dict = get_history_dict(user_id, is_teacher_mode)
    if user_id not in history_dict:
        return
    history_dict[user_id].append({"role": role, "content": content})
##
def reset_history(user_id: int, is_teacher_mode: bool):
    history_dict = get_history_dict(user_id, is_teacher_mode)
    history_dict.pop(user_id, None)