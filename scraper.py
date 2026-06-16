import pandas as pd
import json
import requests

# We will scrape the standard Wikipedia page for the 2026 World Cup
URL = "https://en.wikipedia.org/wiki/2026_FIFA_World_Cup"

# This is our base dictionary. We will update these numbers if we find them on the website.
team_stats = {
    "Argentina": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "USA": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Canada": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Ecuador": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "South Korea": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Ghana": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "France": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Belgium": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Croatia": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Paraguay": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Jordan": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Cape Verde": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Germany": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Morocco": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Austria": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Iran": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Australia": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "South Africa": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Spain": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Norway": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Scotland": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Uzbekistan": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Qatar": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Ivory Coast": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Netherlands": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Mexico": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Sweden": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "DR Congo": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Curacao": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Turkey": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "England": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Japan": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Senegal": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Haiti": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Bosnia": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Panama": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Portugal": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Colombia": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Czech Republic": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "New Zealand": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Switzerland": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Iraq": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Brazil": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Uruguay": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Saudi Arabia": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Tunisia": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Egypt": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0},
    "Algeria": {"pts": 0, "p": 0, "w": 0, "d": 0, "l": 0, "gd": 0, "gf": 0, "ga": 0}
}

try:
    # Read all tables from the Wikipedia page
    tables = pd.read_html(URL, match="Pts")
    
    # Loop through every standings table found
    for df in tables:
        # Wikipedia table headers vary, we map them dynamically
        for index, row in df.iterrows():
            team_name_raw = str(row.iloc[0])
            
            # Clean up Wikipedia strings (remove host symbols, brackets)
            clean_name = team_name_raw.replace("(H)", "").split("[")[0].strip()
            
            # Map alternative names
            name_mapping = {
                "United States": "USA",
                "South Korea": "South Korea", # adjust if Wiki uses "Korea Republic"
                "Congo DR": "DR Congo",
                "Czechia": "Czech Republic",
                "Cabo Verde": "Cape Verde"
            }
            clean_name = name_mapping.get(clean_name, clean_name)

            if clean_name in team_stats:
                # Typically: Pld, W, D, L, GF, GA, GD, Pts
                team_stats[clean_name]["p"] = int(row.get('Pld', 0))
                team_stats[clean_name]["w"] = int(row.get('W', 0))
                team_stats[clean_name]["d"] = int(row.get('D', 0))
                team_stats[clean_name]["l"] = int(row.get('L', 0))
                team_stats[clean_name]["gf"] = int(row.get('GF', 0))
                team_stats[clean_name]["ga"] = int(row.get('GA', 0))
                
                # GD often has special characters like plus/minus signs
                gd_raw = str(row.get('GD', '0')).replace('+', '').replace('−', '-')
                team_stats[clean_name]["gd"] = int(gd_raw) if gd_raw.lstrip('-').isdigit() else 0
                
                team_stats[clean_name]["pts"] = int(row.get('Pts', 0))

except Exception as e:
    print("Could not scrape data or data not available yet:", e)

# Dump the updated data into a JSON file
with open("teamStats.json", "w") as f:
    json.dump(team_stats, f)

print("Data successfully saved to teamStats.json")
