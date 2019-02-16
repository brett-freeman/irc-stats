log = open("./eggdrop/420.log.2017-02-10", "r")

for line in log:
    # Separate out the timestamp since it is the first 10 characters in every line
    timestamp = line[1:9]

    # Determine whether this is a message or something else
    if line[11] == '<':
        # Grab the nickname that sent the message
        nickname = line.split(" ")[1].strip("<>")

        # Grab the message the user sent
        message = line.split(" ", 2)[2]

        # Convert to IRSSI format
        converted = timestamp + " < " + nickname + "> " + message

        print(converted)