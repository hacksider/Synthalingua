from modules.imports import *
from modules.languages import get_valid_languages

# Define a constant variable for valid language choices
VALID_LANGUAGES = get_valid_languages()

def valid_port_number(value):
    port = int(value)
    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError(f"Invalid port number: {value}. Please choose a number between 1 and 65535.")
    return port

def set_model_by_ram(ram, language, target_language):
    ram = ram.lower()
    if ram == "1gb":
        model = "tiny.en" if language in ["en", "English"] else "tiny"
    elif ram == "2gb":
        model = "base.en" if language in ["en", "English"] else "base"
    elif ram == "4gb":
        model = "small.en" if language in ["en", "English"] else "small"
    elif ram == "6gb":
        model = "medium.en" if language in ["en", "English"] else "medium"
    elif ram == "12gb":
        model = "large-v3"
        if language in ["en", "English"]:
            red_text = Fore.RED + Back.BLACK
            green_text = Fore.GREEN + Back.BLACK
            yellow_text = Fore.YELLOW + Back.BLACK
            reset_text = Style.RESET_ALL
            print(f"{red_text}WARNING{reset_text}: {yellow_text}12gb{reset_text} is overkill for English. Do you want to swap to {green_text}6gb{reset_text} model? If you are transcribing a language other than English, you can ignore this warning and press {green_text}n{reset_text}.")
            model = "medium.en" if input("y/n: ").lower() == "y" else "large-v3"
    else:
        raise ValueError("Invalid RAM setting provided")

    return model

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ram", default="4gb", help="Model to use", choices=["1gb", "2gb", "4gb", "6gb", "12gb"])
    parser.add_argument("--ramforce", action='store_true', help="Force the model to use the RAM setting provided. Warning: This may cause the model to crash.")
    parser.add_argument("--energy_threshold", default=100, help="Energy level for mic to detect.", type=int)
    parser.add_argument("--mic_calibration_time", help="How long to calibrate the mic for in seconds. To skip user input type 0 and time will be set to 5 seconds.", type=int)
    parser.add_argument("--record_timeout", default=1, help="How real time the recording is in seconds.", type=float)
    parser.add_argument("--phrase_timeout", default=5, help="How much empty space between recordings before we "
                             "consider it a new line in the transcription.", type=float)
    parser.add_argument("--no_log", action='store_true', help="Only show the last line of the transcription.")
    parser.add_argument("--translate", action='store_true', help="Translate the transcriptions to English.")
    parser.add_argument("--transcribe", action='store_true', help="transcribe the text into the desired language.")
    parser.add_argument("--language", help="Language to translate from.", type=str, choices=VALID_LANGUAGES)
    parser.add_argument("--target_language", help="Language to translate to.", type=str, choices=VALID_LANGUAGES)
    parser.add_argument("--auto_model_swap", action='store_true', help="Automatically swap model based on detected language.")
    parser.add_argument("--device", default="cuda", help="Device to use for model. If not specified, will use CUDA if available. Available options: cpu, cuda")
    parser.add_argument("--cuda_device", default=0, help="CUDA device to use for model. If not specified, will use CUDA device 0.", type=int)
    parser.add_argument("--discord_webhook", default=None, help="Discord webhook to send transcription to.", type=str)
    parser.add_argument("--list_microphones", action='store_true', help="List available microphones and exit.")
    parser.add_argument("--set_microphone", default=None, help="Set default microphone to use.", type=str)
    parser.add_argument("--microphone_enabled", default=None, help="Enable microphone by name.", type=str)
    parser.add_argument("--auto_language_lock", action='store_true', help="Automatically locks the language based on the detected language after set ammount of transcriptions.")
    parser.add_argument("--retry", action='store_true', help="Retries the transcription if it fails. May increase output time.")
    parser.add_argument("--use_finetune", action='store_true', help="Use finetuned model.")
    parser.add_argument("--updatebranch", default="master", help="Check which branch from the repo to check for updates. Default is master, choices are master and dev-testing and bleeding-under-work. To turn off update checks use disable. bleeding-under-work is basically latest changes and can break at any time.", choices=["master", "dev-testing", "disable", "bleeding-under-work"])
    parser.add_argument("--keep_temp", action='store_true', help="Keep temporary audio files.")
    parser.add_argument(
    "--portnumber", default=None, help="Port number to run the web server on. If not specified, the web server will not run.", type=valid_port_number)
    parser.add_argument("--about", action='store_true', help="About the project.")
    parser.add_argument("--save_transcript", action='store_true', help="Save the transcript to a file.")
    parser.add_argument("--save_folder", default="out", help="Folder to save the transcript to.")
    parser.add_argument("--stream", default=None, help="Stream mode. Specify the url to the stream. Example: https://twitch.tv/laplusdarknesss_hololive")
    parser.add_argument("--stream_original_text", action='store_true', help="Show's the detected language of the stream.")
    parser.add_argument("--stream_chunks", default=5, help="How many chunks to split the stream into. Default is 5 is recommended to be between 3 and 5. YouTube streams should be 1 or 2, twitch should be 5 to 10.", type=int)
    parser.add_argument("--stream_language", default="en", help="Language of the stream. Default is English.", type=str, choices=VALID_LANGUAGES)
    parser.add_argument("--stream_target_language", default=None, help="Language to translate the stream to. Default is English.", type=str, choices=VALID_LANGUAGES)
    parser.add_argument("--stream_translate", action='store_true', help="Translate the stream.")
    parser.add_argument("--stream_transcribe", action='store_true', help="Transcribe the stream.")
    parser.add_argument("--cookies", default=None, help="Path to cookies.txt file. In NetScape format.")
    return parser.parse_args()


print("Args Module Loaded")