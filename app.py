# Import required libraries
import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.graph_objects as go

# Define emotions and their associated colors
emotions = ['Angry', 'Disgusted', 'Sad', 'Happy', 'Surprised', 'Fearful']
colors = ['#e74c3c', '#9b59b6', '#3498db', '#2ecc71', '#f1c40f', '#e67e22']

# Define function to draw emotional wheel
def draw_emotional_wheel(center_x, center_y, sizes, colors, angles, coordinates, emotions, percentages):
    st.title('Emotional Wheel')
    st.write('The Emotional Wheel shows the dominant emotions based on the input activities.')
    with st.container():
        chart_data = pd.DataFrame({
            'sizes': sizes,
            'colors': colors,
            'angles': angles,
            'coordinates': coordinates,
            'emotions': emotions,
            'percentages': percentages
        })
        fig = go.Figure(
            go.Pie(
                values=chart_data['sizes'],
                labels=chart_data['emotions'],
                hole=0.7,
                sort=False,
                marker={'line': {'color': 'white', 'width': 2}},
                opacity=0.8,
                textinfo='none',
                direction='clockwise',
                title='Emotional Wheel',
                hovertemplate='<b>%{label}</b><br><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
            )
        )
        fig.update_traces(
            hoverinfo='label+value+percent',
            textinfo='none',
            marker=dict(line=dict(color='#000000', width=2))
        )
        for i, coord in enumerate(coordinates):
            fig.add_annotation(
                x=coord[0],
                y=coord[1],
                text=f"{emotions[i]}<br>{percentages[i]}%",
                showarrow=False,
                font=dict(size=24),
                xanchor='center',
                yanchor='middle'
            )
        fig.update_layout(
            title='Emotional Wheel',
            width=800,
            height=800
        )
        st.plotly_chart(fig)

def get_emotion(sentiment_scores):
    # Define the logic for determining emotions based on sentiment scores
    if sentiment_scores['compound'] >= 0.05:
        return "Happy"
    elif sentiment_scores['compound'] <= -0.05:
        return "Sad"
    elif sentiment_scores['pos'] > sentiment_scores['neg']:
        return "Happy"
    elif sentiment_scores['neg'] > sentiment_scores['pos']:
        return "Sad"
    elif sentiment_scores['compound'] > 0 and sentiment_scores['neu'] > sentiment_scores['compound']:
        return "Surprised"
    elif sentiment_scores['compound'] < 0 and sentiment_scores['neu'] > -sentiment_scores['compound']:
        return "Disgusted"
    else:
        return "Angry"

# Get input from user
center_x = 400
center_y = 400

analyzer = SentimentIntensityAnalyzer()
input_activities = st.text_input('Enter activities separated by comma:')
if input_activities:
    activities = input_activities.split(',')
    emotions_count = {emotion: 0 for emotion in emotions}
    sentiment_scores_list = []

    for activity in activities:
        sentiment_score = analyzer.polarity_scores(activity)
        dominant_emotion = get_emotion(sentiment_score)
        emotions_count[dominant_emotion] += 1
        sentiment_scores_list.append(sentiment_score)

    total = sum(emotions_count.values())
    percentages = [f"{count / total * 100:.2f}%" for count in emotions_count.values()]
    sizes = [count / total for count in emotions_count.values()]  # Sizes based on counts
    
    angles = [count / total * 360 for count in emotions_count.values()]
    coordinates = [(center_x + size * pd.np.sin(pd.np.radians(sum(angles[:i+1]))), center_y + size * pd.np.cos(pd.np.radians(sum(angles[:i+1])))) for i, size in enumerate(sizes)]
    
    # Print sentiment scores
    st.write("Sentiment Scores:")
    for i, sentiment_score in enumerate(sentiment_scores_list):
        st.write(f"Activity {i+1}: {sentiment_score}")

    draw_emotional_wheel(center_x=400, center_y=400, sizes=sizes, colors=colors, angles=angles, coordinates=coordinates, emotions=emotions, percentages=percentages)
