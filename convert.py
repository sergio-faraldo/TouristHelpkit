import json

# Load your JSON file
json_file = 'jp.json'  # Replace with your actual file path
with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Open the HTML file to write the output
with open('output.html', 'w', encoding='utf-8') as html_file:
    # Write the basic HTML structure
    html_file.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Translated Data</title>
    <script>
        function toggleSections(articleId) {
          const dataDiv = document.getElementById(articleId);
          const button = document.getElementById(articleId+"_arrow");
    
          if (dataDiv.style.display === "none" || dataDiv.style.display === "") {
            dataDiv.style.display = "flex";  // Show the section
            button.textContent = "▲";        // Change to up arrow
          } else {
            dataDiv.style.display = "none";  // Hide the section
            button.textContent = "▼";        // Change to down arrow
          }
        }
    </script>
    <style>
        /* Style for articles */
        section {
            display: flex;
            flex-direction: column;
            border-radius: 15px; /* Rounded corners */
        }
        
        /* Style for the data div */
        .data {
            display: none; /* Enables flexbox layout for sections */
            flex-wrap: wrap; /* Allows sections to wrap into new lines */
            justify-content: center; /* Centers the sections in the data div */
        }
        
        .spoiler{
            color: #333; 
            font-size: 24px; 
            display: inline-block; 
            float: right; 
            margin: 15px;
        }
        
        /* Style for sections */
        article {
            display: flex; /* Enables flexbox layout */
            flex-direction: column; /* Stacks items vertically */
            background-color: rgba(255, 255, 255, 0.5); /* White background with 50% opacity */
            padding: 10px; /* Padding inside each section */
            margin: 10px; /* Space around sections */
            border-radius: 10px; /* Rounded corners for sections */
            width: 150px; /* Fixed width for each section */
        }
        
        /* Style for h2 headers */
        h2 {
            margin: 15px; /* Add some margin around the h2 */
            width: fit-content;
        }
        
        /* Style for h3 headers */
        h3 {
            margin: 0; /* Remove default margins */
            text-align: center; /* Center the text */
            font-size: 1.5em; /* Increase the font size */
        }        
        button {
            background: none; 
            border: none; 
            cursor: pointer; 
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .icon{
            margin-top: -0.25em;
            align-self: center;
            font-size: 2em;
        }
        .phrase{
            font-size: 1.2em;
            border-bottom-style: groove;
            width: inherit;
            border-bottom-color: rgba(0,0,0,0.2);
            border-bottom-width: 2px;
            padding-bottom: 4px;
        }
        p {
            margin: 0.25em 0; /* Add space between paragraphs */
            align-self: center;
            text-align: center;
            font-family: sans-serif;
        }
    </style>
    </head>
    <body>
    """)

    # Loop through the JSON and create HTML structure
    for category in data:
        # Format color to hex (adding '#' prefix)
        hex_color = f'#{category["color"]}'

        # Button to toggle the visibility of sections
        article_id = category["category"].replace(" ", "_")  # Create a unique ID for the article

        # Write the category as an article, with background color
        html_file.write(f'<section style="background-color: {hex_color}; padding: 15px; margin-bottom: 20px;">\n')
        html_file.write(f'<button onclick="toggleSections(\'{article_id}\')">\n')
        html_file.write(f'<h2>{category["category"]}</h2>\n')

        html_file.write(f'<div id="{article_id}_arrow" class="spoiler">▼</div>\n')

        html_file.write('</button>\n')
        # Div to contain all the sections
        html_file.write(f'<div id="{article_id}" class="data">\n')

        # Loop through each data entry in the category
        for entry in category["data"]:
            html_file.write('<article>\n')
            html_file.write(f'<p class="icon">{entry["icons"]}</p>\n')
            html_file.write(f'<p class="phrase">{entry["phrase"]}</p>\n')
            html_file.write(f'<p class="written_tr">{entry["written_tr"]}</p>\n')
            html_file.write(f'<p class="phonetic_tr">{entry["phonetic_tr"]}</p>\n')
            html_file.write('</article>\n')

        html_file.write('</div>\n')  # Close the data div
        html_file.write('</section>\n')

        # Close the HTML structure
        html_file.write('</body>\n')
        html_file.write('</html>\n')

print("HTML file created successfully!")
