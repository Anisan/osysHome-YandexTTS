# YandexTTS - Yandex Text-to-Speech

![YandexTTS Icon](static/YandexTTS.png)

Text-to-speech synthesis using Yandex SpeechKit API for converting text to speech.

## Description

The `YandexTTS` module provides text-to-speech capabilities for the osysHome platform using Yandex SpeechKit API. It converts text messages to speech audio files with caching support.

## Main Features

- ✅ **Text-to-Speech**: Convert text to speech audio
- ✅ **Voice Selection**: Multiple voice options
- ✅ **Emotion Control**: Control speech emotion
- ✅ **Audio Caching**: Cache generated audio files
- ✅ **Multiple Formats**: Support for MP3 format

## Admin Panel

The module provides an admin interface for:
- Configuring API settings
- Selecting voice and emotion
- Testing TTS synthesis

## Configuration

- **Access Key**: Yandex SpeechKit API access key
- **Speaker**: Voice selection (default: tatyana_abramova)
- **Emotion**: Speech emotion (default: good)

## Available Voices

- **tatyana_abramova**: Female voice
- Other voices available in Yandex SpeechKit

## Available Emotions

- **good**: Neutral/good emotion
- **evil**: Evil emotion
- **neutral**: Neutral emotion

## Usage

### Synthesizing Speech

Use the `say` action:
```python
callPluginFunction("YandexTTS", "say", {
    "message": "Hello, this is a test",
    "level": 0
})
```

## Technical Details

- **API**: Yandex SpeechKit TTS API
- **Format**: MP3 audio format
- **Caching**: MD5 hash-based file caching
- **Language**: Russian (ru_RU)

## Version

Current version: **0.2**

## Category

App

## Actions

The module provides the following actions:
- `say` - Synthesize and play speech

## Requirements

- Flask
- Requests
- osysHome core system

## Author

osysHome Team

## License

See the main osysHome project license

