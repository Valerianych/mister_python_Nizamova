def send_welcome(user_email, client):
    message = "Welcome"
    client.send(user_email, message)
    return True


def send_safe(user_email, client):
    try:
        client.send(user_email, "Welcome")
        return "sent"
    except RuntimeError:
        return "error"
