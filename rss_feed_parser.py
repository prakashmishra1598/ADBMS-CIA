"""
Documentation : This module parses the XML document retrieved 
                by rss_feed_download.py to display news content

"""
import time
import os
import rss_feed_download
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

print("Downloading rss feed data...Please wait\n\n")

tree = ET.ElementTree(file='news_tech.xml')
root = tree.getroot()

titles = [] #List of titles
links = [] #List of corresponding links to titles
descriptions = [] #List of news descriptions

def getTitles(root):
    """
    Retrieves news titles
    """
    for content in root.findall('.//channel/item/title'):
        titles.append(content.text)

def getLinks(root):
    """
    Retrieves news links
    """
    for content in root.findall('.//channel/item/link'):
        links.append(content.text)

def getDescriptions(root):
    """
    Retrieves news Descriptions
    """
    for content in root.findall('.//channel/item/description'):
        descriptions.append(content.text)

def showTitles():
    """
    Prints titles in the document
    """
    getTitles(root)
    for i in range(0,len(titles)):
        print("{0}. {1}".format((i+1),titles[i]))

def showLinks():
    """
    Prints links to news articles in the document
    """
    getLinks(root)
    for i in range(len(links)):
        print("{0}. {1}".format((i+1),links[i]))

def showDescriptions():
    """
    Prints description of news articles in the document
    """
    getDescriptions(root)
    for i in range(len(descriptions)):
        print("{0}. {1}".format((i+1),descriptions[i]))

def showAll():
    """
    Prints detailed news from the document
    """
    getTitles(root)
    getLinks(root)
    getDescriptions(root)
    for i in range(0,len(titles)):
        print("\t\t\t\t{0}. \nTitle: {1}\nLink: {2}\nDesription: {3}".format((i+1),titles[i],links[i],descriptions[i]))

def main():
    while(True):
       
        os.system("clear")

        print("1. Print all news titles")
        print("2. Print all news links")
        print("3. Print all news descriptions")
        print("4. Print detailed news")
        print("5. Exit")
        
        choice = int(input("Enter your choice:"))
        
        if ((choice > 5) or (choice<1)):
            print("**********Invalid choice**********")
        elif (choice == 1):
            showTitles()
            time.sleep(3)
        elif (choice == 2):
            showLinks()
            time.sleep(3)
        elif (choice == 3):
            showDescriptions()
            time.sleep(3)
        elif (choice == 4):
            showAll()
            time.sleep(8)
        elif (choice == 5):
            print("Exiting....")
            sys.exit(0)  

if __name__ == main():
    main()
