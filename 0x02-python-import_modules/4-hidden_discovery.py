#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    definitions = dir(hidden_4)
    for i in range(0, len(definitions)):
        if definitions[i][0] != '_' and definitions[i][1] != '_':
            print(definitions[i])
