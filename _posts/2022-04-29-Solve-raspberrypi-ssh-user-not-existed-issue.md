---
layout: post
title: 树莓派 ssh 连接失败问题的解决
tag: ['raspberrypi,', 'ssh,', 'debian,', 'openssl']
comments: true
---

# 最新版树莓派系统安装后 ssh 连接失败的问题

## 问题

最近重新配置了树莓派，烧写了 Pi OS Lite 系统，并按照之前的做法无屏配置网络和打开 ssh 功能。但是 ssh 到树莓派后输入密码一直提示“Permission denied, please try again.”，百思不得其解，尝试多次后仍不知问题何在。

## 原因

经过多方搜索，终于发现了问题所在，那就是 2022-04-04 发布的 Pi OS 中移除了默认的 pi 用户: [An update to Raspberry Pi OS Bullseye](https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/)。 而由于这个问题较新，无论是英语还是中文都很难搜到对应的解决方法，最后是在一个 B 站视频评论区里发现了解决方法。

## 解决办法

在 SD 卡的 boot 分区新建一个 `userconf` 或者 `userconf.txt` 文件，里面输入这样格式的 `username:encrypted-password`， username 即用户名，加密的密码部分可以用 openssl 来生成：

```bash
echo 'mypassword' | openssl passwd -6 -stdin
```

这里要求 openssl 的版本要 >= 1.1.1 （1.1.0 踩坑，没有 -6 选项）。而对于没有 openssl 的系统，这里提供一个用户名 `pi` 和密码为 `raspberry` 的结果：`pi:$6$jNFuA8DipMNqijv7$TSOaMKmXctoqWykHD60crnZCoS4eR02rdeVh93sH7KgRRoqwUFJMK9ro6AYXZJzf1yjuGZJrAvuAczBprXVM./`。复制这行到 `userconf` 文件中，重新插入树莓派开机即可使用 ssh 登录 pi 账户。不过这里还是建议登录配置完后通过 `raspi-config` 修改密码或者配置新用户。

## 注

在这以后新烧录的无屏启动的树莓派就需要在 boot 分区额外添加三个文件：`ssh` 空文件、`userconf` 用户密码文件和 `wpa_supplicant.conf` WiFi 配置文件。

并且吐槽树莓派制造商一句，对于带 GUI 版本的 Pi OS 去掉默认用户无可厚非，但是对于 Lite 版本，应该有很多人是使用 ssh 去管理，去掉默认用户而且不在显著位置注明，真的是在浪费人生。