import pync


def send_notification():
    title = input("What should be the title?")
    message = input("What should be the message?")
    pync.notify(message=message, title=title)
