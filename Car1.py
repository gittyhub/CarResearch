from urllib2 import urlopen

default = 'audi/s4/2012:2015'

ti = 'Trade-in: '
pp = 'Private Party: '
dr = 'Dealer Retail: '

name = raw_input('What car you want to research, please use this format, make/model/year? \n'+ 'Example, audi/s4/2012:2015 \n') or default 

edmund_url = 'http://www.edmunds.com/'+name+'/tmv-appraise-results.html'
html = urlopen(edmund_url).read()

def year(x):
  a1 = [] 		#creates  an empty list
  a=x.rsplit('/',1)[1]  #reverse splits x, on the last backslash, and takes the position 1
  a=a.split(':') 	#from the above is where to split the year 1999:2003, this splits on :
  for i in a:		
    a1.append(int(i))
  a = range(a1[0],a1[1])
  return(a)

def get_all_page(x):
  edmund_url = 'http://www.edmunds.com/'+name+'/tmv-appraise-results.html'
  y = year(x)		#gets the year range we want 1999:2003
  x = x.rsplit('/',1)[0]#this gets the make and model for usd
  for i in y:
    edmund_url = 'http://www.edmunds.com/'+x+'/'+str(i)+'/tmv-appraise-results.html'
    html = urlopen(edmund_url).read()
    f = open("edmund.html",'w')
    f.write(html)
    
    print(i) 
    print(edmund_url)
    trade_in = html.find('Trade-in')
    price = html.find("$", trade_in)
    ti_price = html[price:price+7]
    print(ti+'     '+ti_price+'\t')
    #i.append(ti_price)

    private_party = html.find('Private Party')
    price = html.find("$", private_party)
    pp_price = html[price:price+7]
    print(pp+pp_price+'\t')
    #i.append(pp_price)

    dealer_trade = html.find('Dealer Retail')
    price = html.find("$", dealer_trade)
    dt_price = html[price:price+7]
    print(dr+dt_price+'\t')
    #i.append(dt_price)

f = open("edmund.html",'w')
f.write(html)
f.close()


'''trade_in = html.find('Trade-in')
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
print(dr+car_price)'''

#print(year(name))

get_all_page(name)
