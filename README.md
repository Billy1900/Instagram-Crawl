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
```shell
$ cd $(Pkg_Path)/Crawl/bin 
$ xattr -d com.apple.quarantine chromedriver
```

## 1.2 Login Information complement
Due to the limitation, you have to put your user information in `Crawl/UserInfo` file including `username` and `password`.

## 1.3 Others
The rest package requirements are written in the `requirement.txt` file.

# 2. How to use?
This program can be used to get Instagram posts/profile/hashtag data without using Instagram API.

There are some arguments in `main.py` you can choose.
```python
parser.add_argument(
        "--mode", type=str, default="hashtag", help="options: [posts, posts_full, profile, profile_script, hashtag]"
    )
```

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

# 3. Supplementary
- [youtube-dl](https://github.com/ytdl-org/youtube-dl) is a command-line program to download videos from YouTube.com and a few more sites. It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform specific.
- [Annie](https://github.com/iawia002/annie) is a fast, simple and clean video downloader built with Go.
- [Geziyor](https://github.com/geziyor/geziyor): Geziyor is a blazing fast web crawling and web scraping framework. It can be used to crawl websites and extract structured data from them. Geziyor is useful for a wide range of purposes such as data mining, monitoring and automated testing.
