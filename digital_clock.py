#!/usr/bin/env python3
"""
Simple Digital Clock - Display current time in different time zones
"""

from datetime import datetime
import pytz

# Common timezones
TIMEZONES = {
    '1': ('UTC', 'pytz.UTC'),
    '2': ('US/Eastern', 'America - New York'),
    '3': ('US/Pacific', 'America - Los Angeles'),
    '4': ('Europe/London', 'Europe - London'),
    '5': ('Europe/Paris', 'Europe - Paris'),
    '6': ('Asia/Tokyo', 'Asia - Tokyo'),
    '7': ('Asia/Dubai', 'Asia - Dubai'),
    '8': ('Australia/Sydney', 'Australia - Sydney'),
}

def display_time(timezone_name):
    """Display current time in specific timezone"""
    try:
        tz = pytz.timezone(timezone_name)
        now = datetime.now(tz)
        return now.strftime("%Y-%m-%d %H:%M:%S %Z")
    except:
        return "Invalid timezone"

def show_all_times():
    """Show time in all timezones"""
    print("\n" + "="*60)
    print("CURRENT TIME IN DIFFERENT TIME ZONES")
    print("="*60)
    for key, (tz_name, display_name) in TIMEZONES.items():
        time_str = display_time(tz_name)
        print(f"{display_name:25} | {time_str}")
    print("="*60 + "\n")

def main():
    """Main program"""
    while True:
        print("\n--- DIGITAL CLOCK ---\n")
        print("1. Show time in all zones")
        print("2. Show time in specific zone")
        print("3. Exit\n")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            show_all_times()
        
        elif choice == '2':
            print("\nAvailable timezones:")
            for key, (tz_name, display_name) in TIMEZONES.items():
                print(f"{key}. {display_name}")
            
            tz_choice = input("\nSelect timezone (1-8): ").strip()
            
            if tz_choice in TIMEZONES:
                tz_name, display_name = TIMEZONES[tz_choice]
                time_str = display_time(tz_name)
                print(f"\nTime in {display_name}: {time_str}\n")
            else:
                print("\n❌ Invalid choice!\n")
        
        elif choice == '3':
            print("\nGoodbye! 👋\n")
            break
        
        else:
            print("\n❌ Invalid choice!\n")

if __name__ == "__main__":
    main()
