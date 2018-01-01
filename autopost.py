#-*- coding: utf-8 -*-
import time
from facepy import GraphAPI

# get api from here  https://developers.facebook.com/tools/explorer
api = "EAACEdEose0cBANd5wLEnM1DzMzjhPLdCj0DTMXuOyCiTkzcm2R7oYDnkqpZAdWywFw5H5oRqmbQj171ZBFzBk71fqKMacVmDJoiKnL50KDRo13LC9nEyjbAdwvKO7QOXQYkIQe7mT25KFISPjGMp24mP2ccXMMZBwFcj32LHDrGbWQlYlXZCmkyMBe8ZCJjxtiHqRL7aZADgZDZD"
graph = GraphAPI(api)
message = 'only test'
#list of group_id for test
groups1 = [ '2007658576148667']
#list of person_id for test
groups = [ '1603076759928998','100004972118793']


#for group_id in groups:
	#code for post to group
#	print "Posting to " + 'http://www.facebook.com/groups/' + str(group_id)
	#code for post to personal_wall
#	print "Posting to " + 'http://www.facebook.com/' + str(group_id)
#	graph.post(path =str(group_id) + '/feed', message=message)
	#gian~ tg tranh an check-point tu facebook
	#time.sleep(10)
#print "Done"
graph.r
my_likes = graph.get('me/feed/')
friends = graph.get('me/friends/')
print my_likes