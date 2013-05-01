#!/usr/bin/python
# -*- coding: utf-8 -*-


class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return "%s %s" % (self.value, other)

    def __getitem__(self, item):
        return self.value


cinco = Number(5)
print cinco + "Hermanos"

print cinco[10]