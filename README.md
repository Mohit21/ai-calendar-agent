# ai-calendar-agent: Refer to https://github.com/Mohit21/ai-calendar-agent/blob/main/calendar-ai-agent.png for testing results with Gmail.
1. calendar_reader.py - Logic to access the Calendar API and pass the content to the OpenAI agent.
2. agent.py - Uses the gpt-4.1-mini model to analyze the content of the google calendar response.
3. main.py - Orchestrator for carrying out the function of the AI calendar sequentially.
4. notifier.py - Responsible for notifying and sending the email via SMTP.



