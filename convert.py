# Import
import argparse

# Arguments
parser = argparse.ArgumentParser(
    description='BAD2DIRECT - Converts regular bad google drive links to direct ones')
parser.add_argument('--link',
    type=str, help='Google drive link')

# Table
args = parser.parse_args()

# Link
url = args.link

# Validate
if not isinstance(url, str):
    raise Exception("URL is not a string, aborting...")

# Extracting
start = url.index('/d/')
end = url.index('/view?', start + 3)

# ID
file_id = url[start + 3 : end]

# Print
message = "https://drive.google.com/uc?id=%s&export=download&confirm=t" % file_id

print(message)
