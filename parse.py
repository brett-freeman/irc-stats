
log = open("./eggdrop/420.log.2017-02-10", "r")

for line in log:
    line = line.split(" ", 2)
    timestamp = line[0][1:9]
    nickname = line[1].strip("<").strip(">")
    if "<" not in line[1]:
        reason = line[2].split(":")[1][1:]
        converted = timestamp + " -!- " + nickname + " " + line[2].split(":")[0].replace("(", "[").replace(")", "]").replace("left irc:", "has quit") + " [" + reason + "]"
    else:
        converted = timestamp + " < " + nickname + "> " + line[2]

    print(converted)

