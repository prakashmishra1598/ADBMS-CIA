"""
Documentation : This module retrieves rss feed of a website 
                in the form of a XML document

"""
import urllib.request
def downloadXml():
    """
    This function retrieves the xml document from the rss feed of 
    a website and saves it locally
    """
    url = "http://feeds.feedburner.com/gadgets360-latest"
    urllib.request.urlretrieve(url,'news_tech.xml')#Retrieve feed url and store it locally

downloadXml()
