# Instagram-Crawl
A tool to Crawl post, profile, hashtags information in Instagram.


# 1. Requirements
## 1.1 ChromeDriver
Install it on this [website](https://sites.google.com/chromium.org/driver/) and put it in the directory `bin/`. You have to choose different version which is compatible with your operating system (Mac, windows, Linux). 

And then make your chromedriver verified doing the following steps:
  - open terminal
  - Navigate to path where your chromedriver file is located
  - Execute `xattr -d com.apple.quarantine chromedriver`

Example:
<pre>
$ cd $(Pkg_Path)/Crawl/bin 
$ xattr -d com.apple.quarantine chromedriver
</pre>

## 1.2 Login Information complement
Due to the limitation, you have to put your user information in `Crawl/UserInfo` file including `username` and `password`.

## 1.3 Others
The rest package requirements are written in the `requirement.txt` file.

# 2. How to use?
This program can be used to get Instagram posts/profile/hashtag data without using Instagram API.

There are some arguments in `main.py` you can choose.
<pre>
parser.add_argument(
        "--mode", type=str, default="hashtag", help="options: [posts, posts_full, profile, profile_script, hashtag]"
    )
</pre>

- posts: to get url, caption, first photo for each post.
- posts_full: you will get url, caption, all photos, time, comments, number of likes and views for each post.
- profile: to get the user information including post nums, followers, following numbers.
- profile_script: get more user info than profile mode.
- hashtag: get all the posts' information of tag. It takes much longer to get data if the post number is over about 1000 since Instagram has set up the rate limit for data request

Example
```shell
python main.py --mode posts --username cal_foodie --number 1000 --output output/cal_foodie.json
```

Print the result to the console if not specifying the output path of post `-o, --output`.
