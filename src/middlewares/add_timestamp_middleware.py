import time

def add_timestamp_middleware():
    def modified_function(event, context, next):
        timestamp = time.time()
        mutated_event = {**event, "timestamp": timestamp}
        return next(mutated_event, context)

    return modified_function