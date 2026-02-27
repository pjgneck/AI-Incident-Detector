from trace import Trace

def main():
    # Set up our parameters
    endpoint_to_test = "/api/v1/user-data"
    number_of_logs = 5
    
    # Instantiate the Trace class
    # This will automatically generate the Log objects inside
    current_trace = Trace(number_of_logs, endpoint_to_test, host="localhost")
    
    # Output the results
    print(f"--- Trace Report for {endpoint_to_test} ---")
    current_trace.print_trace()

# This is the standard way to call main in Python
if __name__ == "__main__":
    main()