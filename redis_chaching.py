import redis

# Replace these values with your Redis server information
redis_host = '0.0.0.0'
redis_port = 6379
redis_password = '***'

# Create a connection to the Redis server
redis_connection = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    decode_responses=True
)

def fetch_data_from_source(data_key):
    # This is a placeholder for fetching data from the actual source (e.g., a database)
    # In a real-world scenario, you would replace this with your data fetching logic.
    print(f"Fetching data from source for key '{data_key}'")
    return f"Data for key '{data_key}' from source"

def get_data_with_caching(data_key):
    # Try to retrieve the data from the cache (Redis)
    cached_data = redis_connection.get(data_key)

    if cached_data:
        print(f"Data found in cache for key '{data_key}'")
        return cached_data
    else:
        # Data not found in cache, fetch from the source
        data_from_source = fetch_data_from_source(data_key)

        # Store the fetched data in the cache with an expiration time (e.g., 60 seconds)
        redis_connection.setex(data_key, 60, data_from_source)

        print(f"Data stored in cache for key '{data_key}'")
        return data_from_source

# Test the caching function
data_key_to_fetch = 'example_key'
cached_data = get_data_with_caching(data_key_to_fetch)
print(f"Final Data: {cached_data}")

# Close the connection (optional)
redis_connection.close()
