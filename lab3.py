import requests
import datetime 
r = requests.get('https://api.meetup.com/2/open_events?&sign=true&lat=40.75&country=us&topic=java,android,hacker,ruby,python&city=new-york&state=ny&category=34&lon=-73.98999786376953&time=,1w&key=4547d1a36616e767f195658726e687e')
res = r.json()
file = open("meetup.html", "w+", encoding='utf-8')
file.write("<style type='text/css'> .content { margin: 0 auto 30px; width:800px; border: 2px solid gray; padding: 10px;} .date {margin: 0 auto; width:800px; } </style>")
t = datetime.date.today()
tdel = t + datetime.timedelta(days=7)
file.write("<h2 align='center'>" + "Events IT this week: from   " + str(t.strftime('%d %B %Y')) +"  to   "+ str(tdel.strftime('%d %B %Y')) + "</h2>")
for item in res['results']:
  time = datetime.datetime.fromtimestamp(item['time']/1000)
  file.write("<div class='date'>" + str(time.strftime('%B  %d') + "</div>")) 
  file.write("<div class='content'>")
  file.write("<span>" + str(time.strftime('%H:%M %p') + "</span><h2 align='center'>" + str((item['group'])['name']) + "</h2>"))
  try:
      file.write("<div align='center'>Address: " + str((item['venue'])['address_1']) + "</div>")
  except:
    pass
  try:
    file.write("<div align='center'>Another address: " + str((item['venue'])['address_2']) + "</div>")
  except:
    pass
  file.write("<div align='center'>" + str(item['name'] + "</div>"))
  try:
    file.write("<p>" + str(item['description']) + "</p>")
  except:
    pass
  file.write("</div>")
file.close()
