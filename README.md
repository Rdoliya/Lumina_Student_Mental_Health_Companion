# 🌟 Lumina - Student Mental Health Companion

A production-ready Streamlit application designed to provide empathetic, context-aware mental health support for students with built-in safety mechanisms for crisis situations.

## 📋 Table of Contents

- [Features](#features)
- [Developer Information](#developer-information)
- [Technical Specifications](#technical-specifications)
- [Installation](#installation)
- [Usage](#usage)
- [Application Architecture](#application-architecture)
- [Safety Features](#safety-features)
- [UI/UX Design](#uiux-design)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality
- **Sentiment-Based Responses**: Intelligent response system that adapts to user's emotional state
- **Crisis Detection**: Automatic detection of crisis keywords with immediate emergency resource display
- **Mood Tracking**: Visual chart showing sentiment patterns throughout the session
- **Relaxation Exercises**: Guided breathing techniques and grounding exercises
- **Gratitude Journaling**: Prompts to encourage positive thinking
- **Session Statistics**: Track messages, duration, and average mood

### Safety Features
- **Crisis Keyword Detection**: Comprehensive list of emergency keywords
- **Emergency Resources**: Immediate access to crisis hotlines and text lines
- **Professional Disclaimer**: Clear communication about AI limitations
- **Non-Judgmental Support**: Empathetic and validating responses

### User Experience
- **Modern Chat Interface**: Clean, intuitive chat bubbles with avatars
- **Responsive Design**: Works on desktop and mobile devices
- **Calm Color Palette**: Soothing colors designed to reduce visual stress
- **Real-Time Feedback**: Immediate sentiment analysis and responses

## 👨‍💻 Developer Information

**Rishyup Doliya**
- 📱 Phone: +91 7206988702
- 📧 Email: Rishyup.doliya@gmail.com
- 🔗 LinkedIn: [www.linkedin.com/in/rishyup-doliya-833b352b0/](https://www.linkedin.com/in/rishyup-doliya-833b352b0/)
- 💻 GitHub: [https://github.com/rishyup](https://github.com/rishyup)

### Background
- **Education**: Bachelor of Technology in AI & DS, CGC LANDRAN (Expected 2027)
- **Experience**: 
  - ML Intern at Zillion Skills (May - July 2025)
  - AI Engineer at EDUNET FOUNDATION (Nov 2025 - Present)
- **Skills**: Python, C/C++, Java, Data Analytics, Gen AI, Power BI, Tableau, ML, NLP, DL

### Notable Projects
- **HealthMitra**: AI-powered health assistant using Large Language Models
- **ATS Resume Analyser**: Full-stack web application for resume analysis
- **Music Genre Classification**: ML pipeline for genre classification

## 🔧 Technical Specifications

### Framework & Libraries
- **Python Version**: 3.8+
- **Primary Framework**: Streamlit (latest stable version)
- **Sentiment Analysis**: VADER (vaderSentiment library)
- **Data Visualization**: Plotly
- **Data Processing**: Pandas

### Sentiment Analysis Choice
**VADER (Valence Aware Dictionary and sEntiment Reasoner)** was chosen over TextBlob because:
- **Social Media Optimized**: Specifically designed for social media text
- **Handles Emojis & Slang**: Better understanding of modern communication
- **Compound Score**: Provides a unified sentiment score (-1 to +1)
- **No Training Required**: Ready to use out of the box
- **Fast Performance**: Efficient for real-time applications

### Sentiment Thresholds
- **Negative**: Score < -0.1 (catches mild distress)
- **Neutral**: -0.1 to 0.4 (balanced emotional state)
- **Positive**: Score > 0.4 (genuine positive sentiment)

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step-by-Step Setup

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd lumina-mental-health
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install streamlit vaderSentiment pandas plotly
   ```

3. **Verify installation**
   ```bash
   streamlit --version
   ```

## 📖 Usage

### Running the Application

1. **Start the application**
   ```bash
   streamlit run lumina_mental_health.py
   ```

2. **Open in browser**
   - The application will automatically open in your default web browser
   - Or manually navigate to `http://localhost:8501`

     *OR*
     -You can use the Application online on its own website.
     <https://luminamentalhealth.streamlit.app/>

### User Guide

1. **Welcome Screen**: Read the introduction and purpose of Lumina
2. **Share Your Thoughts**: Type your message in the chat input area
3. **Receive Support**: Get empathetic responses based on your emotional state
4. **Track Your Mood**: View sentiment patterns in the sidebar chart
5. **Use Tools**: Access breathing exercises and gratitude prompts
6. **Session Stats**: Monitor your session progress in the sidebar

### Features Overview

#### Chat Interface
- **User Messages**: Displayed with sentiment indicators (😊 😐 😔)
- **Assistant Responses**: Tailored to your emotional state
- **Timestamps**: Track when each message was sent

#### Sidebar Tools
- **Mood Tracker**: Visual line chart of sentiment over time
- **Breathing Exercise**: Guided box breathing technique
- **Session Statistics**: Message count, duration, average mood
- **Clear Chat**: Reset conversation history
- **Developer Info**: Contact information and links

## 🏗️ Application Architecture

### Code Structure

```
lumina_mental_health.py
├── Imports
├── Configuration & Constants
│   ├── Color Scheme
│   ├── Sentiment Thresholds
│   ├── Crisis Keywords
│   ├── Relaxation Tips
│   ├── Motivational Quotes
│   └── Emergency Resources
├── Helper Functions
│   ├── Session State Management
│   ├── Sentiment Analysis
│   ├── Crisis Detection
│   ├── Response Generation
│   ├── UI Components
│   └── Statistics Calculation
└── Main Application Logic
    ├── Sidebar
    ├── Chat Interface
    └── User Input Handling
```

### Key Components

1. **Session State Management**
   - Persistent chat history
   - Sentiment score tracking
   - Timestamp recording
   - Session statistics

2. **Sentiment Analysis Pipeline**
   - Input validation
   - VADER sentiment analysis
   - Crisis keyword detection
   - Sentiment categorization

3. **Response Generation System**
   - Crisis response (highest priority)
   - Negative sentiment response
   - Neutral sentiment response
   - Positive sentiment response

4. **UI/UX Components**
   - Modern chat interface
   - Interactive mood chart
   - Breathing exercise tool
   - Session statistics display

## 🛡️ Safety Features

### Crisis Detection System

**Comprehensive Keyword List**:
- suicide, self-harm, kill myself, end it all
- not worth living, want to die, die, death
- hurt myself, end my life, no reason to live
- better off dead, want to end it, suicidal
- cut myself, harm myself, kill me

**Crisis Response Protocol**:
1. Immediate detection of crisis keywords
2. Display prominent emergency resource box
3. Provide crisis hotline numbers (988)
4. Include Crisis Text Line information (Text HOME to 741741)
5. Show AI disclaimer
6. Override normal sentiment-based responses

### Emergency Resources
- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **Professional Disclaimer**: Clear communication about limitations

## 🎨 UI/UX Design

### Color Palette
- **Primary Green**: #A8D5BA (calming, nature-inspired)
- **Light Green**: #E8F5E9 (soft background)
- **Primary Blue**: #B3E5FC (trustworthy, serene)
- **Light Blue**: #E1F5FE (gentle accent)
- **Neutral Gray**: #F5F5F5 (clean background)
- **Alert Red**: #FF6B6B (emergency situations)

### Design Principles
- **Minimalism**: Clean, uncluttered interface
- **Accessibility**: High contrast, readable fonts
- **Calming Aesthetic**: Soft colors, generous spacing
- **Intuitive Navigation**: Clear user flow
- **Responsive Design**: Works on all devices

### User Experience Flow
1. **Onboarding**: Welcome message explaining purpose
2. **Input**: Easy-to-use chat interface
3. **Processing**: Real-time sentiment analysis
4. **Response**: Immediate, context-aware feedback
5. **Tracking**: Visual mood monitoring
6. **Support**: Access to tools and resources

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test all new features
- Update documentation
- Ensure safety features remain intact

## 📄 License

This project is created for educational and mental health support purposes.

## ⚠️ Disclaimer

**Lumina is an AI companion and not a substitute for professional mental health care.** 

If you or someone you know is experiencing severe distress, please:
- Contact a mental health professional
- Call emergency services (911 in the US)
- Reach out to crisis hotlines (988 in the US)
- Text HOME to 741741 for Crisis Text Line

## 🔮 Future Enhancements

1. **Multi-language Support**: Broader accessibility
2. **Voice Input/Output**: Hands-free interaction
3. **Professional Integration**: Seamless referral to counseling services
4. **Long-term Tracking**: Persistent mood data storage
5. **Personalized Resources**: Tailored recommendations
6. **Meditation Library**: Guided mindfulness exercises
7. **Sleep Tracking**: Sleep quality improvement tools
8. **Academic Stress Tools**: Specialized student support

## 📞 Support

For technical support or questions:
- **Developer**: Rishyup Doliya
- **Email**: Rishyup.doliya@gmail.com
- **GitHub**: https://github.com/rishyup

---

**Made with ❤️ for student mental health support**

*Remember: You are not alone. Help is always available.*
