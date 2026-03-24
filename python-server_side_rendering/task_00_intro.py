
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Invalid input: template must be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list):
        print(f"Invalid input: attendees must be a list, got {type(attendees).__name__}")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees must be a list of dictionaries")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, 1):
        output_text = template
        name = attendee.get("name") or "N/A"
        output_text = output_text.replace("{name}", name)

        event_title = attendee.get("event_title") or "N/A"
        output_text = output_text.replace("{event_title}", event_title)

        event_date = attendee.get("event_date") or "N/A"
        output_text = output_text.replace("{event_date}", event_date)

        event_location = attendee.get("event_location") or "N/A"
        output_text = output_text.replace("{event_location}", event_location)

        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(output_text)
