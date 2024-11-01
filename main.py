import streamlit as st
import requests
import json
st.title("SANUTHA'S WEATHER DASHBOARD")
st.subheader("ASIA/COLOMBO WEATHER-REPORT")
def get_weather_data(latitude,longitude):
    
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
    value = requests.get(url)
    if value.status_code == 200:
        data=value.json()
        return data.get('current_weather',{})
    else:
        st.error("failed to retreve data")
        return{}
st.image("image.jpeg")
st.sidebar.write("WAETHER DETAILS")

latitude = st.text_input("Enter Latitude", value="52.52") 
longitude = st.text_input("Enter Longitude",value="13.41")
option = st.sidebar.selectbox("What would you like to choose",
("sunrise", "sunset", "precipitation","max_tempereture","min_tempereture"))
st.sidebar.write("You selected:", option)


if st.button("submit"):
    weather_data=get_weather_data(latitude,longitude)

    if weather_data:
        st.write(f"*Temperature:* {weather_data.get('temperature','N/A')}°C")
        st.write(f"*wind_speed_10m:* {weather_data.get('wind_speed_10m','N/A')}m/s")
        st.write(f"*relative_humidity_2m:* {weather_data.get('relative_humidity_2m','N/A')}r/h")
        temp = weather_data.get("tempereture",0)
        # wind = weather_data.get("wind_speed_10m",0)
        # hum = weather_data.get("relative_humidity_2m",0)
        if temp>25:
            st.success("It's a warm day")
        elif temp>15:
            st.info("It's a mild day")
        else:
            st.warning("It's a cold day")

        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature (°C)", temp)
        col2.metric("Wind Speed (m/s)", weather_data.get('windspeed', 0))
        col3.metric("Humidity (%)", weather_data.get('relative_humidity', 'N/A'))

# Lat = value['latitude']
# Long = value['longitude']
# temp = value["current"]["temperature_2m"]
# wind = value['current']['wind_speed_10m']
# hum = value['current']["relative_humidity_2m"]
# col1.metric('Temperature',temp) 
# col2.metric("Wind", wind)
# col3.metric("Humidity", hum )
st.video("https://www.youtube.com/watch?v=-nc146I26SU&pp=ygUNd2VhdGhlciB2aWRlbw%3D%3D")
# background-image: ("")
# st.markdown(page_bg_img, unsafe_allow_html=True) 
# st.write('Latitude: ' + str(Lat))
# st.write('Longtitude: ' + str(Long))

# import streamlit as st
# import requests
# import json

# # Basic app information
# st.write("Sanutha")
# st.title("SANUTHA'S WEATHER DASHBOARD")
# st.subheader("ASIA/COLOMBO WEATHER-REPORT")

# # API request
# resp = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true')
# # Correcting the URL to `current_weather=true` to get current weather data
# if resp.status_code == 200: # Check if the request was successful
# value = resp.json() # Using `.json()` directly instead of `json.loads(resp.text)`
# st.image("image.jpeg")

# # Sidebar setup
# st.sidebar.write("WEATHER DETAILS")
# option = st.sidebar.selectbox("What would you like to choose",
# ("sunrise", "sunset", "precipitation", "max_temperature", "min_temperature"))
# st.sidebar.write("You selected:", option)

# # Latitude and longitude inputs
# latitude = st.sidebar.text_input("Latitude", value="52.52")
# longitude = st.sidebar.text_input("Longitude", value="13.41")

# # Accessing weather values from the JSON response
# try:
# # Updated API response parsing based on correct fields
# temp = value["current_weather"]["temperature"]
# wind = value["current_weather"]["windspeed"]
# hum = value["current_weather"].get("humidity", "N/A") # Humidity may not always be available

# # Displaying metrics
# col1, col2, col3 = st.columns(3)
# col1.metric('Temperature (°C)', temp)
# col2.metric("Wind Speed (m/s)", wind)
# col3.metric("Humidity (%)", hum)

# # Display selected video
# st.video("https://www.youtube.com/watch?v=-nc146I26SU")

# # Display longitude if needed
# st.write('Longitude:', longitude)
# except KeyError:
# st.error("Could not retrieve all weather data. Please check the response format or try again.")

# else:
# st.error("Failed to retrieve data. Please check the API or your connection.")
