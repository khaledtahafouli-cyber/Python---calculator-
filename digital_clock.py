#!/usr/bin/env python3
"""
Digital Clock with Multiple Time Zones
A simple command-line clock that displays the current time in different time zones.
"""

from datetime import datetime
import pytz
from typing import List, Dict


class DigitalClock:
    """A digital clock that can display time in multiple time zones."""
    
    def __init__(self, timezones: List[str] = None):
        """
        Initialize the digital clock with specified time zones.
        
        Args:
            timezones: List of timezone strings (e.g., ['UTC', 'US/Eastern', 'Europe/London'])
                      If None, uses common timezones.
        """
        if timezones is None:
            self.timezones = [
                'UTC',
                'US/Eastern',
                'US/Central',
                'US/Mountain',
                'US/Pacific',
                'Europe/London',
                'Europe/Paris',
                'Asia/Tokyo',
                'Asia/Dubai',
                'Australia/Sydney'
            ]
        else:
            self.timezones = timezones
    
    def get_time_in_timezone(self, timezone: str) -> str:
        """
        Get the current time in a specific timezone.
        
        Args:
            timezone: Timezone string (e.g., 'US/Eastern')
            
        Returns:
            Formatted time string
        """
        try:
            tz = pytz.timezone(timezone)
            time_now = datetime.now(tz)
            return time_now.strftime("%H:%M:%S")
        except pytz.exceptions.UnknownTimeZoneError:
            return "Invalid timezone"
    
    def get_date_in_timezone(self, timezone: str) -> str:
        """
        Get the current date in a specific timezone.
        
        Args:
            timezone: Timezone string (e.g., 'US/Eastern')
            
        Returns:
            Formatted date string
        """
        try:
            tz = pytz.timezone(timezone)
            date_now = datetime.now(tz)
            return date_now.strftime("%Y-%m-%d")
        except pytz.exceptions.UnknownTimeZoneError:
            return "Invalid timezone"
    
    def display_clock(self, show_date: bool = True) -> None:
        """
        Display the current time in all configured time zones.
        
        Args:
            show_date: Whether to show the date along with time
        """
        print("\n" + "="*60)
        print("DIGITAL CLOCK - WORLD TIME ZONES")
        print("="*60)
        
        for timezone in self.timezones:
            try:
                tz = pytz.timezone(timezone)
                time_now = datetime.now(tz)
                
                if show_date:
                    formatted_time = time_now.strftime("%Y-%m-%d %H:%M:%S %Z")
                else:
                    formatted_time = time_now.strftime("%H:%M:%S %Z")
                
                # Get UTC offset
                utc_offset = time_now.strftime("%z")
                if utc_offset:
                    utc_offset = f"UTC{utc_offset[:3]}:{utc_offset[3:]}"
                
                print(f"{timezone:20} | {formatted_time:35} | {utc_offset}")
            
            except pytz.exceptions.UnknownTimeZoneError:
                print(f"{timezone:20} | Invalid timezone")
        
        print("="*60 + "\n")
    
    def display_24hr_format(self) -> None:
        """Display time in 24-hour format for all timezones."""
        self.display_clock(show_date=False)
    
    def display_with_date(self) -> None:
        """Display time and date for all timezones."""
        self.display_clock(show_date=True)
    
    def get_current_utc_time(self) -> str:
        """Get current UTC time."""
        utc_time = datetime.now(pytz.UTC)
        return utc_time.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    def convert_time(self, time_str: str, from_tz: str, to_tz: str) -> str:
        """
        Convert time from one timezone to another.
        
        Args:
            time_str: Time string in format "HH:MM:SS"
            from_tz: Source timezone
            to_tz: Destination timezone
            
        Returns:
            Converted time string
        """
        try:
            from_timezone = pytz.timezone(from_tz)
            to_timezone = pytz.timezone(to_tz)
            
            # Create a datetime object for today with the given time
            now = datetime.now()
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            dt = from_timezone.localize(
                datetime(now.year, now.month, now.day, 
                        time_obj.hour, time_obj.minute, time_obj.second)
            )
            
            converted_dt = dt.astimezone(to_timezone)
            return converted_dt.strftime("%Y-%m-%d %H:%M:%S %Z")
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """Main function to run the digital clock."""
    print("\n--- DIGITAL CLOCK APPLICATION ---\n")
    
    # Create clock with default timezones
    clock = DigitalClock()
    
    while True:
        print("Options:")
        print("1. Display current time in all timezones")
        print("2. Display current time and date")
        print("3. Get time in specific timezone")
        print("4. Convert time between timezones")
        print("5. Get current UTC time")
        print("6. Add custom timezone")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            clock.display_24hr_format()
        
        elif choice == "2":
            clock.display_with_date()
        
        elif choice == "3":
            timezone = input("Enter timezone (e.g., 'US/Eastern'): ").strip()
            time_str = clock.get_time_in_timezone(timezone)
            date_str = clock.get_date_in_timezone(timezone)
            print(f"\nTime in {timezone}: {date_str} {time_str}\n")
        
        elif choice == "4":
            print("\nAvailable timezones:", ", ".join(clock.timezones[:5]), "...")
            from_tz = input("Enter source timezone: ").strip()
            to_tz = input("Enter destination timezone: ").strip()
            time_str = input("Enter time (HH:MM:SS): ").strip()
            result = clock.convert_time(time_str, from_tz, to_tz)
            print(f"\nConverted time: {result}\n")
        
        elif choice == "5":
            utc_time = clock.get_current_utc_time()
            print(f"\nCurrent UTC time: {utc_time}\n")
        
        elif choice == "6":
            new_tz = input("Enter timezone to add: ").strip()
            if new_tz not in clock.timezones:
                clock.timezones.append(new_tz)
                print(f"✓ Timezone '{new_tz}' added successfully!\n")
            else:
                print(f"✗ Timezone '{new_tz}' already exists!\n")
        
        elif choice == "7":
            print("\nGoodbye! 👋\n")
            break
        
        else:
            print("❌ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
