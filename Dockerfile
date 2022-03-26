FROM ramadhani892/ramubot:master
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
RUN git clone -b RAM-UBOT https://github.com/ramadhani892/RAM-UBOT /home/ramagans/
WORKDIR /home/ramagans/
CMD ["python3", "-m", "userbot"]
