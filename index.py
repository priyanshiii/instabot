import requests
import urllib
#accesstoken generated
ACCESS_TOKEN = "1655525547.edb4001.256a7090fa374b04972e0d76eecd1849"

#url of instagram api
BASE_URL = "https://api.instagram.com/v1/"

#function to define "self"
def my_info():

    request_url = BASE_URL + 'users/self/?access_token=%s' % ACCESS_TOKEN
    print 'GET request url : %s' % request_url
    my_info = requests.get(request_url).json()

#to check the status code if it is okay
    #meta code means data or information about code
    if my_info['meta']['code'] == 200:
        if len(my_info['data']):
            print 'Username: %s' % (my_info['data']['username'])
            print 'No. of followers: %s' % (my_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (my_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (my_info['data']['counts']['media'])
        else:
            print 'errrr,User does not exist!'
    else:
        print 'Status code other than 200 received'
my_info()

# code to retrieve friend id through access token

def get_friend_id(insta_user):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_user, ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    friend_info = requests.get(request_url).json()
    if friend_info['meta']['code'] == 200:
        if len(friend_info['data']):
            return friend_info['data'][0]['id']
        else:
            return None
    else:
        print 'Network Problem'

#code to retrieve friend information(followers,following,media,username)

def get_friend_info(insta_user):
    friend_id = get_friend_id(insta_user)
    if friend_id == None:
        print 'User does not exist!'
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (friend_id, ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    friend_info = requests.get(request_url).json()

    if friend_info['meta']['code'] == 200:
        if len(friend_info['data']):
            print 'Username: %s' % (friend_info['data']['username'])
            print 'No. of followers: %s' % (friend_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (friend_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (friend_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'



insta_user = raw_input('enter the user name')
get_friend_info(insta_user)
#to see your own media(posts,profile picture)
#urrlib is a library used for storing the id(user id) in jpeg format
def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'image downloaded!'
        else:
            print 'errr Post does not exist!'
    else:
        print 'Status code other than 200!'

#standard resolution is a kind of picture view,we can use thumbnail as well.

#to get your own post(media)
def image_url():
def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            age_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'your image has been downloaded!'
        else:
            print 'errrr,Post does not exist!'
    else:
        print 'Status code other than 200 received!'


def get_user_post(insta_username):
    user_id = get_friend_id()(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'errr,Post does not exist!'
    else:
        print 'Status code other than 200 received!'


def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"

        print "j.Exit"

        choice = raw_input("Enter you choice: ")
        if choice == "a":
            my_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_friend_info()(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "j":
            exit()
        else:
            print "wrong choice"
            start_bot()