import simplejson as json
import urllib2
import backpropnet

##get alle Begegnungen dieser Spieltag --- parametrierung f spieltag (group_order_id) noetig
req = urllib2.Request("http://openligadb-json.heroku.com/api/matchdata_by_group_league_saison?group_order_id=16&league_saison=2011&league_shortcut=bl1")
opener = urllib2.build_opener()
f = opener.open(req)
games = []
	
data = json.load(f)
#backpropnet.demo(pat = [[[0,0], [0]],[[0,1], [1]],[[1,0], [1]],[[1,1],[0]]])

##get Tupel partizipient_1, partizipient_2
for i in data.get('matchdata'):
 games.append([i.get('id_team1'),i.get('id_team2')])
 #print i.get('id_team1')
 #print i.get('id_team2')
 
print "hoppa"
generalurlstr = "http://openligadb-json.heroku.com/api/matchdata_by_teams?team_id_1={0}&team_id_2={1}"


def getHerokuData(requeststring):
 print "hossa"
 req = urllib2.Request(requeststring)
 opener = urllib2.build_opener()
 f = opener.open(req)
 data = json.load(f)
 return data

for i in games:
  urlstring = generalurlstr.format(i[0],i[1])
  #print urlstring
  alleBegegnungen = getHerokuData(urlstring)
  historErgebnisse = []
#  print alleBegegnungen
  heimspieler = alleBegegnungen.get('matchdata')[0].get('id_team1')
  for j in alleBegegnungen.get('matchdata'):
    if(j.get('points_team1') != -1):
        if(j.get('id_team1') == heimspieler):
            historErgebnisse.append([j.get('id_team1'), j.get('points_team1'), j.get('id_team2'), j.get('points_team2')])
        else:
            historErgebnisse.append([j.get('id_team2'), j.get('points_team2'), j.get('id_team2'), j.get('points_team1')])
  
  print historErgebnisse


