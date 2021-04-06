from pprint import pprint

from firebase import firebase

# https://chamayetu-ddca4.firebaseio.com/
firebase = firebase.FirebaseApplication('https://chamayetu-ddca4.firebaseio.com/', None)

# obtain the users node data
users = firebase.get('/users', None)
pprint(users)

# obtain the users node data
chamas = firebase.get('/chamas', None)
pprint(chamas)

# creating a new node
new_chama = {"name": "Boda",
             "members": 9,
             "nextMeetingTime": "October 9th 2016",
             "venue": "Nakuru",
             "milestone": "Buy Property in Rongai",
             "milestoneDate": "November 30th 2016",
             "dateCreated": "January 1st 2016",
             "amountExpected": 4500,
             "totalAmount": 10231}

post = firebase.post(url='/chamas', data=new_chama, headers={'print': 'pretty'})
print(post)
