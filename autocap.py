import convertToWav
import uploadToAPI
import getTranAPI
import exportSRT
import checkStatus
import sys
import getopt
import os
import time


def usage():
    msg = """Auto-generate Video Caption
Usage: autocap.py -f video_file -t token [-o output_file]
-h  --help            -  show this
-f  --video_file      -  path to the video file
-t  --token           -  AssemblyAI API token
[-o --output_file]    -  default: [file_name].str"""
    print(msg)
    sys.exit(0)


def run(sourceVideoPath, API_token, output):
    print("converting ...")
    convertToWav.convert(sourceVideoPath)

    print("upload audio to API")
    upload_url = uploadToAPI.getUploadUrl(API_token)
    print(upload_url)

    print("get transcript ID")
    transcriptID = getTranAPI.getID(upload_url, API_token)
    print(transcriptID)

    print("check for status")
    status = ""
    while (status != "completed"):
        newStatus = checkStatus.check(transcriptID, API_token)
        if (status != newStatus):
            status = newStatus
            print(status)
        time.sleep(1)
    
    print("export to srt")
    exportSRT.export(transcriptID, API_token, output)

    os.remove("convert.wav")
    print("remove convert.wav")
    print("done")


def main(argv):
    sourceVideoPath = ""
    API_token = ""
    output = ""

    if not len(sys.argv[1:]):
        usage()

    options = "h:f:t:o:"
    long_options = ["help", "video_file", "token", "output_file"]

    try:
        opts, args = getopt.getopt(argv, options, long_options)
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-f", "--video_file"):
            sourceVideoPath = a
        elif o in ("-t", "--token"):
            API_token = a
        elif o in ("-o", "--output_file"):
            output = a
        else:
            assert False, "Unhandled Option"

    if sourceVideoPath == "" or API_token == "":
        usage()
    if (output == ""):
        base = os.path.basename(sourceVideoPath)
        output = os.path.splitext(base)[0] + ".srt"

    run(sourceVideoPath, API_token, output)


if __name__ == "__main__":
    main(sys.argv[1:])
