# Using Python Slim-Buster
FROM skyzuxzy/skyzu-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Rzydx-Userbot ━━━━━
    
RUN git clone -b Rzydx-Userbot https://github.com/Rzydx/Rzydx-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Rzydx/Rzydx-Userbot/Rzydx-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
