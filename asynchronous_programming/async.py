import asyncio
import random

# Loading data from server
async def fetch_data(server: str):
    print(f"Request to server  {server}...")
    await asyncio.sleep(random.uniform(1, 3))  
    data = f"data_from_{server}"
    print(f"Data recieved с {server}")
    return data

# Data processing emulation
async def process_data(data: str):
    print(f"Data processing: {data}")
    await asyncio.sleep(random.uniform(0.5, 1.5)) 
    processed = data.upper()
    print(f"Processing complete: {processed}")
    return processed

# Emulation of saving data 
async def save_data(processed: str):
    print(f"Saving: {processed}")
    await asyncio.sleep(0.5)
    print(f"Saved: {processed}")

# Main function to handle 1 server
async def handle_server(server: str):
    data = await fetch_data(server)
    processed = await process_data(data)
    await save_data(processed)

# Main corutine
async def main():
    servers = ['server1', 'server2', 'server3', 'server4']
    
    tasks = [handle_server(s) for s in servers]
    await asyncio.gather(*tasks)

# Runs through event loop
if __name__ == "__main__":
    asyncio.run(main())
