HedgeCast

Business Domain Logic:

Upload Video
Consume Video / playlist
Group Videos
Play Videos

User registration

Payment processing
    Recurring
        -> Stripe

Videos:e
    Add to playlist
    Access Type: Free | Premium (premium)

Will need:
Video transcoding --> will have to do manually
    Mobile (low)
    Desktop (medium)
    Premium (For paid users? hd)
S3 Buckets
Don't need docker

Postgres:
    plan
    user
    user_plan
    video
    playlist
    video_playlist

plan:
    holds stripe specific knowledge of a plan
user:
    holds user information
user_plan:
    one-to-one representation of user -> plan
video:
    information about videos
playlist:
    playlists for videos
video_playlist:
    many-to-many representation of of videos -> playlist
