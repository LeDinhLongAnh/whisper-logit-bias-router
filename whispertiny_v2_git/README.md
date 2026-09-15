# Whisper Logit Bias - Router Domain

This is a minimal extraction of the Whisper Logit Bias engine for the Intent Router project.

It uses a monkey-patching technique to inject logit biases into the official openai-whisper library at runtime, so you do NOT need a modified version of Whisper.

## Installation

1. Install the official Whisper library:
   ``bash
   pip install -U openai-whisper
   ``
2. You need fmpeg installed on your system to process audio.

## Usage

See example_usage.py for a complete working example. 

Note: When you run the script for the first time, it will automatically download the Whisper ase.en model into the .models directory.
