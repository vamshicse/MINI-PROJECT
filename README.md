# Rainfall Prediction Dashboard

Rainfall Prediction Dashboard is a comprehensive system that combines meteorology, machine learning, and real-time data visualization to predict rainfall and provide actionable insights. The project includes a backend for data processing and machine learning models, and a frontend for interactive and animated data visualization.

## Features

### Backend

- **Real-time Rainfall Prediction**: Uses Random Forest Regressor for accurate predictions.
- **Yearly Rainfall Forecasting**: Employs Linear Regression for long-term forecasting.
- **Live Weather Data Integration**: Fetches live weather data every 5 seconds using OpenWeather API.
- **Emergency Alerts**: Provides alerts for heavy rainfall and potential floods.
- **Self-learning System**: Improves model accuracy over time.

### Frontend

- **Interactive Dashboard**: Displays live rainfall predictions and trends.
- **AI Chatbot**: Answers weather and rainfall-related queries.
- **Location-based Predictions**: Supports predictions for different regions.
- **Dark Mode UI**: Modern design with smooth animations and dark mode support.
- **Customizable Settings**: Allows users to adjust data refresh rates and display preferences.

### Additional Features

- **Emergency Alerts**: Notifies users of extreme weather conditions.
- **Data Visualization**: Interactive graphs for rainfall trends and comparisons.
- **Cloud Deployment**: Hosted on Render/Heroku for public access.

## Technologies Used

- **Backend**: Flask, Scikit-learn, Pandas, Joblib
- **Frontend**: Dash, React.js, Plotly, Bootstrap
- **Database**: SQLite/Firebase
- **API**: OpenWeather API
- **Hosting**: Render/Heroku/AWS

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/miketobz/RainfallPredictionDashboard.git
   cd RainfallPredictionDashboard
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the backend:

   ```bash
   python backend/api.py
   ```

4. Run the frontend:
   ```bash
   python frontend/app.py
   ```

## Deployment

To deploy the project, use the following command:

```bash
npm run deploy
```

## Lessons Learned

- High-dimensional datasets require careful feature selection to avoid overfitting.
- Random Forest Regressor outperformed other models in terms of accuracy.
- Imbalanced datasets can significantly affect model performance.

## Authors

- [@MichaelTobiko](https://github.com/miketobz)

## Acknowledgements

- [What Is a Regression Model?](https://www.imsl.com/blog/what-is-regression-model)
- [Approaching (Almost) Any Machine Learning Problem](https://www.amazon.com/Approaching-Almost-Machine-Learning-Problem/dp/8269211508)
- [Austin Weather Dataset](https://www.kaggle.com/datasets/grubenm/austin-weather)

## 🔗 Links

[![LinkedIn](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/michael-tobiko-1563a693)
[![Twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/MichaelTobiko)
