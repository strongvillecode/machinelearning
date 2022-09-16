#! /usr/bin/python3
from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
	n = random,choice([hp, code, zombie, hungergames])
	n.madlib()
