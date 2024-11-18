https://github.com/SeleniumHQ/docker-selenium

http://localhost:4444/ui/

http://localhost:7900/?autoconnect=1&resize=scale&password=secret

TODO: Need to make a dev container compose file of Python + Webdriver

docker run --rm -it -p 4444:4444 -p 7900:7900 --shm-size 2g selenium/standalone-chrome
