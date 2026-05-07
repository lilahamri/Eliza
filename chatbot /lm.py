import httpx
from config import LM_STUDIO_URL, STUDENT_MAX_TOKENS, TEACHER_MAX_TOKENS
from prompts import get_system_prompt
from history import get_history_dict

async def ask_lm_studio(user_id: int, question: str, is_teacher_mode: bool) -> str:
    
    history_dict = get_history_dict(user_id, is_teacher_mode)
    
    if user_id not in history_dict:
        system_prompt = get_system_prompt(is_teacher_mode)
        history_dict[user_id] = [{"role": "system", "content": system_prompt}]
    
    history_dict[user_id].append({"role": "user", "content": question})
    
    max_tokens = TEACHER_MAX_TOKENS if is_teacher_mode else STUDENT_MAX_TOKENS
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                LM_STUDIO_URL,
                json={
                    "model": "local-model",
                    "messages": history_dict[user_id],
                    "temperature": 0.7,
                    "max_tokens": max_tokens,
                }
            )
            
            if response.status_code != 200:
                return f"❌ Erreur LM Studio: {response.status_code}"
            
            result = response.json()
            reply = result["choices"][0]["message"]["content"]
            
            history_dict[user_id].append({"role": "assistant", "content": reply})
            
            if len(reply) > 1900:
                reply = reply[:1900] + "..."
            
            return reply
            
    except httpx.ConnectError:
        return " Impossible de se connecter à LM Studio. Vérifie que le serveur est lancé."
    except httpx.TimeoutException:
        return "❌ Délai d'attente dépassé. Le modèle met trop de temps à répondre."
    except Exception as e:
        return f"❌ Erreur : {str(e)}"