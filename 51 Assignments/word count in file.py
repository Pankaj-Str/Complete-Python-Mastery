#codeswithpankaj.com
#Word count and writting the word count to #different file
def count_words(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            word_count = len(content.split())
        
        with open(output_file, 'w') as output:
            output.write(f"Word count: {word_count}")
            
        print(f"Word count successfully written to {output_file}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
count_words('p4n.txt', 'output.txt')