## Synthalingua 
### [Download](https://github.com/cyberofficial/Synthalingua/releases/)
Synthalingua is a tool that translates audio from one language to English in almsost real time. It's a self hosted tool that can be used to translate audio from any language to English. It uses uses the power of A.I. to handle the input transcription and translation. Even though it's really powerful, it's still in beta and is not perfect. It's still a work in progress and will be updated in a reasonable amount of time.

[![CodeQL](https://github.com/cyberofficial/Synthalingua/actions/workflows/codeql.yml/badge.svg)](https://github.com/cyberofficial/Synthalingua/actions/workflows/codeql.yml)

#### Readme will update as time goes. This is a work in progress.

### Table of Contents
1. [Disclaimer](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#things-to-knowdisclaimerswarningsetc)
2. [To Do List](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#todo)
3. [Contributors](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#contributors)
4. [Installing/Setup](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#installation)
5. [Usage and File Arguments](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#usage)
     * [Examples](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#examples)
6. [Troubleshooting](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#troubleshooting)
7. [Addtional Info](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#additional-information)
8. [Video Demos](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#video-demonstration)
9. [Extra Notes](https://github.com/cyberofficial/Synthalingua/tree/dev-testing#things-to-note)

## Things to know/Disclaimers/Warnings/etc
- This tool is not perfect. It's still in beta and is not perfect. It's still a work in progress and will be updated in a reasonable amount of time.
- The tool will prioritize the language you select over the language it detects. For example if you select Japanese and the speaker is speaking in Spanish it will try and translate it to Japanese. If you want it to translate it to Spanish, you can select Spanish as the language or set the language to auto detect.
- Translations will be more accurate if the speaker is speaking clearly and slowly. If the speaker is speaking fast or unclear, the translation will be less accurate. Though it will still be able to translate it to some degree.
- The tool is not to be used in a professional setting. It's not perfect and is not meant to be used in a professional setting. It's meant to be used for fun and to learn languages and enjoy content at a reasonable pace. You may be required to try and understand the content on your own before using this tool.
- You agree to not use the tool to produce misinformation; Example: If the tool says one thing and the speaker says another, you must do your own research to find out what is true. You may not use the tool to spread misinformation at all.
- You agree to not use the tool to produce hate speech; Example: If the tool says one thing and the speaker says another, you must do your own research to find out what is true. You may not use the tool to spread hate speech at all.
- Since this tool allows connecting to Discord, you must also adhere to Discord's Terms of Service. You may not use the tool to break Discord's Terms of Service or bypass any restrictions Discord has in place, if you use the Discord feature.
- You run your own risk and liability, I (the repo owner), will not be held liable for any damages caused by the tool. You are responsible for your own actions and can not blame me if the tool breaks tos or eulas, or if you get banned from Discord or any other service you use the tool with.
- The tool's model was tuned for conversational speech. It may not work well with other types of speech. For example, it may not work well with news broadcasts, or with a speaker that is speaking in traditional speech. It will work best with conversational speech and prioritizes names over alternate terms of names. For example in Japanese; "Okayu" will always be "Okayu" and not porridge. The A.I. will only translate "porridge" if it's in the context of a sentence is detected with enough confidence. A name will always be translated to the name even though it may have a different spelling in the target language. For example, "Okayu" will always be "Okayu" and not "Okaru" or "Okaru" will always be "Okaru" and not "Okayu" given enough context. The A.I. will only translate "Okayu" if it's in the context of a sentence is detected with enough confidence.
- The tool is not meant to replace actual translators. It's meant to be used for fun and to learn languages and enjoy content at a reasonable pace. You may be required to try and understand the content on your own before using this tool.
- Your hardware will affect the outcome of the tool. If you have a weak CPU, the tool will not work as well. If you have a weak GPU, the tool will not work as well. *If you have a weak internet connection, the tool will not be affected. If you have a weak microphone or bad audio input, the tool will not work as well. 
- This is a tool not a service. You are responsible for your own actions and can not blame me if the tool breaks tos or eulas, or if you get banned from Discord or any other service you use the tool with.

## TODO
| Todo  | Sub-Task | Status |
|-------|----------|--------|
| Add support for AMD GPUs. | ROCm support - Linux Only | ✅ |
|       | OpenCL support - Linux Only | ✅ |
| Add support API access. |          | ❌ |
| Custom localhost web server. |      | ❌ |
| Add reverse translation. |        | ❌ |
|       | Localize script to other languages. (Will take place after reverse translations.) | ❌ |
| Custom dictionary support. |       | ❌ |
| GUI.  |          | ❌ |
| Linux support. |          | ✅ |
| Improve performance. |         | ❌ |
|       | Compressed Model Format for lower ram users | ✅ |
|       | Better large model loading speed | ❌ |
|          | Split model up into multiple chunks based on usage | ❌ |
| Increase model swapping accuracy. | | ❌ |


# Contributors 
#### [@DaniruKun](https://github.com/DaniruKun) - https://watsonindustries.live
#### [@Expletive](https://github.com/Expletive) - https://evitelpxe.neocities.org 

# System Requirements
| Supported GPUs | Description |
| -------------- | ----------- |
| Nvidia Dedicated Graphics | Supported |
| Nvidia Integrated Graphics | Tested - Not Supported |
| AMD/ATI | * Linux Verified |
| Intel Arc | Not Supported |
| Intel HD | Not Supported |
| Intel iGPU | Not Supported |

| Requirement | Minimum | Moderate | Recommended | Best Performance |
| ----------- | ------- | -------- | ----------- | ---------------- |
| CPU Cores | 2 | 6 | 8 | 16 |
| CPU Clock Speed (GHz) | 2.5 or higher | 3.0 or higher | 3.5 or higher | 4.0 or higher |
| RAM (GB) | 4 or higher | 8 or higher | 16 or higher | 16 or higher |
| GPU VRAM (GB) | 2 or higher | 6 or higher | 8 or higher | 12 or higher |
| Free Disk Space (GB) | 10 or higher | 10 or higher | 10 or higher | 10 or higher |
| GPU (suggested) As long as the gpu you have is within vram spec, it should work fine. | Nvidia GTX 1050 or higher | Nvidia GTX 1660 or higher | Nvidia RTX 3070 or higher | Nvidia RTX 3090 or higher |

Note:
- Nvidia GPU support only
- Nvidia GPU is suggested but not required.
- AMD GPUs are not supported yet, but will be supported soon.

The tool will work on any system that meets the minimum requirements. The tool will work better on systems that meet the recommended requirements. The tool will work best on systems that meet the best performance requirements. You can mix and match the requirements to get the best performance. For example, you can have a CPU that meets the best performance requirements and a GPU that meets the moderate requirements. The tool will work best on systems that meet the best performance requirements.

## Installation
1. Download and install [Python 3.10.9](https://www.python.org/downloads/release/python-3109/).
     * Make sure to check the box that says "Add Python to PATH" when installing. If you don't check the box, you will have to manually add Python to your PATH. You can check this guide: [How to add Python to PATH](https://datatofish.com/add-python-to-windows-path/).
     * You can choose any python version that is 3.10.9 up to the latest version. The tool will work on any python version that is 3.11 or higher. Must be 3.10.9+ not 3.11.x.
2. Download and install [Git](https://git-scm.com/downloads).
     * Using default settings is fine.
3. Download and install FFMPEG
     * Instructions: https://github.com/cyberofficial/Synthalingua/issues/2#issuecomment-1491098222
4. Download and install CUDA [Optional, but needs to be installed if using GPU]
     * https://developer.nvidia.com/cuda-downloads
5. Run setup script
     * **On Windows**: `setup.bat`
     * **On Linux**: `setup.bash`
     * If you get an error saying "Setup.bat is not recognized as an internal or external command, operable program or batch file.", houston we have a problem. This will require you to fix your operating system.
6. Run the newly created batch file/bash script. You can edit that file to change the settings.
     * If you get an error saying it is "not recognized as an internal or external command, operable program or batch file.", make sure you have python installed and added to your PATH, and make sure you have git installed. If you have python and git installed and added to your PATH, then create a new issue on the repo and I will try to help you fix the issue.

## Usage 

This script uses argparse to accept command line arguments. The following options are available:
| Flag | Description |
| ---- | ----------- |
| `--ram` | Change the amount of RAM to use. Default is 4GB. Choices are "1GB", "2GB", "4GB", "6GB", "12GB". |
| `--ramforce` | Use this flag to force the script to use desired VRAM. May cause the script to crash if there is not enough VRAM available. |
| `--non_english` | Use non-English models for transcription. Enables the use of non-English models. |
| `--energy_threshold` | Set the energy level for microphone to detect. Default is 100. Choose from 1 to 1000; anything higher will be harder to trigger the audio detection. |
| `--record_timeout` | Set the time in seconds for real-time recording. Default is 2 seconds. |
| `--phrase_timeout` | Set the time in seconds for empty space between recordings before considering it a new line in the transcription. Default is 1 second. |
| `--translate` | Translate the transcriptions to English. Enables translation. |
| `--language` | Select the language to translate from. Available choices are a list of languages in ISO 639-1 format, as well as their English names. |
| `--auto_model_swap` | Automatically swap the model based on the detected language. Enables automatic model swapping. |
| `--device` | Select the device to use for the model. Default is "cuda" if available. Available options are "cpu" and "cuda". When setting to CPU you can choose any RAM size as long as you have enough RAM. The CPU option is optimized for multi-threading, so if you have like 16 cores, 32 threads, you can see good results. |
| `--cuda_device` | Select the CUDA device to use for the model. Default is 0. |
| `--discord_webhook` | Set the Discord webhook to send the transcription to. |
| `--list_microphones` | List available microphones and exit. |
| `--set_microphone` | Set the default microphone to use. You can set the name or its ID number from the list. |
| `--auto_language_lock` | Automatically lock the language based on the detected language after 5 detections. Enables automatic language locking. Will help reduce latency. Use this flag if you are using non-English and if you do not know the current spoken language. |
| `--use_finetune` | Use fine-tuned model. This will increase accuracy, but will also increase latency. Additional VRAM/RAM usage is required. |
| `--retry` | Retries translations and transcription if they fail. |
| `--about` | Shows about the app. |


## Examples
You have a GPU with 6GB of memory and you want to use the Japanese model. You also want to translate the transcription to English. You also want to send the transcription to a Discord channel. You also want to set the energy threshold to 300. You can run the following command:
`python transcribe_audio.py --ram 6gb --non_english --translate --language ja --discord_webhook "https://discord.com/api/webhooks/1234567890/1234567890" --energy_threshold 300`

When choosing ram, you can only choose 1gb, 2gb, 4gb, 6gb, 12gb. There are no in-betweens.

Lets say you have multiple audio devices and you want to use the one that is not the default. You can run the following command:
`python transcribe_audio.py --list_microphones`
This command will list all audio devices and their index. You can then use the index to set the default audio device. For example, if you want to use the second audio device, you can run the following command:
`python transcribe_audio.py --set_microphone "Realtek Audio (2- High Definiti"` to set the device to listen to. *Please note the quotes around the device name. This is required to prevent errors. Some names may be cut off, copy exactly what is in the quotes of the listed devices.

Example lets say I have these devices:
```
Microphone with name "Microsoft Sound Mapper - Input" found, the device index is 1
Microphone with name "VoiceMeeter VAIO3 Output (VB-Au" found, the device index is 2
Microphone with name "Headset (B01)" found, the device index is 3
Microphone with name "Microphone (Realtek USB2.0 Audi" found, the device index is 4
Microphone with name "Microphone (NVIDIA Broadcast)" found, the device index is 5
```

I would put `python transcribe_audio.py --set_microphone "Microphone (Realtek USB2.0 Audi"` to set the device to listen to.
-or-
I would put `python transcribe_audio.py --set_microphone 4` to set the device to listen to.

## Troubleshooting

If you encounter any issues with the tool, here are some common problems and their solutions:

* Python is not recognized as an internal or external command, operable program or batch file.
    * Make sure you have Python installed and added to your PATH.
    * If you recently installed Python, try restarting your computer to refresh the PATH environment variable.
    * Check that you installed the correct version of Python required by the application. Some applications may require a specific version of Python.
    * If you are still having issues, try running the command prompt as an administrator and running the installation again. However, only do this as a last resort and with caution, as running scripts as an administrator can potentially cause issues with the system.
* I get an error saying "No module named 'transformers'".
    * Re-run the setup.bat file.
        * If issues persist, make sure you have Python installed and added to your PATH.
        * Make sure you have the `transformers` module installed by running `pip install transformers`.
        * If you have multiple versions of Python installed, make sure you are installing the module for the correct version by specifying the Python version when running the command, e.g. `python3.9 -m pip install transformers`.
        * If you are still having issues, create a new issue on the repository and the developer may be able to help you fix the issue.
* Git is not recognized as an internal or external command, operable program or batch file.
    * Make sure you have Git installed and added to your PATH.
    * If you recently installed Git, try restarting your computer to refresh the PATH environment variable.
    * If you are still having issues, try running the command prompt as an administrator and running the installation again. However, only do this as a last resort and with caution, as running scripts as an administrator can potentially cause issues with the system.
* CUDA is not recognized or available.
    * Make sure you have CUDA installed. You can get it from [here](https://developer.nvidia.com/cuda-downloads).
    * CUDA is only for NVIDIA GPUs. If you have an AMD GPU, you have to use the CPU model. ROCm is not supported at this time.
* [WinError 2] The system cannot find the file specified
    Try this fix: https://github.com/cyberofficial/Real-Time-Translation/issues/2#issuecomment-1491098222
* Translator can't pickup stream sound
    * Check out this discussion thread for a possible fix: [#12 Discussion](https://github.com/cyberofficial/Synthalingua/discussions/12)



# Additional Information
* Models used are from OpenAI Whisper - [Whisper](https://github.com/openai/whisper)
    * Models were fine tuned using this [Documentation](https://huggingface.co/blog/fine-tune-whisper#load-whisperfeatureextractor)

# Video Demonstration
Command line arguments used. `--ram 6gb --record_timeout 2 --language ja --energy_threshold 500`
[<img src="https://i.imgur.com/sXTWr76.jpg" width="50%">](https://streamable.com/m9mhfr)

Command line arguments used. `--ram 12gb --record_timeout 5 --language id --energy_threshold 500`
[<img src="https://i.imgur.com/2WbWpH4.jpg" width="50%">](https://streamable.com/skuhoh)

# Things to note!
- When crafting your command line arguments, you need to make sure you adjust the energy threshold to your liking. The default is 100, but you can adjust it to your liking. The higher the number, the harder it is to trigger the audio detection. The lower the number, the easier it is to trigger the audio detection. I recommend you start with 100 and adjust it from there. I seen best results with 250-500.
- When using the discord webhook make sure the url is in quotes. Example: `--discord_webhook "https://discord.com/api/webhooks/1234567890/1234567890"`
- An active internet connection is required for initial usage. Over time you'll no longer need an internet connection. Changing RAM size will download certain models, once downloaded you'll no longer need internet.
- The fine tuned model will automatically be downloaded from OneDrive via Direct Public link. In the event if failure


