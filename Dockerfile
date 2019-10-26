FROM sonm/blender:dual-cuda10

RUN mkdir /result

ADD ./stuff/* /

ENTRYPOINT ["/run.sh"]
