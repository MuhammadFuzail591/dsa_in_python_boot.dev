def get_follower_prediction(follower_count, influencer_type, num_months):
    
    num_of_followers = 0

    if(influencer_type == "fitness"):
        num_of_followers = follower_count * (4**num_months)
        print(f"fitness: {num_of_followers} ")
    elif(influencer_type=="cosmetic"):
        num_of_followers = follower_count * (3**num_months)
        print(f"cosmetic`s: {num_of_followers} ")

    else:
        num_of_followers = follower_count * (2**num_months)
        print(f"others: {num_of_followers} ")


    print(2**64)
    print(2**32)

    return num_of_followers

get_follower_prediction(23,"other",2)


