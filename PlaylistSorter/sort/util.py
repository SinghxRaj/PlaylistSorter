def sort_on_key(key, items) -> list:
  """
  Sorts tracks based on the attribute that was based in.

  Args
  -----------------
  key (string) - The way we want to sort the tracks
  items (list) - The tracks we want to sort

  Returns
  ----------------
  (list of dicts) - The sorted tracks
  """
  return {
    "Name of Song (Alphabetical)": sorted(
      items, key=lambda item: item["track"]["name"]
    ),
    "Name of Song (Reverse Alphabetical)": sorted(
      items, key=lambda item: item["track"]["name"],
      reverse=True
    ),
    "Name of Artist (Alphabetical)": sorted(
      items, key=lambda item: item["track"]["artists"][0]["name"]
    ),
    "Name of Artist (Reverse Alphabetical)": sorted(
      items, key=lambda item: item["track"]["artists"][0]["name"],
      reverse=True
    ),
    "Release Date (Newest to Oldest)": sorted(
      items, key=lambda item: item["track"]["album"]["release_date"]
    ),
    "Release Date (Oldest to Newest)": sorted(
      items, key=lambda item: item["track"]["album"]["release_date"],
      reverse=True
    ),
    "Song Duration (Shortest to Longest)": sorted(
      items, key=lambda item: item["track"]["duration_ms"]
    ),
    "Song Duration (Longest to Shortest)": sorted(
      items, key=lambda item: item["track"]["duration_ms"],
      reverse=True
    ),
    "Popularity (Least to Most)": sorted(
      items, key=lambda item: item["track"]["popularity"]
    ),
    "Popularity (Most to Least)": sorted(
      items, key=lambda item: item["track"]["popularity"],
      reverse=True
    )
  }[key]