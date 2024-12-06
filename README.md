# **AI-Powered Mental Health Assistant**

An innovative AI-driven platform designed to provide users with tools for tracking mental health, engaging with gamification, and accessing personalized support resources. Our app integrates advanced AI features with an intuitive user interface to empower users to take control of their mental well-being. (Mohit could add some content)

---

## **Table of Contents**
1. [Key Features](#key-features)
2. [Technology Stack](#technology-stack)
3. [Project Setup](#project-setup)
4. [Core Components Introduction](#core-components)
5. [User Experience and User Interface](#user-experience-and-user-interface)
6. [How It Works](#how-it-works)
7. [Testing](#testing)
8. [Core Implementation](#core-implementation)
9. [Future Enhancements](#future-enhancements)
10. [Contributors](#contributors)
11. [License](#license)

---

## **Features**

### **Core Features**
- **Mood Tracking**:
  - Log daily moods with a simple and intuitive interface.
  - Take a short note for every record help users recall
  - Track historical trends and visualize progress over time.

- **Daily Challenges**:
  - Automatically assigned challenges tailored to user preferences and needs.
  - Includes mindfulness exercises, gratitude journaling, and self-care tasks.

- **Gamification**:
  - Streak tracking encourages users to log consistently.
  - Badges awarded for achieving milestones, such as 3-day, 7-day, or 30-day streaks.

- **Support Services**:
  - Access to regional emergency contacts and professional connections.
  - Tab-based navigation for ease of use.

- **Recommendations**:
 - Provide users with a video or article resource about mental health on the dashboard page.
 - Provide a wide range of articles and video resources in the website's resource library for users to browse.
 
### **AI Integration**
- Personalized recommendations powered by OpenAI.
- Our website provides users with psychological health consultations through AI doctors, each specializing in different fields

---

## **Technology Stack**

| **Component**         | **Technology**        |
|------------------------|-----------------------|
| **Frontend**           | HTML, CSS, JavaScript |
| **Backend**            | Django               |
| **Database**           | SQLite               |
| **AI Integration**     | OpenAI API           |
| **Third-Party APIs**   | Emergency resource APIs |

---

## **Project Setup**

### **Prerequisites**
- Python 3.8+
- pip (Python package manager)

### **Installation Steps**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/{your-repo}/Mental_health.git
   cd Mental_health
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## **Core Components Introduction**

### **1. Mood Tracking**
- Allows users to log their emotions daily. The users could record their mood base on their situation at that day and they could take notes for the reason why they post those scores.
<img src="./screenshots/log_mode.png" alt="Alt text" width="500">

- Users could track their mood description record
<img src="./screenshots/mood_description_record.png" alt="Alt text" width="500">

- Users can track their emotional fluctuation curve through a line chart to understand their recent emotional stability.
<img src="./screenshots/mood_curve.png" alt="Alt text" width="500">

### **2. Daily Challenges**
- Tasks tailored to user engagement (include journaling, meditation, and gratitude exercises).
<img src="./screenshots/chanllege.png" alt="Alt text" width="500">

- when users finish the tasks they can mark us complete and the task will update everyday to attract users.

### **3. Gamification**
- Awards badges for streak milestones to boost motivation.
- Tracks longest streaks and provides visual progress.
![Alt text](./screenshots/badge.png)

### **4. Recommendation**
- Randomly recommend an article or video from the content library on the dashboard page.
![Alt text](./screenshots/recommendations_dashboard.png)
- Users can visit the recommendation page to view all videos and articles, allowing them to enrich their knowledge and learn how to maintain mental health.
![Alt text](./screenshots/educational_sources.png)

### **5. Support Services**
- Provides users with:
  - Emergency contacts for mental health crises.
  - Professional connections, such as therapists and counselors. 
![Alt text](./screenshots/service_page.png)
![Alt text](./screenshots/professional.png)

### **6. AI Integration**
- Use the OpenAI API to create three virtual doctors, each specializing in different fields, to provide users with more professional consultation services .
![Alt text](./screenshots/chatbot.png)

## **User Experience and User Interface**
1. **Notification**:
- A welcome notification for first-time registration is placed on the Notification page to enhance users' positive impression of the website.
2. **Emoji**:
Use emoji expressions to add fun when recording emotions.
3.**Dashboard Icon**
The icon in the dashboard welcome section changes based on the time of day. For example, if you log in during the morning, the icon will be a sun
## **How It Works**

1. **User Interaction**:
   - Users log in, track moods, and access daily challenges.

2. **AI-Powered Personalization**:
   - OpenAI generates challenges based on mood logs and trends.

3. **Gamification**:
   - Users earn badges and track streaks for consistent engagement.

4. **Support Services**:
   - Emergency and professional resources are dynamically fetched using third-party APIs.

---

## **Testing**

### **Run Tests**
To ensure all components are working as intended:
```bash
python manage.py test
```

### **Tested Features**
- User authentication
- Mood logging and streak tracking
- AI-generated challenges
- Badge awarding
- Support services (emergency contacts and professional connections)

---

## **Core Implementation**

Below are the core code snippets that power the main features of the AI-powered mental health assistant.

### **1. Mood Tracking**

**File**: `moodtracking/models.py`

```python
from django.db import models
from users.models import User

class MoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mood_logs')
    mood_score = models.IntegerField()  # Scale: 1 (low) to 10 (high)
    description = models.TextField(blank=True)  # Optional text entry for mood
    sentiment = models.CharField(max_length=50, blank=True)  # Result from AI analysis
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood_score} - {self.timestamp}"

    def get_points(self):
        return self.mood_score  # Simple example: mood score equals points
```

**Purpose**:
- This model logs user moods, including a score, optional description, and timestamp.
- Sentiment can be analyzed and stored using AI.

---

### **2. Daily Challenges**

**File**: `gamification/models.py`

```python
class ChallengeTemplate(models.Model):
    task = models.TextField()  # Description of the challenge

    def __str__(self):
        return self.task

class DailyChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_challenges')
    task = models.TextField()
    date_assigned = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Challenge for {self.user.username} on {self.date_assigned}"
```

**Purpose**:
- The `ChallengeTemplate` model stores predefined tasks.
- The `DailyChallenge` model assigns specific tasks to users and tracks completion.

---

### **3. Gamification**

**File**: `gamification/signals.py`

```python
@receiver(post_save, sender=MoodLog)
def update_streak(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        streak, _ = Streak.objects.get_or_create(user=user)

        if streak.last_activity_date == date.today():
            return  # Skip if already updated today

        if streak.last_activity_date == date.today() - timedelta(days=1):
            streak.current_streak += 1
        else:
            streak.current_streak = 1

        streak.longest_streak = max(streak.longest_streak, streak.current_streak)
        streak.last_activity_date = date.today()
        streak.save()

        award_badges(user, streak.current_streak)
```

**Purpose**:
- Tracks user streaks for consistent mood logging.
- Awards badges based on streak milestones.

---

### **4. Support Services**

**File**: `support/models.py`

```python
class EmergencyContact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ProfessionalConnection(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
```

**Purpose**:
- Stores emergency contact details and professional resources.
- Supports region-based filtering for relevance.

---

### **5. AI Integration**

**File**: `chatbot/models.py`

```python
class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
```
**Purpose**:
- Stores chatting history.

**File**: `chatbot/views.py`

```python
@csrf_exempt
def chatbot_response(request):
    ...
    # General chatbot logic
    system_message = (
        "You are a professional and empathetic assistant for a mental health platform. "
        "Provide support on mindfulness, stress management, and emotional well-being. "
        "Suggest available doctors for specific queries and answer questions about subscriptions and benefits of the app."
    )

    # Handle general queries
    keywords_subscription = ["subscription", "pricing", "benefits", "features"]
    if any(keyword in user_message.lower() for keyword in keywords_subscription):
        return JsonResponse({
            "message": (
                "Our app offers personalized mental health support, mood tracking, mindfulness exercises, "
                "and access to licensed professionals. You can explore our subscription plans on the 'Pricing' page."
            )
        })

    if "doctor" in user_message.lower():
        doctor_options = ", ".join([f"{doc_id}: {doc}" for doc_id, doc in DOCTOR_PROFILES.items()])
        return JsonResponse({
            "message": f"We have the following doctors available:\n{doctor_options}. "
                       "Please provide the doctor number to start a conversation."
        })

    # Call OpenAI API for the AI's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        max_tokens=200,
        temperature=0.7,
    )
    
    ...
```

**Purpose**:
- Provides dynamic responses to enhance user engagement.

---

## **Future Enhancements**

### **Planned Features**:
1. **Advanced Personalization**:
   - AI will adapt recommendations based on detailed user profiles.
2. **Community Features**:
   - Introduce group challenges and social forums.
3. **Multilingual Support**:
   - Make the app accessible in multiple languages.
4. **Therapist Integration**:
   - Connect users directly with licensed professionals for virtual therapy sessions.
5. **Enhanced Analytics**:
   - Provide insights into user engagement for mental health professionals.

---

## **Contributors**
- **GNG 5300 Group 5**
  - Mohit Upadhyay (**Your Name**: [https://github.com/Upadhyaymohit28/Mental_health](https://github.com/Upadhyaymohit28/Mental_health))
  - Zewei Wang (**Rocker**: [https://github.com/zewei-wang/Mental_health/tree/main](https://github.com/zewei-wang/Mental_health))
  - Xu Gao (**Wadeahh3**: [https://github.com/Wadeahh3/Mental_health](https://github.com/Wadeahh3/Mental_health))

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---