FROM python:3.5.6-alpine3.7

ADD feedersbot.py /

RUN cd /tmp/ && \
  wget http://ffmpeg.org/releases/ffmpeg-4.1.tar.gz && \
  tar zxf ffmpeg-4.1.tar.gz && rm ffmpeg-${FFMPEG_VERSION}.tar.gz

# Compile ffmpeg.
RUN cd /tmp/ffmpeg-4.1 && \
  ./configure \
  --prefix=${PREFIX} \
  --enable-version3 \
  --enable-gpl \
  --enable-nonfree \
  --enable-small \
  --enable-libmp3lame \
  --enable-libx264 \
  --enable-libx265 \
  --enable-libvpx \
  --enable-libtheora \
  --enable-libvorbis \
  --enable-libopus \
  --enable-libfdk-aac \
  --enable-libass \
  --enable-libwebp \
  --enable-librtmp \
  --enable-postproc \
  --enable-avresample \
  --enable-libfreetype \
  --enable-openssl \
  --disable-debug \
  --disable-doc \
  --disable-ffplay \
  --extra-libs="-lpthread -lm" && \
  make && make install && make distclean

RUN apk add --no-cache curl python pkgconfig python-dev openssl-dev libffi-dev musl-dev make gcc
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python

RUN python -m pip install --upgrade pip

RUN pip install discord

RUN pip install youtube_dl

RUN pip install

#RUN pip install cffi

RUN pip install pynacl

CMD [ "python", "./feedersbot.py" ]