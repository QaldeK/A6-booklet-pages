#!/usr/bin/env python3

import subprocess


class A6():
    """docstring for A6"""

    def __init__(self):

        self.allPages = []
        aa = a = b = c = d = 0

        what = input("What ? \n => couv only (c), txt only (t), all (a) ? : ")

        if what == "t":
            aa = input("how many page ? (Must be a multiple of 4): ")
            a = int(aa) - 1
            b = 2
            c = a
            d = b
            self.AllText(aa, a, b, c, d)

        elif what == "c":
            aa = input("how many page ? : ")
            a = int(aa) + 1
            b = 0
            c = a
            d = b
            self.Couv(aa, a, b, c, d)

        else:
            aa = input("how many page ? : ")
            a = int(aa) + 1
            b = 0
            c = a
            d = b 
            self.AllText(aa, a, b, c, d)

    def AllText(self, aa, a, b, c, d):
        while (b * 2) < int(aa):
            a -= 1
            b += 1
            c = a - 1
            d = b + 1

            pages = a, b, a, b, d, c, d, c,
            a = c
            b = d

            self.allPages.append(pages)

        pagesOrder = str(self.allPages)
        self.result(pagesOrder)

    def Couv(self, aa, a, b, c, d):
        while b < 2:
            a -= 1
            b += 1
            c = a - 1
            d = b + 1

            pages = a, b, a, b, d, c, d, c,
            self.allPages.append(pages)

            a = c
            b = d


        pagesOrder = str(self.allPages)
        self.result(pagesOrder)


    def result(self, pagesOrder):

        pagesOrder = pagesOrder.replace('(', '') 
        pagesOrder = pagesOrder.replace(')', '')
        pagesOrder = pagesOrder.replace('[', '')
        pagesOrder = pagesOrder.replace(']', '')

        print(pagesOrder + '\n')

        self.copy2clip(pagesOrder)

        print("all is in your copyboard, use ctrl + v for paste it !")

        self.__init__()
        
    def copy2clip(self, pagesOrder):
        ''' depend of clipit : sudo apt install clipit '''

        cmd = "clipit " + pagesOrder
        return subprocess.check_call(cmd, shell=True)


A6()