def text_messages(show_messages):
    """Make a list containg a series of short text messages.  Pass the list to a function called show_messages(), which prints each message."""
    for message in show_messages:
        msg = f"\nHello! It's nice to meet you {message.title()}."
        print(msg)


usernames = ['Tyler', 'Patrick', 'Brittni']
text_messages(usernames)

unsent_messages = ['Help!', 'SOS', 'Mayday!']
sent_messages = []

while unsent_messages:
    current_messages = unsent_messages.pop()
    print(f"Sending message: {unsent_messages}")
    sent_messages.append(unsent_messages)

print("\nThe following messages have been sent:")
for sent_message in sent_messages:
    print(sent_message)
