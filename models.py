class Feeds(object):
	def __init__(self):
		this.feeds = {
			'usa headlines' : 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
			'international headlines' : 'http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml',
			'world' : {
						'world': 'http://www.nytimes.com/services/xml/rss/nyt/World.xml',			
						'africa': 'http://www.nytimes.com/services/xml/rss/nyt/Africa.xml',
						'americas':'http://www.nytimes.com/services/xml/rss/nyt/Americas.xml',
						'asia pacific':'http://www.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml',
						'europe':'http://www.nytimes.com/services/xml/rss/nyt/Europe.xml',
						'middle east':'http://www.nytimes.com/services/xml/rss/nyt/MiddleEast.xml',
					},
			'usa' : {
						'usa': 'http://www.nytimes.com/services/xml/rss/nyt/US.xml',			
						'education': 'http://www.nytimes.com/services/xml/rss/nyt/Education.xml',
						'learning network blog':'http://learning.blogs.nytimes.com/feed',
						'politics':'http://www.nytimes.com/services/xml/rss/nyt/Politics.xml',
						'the upshot':'http://www.nytimes.com/services/xml/rss/nyt/Upshot.xml',
					},
			'ny' :  {
						'ny/region': 'http://www.nytimes.com/services/xml/rss/nyt/NYRegion.xml',			
						'city room blog': 'http://cityroom.blogs.nytimes.com/feed/',
						'fort greene':'http://fort-greene.blogs.nytimes.com/feed',
						'east village':'http://eastvillage.thelocal.nytimes.com/feed/',
					},
			'business' :  {
						'business': 'http://feeds.nytimes.com/nyt/rss/Business',			
						'energy and environment': 'http://www.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml',
						'international business':'http://www.nytimes.com/services/xml/rss/nyt/InternationalBusiness.xml',
						'small business':'http://www.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml',
						'your the boss blog':'http://boss.blogs.nytimes.com/feed',
						'economy':'http://www.nytimes.com/services/xml/rss/nyt/Economy.xml',
						'deal book':'http://www.nytimes.com/services/xml/rss/nyt/Dealbook.xml',
						'media and advertising':'http://www.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml',
						'your money':'http://www.nytimes.com/services/xml/rss/nyt/YourMoney.xml',
					},
			'technology' :  {
						'technology': 'http://feeds.nytimes.com/nyt/rss/Technology',			
						'bits blog': 'http://bits.blogs.nytimes.com/feed/',
						'personal tech':'americas',
					},
			'sports' :  {
						'sports': 'http://www.nytimes.com/services/xml/rss/nyt/Sports.xml',			
						'international sports': 'http://www.nytimes.com/services/xml/rss/nyt/InternationalSports.xml',
						'baseball':'http://www.nytimes.com/services/xml/rss/nyt/Baseball.xml',
						'college basketball':'http://www.nytimes.com/services/xml/rss/nyt/CollegeBasketball.xml',
						'college football':'http://www.nytimes.com/services/xml/rss/nyt/CollegeFootball.xml',
						'golf':'http://www.nytimes.com/services/xml/rss/nyt/Golf.xml',
						'hockey': 'http://www.nytimes.com/services/xml/rss/nyt/Hockey.xml',			
						'basketball': 'http://www.nytimes.com/services/xml/rss/nyt/ProBasketball.xml',
						'football':'http://www.nytimes.com/services/xml/rss/nyt/ProFootball.xml',
						'soccer':'http://www.nytimes.com/services/xml/rss/nyt/Soccer.xml',
						'tennis':'http://www.nytimes.com/services/xml/rss/nyt/Tennis.xml',
						'gambit blog':'http://gambit.blogs.nytimes.com/feed/',						
					},
			'science' :  {
						'science': 'http://www.nytimes.com/services/xml/rss/nyt/Science.xml',			
						'environment': 'http://www.nytimes.com/services/xml/rss/nyt/Environment.xml',
						'space and cosmos':'http://www.nytimes.com/services/xml/rss/nyt/Space.xml',
					},
			'health' :  {
						'health': 'http://www.nytimes.com/services/xml/rss/nyt/Health.xml',			
						'well blog': 'http://well.blogs.nytimes.com/feed/',
						'the new old age blog':'http://newoldage.blogs.nytimes.com/feed/',
						'research':'http://www.nytimes.com/services/xml/rss/nyt/Research.xml',
						'fitness and nutrition':'http://www.nytimes.com/services/xml/rss/nyt/Nutrition.xml',
						'money and politics':'http://www.nytimes.com/services/xml/rss/nyt/HealthCarePolicy.xml',
						'views':'http://www.nytimes.com/services/xml/rss/nyt/Views.xml',

					},
			'arts' :  {
						'world': 'world',			
						'africa': 'test',
						'americas':'americas',
						'asia pacific':'asia pacific',
						'europe':'europe',
						'middle east':'middle east',
						'asia pacific':'asia pacific',
						'europe':'europe',
						'middle east':'middle east',
						'asia pacific':'asia pacific',
						'europe':'europe',
						'middle east':'middle east',												
					},	
			'style' :  {
						'world': 'world',			
						'africa': 'test',
						'americas':'americas',
						'asia pacific':'asia pacific',
						'europe':'europe',
						'middle east':'middle east',
						'asia pacific':'asia pacific',
						'europe':'europe',
						'middle east':'middle east',						
					},
			'travel' :  {
						'world': 'world',			
						'africa': 'test',
						'americas':'americas',
					},
			'magazine' :  {
						'world': 'world',			
					},
			'jobs' : '',
			'real estate' :  {
						'world': 'world',			
						'africa': 'test',
					},
			'autos' : '', 
			'after deadline blog' : '', 
			'lens blog' : '', 
			'the public editor' :  {
						'world': 'world',			
					}, 
			'wordlay blog' : '', 
			'obituaries' : '',
			'times wire' : '', 
			'most e-mailed' : '', 
			'most shared' : '',
			'most viewed' : '', 
			'columnists' : '', 
			'editorials' : '', 
			'op-eds' : '', 
			'opinionator' : '', 
			'blogs' : '', 
			'sunday review' : '', 
			'letters' : '', 
			'video' : '', 
			'international opinion' : '',
		}
	def get_feed(self, selected_feed, feed_list):
		pass

	def has_subcat(feed_key):
		if feed_key:
			return true
		else:
			return false
	
	def feed_exists(self, test):
		pass
