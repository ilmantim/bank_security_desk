def format_duration(duration):
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    formatted_duration = f'{hours:02}:{minutes:02}'
    return formatted_duration
