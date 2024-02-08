# services/riot_api.py
import requests
from typing import List
from ..config import API_KEY  # Assuming your API key is stored in config.py

class RiotAPIService:
    def __init__(self):
        self.base_url = "https://REGION.api.riotgames.com"
        self.headers = {"X-Riot-Token": API_KEY}
    
    def get_summoner_by_name(self, summoner_name: str) -> dict:
        url = f"{self.base_url}/tft/summoner/v1/summoners/by-name/{summoner_name}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_match_ids_by_puuid(self, puuid: str, count: int = 20) -> List[str]:
        url = f"{self.base_url}/tft/match/v1/matches/by-puuid/{puuid}/ids?count={count}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    # Add more methods as needed
