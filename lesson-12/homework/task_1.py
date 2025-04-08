from bs4 import BeautifulSoup

with open('lesson-12/homework/weather.html','r') as file:
    html_doc=file.read()
soup=BeautifulSoup(html_doc,'html.parser')

forecast_entries=soup.find('tbody')

tds = soup.find_all("td")

forecast_data=[td.text for td in tds]


for i in range(5):
    day_info = forecast_data[i*3:3*(i+1)]

    print(f"{day_info[0]}, {day_info[1]}, {day_info[2]}")

temps=[]
for i in range(5):
    day_info = forecast_data[i*3:3*(i+1)]
    raw_temp = day_info[1].split("°")
    temps.append(int(raw_temp[0]))
    

print(max(temps))


for i in range(5):
    day_info = forecast_data[i*3:3*(i+1)]
    raw_days=day_info[2]
    if raw_days=="Sunny":
        print(day_info[0])

sum=sum(temps)
avg=sum/5
print(avg)    