# Basic Hello World program in python to test out git commiting.
print("Hello!, Hola!, 你好, Ola!")
print("Let me tell you a story:")

# Reads and parses WagonTrip.txt into an interactive story.
def main():
    player_score = 0
    file = open('WagonTrip.txt', 'r')
    story = file.readlines()

    output = True # True if lines from story should be printed to console.
    choice = '' # User given options for the story branches.
    i = 0 # Index of the loop, or line # within the text file.

    while i < len(story):
        line = story[i]

        # Logic for parsing the file,
        if line[0] == '*': # * indicates a user prompt.
            print("!!-------------------------------------------!!")
            choice = input(line.strip('*')).lower()
            print(">>------------------------------------------->>")

        elif line[0] == '#': # # indicates an option branch.
            if line.strip('# \n') == choice or line.strip('# \n') == '!':
                output = True
            elif output:
                output = False

        elif output:
            if line[0] == '@': # @ indicates a line-jump.
                i = int(line.strip('@'))
                output = True
            else:
                print(line)

        i += 1

    file.close()
    print("Thank you for playing!")

main()
