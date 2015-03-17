# nytimes_feed
# Command line tool that lets user have latest feed details 
# emailed to them, and a link displayed to selection in the terminal

import sys
from models import Feed

# List of available feeds
feeds = ['usa headlines','international headlines','world','usa','ny','business','technology','sports','science','health','arts','style','travel','magazine','jobs','real estate','autos', 'after deadline blog', 'lens blog', 'the public editor', 'wordlay blog', 'obituaries','times wire', 'most e-mailed', 'most shared','most viewed', 'columnists', 'editorials', 'op-eds', 'opinionator', 'blogs', 'sunday review', 'letters', 'video', 'international opinion']

print "\n Welcome to the NY Times feed by mail service.  For more information about this script type 'python nytimes_feed.py help' \n \n"

#Setup email service on computer

#Get user input parameter and determine what to do with it

if sys.argv[1]:
	#Check if arg is in the list of valid feeds
	if sys.argv[1] in feeds:
		print "Feed exists! \n"
		#Check to see if there are subfeeds for this particulat feed

	else:
		print "Alas!  This feed does not exist.  To see a list of feeds please run the following command \n python %s feeds" % sys.argv[0]	
else:
	print "You fool!  Dont you see what you have done! Just kidding... Its just that this feed doesnt exist (or does it...).  To check out a list of available feeds you can run the following command \n python %s feeds" % sys.argv[0]
