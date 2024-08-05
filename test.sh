
#!/bin/bash

# Test URLs
urls=("https://www.example.com" "https://www.google.com")

for url in "${urls[@]}"; do
  # Create a JSON message with the URL
  message=$(jq -n --arg url "$url" '{url: $url}')

  # Send the message to the Python script
  echo -n "$(echo -n "$message" | wc -c)" | xxd -p -c 4
  echo -n "$message"

  # Read the response from the Python script
  read -r response

  # Print the response
  echo "Response: $response"
done
