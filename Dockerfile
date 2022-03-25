FROM rzydx/rzydx-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Rzydx-Userbot https://github.com/Rzydx/Rzydx-Userbot /home/Rzydx-Userbot/ \
    && chmod 777 /home/Rzydx-Userbot \
    && mkdir /home/Rzydx-Userbot/bin/
WORKDIR /home/Rzydx-Userbot/
COPY ./sample_config.env ./config.env* /home/Rzydx-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
