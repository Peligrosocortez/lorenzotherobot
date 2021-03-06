from src.lib import llama as llamadb
import src.lib.twitch as twitch
from src.lib.queries.points_queries import *
import globals


def cron():
    treatsForAll(1)

def treatsForAll(delta):
    if get_stream_status():
        user_dict, all_users = twitch.get_dict_for_users()
        try:
            modify_points_all_users(1)
            print "Treats added to " + str(all_users)
        except:
            return "Twitch's backend is down. Treats can't be added in this state. Moderators should monitor http://twitchstatus.com/ for updates."

    #for user in user_list:
    #    llamadb.newConnection().addPoints(user, delta)
    # return str(delta) + " treats added to everyone in the chat! Raise your Kappas! \Kappa/"


def treats(args):

    usage = "!treats (add/remove [username] [amount])"

    approved_list = [
        'curvyllama', 'peligrosocortez', 'singlerider', 'newyork_triforce', 'agathos1337']

    add_remove = args[0]
    delta_user = args[1].lower()

    try:
        delta = int(args[2])
    except:
        return "amount has to be a number, ya dingus!"

    mod_name = globals.CURRENT_USER

    if mod_name not in approved_list:
        return "Only " + ", ".join(approved_list) + " are allowed to do that!"
    
    elif add_remove == "add":
        
        if delta_user == "all":
            modify_points_all_users(delta)
        else:
            modify_user_points(delta_user, delta)
        
    elif add_remove == "remove":
        delta *= -1
        modify_user_points(delta_user, delta)
        
    elif add_remove == "set":
        set_user_points(delta_user, delta)

    

    return "{} treats for {}!".format(delta, delta_user)
