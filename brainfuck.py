from sys import stdin

def main(filepath):
    code, filterCode = [], filter(clean, list(open("filepath", "r").read()))
    for c in filterCode:
        code.append(c)
    data, dataPointer, codePointer, loopStart = [0], 0, 0, None

    while True:
        if code[codePointer] == ">":
            dataPointer += 1
            if dataPointer == len(data):
                data.append(0)

        elif code[codePointer] == "<":
            if dataPointer == 0:
                dataPointer = len(data)-1
            else:
                dataPointer -= 1

        elif code[codePointer] == "+":
            data[dataPointer] = 0 if data[dataPointer] >= 255 else data[dataPointer]+1

        elif code[codePointer] == "-":
            data[dataPointer] = 255 if data[dataPointer] <= 0 else data[dataPointer]-1

        elif code[codePointer] == ".":
            print(chr(data[dataPointer]), end="")

        elif code[codePointer] == ",":
            inp = stdin.readline()[0]
            data[dataPointer] = ord(inp)

        elif code[codePointer] == "[":
            loopStart = codePointer

        elif code[codePointer] == "]":
            if data[dataPointer] != 0:
                codePointer = loopStart

        else:
            print(f"An error has occured: Invalid command: {code[codePointer]}")

        codePointer += 1

        if codePointer == len(code):
            break


def clean(f):
    return True if f in ["+", "-", ">", "<", ".", ",", "[", "]"] else False

if __name__ == "__main__":
    main(str(input("File Path:\n>>")))
