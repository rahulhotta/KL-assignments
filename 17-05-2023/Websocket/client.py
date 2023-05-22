import asyncio
import websockets

# Define the client's behavior when connected to the server
async def connect_to_server():
    # Connect to the WebSocket server
    async with websockets.connect('ws://localhost:8080') as websocket:
        print("Connected to the server.")

        # Continuously send messages to the server
        while True:
            message = input("Enter a message to send: ")
            await websocket.send(message)
            print("Sent message to server:", message)

            # Wait for a response from the server
            response = await websocket.recv()
            print("Received response from server:", response)

# Run the client
asyncio.get_event_loop().run_until_complete(connect_to_server())