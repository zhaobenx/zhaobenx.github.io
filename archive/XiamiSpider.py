# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 13:59:19 2017

@author: 凌丰
"""
import sys
from urllib.parse import unquote, quote

import urllib.request
import argparse

import json
# import requests


def caesar(location):
    num = int(location[0])
    avg_len = len(location[1:]) // num
    remainder = len(location[1:]) % num

    result = []
    for i in range(remainder):
        line = location[i * (avg_len + 1) + 1: (i + 1) * (avg_len + 1) + 1]
        result.append(line)

    for i in range(num - remainder):
        line = location[(avg_len + 1) * remainder:][i *
                                                    avg_len + 1: (i + 1) * avg_len + 1]
        result.append(line)

    s = []
    for i in range(avg_len):
        for j in range(num):
            s.append(result[j][i])

    for i in range(remainder):
        s.append(result[i][-1])

    return unquote(''.join(s)).replace('^', '0')


def get_url(id):

    target_url = 'http://www.xiami.com/song/playlist/id/' + \
        str(id) + '/object_name/default/object_id/0/cat/json'
    # print(target_url)
    request = urllib.request.Request(target_url)
    request.add_header('content-type', 'application/json')
    request.add_header(
        'User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0')

    response = urllib.request.urlopen(request)
    json_content = json.load(response)
    # print(json_content)
    # print(json_content.json()['data']['trackList'][0]['location'])
    name = json_content['data']['trackList'][0]['songName'] + '-' + \
        json_content['data']['trackList'][0]['singers'] + '.mp3'

    encoded_url = json_content['data']['trackList'][0]['location']

    return name, encoded_url


def download(url, name):
    with open('mp3/' + name, 'wb') as f:
        f.write(urllib.request.urlopen(url).read())


def search(name):
    url = 'http://api.xiami.com/web?v=2.0&app_key=1&key={}&page=1&limit=5&r=search/songs'.format(
        quote(name))
    request = urllib.request.Request(url)
    request.add_header('content-type', 'application/json, text/plain, */*')
    request.add_header(
        'User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0')
    request.add_header('Referer', 'http://m.xiami.com/')
    response = urllib.request.urlopen(request)
    json_content = json.load(response)
    # print(json_content)
    # print(response.read())
    return json_content['data']['songs'][0]['listen_file'],\
        json_content['data']['songs'][0]['song_name'] + '-' +\
        json_content['data']['songs'][0]['artist_name'] + '.mp3'


def download_by_id(id):
    name, encoded_url = get_url(1774490672)
    download(caesar(encoded_url), name)
    print(name + " successful")


def download_by_name(name_list):
    for i in name_list:
        download(*search(i))
        print(i + " successful")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='请输入歌名或id')
    parser.add_argument('-d', type=int, dest='song_id',
                        help='根据id下载')
    parser.add_argument('-n','--name', dest='name_list', default=[], action='append',
                        help='输入歌曲名, 如 --name "hello world",如有空格请以引号括开，可输入多个name')

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args.song_id:
        download_by_id(id)
    if args.name_list:
        download_by_name(args.name_list)
