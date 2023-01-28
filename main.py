import yaml
from yaml import Loader
from src.decide import Decide


def main():
    inputFile = open('input.yml', 'r')
    input = yaml.load(inputFile, Loader=Loader)
    Decide(input).decide()

if __name__=="__main__":
    main()
