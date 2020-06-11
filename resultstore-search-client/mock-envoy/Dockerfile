FROM envoyproxy/envoy:v1.14.1
COPY ./envoy.yaml /etc/envoy_mock/envoy.yaml
CMD /usr/local/bin/envoy -c /etc/envoy_mock/envoy.yaml
