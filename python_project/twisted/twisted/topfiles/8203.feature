twisted.protocols.haproxy.proxyEndpoint provides an endpoint that wraps any other stream server endpoint with the PROXY protocol that retains information about the original client connection handled by the proxy; this wrapper is also exposed via the string description prefix 'haproxy'; for example 'twistd web --port haproxy:tcp:8765'.
