import asyncio ,websockets,json,requests


async def websocket_to_local(websocket_uri):
    async with websockets.connect(websocket_uri) as websocket:
        print("Connected to WebSocket server")
        while True:
            data = await websocket.recv()
            try:
                json_data = json.loads(data)
                print("Received JSON data:")
            
                def intent_handling(str):
                    match str:
                        case "playmusic":
                            name=json_data['tokens'][1]
                            local_uri="http://localhost:5000/api/music/play/"+name
                            return requests.post(local_uri, json=json_data)
                        case "pausemusic":
                            local_uri="http://localhost:5000/api/music/pause"
                            return requests.post(local_uri, json=json_data)
                        case "getmusiclibrary":
                            local_uri= "http://localhost:5000/api/music/library"
                            return requests.get(local_uri)
                        case "unpausemusic":
                            local_uri= "http://localhost:5000/api/music/unpause"
                            return requests.post(local_uri, json=json_data)
                        case "stopmusic":
                            local_uri= "http://localhost:5000/api/music/stop"
                            return requests.post(local_uri, json=json_data)
                        case "getmusic":
                            last=json_data['tokens'][-1]
                            local_uri= "http://localhost:5000/api/music/library/"+last
                            return requests.get(local_uri)    
                        case "createtask":
                            local_uri= "http://localhost:5000/api/todolist/create"
                            return requests.post(local_uri, json=json_data)
                        case "gettasks":
                            local_uri= "http://localhost:5000/api/todolist/tasks"
                            return requests.get(local_uri)
                        case "gettask":
                            last=json_data['tokens'][-1]
                            local_uri= "http://localhost:5000/api/todolist/tasks/" +last
                            return requests.get(local_uri)     
                        case "updatetask":
                            last=json_data['tokens'][4]
                            local_uri= "http://localhost:5000/api/todolist/tasks/" +last
                            return requests.put(local_uri, json=json_data)
                        case "deletetask":
                            last=json_data['tokens'][-1]
                            local_uri= "http://localhost:5000/api/todolist/tasks/" +last
                            return requests.delete(local_uri)               
                
                response=intent_handling(json_data["intent"]["name"])
                print("Response from local server:", response.text)
            except json.JSONDecodeError:
                print("Received non-JSON data")

if __name__ == "__main__":
    websocket_uri ="ws://localhost:12101/api/events/intent"
    asyncio.run(websocket_to_local(websocket_uri))

