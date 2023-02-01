import yaml

from main.decide import Decide


def main():
    with open("tests/input/positiveInput.yml", 'r') as f:
        input = yaml.safe_load(f)
    if Decide(input).decide() is True:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    main()
