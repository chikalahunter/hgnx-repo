from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
import pytz
import os

app = FastAPI()

@app.get("/get_info")
async def get_info(
    slack_name: str = Query(..., description="chika ugwu"),
    track: str = Query(..., description="Backend"),
):
    # Get current day of the week
    current_day = datetime.now(pytz.utc).strftime('%A')

    # Get current UTC time
    current_time = datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get GitHub URLs
    github_url = 'https://github.com/chikalahunter/hgnx-repo'
    github_file_url = f'https://github.com/chikalahunter/hgnx-repo/blob/main/Hngx%20first%20task'
    github_source_url = f'https://github.com/chikalahunter/hgnx-repo/tree/main'

    # Create the response JSON
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_source_url': github_source_url,
        'status_code': 200
    }

    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

