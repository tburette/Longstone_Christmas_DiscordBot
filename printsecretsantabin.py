import sys
import pickle

def main():
    # Get filename from command line argument or use default
    filename = sys.argv[1] if len(sys.argv) > 1 else "secretsanta.bin"
    
    try:
        # Open the file and load data
        with open(filename, "rb") as file:
            data = pickle.load(file)
        
        # Print the loaded data
        print(data)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except pickle.UnpicklingError:
        print("Error: Failed to unpickle the file. It may be corrupted.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
