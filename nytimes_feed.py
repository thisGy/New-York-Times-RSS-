# nytimes_feed
# Command line tool that lets user have latest feed details 
# emailed to them, and a link displayed to selection in the terminal

import sys
import webbrowser
from models import Feeds

# List of available feeds
Feeds = Feeds()
feeds = Feeds.feeds

print "\n Welcome to the NY Times RSS feed service.  For more information about this script type 'python nytimes_feed.py help' \n \n"

#Setup email service on computer


#Get user input parameter and determine what to do with it
if sys.argv[1]:
	#Check if arg is in the list of valid feeds
	if sys.argv[1] in feeds:

		#Check if they entered a second param
		if len(sys.argv) < 3:
			print "Please select a feed from the following options:"
			
			for key in feeds[sys.argv[1]]:
				#Print available feeds from selected category
				print "%s" %key

			#Let user enter feed of interest
			choice = raw_input("Please Select:")

			if choice in feeds[sys.argv[1]]:
				#Check to see if there are subfeeds for this particulat feed
				print "Feed found! Opening in browser..."
				#print "Feed: %s" %feeds[sys.argv[1]][choice]
				webbrowser.open_new_tab(feeds[sys.argv[1]][choice])
			else:
				print "Cant find feed...."

		else:	
			# Check for second argument, otherwise show user a list of options for that feed category
			if sys.argv[2] in feeds[sys.argv[1]]:
				#Check to see if there are subfeeds for this particulat feed
				print "Feed found! Opening in browser..."
				#print "Feed: %s" %feeds[sys.argv[1]][sys.argv[2]]
				webbrowser.open_new_tab(feeds[sys.argv[1]][sys.argv[2]])			
			else:
				print "Cant find feed...."

	else:
		# All other args that arent feeds default to help
		Feeds.help()
else:
	print "You fool!  Dont you see what you have done! Just kidding... Its just that this feed doesnt exist (or does it...).  To check out a list of available feeds you can run the following command \n python %s feeds" % sys.argv[0]
