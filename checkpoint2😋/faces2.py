def main():
    emoji=input("Write a message with an emoticon: ")
    convert(emoji)

def convert(message):
    message = message.replace( ":)", "😊").replace( ":(", "🙁").replace( ";)", "😉").replace( ":P", "😋").replace( "B)", "😎").replace( ":3", "😗").replace( "XD", "😆").replace( ":/", "🫤")
    print(message)

main()