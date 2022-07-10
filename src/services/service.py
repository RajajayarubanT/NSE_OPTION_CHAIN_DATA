import requests
import json

def findresult(symbol, date, strikeType, strikePrice) :

    if symbol :
        
        symbol = symbol or 'NIFTY'
        date = date or '02-06-2022'
        strikeType = strikeType or 'CE'
        strikePrice = strikePrice or '14300.00'
                
        url= 'https://www.nseindia.com/api/chart-databyindex?index=OPTIDX'+symbol+date+strikeType+strikePrice
        
        
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9',
            'referer': 'https://www.nseindia.com/option-chain',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'cookie': '_ga=GA1.2.1143612573.1638772468; nsit=mW7aSshD_H_vPK-FGMp9QtCs; ak_bmsc=BB3BB0D798E2B6598FD7180C342FF909~000000000000000000000000000000~YAAQN0s5F2tKAvCAAQAAph2eBg/jBdXjDkHecL5lr9SqRxb5Uy2A0zcWGR9JXmcJJLf9L5yObka348GbUdHslw13LqqXQi1pK6hP/Jehg2e/pq77IF25ZdMA90Vg5q+oPmfZNz3zFb4TjYDSCJ7i643rvqhkJxVDau8aNBsRPCjT/qLh+w5u/xhVZJZuILNpZi66KW1BSGA63Jla93i37duiNUXB17pBpT7JCRaK1/Hn6Jvq1ASkfBsVxXnWQoBJaHlIV6A+povtbNFSq/NPekpRVRkUpo8YI5jJUsLVV2QU96Y29Z+kpmtc4QyEz7s0q27T7/ZsGYYBD/DROE9gjLzJ364wzBObFCeu67fGHlTVN2sZ15V2BFnPilEAb1NnqvJiRNStfg2ymtiELfzmyLCzneugCO7y3fhDqiva8PSOrZd1Q5DF4iNNhBkU2wBsz0pJ8JbMO+cBWOM8Z1ZiTj7pJYNpnBdJyhokpEsNPjILlTTf6eX9S4QydA==; AKA_A2=A; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY1MzY3NDEwMSwiZXhwIjoxNjUzNjc3NzAxfQ.O36JQoul8zgbl9oj2Nf10r8_SC4EK60F-TYYiQzpgTk; bm_sv=3D0CDB89F3053D34A50667B78EC4C1E5~YAAQlzkgFwJDS/CAAQAAWFmoBg9TuvIIccrF0CG8qxQPROZK0YhkCO4+XUU2YN6hK+h+XqO3y7lGZTJy3Eu1QmxwjZJRNrN5IJZSIDHktz45bV0F44VOEzQ3qgZAl9Ubsy7TiOQ5A+KkTpHe0iEFbJE0BFcOyeNV9zy8K8Eq94UmCZ61Eir5MQdOPVQerxIcz8nL2ivvh3goCtqDqynFT/b6o+G5ajba36+ave6rUv6xdH4ub3/RNsQ+XCdB04lNLNJj~1; RT="z=1&dm=nseindia.com&si=ecaea57b-f6fb-43c6-8164-98becb851162&ss=l3oqgpm7&sl=5&tt=51w&bcn=%2F%2F684d0d43.akstat.io%2F&ld=eed9&nu=kpaxjfo&cl=ekgw"'

        }
        
        
        res = requests.get(url, headers=headers).text
        
        data = json.loads(res)
        
        data = data['grapthData']
        
        return data
          