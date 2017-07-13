import requests
import urllib
import termcolor
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#requests is a library that will allow to send HTTP requests.
#urllib simply helps in fetching data across the WWW.
#termcolor is a library used for showing text in specified color.
#time library is used to stop time for certain specified seconds.
#matplotlib is an api that is used for embedding plots in an appliction.
#wordcloud is a library used to plot cloud of words.


print termcolor.colored('welcome to instabot','red')
time.sleep(2)
hashTags=[]
caption=[]
#accesstoken generated
ACCESS_TOKEN = "1655525547.edb4001.256a7090fa374b04972e0d76eecd1849"
#sandbox users
list_of_sandbox_users = ['nitttish_','insta.mriu.test.5','shadan_fcb']
#url of instagram api
BASE_URL = "https://api.instagram.com/v1/"


#function is created to define "self" and to retrieve own information(function 1)
def my_info():
    request_url = BASE_URL + 'users/self/?access_token=%s' % ACCESS_TOKEN
    print 'GET request url : %s' % request_url
    my_info = requests.get(request_url).json()


#to check the status code if it is okay
#meta code means data or information about code
    if my_info['meta']['code'] == 200:
        if len(my_info['data']):
            print termcolor.colored('my_info : %s' % ['data'], 'red')
            time.sleep(1)
            print 'Username: %s' % (my_info['data']['username'])
            print 'No. of followers: %s' % (my_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (my_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (my_info['data']['counts']['media'])
        else:
            print termcolor.colored('Errr,User does not exist!','blue')
    else:
        print  termcolor.colored(' Status code 200 not recieved : ','blue')


# code to retrieve friend id through access token
#function is created to access the id of another user(function 2)
def get_buddy_id(insta_username):
    print termcolor.colored('you can select users from this list :', 'blue')

    for k in list_of_sandbox_users:
        print k
    user_name = raw_input('enter the user name: ')

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    buddy_info = requests.get(request_url).json()
    if buddy_info['meta']['code'] == 200:
        time.sleep(1)
        if len(buddy_info['data']):
            return buddy_info['data'][0]['id']
        else:
            return None
    else:
        print 'Oops!,Network Problem'


#code to retrieve friend information(followers,following,media,username)
#function is created to access the information of another user(function 4)
def get_buddy_info(insta_user):
    buddy_id = get_buddy_id(insta_user)
    if buddy_id == None:
        print 'User does not exist!'
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (buddy_id, ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    buddy_info = requests.get(request_url).json()

    if buddy_info['meta']['code'] == 200:
        time.sleep(1)
        if len(buddy_info['data']):
            print 'Username: %s' % (buddy_info['data']['username'])
            print 'No. of followers: %s' % (buddy_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (buddy_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (buddy_info['data']['counts']['media'])
        else:
            print termcolor.colored('User does not seem to be on instabot!','blue')
    else:
        print  termcolor.colored(' Status code 200 not recieved : ', 'blue')


#to see your own media(posts,profile picture)
#function is created to access our own recent post(function 5)
def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        time.sleep(1)
        if len(own_media['data']):

            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print termcolor.colored('Your image is downloaded!','red')
        else:
            print termcolor.colored('Errr,Post does not exist!','blue')
    else:
        print  termcolor.colored(' Status code 200 not recieved : ', 'blue')


#code to retrieve the recent media of another user
#function is created to access the recent post of another user(function 6)
def get_user_post(insta_user):
    user_id = get_buddy_id(insta_user)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        time.sleep(1)
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print termcolor.colored('Your image is downloaded!','red')
        else:
            print termcolor.colored('Errr,Post does not exist!','blue')
    else:
        print  termcolor.colored(' Status code 200 not recieved : ', 'blue')


#function is created to get id of the recent post of the user(function 7)
def get_post_id(insta_username):
    user_id = get_buddy_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
         if len(user_media['data']):
          return user_media['data'][0]['id']
         else:
             print 'There is no recent post of the user!'
             exit()
    else:
         print 'Status code other than 200 received!'
    exit()
    get_post_id(insta_username)


#code to like  the post
#function is created to like a post of another user,recent one(function 8)
def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like successful!'
    else:
        print termcolor.colored('Like was not successful,try again later', 'blue')


#code to comment on the recent media
#function to post a comment on the post of the user(function 9)
def post_a_comment(insta_username):
     media_id = get_post_id(insta_username)
     comment_text = raw_input("Your comment: ")
     payload = {"access_token": ACCESS_TOKEN, "text": comment_text}
     request_url = (BASE_URL + 'media/%s/comments') % (media_id)
     print 'POST request url : %s' % (request_url)

     make_comment = requests.post(request_url, payload).json()
     if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
     else:
         print "Unable to add comment. Try again!"


#function is created for showing the number of users who liked my recent media
#(function 10)
def users_liked_my_post():
     post_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
     user_media = requests.get(post_url).json()
     if user_media['meta']['code'] == 200:
       if len(user_media['data']):
         store_media_id = user_media['data'][0]['id']
         media_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (store_media_id, ACCESS_TOKEN)
         details = requests.get(media_url).json()
         print details
       else:
         print 'data not exist'
     else:
        print 'user not exist'


#function is created to make a wordcloud on the basis of hashtags used on the recent post
#(function 11)
def word():
    buddy_name = raw_input('enter the name of the user :')
    url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (buddy_name, ACCESS_TOKEN)
    buddy_details = requests.get(url).json()
    if buddy_details['meta']['code'] == 200:
        if len(buddy_details['data']):
            id = []
            id = (buddy_details['data'][0]['id'])
            if id == None:
                print 'user id does not exist : '
            else:
                url = (BASE_URL + 'users/%s/media/recent/?access_token=%s' % (id, ACCESS_TOKEN))
                posts_details = requests.get(url).json()
                if len(posts_details['data']):
                    k = posts_details['data'][0]['tags']
                    caption.append(k)

                    print caption
                thefile = open('test.txt', 'w')

                for item in caption:
                    thefile.write("%s\n" % item)
                    thefile.close()
                    with open('test.txt', 'r') as myfile:

                        data = myfile.read()
                    print len(data)
#Generate a word cloud image
                    wordcloud = WordCloud().generate(data)

#Display the generated image
                    plt.figure()
                    plt.imshow(wordcloud, interpolation="bilinear")
                    plt.axis("off")
                    plt.show()

                else:
                    print 'no data is present'
        else:
            print 'data does not exist '
    else:
        print 'status error'


#showing menu to the user by defining the function start_instabot
#(function 12)
def start_instabot():
    while True:
        print '\n'
        print 'Choose from the following options'
        print '1.Get your own details\n'
        print '2.Get details of a user by username\n'
        print '3.Get your own recent post\n'
        print '4.Get the recent post of a user by username\n'
        print '5.Like the recent post of the user\n'
        print '6.Post a comment on the recent post the user\n'
        print '7.Get the users who liked my recent post from the sandbox list\n'
        print '8.Plot a word cloud on the basis of hastags\n'
        print '9.Exit'

        choice = raw_input("Enter you choice: ")
        if choice == "1":
            my_info()
        elif choice == "2":
            insta_username = raw_input("Enter the username of the user: ")
            get_buddy_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice =="5":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice =="6":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
        elif choice =="7":
            users_liked_my_post()
        elif choice =="8":
            word()
        elif choice == "9":
            exit()
        else:
            print "wrong choice"
start_instabot()
