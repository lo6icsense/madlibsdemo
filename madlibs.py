# string concatenation (aka how to put strings together)
# suppose we want to creat a string that says "subscribe to ____ "
youtuber ="Mike Gonzales"# some string valuable

# a few ways to do this
print("subscribe to "  + youtuber)
print("subscriber to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous_person: ")


madlib = f"Computer programming is so {adj}! It makes me so excited all the time beacuse \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)