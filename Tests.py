    initialize()
    perform_activity("running", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 40)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) # resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute()) # running
    perform_activity("textbooks", 30)
    print(get_cur_health()) # 150 = 90 + 30*2
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
    initialize()
    offer_star("running")
    perform_activity("running", 5) # gets extra hedons
    print(get_cur_health())   #5*3
    print(get_cur_hedons()) #
    perform_activity("running", 2) # no extra hedons
    print(get_cur_health())
    print(get_cur_hedons())