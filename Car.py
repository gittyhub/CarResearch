from urllib2 import urlopen

edmund_url = "http://www.edmunds.com/audi/q7/2014/tmv-appraise-results.html"

html = urlopen(edmund_url).read()
dealer_trade = html.find("Dealer Retail")
print(dealer_trade)
print(html[dealer_trade:dealer_trade+85])

