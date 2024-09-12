import frappe
import requests
from frappe.utils import now_datetime

def sync_test_amba_with_vijay(doc, method):
    url = "http://127.0.0.1:8000/api/resource/test_amba"
    headers = {
        "Authorization": "token a1bce194c1fd509:d8b686b466af00e"
    }

    try:
        # Fetch the updated list of items from test_amba
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json().get("data", [])

        # Get current date (without time)
        current_date = now_datetime().strftime("%Y-%m-%d")

        # Initialize a dictionary to store the name1, creation date, and document name by item_name
        item_data_dict = {}
        for item in data:
            item_name = item.get("name")
            if item_name:
                item_url = f"{url}/{item_name}"
                try:
                    item_response = requests.get(item_url, headers=headers)
                    item_response.raise_for_status()
                    item_data = item_response.json().get("data", {})
                    
                    # Only include items created on the current date
                    creation_date = item_data.get("creation", "").split(" ")[0]  # Extract the date part
                    if creation_date == current_date:
                        item_data_dict[item_name] = {
                            "name1": item_data.get("name1", ""),
                            "creation": item_data.get("creation", ""),
                            "doc_name": item_data.get("name", "")  # Add document name
                        }
                except requests.HTTPError as e:
                    if e.response.status_code == 404:
                        print(f"Item '{item_name}' not found.")
                    else:
                        print(f"Error fetching data for item '{item_name}': {e}")
            else:
                print("Item name is missing in the response.")

        # Get or create a document for today and update it with filtered data
        vijay_doc = get_or_create_vijay_doc()

        # Detect modifications
        detect_and_update_modifications(vijay_doc, item_data_dict)

        # Update document with the new data and mark deleted items
        update_vijay_doc(vijay_doc, item_data_dict)

        # Save and commit changes
        vijay_doc.save()
        frappe.db.commit()
        print(f"Document for {now_datetime().strftime('%Y-%m-%d')} has been created or updated successfully.")

    except requests.RequestException as e:
        print("Error fetching data from API:", e)

def get_or_create_vijay_doc():
    """Get or create a document in the 'vijay' Doctype for today."""
    today = now_datetime().strftime("%Y-%m-%d")

    # Check if a document for today exists
    existing_vijay_docs = frappe.get_all(
        "vijay", 
        filters={"creation": ["like", f"{today}%"]}, 
        fields=["name"], 
        limit_page_length=1
    )

    if existing_vijay_docs:
        # If a document for today exists, get it
        vijay_doc = frappe.get_doc("vijay", existing_vijay_docs[0].name)
        print(f"Updating existing document: {vijay_doc.name}")
    else:
        # Create a new document if one doesn't exist for today
        vijay_doc = frappe.get_doc({
            "doctype": "vijay",
            "test": ""  # Initialize with default value or empty string
        })
        print("Creating new document for today")

    return vijay_doc

def detect_and_update_modifications(vijay_doc, current_item_data_dict):
    """Detect and update modifications in the 'vijay' document if there are changes in the data."""
    # Fetch existing document's data
    existing_data = vijay_doc.test
    existing_lines = existing_data.split("\n") if existing_data else []

    # Check for modifications
    for item_name, item_data in current_item_data_dict.items():
        item_found = False
        for line in existing_lines:
            if item_name in line:
                # Check if name1 or other fields have changed
                old_name1 = line.split(":")[-1].strip()  # Assuming 'name1' is after ':'
                new_name1 = item_data['name1']
                if old_name1 != new_name1:
                    print(f"Modification detected for {item_name}. Updating...")
                    line_index = existing_lines.index(line)
                    existing_lines[line_index] = f"{item_name} (Created on {item_data['creation']}) \n (Document: {item_data['doc_name']}): {new_name1}"
                item_found = True
                break

        if not item_found:
            # If item is not found in existing lines, it's new and will be added later
            continue

    # Update the document with modified lines
    vijay_doc.test = "\n".join(existing_lines)

def update_vijay_doc(vijay_doc, current_item_data_dict):
    """Update 'vijay' document with current items and mark items as deleted or modified."""
    # Fetch existing document's data
    existing_data = vijay_doc.test
    existing_lines = existing_data.split("\n") if existing_data else []

    # Create a set of current item names
    current_item_names = set(current_item_data_dict.keys())

    # Create a dictionary to store the updated lines
    updated_lines = []
    item_names_in_updated_lines = set()

    # Process existing lines
    for line in existing_lines:
        if "Created on" in line:
            # Extract item name and creation date-time
            parts = line.split(" (Created on")
            item_name = parts[0].strip()
            creation_date_time = parts[1].split(")")[0].strip()  # Full date-time of creation

            # Extract document name (if available)
            doc_name = ""
            if "Document:" in line:
                doc_name = line.split("Document:")[1].strip().replace(")", "")

            # Check if the item still exists in the current data
            if item_name in current_item_names:
                current_item = current_item_data_dict[item_name]

                # Compare name1 to check for modification
                current_name1 = current_item["name1"]
                if current_name1 not in line:
                    # If name1 has changed, update with the new value and mark as modified
                    updated_lines.append(
                        f"{item_name} (Created on {creation_date_time}) (Modified at {now_datetime().strftime('%Y-%m-%d %H:%M:%S')}): {current_name1}"
                    )
                else:
                    # If no changes, keep the line as is
                    updated_lines.append(line)

                # Mark the item as processed
                item_names_in_updated_lines.add(item_name)
            else:
                # Mark as deleted if the item no longer exists in the current data
                if "(Deleted)" not in line:
                    updated_lines.append(
                        f"{item_name} (Created on {creation_date_time}) (Deleted at {now_datetime().strftime('%Y-%m-%d %H:%M:%S')})"
                    )
                else:
                    # If already marked as deleted, retain the line
                    updated_lines.append(line)

                # Mark the item as processed
                item_names_in_updated_lines.add(item_name)
        else:
            updated_lines.append(line)

    # Add new items that are not already in the document
    for item_name, item_data in current_item_data_dict.items():
        if item_name not in item_names_in_updated_lines:
            # Include creation date-time and other details
            creation_date_time = item_data['creation']  # Full date-time of creation
            updated_lines.append(f"{item_name} (Created on {creation_date_time}): {item_data['name1']}")

    # Update the document with the new data and modified/deleted marks
    vijay_doc.test = "\n".join(updated_lines)