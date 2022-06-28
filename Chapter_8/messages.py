def text_messages(messages):
    """Make a list containg a series of short text messages.  Pass the list to a function called show_messages(), which prints each message."""
    for message in messages:
        msg = f"\n{message.title()}."
        print(msg)


usernames = ['Hello', 'Have a great day', 'Goodbye']
text_messages(usernames)

unsent_messages = ['Help!', 'SOS', 'Mayday!']
sent_messages = []

while unsent_messages:
    current_messages = unsent_messages.pop()
    print(f"Sending message: {current_messages}")
    sent_messages.append(current_messages)

print("\nThe following messages have been sent:")
for sent_message in sent_messages:
    print(sent_message)
