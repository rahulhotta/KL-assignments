import asyncio
import websockets

# Define the server's behavior when a connection is established
async def handle_connection(websocket, path):
    print("A client has connected.")

    # Continuously listen for messages from the client
    while True:
        message = await websocket.recv()
        print("Received message from client:", message)

        # Send a response back to the client
        response = "Server received your message: " + message
        await websocket.send(response)

# Start the WebSocket server
start_server = websockets.serve(handle_connection, 'localhost', 8080)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()