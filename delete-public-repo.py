import urllib.request
from urllib.error import HTTPError
from github import Github

if __name__ == '__main__':
    
    gitUser = Github('TOKEN')
    user = 'USER'
    try:
        repos = gitUser.get_user(user).get_repos('type=public')
        for repo in repos:
            request = urllib.request.Request(
            'https://api.github.com/repos/%s' % repo.full_name, 
            method='DELETE')
            request.add_header('Authorization', 'TOKEN')
            response = urllib.request.urlopen(request)

            if response.code == 204:
                print('repo %s has been successfully deleted' % repo.full_name)
            else:
                print('Error %s' % response.code)
            
    except HTTPError as error:

        if error.code == 403:
            print('Repository %s is unavailable due to DMCA takedown.' % repo.full_name)
        else:
            raise error
    except Exception as e:
        print(e)