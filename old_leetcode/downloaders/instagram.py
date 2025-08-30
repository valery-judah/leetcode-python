# Get instance
import instaloader

L = instaloader.Instaloader()

# Login or load session
username = "gulnaramum"
password = "Ahfoomiu1234"
L.login(username, password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "argentina_family1")

if __name__ == "__main__":
    # Print list of followees
    follow_list = []
    count = 0
    for followee in profile.get_followers():
        follow_list.append(
            f"https://instagram.com/{followee.username}, {followee.full_name}, {followee.followers}, {followee.follows}, {followee.username}"
        )
        file = open("argentinafamilty_followers.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        print(follow_list[count])
        count = count + 1
