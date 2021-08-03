#!/usr/bin/env python

from github import Github
from github.GithubException import GithubException

if __name__ == '__main__':


    gitUser = Github('TOKEN')

    try:
        followers = [follower.id for follower in gitUser.get_user().get_followers()] 
         
        for following in gitUser.get_user().get_following():

            if following.id not in followers:
                gitUser.get_user().remove_from_following(following)

    except Exception as e:
        print(e)