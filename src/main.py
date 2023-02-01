import yaml

from main.src.decide import Decide


def main():
    with open("tests/input/input.yml", 'r') as f:
        input = yaml.safe_load(f)
    if Decide(input).decide() is True:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    main()
