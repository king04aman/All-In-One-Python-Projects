import requests
import folium

# Function to fetch real-time traffic data based on GPS coordinates
def get_traffic_data(lat, lng):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"https://api.trafficapi.com/v1/traffic?latitude={lat}&longitude={lng}&key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # Returns JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching traffic data: {e}")
        return None
   
# Function to visualize traffic data on a map
def visualize_traffic(data, lat, lng):
    # Create a map centered around the given GPS coordinates
    m = folium.Map(location=[lat, lng], zoom_start=12)

    # Check if traffic data exists
    if data and "incidents" in data:
        for incident in data['incidents']:
            folium.Marker(
                location=[incident['lat'], incident['lng']],
                popup=incident['description'],
                icon=folium.Icon(color='red')
            ).add_to(m)
    else:
        print("No traffic incidents found.")

    # Save the map to an HTML file
    m.save("traffic_map.html")
    print("Traffic map saved as traffic_map.html")

def main():
    # Example GPS coordinates (latitude, longitude)
    lat = 37.7749  # Replace with your latitude
    lng = -122.4194  # Replace with your longitude

    # Fetch real-time traffic data
    traffic_data = get_traffic_data(lat, lng)

    # Visualize the traffic on a map
    visualize_traffic(traffic_data, lat, lng)

if __name__ == "__main__":
    main()
