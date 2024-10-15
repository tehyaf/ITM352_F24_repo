import gdown

# Google Drive file ID
file_id = '10X2Icx78XKTbt3ZRj3F-FlzmW_NugEpz'
# Convert to a downloadable link
download_url = f'https://drive.google.com/uc?id={file_id}'

# Output filename for the downloaded file
output_file = 'taxi_1000.csv'

# Download the file
gdown.download(download_url, output_file, quiet=False)

# Now you can process the CSV file as per the previous code

