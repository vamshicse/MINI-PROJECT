import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import requests

# Weather API details
API_KEY = "0a78d51d997a1b4a0a822973ff99e173"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# App layout
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("Rainfall Prediction Dashboard", className="text-center text-warning"), width=12),
        className="mb-4"
    ),
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Input(
                    id="city-input",
                    type="text",
                    placeholder="Enter city name...",
                    className="form-control mb-2",
                    style={"width": "100%"}
                ),
                dbc.Button("Search", id="search-button", color="success", className="w-100")
            ], className="mb-4"),
            html.Div(id="weather-icon", className="text-center mb-3"),
            html.H4(id="city-name", className="text-center text-warning"),
            html.H2(id="temperature", className="text-center text-warning"),
            html.P(id="weather-description", className="text-center text-warning"),
            html.P(id="humidity", className="text-center text-warning"),
            html.P(id="wind-speed", className="text-center text-warning"),
            html.P(id="rain-prediction", className="text-center text-danger")
        ], width=4, className="bg-dark p-4 rounded"),
        dbc.Col([
            dcc.Graph(id="weather-chart", config={"displayModeBar": False})
        ], width=8)
    ])
], fluid=True, className="bg-light text-dark p-4")

# Callback to fetch weather data and update UI
@app.callback(
    [
        Output("city-name", "children"),
        Output("temperature", "children"),
        Output("weather-description", "children"),
        Output("humidity", "children"),
        Output("wind-speed", "children"),
        Output("rain-prediction", "children"),
        Output("weather-icon", "children"),
        Output("weather-chart", "figure")
    ],
    [Input("search-button", "n_clicks")],
    [dash.dependencies.State("city-input", "value")]
)
def update_weather(n_clicks, city):
    if not city:
        return ["Enter a city name to get started!", "", "", "", "", "", "", {}]

    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Extract weather details
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        rain_volume = data.get("rain", {}).get("1h", 0)

        rain_prediction = "No rain expected."
        if "rain" in weather_desc or "drizzle" in weather_desc or "thunderstorm" in weather_desc:
            rain_prediction = "It might rain. Carry an umbrella!"
            if rain_volume == 0:
                rain_prediction += " Light drizzle expected soon."
            elif rain_volume < 2.5:
                rain_prediction += " Light rain."
            elif 2.5 <= rain_volume < 10:
                rain_prediction += " Moderate rain."
            elif 10 <= rain_volume < 50:
                rain_prediction += " Heavy rain."
            else:
                rain_prediction += " Intense rainfall or storm!"

        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        weather_icon = html.Img(src=icon_url, style={"width": "100px", "height": "100px"})

        chart_figure = {
            "data": [
                {"x": ["Morning", "Afternoon", "Evening", "Night"], "y": [temp, temp + 2, temp - 1, temp - 3], "type": "bar"}
            ],
            "layout": {
                "title": "Temperature Variation",
                "xaxis": {"title": "Time of Day"},
                "yaxis": {"title": "Temperature (°C)"},
                "plot_bgcolor": "#222",
                "paper_bgcolor": "#222",
                "font": {"color": "white"}
            }
        }

        return [
            f"Weather in {city.capitalize()}",
            f"{temp}°C",
            f"Condition: {weather_desc.capitalize()}",
            f"Humidity: {humidity}%",
            f"Wind Speed: {wind_speed} m/s",
            rain_prediction,
            weather_icon,
            chart_figure
        ]
    except requests.exceptions.RequestException as e:
        return [f"Error fetching weather data: {e}", "", "", "", "", "", "", {}]

if __name__ == "__main__":
    app.run(debug=False)  # Disable debug mode to avoid unnecessary errors