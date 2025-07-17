from mastodon import Mastodon
# Setting up Mastodon
mastodon = Mastodon(
  access_token='<access_token>', # this is your access token from the Development tab from the step before
  api_base_url='mastodon.social' # this is the URL of your bot's server
)
# Write a "Hello World!" post
mastodon.status_post("Hello World!")