class FileReaderWriter:
    def read(self, filepath):
        raise NotImplementedError("!Subclasses should implement this!")

    def write(self, filepath, content):
        raise NotImplementedError("!Subclasses should implement this!")

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        """Reads and returns the content of a text file."""
        try:
            with open(filepath, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "File not found."

    def write(self, filepath, content):
        """Writes content to a text file (Overrides existing content)."""
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"Content written to {filepath} successfully.")

# Sample usage:
if __name__ == "__main__":
    # Create instance of TextFileReaderWriter
    file_rw = TextFileReaderWriter()

    # Write content to file
    file_rw.write("sample.txt", "This is a sample content for the file.")

    # Read file contents
    content = file_rw.read("sample.txt")
    print("File content:")
    print(content)
