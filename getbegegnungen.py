import simplejson as json
import urllib2
import backpropnet

vorhersage = []

def floatMul100(x):
  return float(x) * 0.001

##get alle Begegnungen dieser Spieltag --- parametrierung f spieltag (group_order_id) noetig
req = urllib2.Request("http://openligadb-json.heroku.com/api/matchdata_by_group_league_saison?group_order_id=16&league_saison=2011&league_shortcut=bl1")
opener = urllib2.build_opener()
f = opener.open(req)
games = []
game_ids = []
	
data = json.load(f)
print data

##get Tupel partizipient_1, partizipient_2
for i in data.get('matchdata'):
 games.append([i.get('id_team1'),i.get('id_team2')])
 game_ids.append(i.get('match_id'))
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

inti = -1
for i in games:
  inti += 1
  urlstring = generalurlstr.format(i[0],i[1])
  #print urlstring
  alleBegegnungen = getHerokuData(urlstring)
  historErgebnisse = []
#  print alleBegegnungen
  heimspieler = alleBegegnungen.get('matchdata')[0].get('id_team1')
  for j in alleBegegnungen.get('matchdata'):
    if(j.get('points_team1') != '-1'):
    	einErg = []
        if(j.get('id_team1') == heimspieler):
            einErg.append(map(floatMul100, [(j.get('id_team1')), (j.get('id_team2'))]))
            einErg.append(map(floatMul100, [(j.get('points_team1')), (j.get('points_team2'))]))
        else:
            einErg.append(map(floatMul100, [(j.get('id_team2')), (j.get('id_team1'))]))
            einErg.append(map(floatMul100, [(j.get('points_team2')), (j.get('points_team1'))]))
            
        print einErg
        historErgebnisse.append(einErg)
  
  print historErgebnisse
  pat = historErgebnisse
  #def demo(pat):
  # Teach network XOR function
  #moved
  # create a network with 3 input, 4 hidden, and 2 output nodes
#  n = backpropnet.NN(2, 3, 2)
  # train it with some patterns
#  n.train(pat)
  # test it
#  n.test(pat)
#  vorhersage.append([game_ids[inti],n.getTore(pat[0][0])])

#print vorhersage
