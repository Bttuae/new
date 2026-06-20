from bs4 import BeautifulSoup

def format_html_file(input_file, output_file):
    # Read the unformatted HTML
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Format the HTML with proper indentation
    formatted_html = soup.prettify()
    
    # Save the beautifully formatted HTML back to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_html)
    print(f"Successfully formatted and saved to {output_file}")

# Example usage:
format_html_file('index_old.html', 'index.html')