# Digital Clock with Multiple Time Zones ⏰

A Python command-line application that displays the current time across different time zones around the world with timezone conversion capabilities.

## Features ✨

- **🌍 Multi-Timezone Display**: View current time in 10+ major world timezones simultaneously
- **📅 Date & Time Options**: Display time only or combined with date
- **🔄 Timezone Conversion**: Convert any time from one timezone to another
- **⏱️ UTC Time**: Quick access to current UTC time
- **➕ Custom Timezones**: Add your own timezones dynamically
- **📊 UTC Offset Display**: See UTC offset for each timezone

## Supported Time Zones (Default)

- UTC
- US/Eastern
- US/Central
- US/Mountain
- US/Pacific
- Europe/London
- Europe/Paris
- Asia/Tokyo
- Asia/Dubai
- Australia/Sydney

## Installation

### Requirements
- Python 3.6+
- pytz library

### Setup

1. Clone the repository or download the files
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

Or install pytz directly:

```bash
pip install pytz
```

## Usage

Run the application:

```bash
python3 digital_clock.py
```

### Menu Options

```
Options:
1. Display current time in all timezones
2. Display current time and date
3. Get time in specific timezone
4. Convert time between timezones
5. Get current UTC time
6. Add custom timezone
7. Exit
```

### Examples

#### Option 1: Display current time in all timezones
```
DIGITAL CLOCK - WORLD TIME ZONES
============================================================
UTC                  | 14:30:45 UTC                            | UTC+00:00
US/Eastern           | 14:30:45 EDT                            | UTC-04:00
US/Pacific           | 11:30:45 PDT                            | UTC-07:00
Europe/London        | 14:30:45 BST                            | UTC+01:00
Asia/Tokyo           | 23:30:45 JST                            | UTC+09:00
...
```

#### Option 3: Get time in specific timezone
```
Enter timezone (e.g., 'US/Eastern'): Asia/Tokyo
Time in Asia/Tokyo: 2026-05-30 23:30:45
```

#### Option 4: Convert time between timezones
```
Enter source timezone: US/Eastern
Enter destination timezone: Asia/Tokyo
Enter time (HH:MM:SS): 14:30:00
Converted time: 2026-05-31 03:30:00 JST
```

## File Structure

```
digital_clock.py       # Main application file
requirements.txt       # Project dependencies
README.md             # Documentation
example_usage.py      # Usage examples
test_digital_clock.py # Unit tests
```

## Code Structure

### DigitalClock Class

Main class that handles all clock operations:

**Methods:**
- `__init(timezones)`: Initialize with timezone list
- `get_time_in_timezone(timezone)`: Get time in specific timezone
- `get_date_in_timezone(timezone)`: Get date in specific timezone
- `display_clock(show_date)`: Display all timezones
- `display_24hr_format()`: Display time only (24-hour)
- `display_with_date()`: Display time and date
- `get_current_utc_time()`: Get current UTC time
- `convert_time(time_str, from_tz, to_tz)`: Convert between timezones

## Example Usage in Code

```python
from digital_clock import DigitalClock

# Create clock with default timezones
clock = DigitalClock()

# Display all timezones
clock.display_with_date()

# Get time in specific timezone
time_ny = clock.get_time_in_timezone('US/Eastern')
print(f"New York time: {time_ny}")

# Convert time
converted = clock.convert_time("14:30:00", "US/Eastern", "Asia/Tokyo")
print(f"Converted: {converted}")

# Create clock with custom timezones
custom_clock = DigitalClock(['UTC', 'US/Eastern', 'Europe/Paris'])
custom_clock.display_24hr_format()
```

## Testing

Run the unit tests:

```bash
python3 test_digital_clock.py
```

## Examples

Run the example usage:

```bash
python3 example_usage.py
```

## Learning Objectives

This project demonstrates:

✅ **Object-Oriented Programming**: Class design and methods
✅ **DateTime Handling**: Working with Python's datetime module
✅ **Timezone Management**: Using pytz for timezone operations
✅ **User Input/Output**: Menu-driven CLI application
✅ **Error Handling**: Try-catch for invalid timezones
✅ **Type Hints**: Python type annotations
✅ **Documentation**: Docstrings and comments
✅ **Unit Testing**: Comprehensive test coverage

## Timezone Reference

To add custom timezones, use timezone identifiers from the IANA timezone database:

Common formats:
- `UTC`, `Etc/UTC`
- `US/Eastern`, `US/Central`, `US/Mountain`, `US/Pacific`
- `Europe/London`, `Europe/Paris`, `Europe/Berlin`
- `Asia/Tokyo`, `Asia/Shanghai`, `Asia/Dubai`, `Asia/Bangkok`
- `Australia/Sydney`, `Australia/Melbourne`
- `America/New_York`, `America/Chicago`, `America/Los_Angeles`
- `Africa/Cairo`, `Africa/Johannesburg`
- `India/Kolkata` (or `Asia/Kolkata`)

[View all IANA timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## Troubleshooting

### ModuleNotFoundError: No module named 'pytz'
```bash
pip install pytz
```

### UnknownTimeZoneError
Make sure the timezone name is correct. Check the IANA timezone database for proper names.

### Time seems incorrect
Ensure your system time and timezone are set correctly. The application uses your system's current time.

## Future Enhancements 🚀

- [ ] GUI interface with tkinter
- [ ] Display analog clock visualization
- [ ] Alarm functionality across timezones
- [ ] Save favorite timezones to config file
- [ ] Command-line arguments for quick operations
- [ ] Web interface with Flask
- [ ] Real-time updates with live ticker

## License

This is an educational project for learning Python basics.

## Author

Created by: khaledtahafouli-cyber

---

**Last Updated**: May 30, 2026