from calendar_reader import get_today_events
from agent import analyze_events
from notifier import send_email

def run_agent():
    events = get_today_events()
    summary = analyze_events(events)
    send_email(summary)

if __name__ == "__main__":
    run_agent()

