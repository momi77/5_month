from django.core.cache import cache

def save_confirmation_code(user_id: int, code: str):
    key = f"confirmation_code:{user_id}"
    cache.set(key, code, timeout=300)  # Сохраняем на 5 минут (300 секунд)

def check_and_delete_confirmation_code(user_id: int, code: str) -> bool:
    key = f"confirmation_code:{user_id}"
    saved_code = cache.get(key)
    if saved_code is None:
        return False  
    if saved_code != code:
        return False
    cache.delete(key)
    return True 
