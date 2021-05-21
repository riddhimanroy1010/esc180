def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global cur_star, cur_star_activity
    cur_star_activity = None

    global last_finished
    global bored_with_stars

    global tired, continous_time, resting_time, star_interval

    continous_time = 0

    resting_time = 0

    star_interval = []

    tired = False

    cur_hedons = 0
    cur_health = 0

    cur_star = None
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000


def star_can_be_taken(activity):
    global cur_star, cur_star_activity, cur_time, bored_with_stars

    if_bored()

    if (bored_with_stars == False) and (cur_star_activity == activity) and \
    (cur_star == cur_time):
        return True
    else:
        return False

def if_bored():
    global bored_with_stars
    if len(star_interval) >= 3:
        if star_interval[-1] - \
        star_interval[-3] <= 120:
            bored_with_stars = True
    elif len(star_interval) < 3:
        bored_with_stars = False
    if bored_with_stars == True:
        bored_with_stars = True

def perform_activity(activity, duration):
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration, last_finished

    global cur_star, cur_star_activity

    global tired
    global continous_time, resting_time

    if cur_time == 0:
        tired = False
    elif resting_time > 120:
        tired = False
    elif cur_time - last_finished < 120 and last_activity != "resting":
        tired = True

    cur_health += estimate_health_delta(activity, duration)
    cur_hedons += estimate_hedons_delta(activity, duration)

    if activity != "running":
        continous_time = 0
    elif activity == "running":
        continous_time += duration
    if activity == "resting":
        resting_time += duration
    elif activity != "resting":
        resting_time = 0

    cur_time += duration
    last_activity = activity
    last_activity_duration = duration
    last_finished = cur_time - last_activity_duration

def get_cur_hedons():
    return(cur_hedons)

def get_cur_health():
    return(cur_health)

def offer_star(activity):
    global cur_star, cur_star_activity, star_interval
    cur_star = cur_time
    cur_star_activity = activity
    star_interval.append(cur_time)

def most_fun_activity_minute():
    running = get_effective_minutes_left_hedons("running")
    textbooks = get_effective_minutes_left_hedons("textbooks")
    resting = 0
    if max(running, textbooks, resting) == running:
        return "running"
    elif max(running, textbooks, resting) == textbooks:
        return "textbooks"
    else:
        return "resting"

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''return the number of hedons per min of activity'''
    if star_can_be_taken(activity) == True:
        star_val = 3
    else:
        star_val = 0
    if not tired:
        if activity == "running":
            return 2 + star_val
        if activity == "textbooks":
            return 1 + star_val
    elif tired:
        return -2 + star_val

def get_effective_minutes_left_health(activity):
    pass

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    global tired
    if star_can_be_taken(activity) == True:
        star_val = 3
    else:
        star_val = 0
    if activity == "running":
        if duration >= 10:
            if not tired:
                tired = True
                return (2*10 - 2*(duration - 10) + star_val*10)
            if tired:
                tired = True
                return (-2*duration + (star_val*10))
        else:
            if not tired:
                tired = True
                return ((2 + star_val)*duration)
            if tired:
                tired = True
                return ((-2 + star_val)*duration)
    elif activity == "textbooks":
        if duration >= 20:
            if not tired:
                tired = True
                return (1*20 - (1*(duration - 20)) + star_val*10)
            if tired:
                tired = True
                return (-2*duration + star_val*10)
        elif duration in range(0, 10):
            if not tired:
                tired = True
                return ((1 + star_val)*duration)
            if tired:
                tired = True
                return ((-2 + star_val)*duration)
        elif duration in range(10, 20):
            if not tired:
                tired = True
                return (1*duration + star_val*10)
            if tired:
                tired = True
                return (-2*duration + star_val*10)
    elif activity == "resting":
        if duration >= 120:
            tired = False
        return 0

def estimate_health_delta(activity, duration):
    if activity == "running":
        if continous_time == 0: #first run or after another activity
            if duration < 180:
                return (3 * duration)
            elif duration >= 180:
                return ((3 * 180) + abs((180 - duration)))
        elif continous_time < 180:
            if continous_time + duration >= 180:
                return ((3 * (180 - continous_time)) + (duration - (180 - continous_time)))
            elif continous_time + duration < 180:
                return (3 * duration)
        elif continous_time >= 180:
            return (duration)
    elif activity == "textbooks":
        return (2*duration)
    elif activity == "resting":
        return 0

################################################################################

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_health())            #90 = 30 * 3
    print(get_cur_hedons())            #-20 = 10 * 2 + 20 * (-2)
    print(most_fun_activity_minute())  #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  #running
    perform_activity("textbooks", 30)
    print(get_cur_health())            #150 = 90 + 30*2
    print(get_cur_hedons())            #-80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            #210 = 150 + 20 * 3
    print(get_cur_hedons())            #-90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health())            #700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons())            #-430 = -90 + 170 * (-2)
    print("--------------next--------------")
    # initialize()
    # offer_star("textbooks")
    # perform_activity("textbooks", 80)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("running", 70)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # perform_activity("resting", 130)
    # print(get_cur_health())
    # print(get_cur_hedons())
    # offer_star("textbooks")
    # print(most_fun_activity_minute())
    # print("next")
    initialize()
    offer_star("textbooks")
    perform_activity("running", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    print("--------------next--------------")
    initialize()
    perform_activity("resting", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("resting", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute()) #running
    offer_star("textbooks")
    print(most_fun_activity_minute()) #textbooks
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute()) #resting
    perform_activity("textbooks", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    print("--------------next--------------")
    # Test Star behaviour
    initialize()
    offer_star("textbooks")
    print(most_fun_activity_minute())  # textbooks
    offer_star("textbooks")
    print(most_fun_activity_minute())  # textbooks
    offer_star("textbooks")
    print(most_fun_activity_minute())  # running
    print("--------------next--------------")
    initialize()
    offer_star("textbooks")
    print(most_fun_activity_minute())  # textbooks
    offer_star("textbooks")
    print(most_fun_activity_minute())  # textbooks
    offer_star("textbooks")
    perform_activity("running", 30)
    print(most_fun_activity_minute())  # resting
    print("--------------next--------------")
    initialize()
    offer_star("textbooks")
    perform_activity("running", 101)
    print(get_cur_health()) # 303
    print(get_cur_hedons()) # -162
    offer_star("textbooks")
    print(most_fun_activity_minute())  # textbooks
    perform_activity("textbooks", 20)
    offer_star("textbooks")
    print(most_fun_activity_minute())  # textbooks
    print("--------------next--------------")
    initialize()
    offer_star("resting")
    offer_star("textbooks")
    perform_activity("running", 101)
    print(get_cur_health()) # 303
    print(get_cur_hedons()) # -162
    perform_activity("textbooks", 20)
    offer_star("textbooks")
    print(most_fun_activity_minute())  # textbooks
    perform_activity("textbooks", 20)
    offer_star("textbooks")
    print(most_fun_activity_minute())  # textbooks
    print("--------------next--------------")
    initialize()
    perform_activity("running", 90)
    perform_activity("running", 90)
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("running", 60)
    perform_activity("running", 120)
    perform_activity("running", 13)
    print(get_cur_hedons())
    print(get_cur_health())
    print(most_fun_activity_minute())
    perform_activity("running", 60)
    perform_activity("running", 170)
    perform_activity("running", 13)
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("resting",120)
    print(most_fun_activity_minute())
    offer_star('running')
    perform_activity("running", 600)
    perform_activity("running", 12)
    perform_activity("running", 134)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("textbooks")
    perform_activity("running", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(star_can_be_taken("running"))
    offer_star("textbooks")
    perform_activity("resting", 119)
    perform_activity('textbooks',11)
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("textbooks", 123)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("textbooks")
    perform_activity("textbooks", 10)
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("textbooks", 10)
    perform_activity("textbooks", 1)
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("resting", 150)
    perform_activity("textbooks", 20)
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("resting", 150)
    perform_activity("textbooks", 20)
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("resting", 150)
    perform_activity("textbooks", 50)
    print(get_cur_hedons())
    print(get_cur_health())
    perform_activity("resting",150)
    offer_star("textbooks")
    perform_activity("textbooks", 10)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("textbooks")
    perform_activity("textbooks", 20)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("textbooks")
    perform_activity("textbooks", 100)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("running")
    perform_activity("textbooks", 10)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("running")
    perform_activity("running", 10)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("running")
    perform_activity("running", 110)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("running")
    perform_activity("textbooks", 11)
    perform_activity("running", 10)
    print(get_cur_hedons())
    print(get_cur_health())
    offer_star("running")
    perform_activity("running", 10)
    offer_star("running")
    perform_activity("running", 10)
    offer_star("running")
    perform_activity("running", 10)
    offer_star("running")
    perform_activity("running", 10)
    print(get_cur_hedons())
    print(get_cur_health())
    print("--------------next--------------")
    initialize()
    offer_star("textbooks")
    perform_activity("running", 120)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("textbooks", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 120)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    print("--------------next--------------")
    initialize()
    print(most_fun_activity_minute())
    offer_star("textbooks")
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("resting", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("textbooks")
    print(most_fun_activity_minute())
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    offer_star("textbooks")
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    print("--------------next--------------")
    initialize()
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    offer_star("textbooks")
    perform_activity("running", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 120)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("running")
    print(most_fun_activity_minute())
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    offer_star("running")
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    perform_activity("running", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    offer_star("running")
    print(most_fun_activity_minute())
    perform_activity("resting", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    print("--------------next--------------")
    initialize()
    #offer_star("running")
    perform_activity("running", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    print("--------------next--------------")
    initialize()
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    perform_activity("textbooks", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    offer_star("textbooks")
    print(most_fun_activity_minute())
    perform_activity("resting", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 120)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 80)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("textbooks", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    print("--------------next--------------")
    initialize()
    perform_activity("running", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    offer_star("textbooks")
    offer_star("textbooks")
    perform_activity("running", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("running", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("running")
    print(most_fun_activity_minute())
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("running", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("resting", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("resting", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print("--------------next--------------")
    initialize()
    perform_activity("running", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("running", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("textbooks")
    perform_activity("textbooks", 120)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("running", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("textbooks")
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    print("--------------next--------------")
    initialize()
    perform_activity("textbooks", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("running", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("running")
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    #offer_star("running")
    offer_star("textbooks")
    perform_activity("textbooks", 140)
    print(get_cur_health())
    print(get_cur_hedons())