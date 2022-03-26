FROM rzydx/rzydxuserbot:master
# ======================
#    Rzydx-Userbot DOCKER
#   FROM DOCKERHUB.COM
# ======================
RUN git clone -b Rzydx-Userbot https://github.com/Rzydx/Rzydx-Userbot /home/rzydx/
WORKDIR /home/rzydx/
CMD ["python3", "-m", "userbot"]
