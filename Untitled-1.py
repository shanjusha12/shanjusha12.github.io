def mission_control():
    print("BEGIN")

    # Step 1: Sensor input
    sensor_data = get_sensor_signals()  # velocity, nearby objects
    print("Sensor data received.")

    # Step 2: Process using reused module
    result = flight_dynamics_module(sensor_data)  # Uses legacy Ariane 4 software
    print("Flight dynamics processed.")

    # Step 3: Validate data
    if not validate_data(result):
        print("Error detected.")

        # Step 4: Check past logs for reference
        if check_logs_for_solution(result):
            if is_exception_manageable(result):
                handle_exception(result)
                log_exception(result)
                print("Exception handled. Resuming mission.")
                continue_mission()
            else:
                notify_main_system(result)
                print("Critical error. Aborting mission.")
                abort_mission()
        else:
            notify_main_system(result)
            print("Unknown error. Aborting mission.")
            abort_mission()
    else:
        # No exception detected
        restore_system_to_normal()
        log_process_state()
        print("No errors. Continuing mission.")
        continue_mission()

    print("FINISH")

# Helper functions (stubs for example)
def get_sensor_signals():
    return {"velocity": 750, "obstacle_distance": 300}

def flight_dynamics_module(data):
    # Simulate processing
    return {"status": "OK", "data": data}

def validate_data(result):
    # Simulate error detection
    return result["status"] == "OK"

def check_logs_for_solution(result):
    return True  # Assume logs found

def is_exception_manageable(result):
    return True  # Assume exception is manageable

def handle_exception(result):
    pass

def log_exception(result):
    pass

def notify_main_system(result):
    pass

def abort_mission():
    pass

def restore_system_to_normal():
    pass

def log_process_state():
    pass

def continue_mission():
    pass

# Execute the function
mission_control()
