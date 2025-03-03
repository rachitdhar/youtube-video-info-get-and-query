# youtube-video-info-get-and-query
Contains two programs - one to get Youtube video information (for a given set of URLs) and store into an excel sheet; and a second program to run SQL queries on this table.

## Instructions

- Enter the Youtube API key (which you can generate from Youtube) in paths.json.
- Place a urls.txt file in the same directory as the programs, containing a list of all the URLs for which you need to extract information.
- Run the youtube_get_and_write_video_info.py program in order to get the information, and obtain a videos.xlsx file.
- In order to query the excel sheet, run the excel_sql_querier.py file, and you can write SQL queries (and view the corresponding outputs) in the command line.
