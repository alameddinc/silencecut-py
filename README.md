# SilenceCutter

SilenceCutter is a Python application that automatically detects and removes silent parts from video files, allowing you to create smoother and more seamless videos.

## Features

- **Silence Detection:** Detects silent sections in videos.
- **Silence Removal:** Removes silent parts to make videos smoother.
- **Merges Close Segments:** Combines non-silent segments that are close to each other.
- **Smooth Transitions:** Adds padding durations to the beginning and end of segments for smoother cuts.
- **User-Friendly:** Simple and easy to use.

## Requirements

- Python 3.x
- moviepy
- pydub

## Installation

```bash
pip install silencecutpy
```

## Usage

```bash
silencecutpy --input project/silencecut-py/example_input.mp4 --output output.mp4
```

## Parameters

- `--input`: Input video file
- `--output`: Output video file
- `--silence_threshold`: Silence threshold value (default: -30)
- `--min_silence_length`: Minimum silence duration (default: 350)
- `--padding_duration`: Transition duration (default: 100)
- `--max_gap`: Maximum segment gap to be merged (default: 100)
- `--temp_dir`: Directory where temporary files will be saved
- `--verbose`: Show detailed outputs

