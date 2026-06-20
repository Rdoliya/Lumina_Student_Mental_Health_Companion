# IMPORTS
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import re

# CONFIGURATION & CONSTANTS

# Color Scheme - Dark & Relaxing palette
COLORS = {
    'primary_green': '#2D5A41', # Darker forest green
    'light_green': '#1E3226',   # Deep leaf green
    'primary_blue': '#1A3A5F',  # Deep ocean blue
    'light_blue': '#0D1B2A',    # Midnight blue
    'neutral_gray': '#121212',  # Near black
    'light_gray': '#1E1E1E',    # Dark gray surface
    'alert_red': '#D32F2F',     # Muted alert red
    'alert_orange': '#F57C00',  # Muted warning orange
    'text_dark': '#E0E0E0',     # Light text for dark background
    'text_light': '#B0BEC5'     # Sub-text gray
}

# Sentiment Thresholds
# Rationale: VADER compound score ranges from -1 (most negative) to +1 (most positive)
# - Negative threshold (-0.1): Slightly below neutral to catch mild distress
# - Positive threshold (0.4): Above neutral to ensure genuine positive sentiment
SENTIMENT_THRESHOLDS = {
    'negative': -0.1,   # Below this is considered negative
    'positive': 0.4     # Above this is considered positive
}

# Crisis Keywords - Comprehensive list for safety detection
# Case-insensitive matching for maximum coverage
CRISIS_KEYWORDS = [
    'suicide', 'self-harm', 'kill myself', 'end it all', 
    'not worth living', 'want to die', 'die', 'death',
    'hurt myself', 'end my life', 'no reason to live',
    'better off dead', 'want to end it', 'suicidal',
    'cut myself', 'harm myself', 'kill me'
]

# Relaxation Tips for Negative Sentiment
RELAXATION_TIPS = [
    {
        'title': 'Box Breathing Technique',
        'steps': [
            'Inhale slowly through your nose for 4 seconds',
            'Hold your breath for 4 seconds',
            'Exhale slowly through your mouth for 4 seconds',
            'Hold your breath again for 4 seconds',
            'Repeat this cycle 4-5 times'
        ]
    },
    {
        'title': '5-4-3-2-1 Grounding',
        'steps': [
            'Identify 5 things you can see around you',
            'Identify 4 things you can touch',
            'Identify 3 things you can hear',
            'Identify 2 things you can smell',
            'Identify 1 thing you can taste'
        ]
    },
    {
        'title': 'Progressive Muscle Relaxation',
        'steps': [
            'Start with your toes - tense them for 5 seconds, then relax',
            'Move to your calves - tense and relax',
            'Continue up through your body: thighs, stomach, hands, shoulders',
            'Finally, tense your face muscles and release',
            'Notice the difference between tension and relaxation'
        ]
    }
]

# Motivational Quotes for Neutral Sentiment
MOTIVATIONAL_QUOTES = [
    "You are stronger than you think. Every small step forward is progress.",
    "Your feelings are valid, and it's okay to take time to process them.",
    "Remember: You've survived 100% of your worst days so far.",
    "Be gentle with yourself. You're doing the best you can.",
    "This too shall pass. Every storm runs out of rain eventually.",
    "You don't have to have it all figured out. Take it one day at a time.",
    "Your mental health is a priority. Your happiness is essential.",
    "It's okay to not be okay. What matters is that you're here, trying.",
    "Progress, not perfection. Every day is a new opportunity.",
    "You are worthy of love, happiness, and peace."
]

# Gratitude Journaling Prompts for Positive Sentiment
GRATITUDE_PROMPTS = [
    "What made you smile today?",
    "Who are you grateful to have in your life?",
    "What's a small victory you achieved recently?",
    "What's something beautiful you noticed today?",
    "Who made a positive impact on you recently?",
    "What are you looking forward to tomorrow?",
    "What's a skill or talent you appreciate about yourself?",
    "What's a comfort or privilege you often take for granted?"
]

# Emergency Resources
EMERGENCY_RESOURCES = {
    'hotline': 'National Suicide Prevention Lifeline: 988',
    'text_line': 'Crisis Text Line: Text HOME to 741741',
    'disclaimer': "I'm an AI and not a substitute for professional help. If you're in crisis, please reach out to a mental health professional or emergency services."
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def initialize_session_state():
    """
    Initialize session state variables for persistent chat history and tracking.
    Called at the start of the application to ensure all state variables exist.
    """
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    if 'sentiment_scores' not in st.session_state:
        st.session_state.sentiment_scores = []
    
    if 'timestamps' not in st.session_state:
        st.session_state.timestamps = []
    
    if 'session_start' not in st.session_state:
        st.session_state.session_start = datetime.now()
    
    if 'message_count' not in st.session_state:
        st.session_state.message_count = 0

def analyze_sentiment(text):
    """
    Analyze the sentiment of input text using VADER.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Dictionary containing sentiment scores (compound, positive, negative, neutral)
              Returns None if analysis fails
    """
    try:
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(text)
        return sentiment
    except Exception as e:
        st.error(f"Sentiment analysis error: {e}")
        return None

def detect_crisis_keywords(text):
    """
    Detect crisis-related keywords in user input.
    
    Args:
        text (str): Input text to check
        
    Returns:
        bool: True if crisis keywords detected, False otherwise
    """
    text_lower = text.lower()
    for keyword in CRISIS_KEYWORDS:
        if keyword in text_lower:
            return True
    return False

def get_sentiment_category(compound_score):
    """
    Categorize sentiment based on compound score.
    
    Args:
        compound_score (float): VADER compound sentiment score
        
    Returns:
        str: 'negative', 'neutral', or 'positive'
    """
    if compound_score < SENTIMENT_THRESHOLDS['negative']:
        return 'negative'
    elif compound_score > SENTIMENT_THRESHOLDS['positive']:
        return 'positive'
    else:
        return 'neutral'

def generate_negative_response():
    """
    Generate empathetic response for negative sentiment.
    Includes relaxation tip and supportive language.
    
    Returns:
        str: Empathetic response with relaxation technique
    """
    import random
    
    # Select a random relaxation tip
    tip = random.choice(RELAXATION_TIPS)
    
    response = f"I hear you, and I want you to know that your feelings are completely valid. It takes courage to share when you're struggling, and I'm here to support you.\n\n"
    response += f"**{tip['title']}**\n\n"
    for i, step in enumerate(tip['steps'], 1):
        response += f"{i}. {step}\n"
    response += f"\nRemember, it's okay to take things one moment at a time. You're not alone in this."
    
    return response

def generate_neutral_response():
    """
    Generate supportive response for neutral sentiment.
    Includes motivational quote and encourages sharing.
    
    Returns:
        str: Supportive response with motivational quote
    """
    import random
    
    quote = random.choice(MOTIVATIONAL_QUOTES)
    
    response = f"Thank you for sharing that with me. I'm here to listen and support you however I can.\n\n"
    response += f"**{quote}**\n\n"
    response += "Feel free to share more about what's on your mind. Sometimes just expressing our thoughts can help us process them better."
    
    return response

def generate_positive_response():
    """
    Generate celebratory response for positive sentiment.
    Includes gratitude journaling prompt and reinforces positivity.
    
    Returns:
        str: Celebratory response with gratitude prompt
    """
    import random
    
    prompt = random.choice(GRATITUDE_PROMPTS)
    
    response = f"That's wonderful to hear! 🌟 It's beautiful when we can recognize and appreciate positive moments in our lives.\n\n"
    response += f"**Gratitude Moment:** {prompt}\n\n"
    response += "Taking time to acknowledge the good things, no matter how small, can help build resilience and attract more positivity into our lives. Keep nurturing that positive mindset!"
    
    return response

def generate_crisis_response():
    """
    Generate emergency response for crisis situations.
    Displays emergency resources prominently.
    
    Returns:
        str: Crisis response with emergency resources
    """
    response = f"⚠️ **I'm concerned about what you've shared, and I want you to know that help is available.** ⚠️\n\n"
    response += f"**📞 {EMERGENCY_RESOURCES['hotline']}**\n\n"
    response += f"**💬 {EMERGENCY_RESOURCES['text_line']}**\n\n"
    response += f"Please reach out to these resources. They are available 24/7 and staffed by trained professionals who can help.\n\n"
    response += f"*{EMERGENCY_RESOURCES['disclaimer']}*"
    
    return response

def generate_response(user_input, sentiment_result):
    """
    Generate appropriate response based on sentiment analysis.
    
    Args:
        user_input (str): User's message
        sentiment_result (dict): Sentiment analysis results
        
    Returns:
        str: Generated response
    """
    # Check for crisis keywords first (highest priority)
    if detect_crisis_keywords(user_input):
        return generate_crisis_response()
    
    # Get sentiment category
    compound_score = sentiment_result['compound']
    category = get_sentiment_category(compound_score)
    
    # Generate response based on category
    if category == 'negative':
        return generate_negative_response()
    elif category == 'positive':
        return generate_positive_response()
    else:
        return generate_neutral_response()

def create_mood_chart():
    """
    Create a line chart showing sentiment scores over the session.
    
    Returns:
        plotly.graph_objects.Figure: Interactive mood chart
    """
    if not st.session_state.sentiment_scores:
        return None
    
    # Create data for chart
    message_numbers = list(range(1, len(st.session_state.sentiment_scores) + 1))
    scores = st.session_state.sentiment_scores
    
    # Create figure
    fig = go.Figure()
    
    # Add line trace
    fig.add_trace(go.Scatter(
        x=message_numbers,
        y=scores,
        mode='lines+markers',
        name='Sentiment Score',
        line=dict(color=COLORS['primary_blue'], width=3),
        marker=dict(size=8, color=COLORS['primary_green'])
    ))
    
    # Add zero line for reference
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    # Update layout
    fig.update_layout(
        title="Your Mood Throughout the Session",
        xaxis_title="Message Number",
        yaxis_title="Sentiment Score",
        yaxis=dict(range=[-1, 1]),
        template="plotly_white",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(size=12)
    )
    
    return fig

def display_breathing_exercise():
    """
    Display guided breathing exercise instructions.
    """
    st.markdown("### 🌬️ Box Breathing Exercise")
    st.markdown("This technique helps reduce stress and promote calm.")
    
    with st.expander("Start Breathing Exercise", expanded=False):
        st.markdown("""
        **Follow this 4-4-4-4 pattern:**
        
        1. **Inhale** slowly through your nose for **4 seconds** 🫁
        2. **Hold** your breath for **4 seconds** ⏸️
        3. **Exhale** slowly through your mouth for **4 seconds** 💨
        4. **Hold** your breath again for **4 seconds** ⏸️
        
        **Repeat this cycle 4-5 times**
        
        *Tip: Focus on counting and your breath to help calm your mind.*
        """)

def calculate_session_stats():
    """
    Calculate session statistics.
    
    Returns:
        dict: Dictionary containing session statistics
    """
    if not st.session_state.sentiment_scores:
        return {
            'messages': 0,
            'avg_sentiment': 0,
            'duration': '0 minutes'
        }
    
    avg_sentiment = sum(st.session_state.sentiment_scores) / len(st.session_state.sentiment_scores)
    duration = datetime.now() - st.session_state.session_start
    duration_minutes = int(duration.total_seconds() / 60)
    
    return {
        'messages': len(st.session_state.sentiment_scores),
        'avg_sentiment': avg_sentiment,
        'duration': f"{duration_minutes} minutes"
    }

def clear_chat_history():
    """
    Clear all chat history and reset session state.
    """
    st.session_state.chat_history = []
    st.session_state.sentiment_scores = []
    st.session_state.timestamps = []
    st.session_state.session_start = datetime.now()
    st.session_state.message_count = 0

# =============================================================================
# MAIN APPLICATION LOGIC
# =============================================================================

def main():
    """
    Main application function that orchestrates the entire Lumina experience.
    """
    # Page configuration
    st.set_page_config(
        page_title="Lumina - Mental Health Companion",
        page_icon="🌟",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for styling
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: {COLORS['light_gray']};
        }}
        .main {{
            padding: 2rem;
        }}
        h1 {{
            color: {COLORS['text_dark']};
            font-weight: 600;
        }}
        .stChatMessage {{
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }}
        .alert-box {{
            background-color: {COLORS['alert_red']};
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }}
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    initialize_session_state()
    
    # =============================================================================
    # SIDEBAR
    # =============================================================================
    with st.sidebar:
        st.markdown(f"""
        <div style='background-color: {COLORS['light_green']}; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;'>
            <h2 style='color: {COLORS['text_dark']}; margin: 0;'>🌟 Lumina</h2>
            <p style='color: {COLORS['text_light']}; margin: 0.5rem 0 0 0;'>Your Mental Health Companion</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Mood Tracker Chart
        st.markdown("### 📊 Mood Tracker")
        mood_chart = create_mood_chart()
        if mood_chart:
            st.plotly_chart(mood_chart, use_container_width=True)
        else:
            st.info("Start chatting to see your mood patterns!")
        
        st.markdown("---")
        
        # Breathing Exercise
        display_breathing_exercise()
        
        st.markdown("---")
        
        # Session Statistics
        st.markdown("### 📈 Session Stats")
        stats = calculate_session_stats()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Messages", stats['messages'])
        with col2:
            st.metric("Duration", stats['duration'])
        
        avg_sentiment_emoji = "😊" if stats['avg_sentiment'] > 0 else "😔" if stats['avg_sentiment'] < 0 else "😐"
        st.metric(f"Avg Mood {avg_sentiment_emoji}", f"{stats['avg_sentiment']:.2f}")
        
        st.markdown("---")
        
        # Clear Chat Button
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            if st.session_state.chat_history:  # Only ask if there's history
                if st.confirm("Are you sure you want to clear all chat history?"):
                    clear_chat_history()
                    st.success("Chat history cleared!")
                    st.rerun()
        
        st.markdown("---")
        
        # Disclaimer
        st.markdown(f"""
        <div style='background-color: {COLORS['light_blue']}; padding: 1rem; border-radius: 10px; font-size: 0.85rem;'>
            <strong>⚠️ Disclaimer:</strong><br>
            Lumina is an AI companion and not a substitute for professional mental health care. If you're experiencing severe distress, please consult a mental health professional.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Developer Information
        st.markdown("### 👨‍💻 Developer")
        st.markdown(f"""
        <div style='font-size: 0.85rem;'>
            <strong>Rishyup Doliya</strong><br>
            📱 +91 7206988702<br>
            📧 Rishyup.doliya@gmail.com<br>
            🔗 <a href='https://www.linkedin.com/in/rishyup-doliya-833b352b0/' target='_blank'>LinkedIn</a><br>
            💻 <a href='https://github.com/rishyup' target='_blank'>GitHub</a>
        </div>
        """, unsafe_allow_html=True)
    
    # =============================================================================
    # MAIN CHAT INTERFACE
    # =============================================================================
    
    # Header
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {COLORS['primary_green']}, {COLORS['primary_blue']}); padding: 2rem; border-radius: 15px; margin-bottom: 2rem;'>
        <h1 style='color: white; margin: 0; text-align: center;'>🌟 Welcome to Lumina</h1>
        <p style='color: white; margin: 1rem 0 0 0; text-align: center; font-size: 1.1rem;'>
            Your safe space to share thoughts, feelings, and emotions. I'm here to listen, support, and help you navigate whatever you're experiencing.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display chat history
    for i, (role, message, sentiment, timestamp) in enumerate(st.session_state.chat_history):
        with st.chat_message(role):
            # Add sentiment indicator for user messages
            if role == "user":
                sentiment_emoji = "😊" if sentiment > 0.4 else "😔" if sentiment < -0.1 else "😐"
                st.markdown(f"*{sentiment_emoji} Sentiment Score: {sentiment:.2f}*")
            
            # Check if this is a crisis response for special styling
            if role == "assistant" and detect_crisis_keywords(st.session_state.chat_history[i-1][1] if i > 0 else ""):
                st.markdown(f"""
                <div class='alert-box'>
                    {message}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(message)
            
            # Display timestamp
            st.caption(f"🕐 {timestamp.strftime('%I:%M %p')}")
    
    # Chat input
    user_input = st.chat_input(placeholder="How are you feeling today?")
    
    if user_input:
        # Validate input
        if not user_input.strip():
            st.warning("Please enter a message.")
            return
        
        if len(user_input.strip()) < 2:
            st.warning("Please enter a longer message.")
            return
        
        # Analyze sentiment
        sentiment_result = analyze_sentiment(user_input)
        
        if sentiment_result is None:
            st.error("Unable to analyze sentiment. Please try again.")
            return
        
        compound_score = sentiment_result['compound']
        current_time = datetime.now()
        
        # Add user message to chat history
        st.session_state.chat_history.append((
            "user",
            user_input,
            compound_score,
            current_time
        ))
        st.session_state.sentiment_scores.append(compound_score)
        st.session_state.timestamps.append(current_time)
        st.session_state.message_count += 1
        
        # Generate response
        response = generate_response(user_input, sentiment_result)
        
        # Add assistant response to chat history
        st.session_state.chat_history.append((
            "assistant",
            response,
            0,  # Assistant messages don't have sentiment scores
            current_time
        ))
        
        # Rerun to display the new messages
        st.rerun()

# =============================================================================
# RUN APPLICATION
# =============================================================================

if __name__ == "__main__":
    main()

"""
================================================================================
POTENTIAL ENHANCEMENTS
================================================================================
1. Integration with professional counseling services for seamless referrals
2. Multi-language support for broader accessibility
3. Voice input/output capabilities for hands-free interaction
4. Personalized resource recommendations based on user patterns
5. Long-term mood tracking with data export functionality
6. Integration with university counseling centers
7. Anonymous peer support communities
8. Guided meditation and mindfulness exercises
9. Sleep tracking and improvement suggestions
10. Academic stress management tools

KNOWN LIMITATIONS
================================================================================
1. Sentiment analysis may not capture complex emotions accurately
2. Crisis detection relies on keyword matching, may miss nuanced expressions
3. No persistent data storage across sessions
4. Limited to text-based interaction
5. Cannot provide professional mental health diagnosis or treatment
6. Responses are pre-programmed and may not address unique situations
7. No integration with real-time emergency services
8. Limited personalization based on user history

================================================================================
"""
