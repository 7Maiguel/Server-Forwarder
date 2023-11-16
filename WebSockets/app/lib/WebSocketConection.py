import asyncio
import websockets
import json

async def connect_to_action_cable():
    uri = "wss://prod-migration.fusepong.com/cable"

    async with websockets.connect(uri) as websocket:
        # Autenticación si es necesaria (ajusta según tus requisitos)
        # Aquí asumimos que estás utilizando un token para la autenticación
        authentication_payload = {
            "command": "subscribe",
            "identifier": json.dumps({"channel": "6"})
        }
        await websocket.send(json.dumps(authentication_payload))

        # Manejar mensajes recibidos
        async for message in websocket:
            print("Mensaje recibido:")
            print(message)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_to_action_cable())
