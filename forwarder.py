import zmq

FRONTEND_URL = "tcp://127.0.0.1:5559"
BACKEND_URL = "ws://127.0.0.1:5556"


def main():
    print(f"Forwarding {FRONTEND_URL} to {BACKEND_URL}")

    try:
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.SUB)
        frontend.bind(FRONTEND_URL)
        
        frontend.setsockopt(zmq.SUBSCRIBE, b"")
        
        # Socket facing services
        backend = context.socket(zmq.PUB)
        backend.bind(BACKEND_URL)

        zmq.proxy(frontend, backend)
    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    main()
