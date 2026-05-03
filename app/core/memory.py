SESSION_MEMORY = {}

def save_session(session_id, data):
    SESSION_MEMORY[session_id] = data

def get_session(session_id):
    return SESSION_MEMORY.get(session_id, {})