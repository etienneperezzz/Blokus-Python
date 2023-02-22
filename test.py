import json

json_string = '{"model": {"current_player":"self.model.current_player.value", "tiles": "self.model.tiles"}}'
json_data = json.loads(json_string)
# Access the data like you would a dictionary
print(json_data["model"]["current_player"])  # Output: value1