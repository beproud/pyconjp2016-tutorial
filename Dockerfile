FROM ubuntu:14.04

RUN sed -i 's|archive.ubuntu.com|ftp.tsukuba.wide.ad.jp/Linux|g' /etc/apt/sources.list
RUN apt-get update && apt-get upgrade -y && apt-get install -y sudo whois
RUN useradd -m docker-user -G sudo -p $(mkpasswd -m sha-256 docker-user)
