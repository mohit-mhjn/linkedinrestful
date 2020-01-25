"""
IMPORTANT LINKS

https://docs.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api
https://developer.linkedin.com/docs/v2/oauth2-client-credentials-flow
https://stackoverflow.com/questions/50626514/linkedin-this-application-is-not-allowed-to-create-application-tokens
https://www.linkedin.com/oauth/v2/accessToken
https://stackoverflow.com/questions/53352125/getting-profile-details-of-other-linkedin-users-using-api-in-python
https://pypi.org/project/python-linkedin-v2/
https://developer.linkedin.com/docs/guide/v2/concepts
"""


import requests

CLIENT_ID = "<>"
CLIENT_SECRET = "<>"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"


def get_token():
    # client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "client_credentials",
                 "client_id": CLIENT_ID,
                 "client_secret": CLIENT_SECRET}
    print(TOKEN_URL)
    response = requests.post(TOKEN_URL, data=post_data)
    token_json = response.json()
    print(token_json)
    return authtoken = None  # ["access_token"]


def get_profile(authtoken):

    req_url = "https://api.linkedin.com/v1/people/~:(id,first-name,email-address,last-name,headline,picture-url," + \
        "industry,summary,specialties,positions:(id,title,summary,start-date,end-date,is-current," + \
        "company:(id,name,type,size,industry,ticker)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes)," + \
        "associations,interests,num-recommenders,date-of-birth,publications:(id,title,publisher:(name)," + \
        "authors:(id,name),date,url,summary),patents:(id,title,summary,number,status:(id,name),office:(name)," + \
        "inventors:(id,name),date,url),languages:(id,language:(name),proficiency:(level,name)),skills:(id,skill:(name))," + \
        "certifications:(id,name,authority:(name),number,start-date,end-date),courses:(id,name,number),recommendations-" + \
        "received:(id,recommendation-type,recommendation-text,recommender)," + \
        "honors-awards,three-current-positions,three-past-positions,volunteer)?format=json"
    url = {public-profile-url}


if __name__ == "__main__":
    authtoken = get_token()


"""
Linkedin :: public API (anyone can access it)

Opex :: <user>

1. Get : Response >> seeing some data >> json
2. Post : No Response >> sending a data >> None \.
3. REST API [get and post] >> post something but response is not None

App >
Step 1 : Get Auth Token and Linkedin Session

REST API (access_token) : post client id and secret
return authtoken (this expires in 30 mins)

REST API (profile-API) : post authtoken
return profile fields

"""
