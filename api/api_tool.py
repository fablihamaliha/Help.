# # @main.route("/meditation")
# def meditation():
#     api_url = "https://api.example.com/meditation"  # Replace with real API URL
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         meditations = response.json()
#     # except requests.exceptions.RequestException as e:
#         meditations = []
#         print(f"Error fetching meditations: {e}")

#     # return render_template("meditation.html", meditations=meditations)
