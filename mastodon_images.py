from mastodon import Mastodon
# Setting up Mastodon
mastodon = Mastodon(
  access_token='<access_token>', # this is your access token from the Development tab from the step before
  api_base_url='mastodon.social' # this is the URL of your bot's server
)

image = mastodon.media_post("generated.jpg", # this is the only required argument. you can either give the filename directly or use the "media_file" argument.
                            mime_type ="image/jpg", # this indicates the filetype. only necessarily needed if you did not use "media_type", otherwise the program will guess the correct file type
                            )

# Write a "Hello World!" post with an image
mastodon.status_post("", # this is the text associated with the message
                      media_ids=image["id"], # as said earlier, the media_post function uploads the image with an id as a dictionary. this calls the correct photo
                      )