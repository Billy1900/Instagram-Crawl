from __future__ import unicode_literals

import argparse
import json
import sys
import os
from io import open

from Crawl.crawler import InsCrawler
from Crawl.settings import override_settings
from Crawl.settings import prepare_override_settings


def usage():
    return """
        python main.py posts -u cal_foodie -n 100 -o ./output
        python main.py posts_full -u cal_foodie -n 100 -o ./output
        python main.py profile -u cal_foodie -o ./output
        python main.py profile_script -u cal_foodie -o ./output
        python main.py hashtag -t taiwan -o ./output
        The default number for fetching posts via hashtag is 100.
    """


def get_posts_by_user(username, number, detail, debug):
    ins_crawler = InsCrawler(has_screen=debug)
    return ins_crawler.get_user_posts(username, number, detail)


def get_profile(username):
    ins_crawler = InsCrawler()
    return ins_crawler.get_user_profile(username)


def get_profile_from_script(username):
    ins_cralwer = InsCrawler()
    return ins_cralwer.get_user_profile_from_script_shared_data(username)


def get_posts_by_hashtag(tag, number, debug):
    ins_crawler = InsCrawler(has_screen=debug)
    return ins_crawler.get_latest_posts_by_tag(tag, number)


def arg_required(args, fields=[]):
    for field in fields:
        if not getattr(args, field):
            parser.print_help()
            sys.exit()


def output(data, filepath):
    out = json.dumps(data, ensure_ascii=False)
    if filepath:
        filepath = os.path.join(os.path.abspath(os.curdir), filepath)
        with open(filepath, "w", encoding="utf8") as f:
            f.write(out)
    else:
        print(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram Crawler", usage=usage())
    parser.add_argument(
        "--mode", type=str, default="hashtag", help="options: [posts, posts_full, profile, profile_script, hashtag]"
    )
    parser.add_argument("-n", "--number", type=int, default=5, help="number of returned posts")
    parser.add_argument("-u", "--username", type=str, default="", help="instagram's username you want to crawl")
    parser.add_argument("-t", "--tag", type=str, default="", help="instagram's tag name")
    parser.add_argument("-o", "--output", type=str, default="output/hashtag.json", help="output file name(json format)")
    parser.add_argument("--debug", action="store_true")

    prepare_override_settings(parser)
    args = parser.parse_args()
    override_settings(args)

    if args.mode in ["posts", "posts_full"]:
        arg_required("username")
        output(
            get_posts_by_user(
                args.username, args.number, args.mode == "posts_full", args.debug
            ),
            args.output,
        )
    elif args.mode == "profile":
        arg_required("username")
        output(get_profile(args.username), args.output)
    elif args.mode == "profile_script":
        arg_required("username")
        output(get_profile_from_script(args.username), args.output)
    elif args.mode == "hashtag":
        arg_required("tag")
        output(
            get_posts_by_hashtag(args.tag, args.number, args.debug), args.output
        )
    else:
        usage()
