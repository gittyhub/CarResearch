from urllib2 import urlopen

default = 'audi/s4/2014'

name = raw_input('What car you want to research, please use this format, make/model/year? \n'+ 'Example, audi/s4/2014: \n') or default 

'''if not name:
  name =  
else:
  print("not empty")'''

edmund_url = 'http://www.edmunds.com/'+name+'/tmv-appraise-results.html'
html = urlopen(edmund_url).read()

f = open("edmund.html",'w')
f.write(html)
f.close()

ti = 'Trade-in: '
pp = 'Private Party: '
dr = 'Dealer Retail: '

trade_in = html.find('Trade-in')
price = html.find("$", trade_in)
car_price = html[price:price+7]
print(ti+'     '+car_price)

private_party = html.find('Private Party')
price = html.find("$", private_party)
car_price = html[price:price+7]
print(pp+car_price)

dealer_trade = html.find('Dealer Retail')
price = html.find("$", dealer_trade)
car_price = html[price:price+7]
print(dr+car_price)

