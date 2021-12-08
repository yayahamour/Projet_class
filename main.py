from dataclasses import dataclass
import os

@dataclass
class eff():
    erg : int

def main():
    string = "zeeazrzrzer"
    for i in range(0,len(string)):
        os.system('cls')
        print(string[:i])

print(eff(""))