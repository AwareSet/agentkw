import json
import os
import pkg_resources
from gensim.summarization.summarizer import summarize
from nltk import sent_tokenize
from youtube_transcript_api import YouTubeTranscriptApi

# the below is a function that takes in a video id and returns a summary of the video
# also the below function saves the transcript of the video in a json file 
# the below function is using the youtube_transcript_api library to get the transcript of the video
# the below function is using the gensim library to summarize the transcript of the video
# the below function is using the nltk library to tokenize the transcript of the video
# the below function is using the json library to save the transcript of the video in a json file
# the below function is using the os library to save the transcript of the video in a json file
# the below function is using the pkg_resources library to save the transcript of the video in a json file
# the below function is using the youtube_transcript_api library to save the transcript of the video in a json file
# the input below is a video id 
# the processing is to get the transcript of the video && tokenize the transcript of the video && summarize the transcript of the video && save the transcript of the video in a json file
# the output is a summary of the video && a json file with the transcript of the video
# the purpose of the below function is to get the transcript of the video && tokenize the transcript of the video && summarize the transcript of the video && save the transcript of the video in a json file
# the below function is using the youtube_transcript_api library to get the transcript of the video
# the below function is using the gensim library to summarize the transcript of the video

# define a function called extract_transcript that takes in a video id as an argument

def extract_transcript(video_id):
    # get the transcript of the video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    # tokenize the transcript of the video this mean split the transcript into 
    ### sentences and save the sentences in a list and save the list in a variable called chunks
    chunks = sent_tokenize(transcript)
    with open('transcript.json', 'w') as f:
        json.dump(chunks, f)
        
    # the path to the transcript.json file is the current directory. the transcript.json file is in the current directory 
    
    transcript_path = pkg_resources.resource_filename(__name__, 'transcript.json')
    # summarize the transcript of the video
    summary = summarize(transcript)
    # return the summary of the video let me explain return here means output means result means answer means response 
    return summary



# explain the above function in your own words 
# what is the purpose of the above function
# what is the input of the above function
# what is the output of the above function
# what is the purpose of the above function


# define a function called extract_transcripts_from_folder that takes in a folder path as an argument .. (folder path is a string) 
def extract_transcripts_from_folder(folder_path):
    # for each file in the folder path that ends with .txt do the following
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            # open the file and read the text in the file and save the text in a variable called text. explain what open does. 
            # tokenize the text in the file and save the sentences in a list and save the list in a variable called chunks
            
            # json.dump(chunks, j) explain what this does
            # the below code saves the transcript of the video in a json file
            
            
            # with is a context manager. explain what a context manager is a context manager is a way to open a file and close a file. 
            # open(f'{file_name}.json', 'w') as j: explain what this does, 
            with open(os.path.join(folder_path, file_name), 'r') as f:
                text = f.read()
                # chunks = sent_tokenize(text) explaining more about the below code 
                # the below code tokenizes the text in the file and saves the sentences in a list and saves the list in a variable called chunks
                #
                chunks = sent_tokenize(text)
                # with open(f'{file_name}.json', 'w') as j: this open = open a file and this open = close a file (f' is a string literal and {file_name} is a variable and .json is a string literal)
                # and 'w' means write mode and as j means save the file in a variable called j 
                # jason.dump is a function that takes in two arguments a list and a file and saves the list in the file
                # list is chunks and file is j list example [1,2,3] file example f which mean a file 
                # called f and the file format is json dump means save
                # with is a function that takes in two arguments 1. a file and 2. a function more 
                with open(f'{file_name}.json', 'w') as j:
                    
                    json.dump(chunks, j)

# what if __name__ == '__main__' means is if the below code is run as a script then do the below code 
# the __name__ is a variable that is set to __main__ if the below code is run as a script
# and __main__ is a string literal which means a string and __main__ is a variable name but
# why the double __ is for python to know that this is a special variable name to not use this variable name for other variables 
# mainly __main__ is a class name and __main__ is a class name that is a string literal 
# more about __main__ visit https://www.youtube.com/watch?v=sugvnHA7ElY and the  


if __name__ == '__main__':
    video_id = 'VIDEO_ID_HERE'
    summary = extract_transcript(video_id)
    print(summary)

    folder_path = 'FOLDER_PATH_HERE'
    extract_transcripts_from_folder(folder_path)
    
    # now to excute the above code run the below command in the terminal 
 # to run the above code in the terminal run the below command in the terminal 
 # python -m summay 
 
 
 # make requirment file for windoews users
    # pip freeze > requirements.txt
    # pip install -r requirements.txt
    # pip install -r requirements.txt --upgrade
    # pip install -r requirements.txt --upgrade --force-reinstall
    # pip install -r requirements.txt --upgrade --force-reinstall --no-cache-dir
    # pip install moudles needed for the above code 
    # pip install gensim # gensim is a library that is used to summarize text
    # pip install nltk # nltk is a library that is used to tokenize text
    # pip install youtube_transcript_api # youtube_transcript_api is a library that is used to get the transcript of a youtube video
    # pip install json # json is a library that is used to save the transcript of a youtube video in a json file
    # pip install os # os is a library that is used to save the transcript of a youtube video in a json file
    # pip install pkg_resources # pkg_resources is a library that is used to save the transcript of a youtube video in a json file
    # pip install sent_tokenize # sent_tokenize is a function that is used to tokenize text
    
    
    #make pip cmd for all the ABOVE 
    # pip install gensim nltk youtube_transcript_api json os pkg_resources sent_tokenize
